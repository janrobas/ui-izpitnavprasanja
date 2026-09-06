#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generira lep PDF iz README.md (zbirka izpitnih vprašanj).

Uporaba:
    python generate_pdf.py

Zahteva:
    pip install markdown
    wkhtmltopdf (dostopen v PATH ali v C:/run/wkhtmltopdf.exe)
"""

import re
import subprocess
import sys
from pathlib import Path

import markdown

BASE = Path(__file__).resolve().parent
MD_FILE = BASE / "README.md"
HTML_FILE = BASE / "Izpitna_vprasanja.html"
PDF_FILE = BASE / "Izpitna_vprasanja.pdf"

TITLE = "UMETNA INTELIGENCA V INFORMATIKI"
SUBTITLE = "Zbirka vprašanj za izpit"
AUTHOR = "Jan Robas"

CSS = """
@page {
    size: A4;
    margin: 22mm 20mm 22mm 20mm;
    @bottom-center {
        content: counter(page);
        font-size: 9pt;
        color: #9aa3ad;
        font-family: 'Segoe UI', sans-serif;
    }
}

html { -webkit-print-color-adjust: exact; }

body {
    font-family: 'Segoe UI', 'Calibri', sans-serif;
    font-size: 11.5pt;
    line-height: 1.5;
    color: #24292f;
    margin: 0;
    padding: 0;
}

/* ---- Naslovna stran ---- */
.cover {
    text-align: center;
    page-break-after: always;
    padding-top: 150pt;
}
.cover h1 {
    font-size: 30pt;
    font-weight: 700;
    color: #111827;
    margin: 0 0 10pt 0;
    line-height: 1.2;
}
.cover .subtitle {
    font-size: 15pt;
    color: #4b5563;
    margin: 0;
}
.cover .author {
    font-size: 13pt;
    color: #6b7280;
    margin-top: 8pt;
}
.cover .rule {
    width: 90pt;
    height: 4px;
    background: #1f6feb;
    margin: 30pt auto;
    border: none;
    border-radius: 2px;
}
.cover .stats {
    margin-top: 36pt;
    font-size: 11pt;
    color: #6b7280;
}

/* ---- Poglavja ---- */
h2 {
    font-size: 17pt;
    font-weight: 700;
    color: #ffffff;
    background: #1f6feb;
    border-radius: 6px;
    padding: 9pt 14pt;
    margin: 26pt 0 16pt 0;
    page-break-before: always;
    page-break-after: avoid;
}
h2:first-of-type { page-break-before: avoid; }

/* ---- Akcentne barve po poglavjih ---- */
h2.ch1 { background: #1f6feb; }
h2.ch2 { background: #8957e5; }
h2.ch3 { background: #0ea5a4; }
h2.ch4 { background: #d97706; }
h2.ch5 { background: #9f1239; }
h2.ch6 { background: #16a34a; }

.ch1 h3 .points { background: #1f6feb; color: #ffffff; }
.ch2 h3 .points { background: #8957e5; color: #ffffff; }
.ch3 h3 .points { background: #0ea5a4; color: #ffffff; }
.ch4 h3 .points { background: #d97706; color: #ffffff; }
.ch5 h3 .points { background: #9f1239; color: #ffffff; }
.ch6 h3 .points { background: #16a34a; color: #ffffff; }

div.q.ch1 { border-left-color: #1f6feb; background: #f0f5ff; }
div.q.ch2 { border-left-color: #8957e5; background: #f3effc; }
div.q.ch3 { border-left-color: #0ea5a4; background: #eaf7f6; }
div.q.ch4 { border-left-color: #d97706; background: #fdf3e7; }
div.q.ch5 { border-left-color: #9f1239; background: #f9eef2; }
div.q.ch6 { border-left-color: #16a34a; background: #e9f8ee; }

div.q.ch1 .label { color: #1f6feb; }
div.q.ch2 .label { color: #8957e5; }
div.q.ch3 .label { color: #0ea5a4; }
div.q.ch4 .label { color: #d97706; }
div.q.ch5 .label { color: #9f1239; }
div.q.ch6 .label { color: #16a34a; }

div.a.ch1 { border-left-color: #1f6feb; background: #f7f9ff; }
div.a.ch2 { border-left-color: #8957e5; background: #f8f6fd; }
div.a.ch3 { border-left-color: #0ea5a4; background: #f4fbfb; }
div.a.ch4 { border-left-color: #d97706; background: #fef9f1; }
div.a.ch5 { border-left-color: #9f1239; background: #fdf5f8; }
div.a.ch6 { border-left-color: #16a34a; background: #f4fbf6; }

div.a.ch1 .label { color: #1f6feb; }
div.a.ch2 .label { color: #8957e5; }
div.a.ch3 .label { color: #0ea5a4; }
div.a.ch4 .label { color: #d97706; }
div.a.ch5 .label { color: #9f1239; }
div.a.ch6 .label { color: #16a34a; }

/* ---- Vprašanja ---- */
h3 {
    font-size: 13pt;
    font-weight: 700;
    color: #111827;
    margin: 24pt 0 6pt 0;
    padding-top: 8pt;
    border-top: 1.5pt solid #e5e7eb;
    page-break-after: avoid;
}
h3 .points {
    display: inline-block;
    background: #eaf2ff;
    color: #1f6feb;
    font-size: 9.5pt;
    font-weight: 700;
    border-radius: 10px;
    padding: 1pt 8pt;
    margin-right: 6pt;
    vertical-align: 2pt;
}

strong { font-weight: 600; }

p { margin: 6pt 0; }

/* Naslov vprašanja + vprašanje ostaneta skupaj */
div.qwrap {
    page-break-inside: avoid;
    page-break-after: avoid;
}

/* Vprašanje / Rešitev bloki */
div.q, div.a {
    border-radius: 0 5pt 5pt 0;
    padding: 8pt 12pt;
    margin: 8pt 0;
    page-break-inside: avoid;
}
div.q {
    border-left: 3pt solid #1f6feb;
    background: #f4f8ff;
}
div.q .label { font-weight: 700; color: #1f6feb; }

div.a {
    border-left: 3pt solid #2da44e;
    background: #f6fbf7;
}
div.a .label { font-weight: 700; color: #1a7f37; }

div.q p, div.a p { margin: 4pt 0; }
div.q p:first-child, div.a p:first-child { margin-top: 0; }
div.q ul, div.q ol, div.a ul, div.a ol { margin: 4pt 0; }

li { margin: 2pt 0; page-break-inside: avoid; }

ul, ol { margin: 6pt 0 6pt 0; padding-left: 20pt; }

code {
    font-family: 'Consolas', monospace;
    font-size: 10pt;
    background: #f3f4f6;
    border-radius: 3px;
    padding: 1pt 4pt;
}

pre {
    font-family: 'Consolas', monospace;
    font-size: 10pt;
    background: #f6f8fa;
    border: 1pt solid #e5e7eb;
    border-radius: 5px;
    padding: 8pt 10pt;
    overflow: hidden;
}
pre code { background: none; padding: 0; }

hr { border: none; border-top: 1pt solid #e5e7eb; margin: 12pt 0; }
"""


def normalize_md(md_text: str) -> str:
    """Vstavi prazno vrstico pred seznami, ki so neposredno za odstavkom
    (Python-Markdown jih sicer zlije v isti odstavek)."""
    lines = md_text.splitlines()
    out = []
    for i, line in enumerate(lines):
        prev = out[-1].strip() if out else ""
        is_list_item = bool(re.match(r"^\s*(?:[-*+]|\d+\.)\s", line))
        prev_is_list = bool(re.match(r"^\s*(?:[-*+]|\d+\.)\s", prev))
        if is_list_item and prev and prev != "---" and not prev_is_list:
            out.append("")
        out.append(line)
    return "\n".join(out)


def prettify(body: str) -> str:
    """Doda badge za točke ter ovije Vprašanje / Rešitev v blok div-e."""

    def points_repl(m):
        return f'<span class="points">{m.group(1)} {m.group(2)}</span>'

    # [1 točka] / [2 točki] / [3 točke] -> barvni badge
    body = re.sub(r"\[(\d+)\s+(točka|točki|točke)\]", points_repl, body)

    # Vprašanje / Rešitev oznake -> class + label span
    body = re.sub(
        r"<p><strong>Vprašanje:</strong>",
        '<p class="q-label"><span class="label">Vprašanje</span>',
        body,
    )
    body = re.sub(
        r"<p><strong>Rešitev:</strong>",
        '<p class="a-label"><span class="label">Rešitev</span>',
        body,
    )

    # Vsebino od oznake Vprašanje do konca Rešitve ovijemo v div bloke,
    # da je rešitev (tudi s seznami) en sam barvni sklop.
    # Naslov vprašanja (h3) + vprašanje (div.q) skupaj v div.qwrap,
    # da naslov ne ostane na koncu strani brez vprašanja.
    lines = body.splitlines()
    out = []
    in_q = in_a = in_qwrap = False
    chapter = 0

    for ln in lines:
        s = ln.strip()

        if s.startswith("<h2"):
            if in_a:
                out.append("</div>")
                in_a = False
            if in_q:
                out.append("</div>")
                in_q = False
            if in_qwrap:
                out.append("</div>")
                in_qwrap = False
            chapter += 1
            out.append(f'<h2 class="ch{chapter}">' + ln[4:])

        elif s.startswith("<h1"):
            out.append(ln)

        elif s.startswith("<hr"):
            if in_a:
                out.append("</div>")
                in_a = False
            if in_q:
                out.append("</div>")
                in_q = False
            if in_qwrap:
                out.append("</div>")
                in_qwrap = False

        elif s.startswith("<h3"):
            if in_a:
                out.append("</div>")
                in_a = False
            if in_q:
                out.append("</div>")
                in_q = False
            if in_qwrap:
                out.append("</div>")
                in_qwrap = False
            out.append(f'<div class="qwrap ch{chapter}">')
            out.append(ln)
            in_qwrap = True

        elif s.startswith('<p class="q-label">'):
            if in_q:
                out.append("</div>")
            out.append(f'<div class="q ch{chapter}">')
            out.append(ln)
            in_q = True

        elif s.startswith('<p class="a-label">'):
            if in_q:
                out.append("</div>")
                in_q = False
            if in_qwrap:
                out.append("</div>")
                in_qwrap = False
            if in_a:
                out.append("</div>")
            out.append(f'<div class="a ch{chapter}">')
            out.append(ln)
            in_a = True

        else:
            out.append(ln)

    if in_qwrap or in_q or in_a:
        out.append("</div>")

    return "\n".join(out)


def build_html(md_text: str) -> str:
    md_text = normalize_md(md_text)
    body = markdown.markdown(
        md_text,
        extensions=["extra", "sane_lists"],
    )
    body = prettify(body)

    lines = body.splitlines()
    title_block, body_start = [], 0
    for i, ln in enumerate(lines):
        if ln.startswith("<h1>"):
            title_block.append(ln)
            body_start = i + 1
            break
        title_block.append(ln)

    n_questions = len(re.findall(r"<h3>", body))

    cover = f"""
    <div class="cover">
        <h1>{TITLE}</h1>
        <p class="subtitle">{SUBTITLE}</p>
        <p class="author">{AUTHOR}</p>
        <hr class="rule" />
        <p class="stats">{n_questions} vprašanj</p>
    </div>
    """

    content = "\n".join(lines[body_start:])
    return f"""<!DOCTYPE html>
<html lang="sl">
<head>
<meta charset="utf-8" />
<title>{TITLE} — {SUBTITLE}</title>
<style>{CSS}</style>
</head>
<body>
{cover}
{content}
</body>
</html>
"""


def find_wkhtmltopdf() -> str:
    for candidate in [BASE / "wkhtmltopdf.exe", Path(r"C:\run\wkhtmltopdf.exe")]:
        if candidate.exists():
            return str(candidate)
    import shutil

    found = shutil.which("wkhtmltopdf")
    if found:
        return found
    print("NAPAKA: wkhtmltopdf ni najden. Namesti ga ali daj v PATH.", file=sys.stderr)
    sys.exit(1)


def main() -> None:
    md_text = MD_FILE.read_text(encoding="utf-8")
    html = build_html(md_text)
    HTML_FILE.write_text(html, encoding="utf-8")
    print(f"HTML zapisan: {HTML_FILE}")

    wkhtml = find_wkhtmltopdf()
    cmd = [
        wkhtml,
        "--enable-local-file-access",
        "--encoding", "UTF-8",
        "--page-size", "A4",
        "--margin-top", "20mm",
        "--margin-bottom", "20mm",
        "--margin-left", "18mm",
        "--margin-right", "18mm",
        "--footer-font-size", "9",
        "--footer-spacing", "6",
        "--footer-center", "[page]",
        str(HTML_FILE),
        str(PDF_FILE),
    ]
    print("Generiram PDF ...")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(result.stdout, file=sys.stderr)
        print(result.stderr, file=sys.stderr)
        sys.exit(result.returncode)

    print(f"PDF zgeneriran: {PDF_FILE} ({PDF_FILE.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()