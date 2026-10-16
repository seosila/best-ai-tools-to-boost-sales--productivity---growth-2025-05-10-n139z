#!/usr/bin/env python3
"""Check that every SellBetterAI category page follows the shared visual template."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
PAGES = sorted((ROOT / "tools").glob("*/index.html"))

REQUIRED_MARKUP = {
    "body shell": '<body class="sb-category-page">',
    "shared header": '<header class="sb-site-header">',
    "skip link": '<a class="sb-skip-link" href="#main-content">',
    "main container": '<main id="main-content" class="container mx-auto px-4 py-10 sm:py-14 max-w-5xl">',
    "breadcrumb": '<nav aria-label="Breadcrumb" class="flex flex-wrap gap-2 text-sm mb-8">',
    "category H1 typography": '<h1 class="text-3xl sm:text-4xl font-bold mt-2 mb-4">',
    "category header spacing": '<header class="mb-10">',
    "shared footer": '<footer class="sb-footer">',
    "shared site CSS": '<link rel="stylesheet" href="/assets/css/site.css">',
    "shared navigation script": '<script src="/assets/js/site-nav.js" defer>',
}

DISALLOWED_CLASS_TOKENS = {
    "bg-purple-50", "bg-purple-600", "border-purple-200",
    "border-gray-100", "shadow-lg",
}
errors = []

if not PAGES:
    print("ERROR: no category pages found under tools/<category>/index.html")
    sys.exit(1)

for path in PAGES:
    html = path.read_text(encoding="utf-8")
    relative = path.relative_to(ROOT).as_posix()

    for label, snippet in REQUIRED_MARKUP.items():
        if snippet not in html:
            errors.append(f"{relative}: missing standard {label}")

    for label, pattern in (
        ("title", r"<title\b"),
        ("description", r'<meta[^>]+name="description"'),
        ("canonical", r'<link[^>]+rel="canonical"'),
        ("H1", r"<h1\b"),
    ):
        count = len(re.findall(pattern, html, flags=re.IGNORECASE))
        if count != 1:
            errors.append(f"{relative}: expected exactly one {label}, found {count}")

    for label, pattern in (
        ("breadcrumb", r'aria-label="Breadcrumb"'),
        ("shared footer", r'<footer[^>]+class="sb-footer'),
        ("skip link", r'class="sb-skip-link"'),
        ("site stylesheet", r'href="/assets/css/site\.css"'),
        ("navigation script", r'src="/assets/js/site-nav\.js"'),
    ):
        count = len(re.findall(pattern, html, flags=re.IGNORECASE))
        if count != 1:
            errors.append(f"{relative}: expected exactly one {label}, found {count}")

    classes = re.findall(r'class="([^"]*)"', html)
    tokens = {token for value in classes for token in value.split()}
    for token in sorted(tokens & DISALLOWED_CLASS_TOKENS):
        errors.append(f"{relative}: nonstandard class token {token}")

    if re.search(r"<style\b|\sstyle\s*=", html, flags=re.IGNORECASE):
        errors.append(f"{relative}: inline/page-specific CSS is not allowed")

    if "font-awesome" in html.lower():
        errors.append(f"{relative}: unexpected page-specific icon stylesheet")

if errors:
    print(f"FAIL: {len(errors)} issue(s) across {len(PAGES)} category pages")
    print("\n".join(f"- {error}" for error in errors))
    sys.exit(1)

print(f"PASS: all {len(PAGES)} category pages follow the shared layout and style rules.")
