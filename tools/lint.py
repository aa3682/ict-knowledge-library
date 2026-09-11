"""Structural lint for the ICT knowledge library.

Run from the repo root:  python tools/lint.py

Checks, in the order AGENTS.md lists them, plus two added 2026-08-10 after silent
failures got through:

  * `sources_agree`  — the bold-key `**Source IDs:**` line and the JSON `sources[]`
    must list the same IDs. Three pages had drifted: an edit updated the header and
    missed the JSON because the array's formatting differed from what the edit
    expected. Nothing else noticed, because every other check reads only one of the
    two lists.
  * `years_agree`    — `**Year Introduced:**` must equal JSON `year_introduced`.

And one added 2026-09-11, after six pages were found dated 2022 against 2016/2017
citations because their only source was a registry stub:

  * `years_vs_citations` — `**Year Introduced:**` is compared against the years encoded
    in the page's own Source IDs. The three surface-agreement checks above all pass when
    every surface carries the *same wrong year*, which is exactly what a stub-sourced
    page looks like. This is the first check that reads the year against evidence rather
    than against another copy of itself.

    Reported as WARNINGS, not problems: a mismatch needs human judgment and is not always
    a defect. A comparison page (`<a>-vs-<b>.md`) is legitimately dated by its newer
    concept while citing an older source for the thing being compared against, and some
    Source IDs carry a legacy year that disagrees with the material (SOURCES.md documents
    these). Stub and placeholder IDs are excluded outright — their year means nothing.

  * `timeline_placement` — AGENTS.md → Lint step 4 ("every concept file appears under its
    `Year Introduced` heading") had no implementation, so every re-dating pass silently
    desynced TIMELINE.md from the pages. Two re-dates on 2026-09-11 broke placement with
    nothing to catch it. Also a warning: TIMELINE lists many pages inside grouped bullets,
    and a page may legitimately be named in a later year's section as a refinement.

Exit status is non-zero if anything fails, so this is CI-safe. Warnings do not affect it.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_SECTIONS = [
    "## Definition",
    "## Formal Criteria",
    "## Formula / Math",
    "## Machine-Readable",
    "## Visual Pattern",
    "## Timeframes",
    "## Examples",
    "## Common Mistakes",
    "## Related Concepts",
    "## Citations",
]

# Source IDs whose encoded year is not evidence of anything. These are registry stubs and
# placeholders — no video ID, no date, no quotation behind them. Including their year is how
# six pages came to be dated 2022 against 2016/2017 material. See SOURCES.md for each.
UNDATED_SOURCES = {
    "ICT-2022-MENTORSHIP-OVERVIEW",
    "ICT-2018-BLOCKS",
} | {f"ICT-2022-E{n:02d}" for n in range(1, 13)}

REQUIRED_FIELDS = [
    "**Category:**",
    "**Aliases:**",
    "**ICT Confidence:**",
    "**Year Introduced:**",
    "**Year Refined:**",
    "**Source IDs:**",
    "**Tags:**",
]


def concept_files() -> list[Path]:
    return [p for p in sorted(ROOT.glob("concepts/*/*.md")) if p.name != "README.md"]


def source_ids() -> set[str]:
    text = (ROOT / "SOURCES.md").read_text(encoding="utf-8")
    return set(re.findall(r"^- `([A-Z0-9\-]+)`", text, re.M))


def main() -> int:
    files = concept_files()
    ids = {p.stem for p in files}
    known_sources = source_ids()
    index = (ROOT / "INDEX.md").read_text(encoding="utf-8")
    problems: list[str] = []
    warnings: list[str] = []

    def bad(msg: str) -> None:
        problems.append(msg)

    def warn(msg: str) -> None:
        warnings.append(msg)

    for f in files:
        rel = f.relative_to(ROOT).as_posix()
        text = f.read_text(encoding="utf-8")

        for section in REQUIRED_SECTIONS:
            if section not in text:
                bad(f"{rel}: missing section {section}")
        for field in REQUIRED_FIELDS:
            if field not in text:
                bad(f"{rel}: missing field {field}")

        match = re.search(r"```json\n(.*?)\n```", text, re.S)
        if not match:
            bad(f"{rel}: no JSON block")
            continue
        try:
            blob = json.loads(match.group(1))
        except json.JSONDecodeError as exc:
            bad(f"{rel}: bad JSON ({exc})")
            continue

        if blob.get("id") != f.stem:
            bad(f"{rel}: JSON id {blob.get('id')!r} != filename")

        for related in blob.get("related", []):
            if related not in ids:
                bad(f"{rel}: related[] points at missing concept {related!r}")

        header_sources = {
            s.strip()
            for s in re.search(r"\*\*Source IDs:\*\* (.+)", text).group(1).split(",")
        }
        json_sources = set(blob.get("sources", []))
        for sid in header_sources | json_sources:
            if sid not in known_sources:
                bad(f"{rel}: unknown source id {sid!r}")
        if header_sources != json_sources:
            bad(
                f"{rel}: header/JSON sources disagree "
                f"(header-only={sorted(header_sources - json_sources)}, "
                f"json-only={sorted(json_sources - header_sources)})"
            )

        # citations_cover_sources — every ID in the header must actually appear in the
        # ## Citations section. Added 2026-08-11 after three pages were re-dated with the
        # header and JSON updated together while the Citations list kept naming the source
        # that had just been removed. header/JSON agreement cannot catch this: Citations is
        # a third surface stating the same fact, and nothing was reading it.
        cit = re.search(r"^## Citations\s*(.*?)\Z", text, re.M | re.S)
        if cit:
            missing = sorted(s for s in header_sources if s not in cit.group(1))
            if missing:
                bad(f"{rel}: Source IDs absent from ## Citations: {missing}")

        header_year = re.search(r"\*\*Year Introduced:\*\* (\d{4})", text).group(1)
        if blob.get("year_introduced") != header_year:
            bad(
                f"{rel}: header year {header_year} != JSON "
                f"year_introduced {blob.get('year_introduced')}"
            )

        # years_vs_citations — see the module docstring. Compares the declared year against
        # the years the page's own Source IDs encode, ignoring stubs and placeholders.
        dated = []
        for sid in header_sources:
            if sid in UNDATED_SOURCES:
                continue
            year_match = re.match(r"^[A-Z]+-(\d{4})-", sid)
            if year_match:
                dated.append((int(year_match.group(1)), sid))
        if dated:
            earliest_year, earliest_id = min(dated)
            declared = int(header_year)
            if declared > earliest_year:
                # A disambiguation page is dated by the newer of the two concepts it
                # separates, while citing an older source for the other one. Expected, not a
                # defect — flagged with a hint rather than suppressed, so a real mis-dating on
                # a comparison page still surfaces.
                hint = (
                    " (comparison page — expected if dated by the newer concept)"
                    if "-vs-" in f.stem
                    else " — dated off a stub?"
                )
                warn(
                    f"{rel}: Year Introduced {declared} is later than its earliest citation "
                    f"{earliest_year} ({earliest_id}){hint}"
                )
            elif declared < earliest_year:
                warn(
                    f"{rel}: Year Introduced {declared} predates every citation "
                    f"(earliest {earliest_year}, {earliest_id}) — introduction unsourced?"
                )

        for link in re.findall(r"\]\((\.\./[^)]+\.md)\)", text):
            if not (f.parent / link).resolve().exists():
                bad(f"{rel}: dead link {link}")
        for link in re.findall(r"\]\(([a-z0-9\-]+\.md)\)", text):
            if not (f.parent / link).exists():
                bad(f"{rel}: dead local link {link}")

        if rel not in index:
            bad(f"{rel}: not listed in INDEX.md")

    for link in sorted(set(re.findall(r"\]\((concepts/[^)]+\.md)\)", index))):
        if not (ROOT / link).exists():
            bad(f"INDEX.md: points at missing file {link}")

    # timeline_placement — see the module docstring.
    timeline = (ROOT / "TIMELINE.md").read_text(encoding="utf-8")
    placed: dict[str, set[str]] = {}
    current_year = None
    for line in timeline.splitlines():
        heading = re.match(r"^## (\d{4})", line)
        if heading:
            current_year = heading.group(1)
        for slug in re.findall(r"\]\(concepts/[^)]*/([a-z0-9\-]+)\.md\)", line):
            placed.setdefault(slug, set()).add(current_year)
    for f in files:
        text = f.read_text(encoding="utf-8")
        year_field = re.search(r"\*\*Year Introduced:\*\* (\d{4})", text)
        if not year_field:
            continue
        years = placed.get(f.stem)
        if years and year_field.group(1) not in years:
            warn(
                f"{f.relative_to(ROOT).as_posix()}: Year Introduced {year_field.group(1)} "
                f"but TIMELINE.md lists it under {sorted(y for y in years if y)}"
            )

    print(f"{len(files)} concept pages, {len(known_sources)} source ids")
    print(f"problems: {len(problems)}")
    for problem in problems:
        print(f"  {problem}")
    print(f"warnings: {len(warnings)}")
    for warning in warnings:
        print(f"  {warning}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
