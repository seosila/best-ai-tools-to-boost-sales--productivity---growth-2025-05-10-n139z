#!/usr/bin/env python3
"""Source-level guardrails for SellBetterAI category pages."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
pages = sorted((ROOT / "tools").glob("*/index.html"))
errors = []
checked = 0
for page in pages:
    html = page.read_text(encoding="utf-8")
    if 'class="sb-category-page"' not in html:
        continue
    checked += 1
    if '<main id="main-content"' not in html:
        errors.append(f"{page.relative_to(ROOT)}: missing main landmark")
    if html.count("<h1") != 1:
        errors.append(f"{page.relative_to(ROOT)}: expected exactly one H1")
    if "Coming soon." not in html and not any(
        token in html for token in ('aria-labelledby="listings-heading"',
                                    'aria-labelledby="profiles-heading"',
                                    'aria-labelledby="tools-heading"',
                                    'aria-labelledby="sales-tool-options"',
                                    'aria-labelledby="cro-options"')):
        errors.append(f"{page.relative_to(ROOT)}: populated page has no recognizable listing section")
print(f"Checked {checked} category pages.")
if errors:
    print("\n".join(errors))
    sys.exit(1)
print("Category page guardrails passed.")
