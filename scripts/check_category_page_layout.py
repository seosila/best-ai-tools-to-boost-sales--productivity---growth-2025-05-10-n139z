#!/usr/bin/env python3
"""Source-level guardrails for SellBetterAI category directory layouts."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
pages = sorted((ROOT / "tools").glob("*/index.html"))
listing_ids = (
    "listings-heading", "profiles-heading", "tools-heading",
    "sales-tool-options", "cro-options", "crm-options",
    "listing-heading", "tool-options",
)
errors = []
checked = 0

for page in pages:
    html = page.read_text(encoding="utf-8")
    if 'class="sb-category-page"' not in html:
        continue
    checked += 1
    label = str(page.relative_to(ROOT))
    if '<main id="main-content" class="sb-category-main' not in html:
        errors.append(f"{label}: missing shared main layout class")
    if html.count("<h1") != 1:
        errors.append(f"{label}: expected exactly one H1")
    if "Coming soon." not in html:
        main_pos = html.find("<main")
        intro_end = html.find("</header>", main_pos)
        positions = [html.find(f'aria-labelledby="{item}"', main_pos) for item in listing_ids]
        positions = [p for p in positions if p >= 0]
        if not positions:
            errors.append(f"{label}: populated page has no recognized listing section")
        elif intro_end < 0 or min(positions) < intro_end:
            errors.append(f"{label}: primary listings should follow the intro header")

print(f"Checked {checked} category pages.")
if errors:
    print("\\n".join(errors))
    sys.exit(1)
print("Category layout guardrails passed.")
