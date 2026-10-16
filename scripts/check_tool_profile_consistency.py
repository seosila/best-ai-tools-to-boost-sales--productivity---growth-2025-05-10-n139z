#!/usr/bin/env python3
"""Check that every SellBetterAI tool profile follows the shared visual template."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
PROFILES = sorted((ROOT / "tools").glob("*/*/index.html"))

REQUIRED_MARKUP = {
    "body shell": '<body class="sb-page">',
    "shared header": '<header class="sb-site-header">',
    "skip link": '<a class="sb-skip-link" href="#main-content">',
    "main container": '<main id="main-content" class="container mx-auto px-4 py-10 sm:py-14 max-w-4xl">',
    "breadcrumb": '<nav aria-label="Breadcrumb" class="flex flex-wrap gap-2 text-sm mb-8">',
    "profile card": '<article class="bg-white rounded-xl shadow-sm p-6 sm:p-8 space-y-8">',
    "profile logo frame": 'class="tool-logo-frame tool-logo-frame--profile mb-4"',
    "H1 typography": '<h1 class="text-3xl sm:text-4xl font-bold mb-4">',
    "shared footer": '<footer class="sb-footer">',
    "shared site CSS": '<link rel="stylesheet" href="/assets/css/site.css">',
    "shared navigation script": '<script src="/assets/js/site-nav.js" defer>',
}

# These tokens were one-off variants, not part of the shared profile palette.
DISALLOWED_CLASS_TOKENS = {"bg-purple-600", "text-gray-900"}
errors = []

if not PROFILES:
    print("ERROR: no tool profiles found under tools/<category>/<tool>/index.html")
    sys.exit(1)

for path in PROFILES:
    html = path.read_text(encoding="utf-8")
    relative = path.relative_to(ROOT).as_posix()

    for label, snippet in REQUIRED_MARKUP.items():
        if snippet not in html:
            errors.append(f"{relative}: missing standard {label}")

    for label, pattern in (("title", r"<title\b"), ("description", r'<meta\b[^>]*name=["\']description["\']'),
                           ("canonical", r'<link\b[^>]*rel=["\']canonical["\']'), ("H1", r"<h1\b")):
        count = len(re.findall(pattern, html, flags=re.IGNORECASE))
        if count != 1:
            errors.append(f"{relative}: expected exactly one {label}, found {count}")

    classes = re.findall(r'\bclass=["\']([^"\']*)["\']', html)
    tokens = {token for value in classes for token in value.split()}
    for token in sorted(tokens & DISALLOWED_CLASS_TOKENS):
        errors.append(f"{relative}: nonstandard color token {token}")

    if re.search(r"<style\b|\sstyle\s*=", html, flags=re.IGNORECASE):
        errors.append(f"{relative}: inline/page-specific CSS is not allowed")

    if "font-awesome" in html.lower():
        errors.append(f"{relative}: unexpected page-specific icon stylesheet")

if errors:
    print(f"FAIL: {len(errors)} issue(s) across {len(PROFILES)} tool profiles")
    print("\n".join(f"- {error}" for error in errors))
    sys.exit(1)

print(f"PASS: all {len(PROFILES)} tool profiles follow the shared layout and style rules.")
