#!/usr/bin/env python3
"""Conversor README.md -> index.html para Documentación Geomática.

El README.md es la ÚNICA fuente de la verdad. Este script lo transforma en
una página HTML estática con estética "chulapa" (Madrid) y tipografía Chulapa
en los títulos. Se ejecuta en local (`python build.py`) y en la GitHub Action
que publica en GitHub Pages.
"""

from __future__ import annotations

import datetime as _dt
import html as _html
import re
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent
README = ROOT / "README.md"
OUTPUT = ROOT / "index.html"

SITE_TITLE = "Documentación Geomática"
SITE_DESCRIPTION = (
    "Punto de acceso a documentación, software de fuente abierta y recursos "
    "útiles para la Topografía y la Geomática."
)
LANG = "es"

MD_EXTENSIONS = [
    "extra",          # tablas, listas de definición, etc.
    "sane_lists",
    "toc",
    "codehilite",
    "admonition",
]
MD_EXTENSION_CONFIGS = {
    "codehilite": {"guess_lang": False},
    "toc": {
        # Ancla clicable en cada título para compartir/enlazar secciones.
        "permalink": "🔗",
        "permalink_title": "Enlace a esta sección",
        "toc_depth": "2-4",
    },
}


def read_readme() -> str:
    if not README.exists():
        raise SystemExit(f"No se encontró la fuente de la verdad: {README}")
    return README.read_text(encoding="utf-8")


def strip_leading_comments(md_text: str) -> str:
    """Elimina comentarios HTML iniciales del README (metadatos internos)."""
    return re.sub(r"^\s*(<!--.*?-->\s*)+", "", md_text, flags=re.DOTALL)


def strip_web_excluded_blocks(md_text: str) -> str:
    """Elimina los bloques marcados como exclusivos de GitHub.

    El contenido entre ``<!-- WEB-EXCLUDE:START -->`` y ``<!-- WEB-EXCLUDE:END -->``
    aparece en el README (GitHub) pero se omite en la web generada, evitando
    elementos redundantes como el badge que enlaza a la propia web.
    """
    pattern = r"<!--\s*WEB-EXCLUDE:START\s*-->.*?<!--\s*WEB-EXCLUDE:END\s*-->\s*"
    return re.sub(pattern, "", md_text, flags=re.DOTALL)


def extract_title(md_text: str) -> str:
    match = re.search(r"^#\s+(.+?)\s*$", md_text, flags=re.MULTILINE)
    return match.group(1).strip() if match else SITE_TITLE


def convert(md_text: str) -> str:
    md = markdown.Markdown(
        extensions=MD_EXTENSIONS,
        extension_configs=MD_EXTENSION_CONFIGS,
        output_format="html5",
    )
    return md.convert(md_text)


def render_page(title: str, body_html: str) -> str:
    year = _dt.date.today().year
    safe_title = _html.escape(title)
    safe_desc = _html.escape(SITE_DESCRIPTION)
    return f"""<!DOCTYPE html>
<html lang="{LANG}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{safe_desc}">
  <title>{safe_title}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
  <a class="skip-link" href="#contenido">Saltar al contenido</a>
  <header class="site-header">
    <div class="wrap">
      <p class="site-kicker">Ingeniería · Topografía · Geomática</p>
      <h1 class="site-title chulapa">{safe_title}</h1>
      <p class="site-subtitle">{safe_desc}</p>
    </div>
  </header>

  <main id="contenido" class="wrap content">
    {body_html}
  </main>

  <footer class="site-footer">
    <div class="wrap">
      <p>Generado a partir de <code>README.md</code> · © {year} Documentación Geomática</p>
      <p class="footer-note">
        Contenido bajo
        <a href="https://creativecommons.org/licenses/by/4.0/deed.es">CC BY 4.0</a>.
        Tipografía <span class="chulapa">Chulapa</span> — Ayuntamiento de Madrid (Madrid-Ferpal), CC BY 4.0.
      </p>
    </div>
  </footer>
</body>
</html>
"""


def build() -> None:
    raw = read_readme()
    md_text = strip_leading_comments(raw)
    md_text = strip_web_excluded_blocks(md_text)
    title = extract_title(md_text)

    # El H1 del README pasa a ser la cabecera; lo quitamos del cuerpo para no duplicarlo.
    md_body = re.sub(r"^#\s+.+?\s*$", "", md_text, count=1, flags=re.MULTILINE)

    body_html = convert(md_body)
    page = render_page(title, body_html)
    OUTPUT.write_text(page, encoding="utf-8")
    print(f"OK: generado {OUTPUT.relative_to(ROOT)} ({len(page):,} bytes)")


if __name__ == "__main__":
    build()
