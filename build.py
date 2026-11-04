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

from markdown.extensions.toc import slugify_unicode

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
        "slugify": slugify_unicode,
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
    <div class="search-container" role="search">
      <div class="search-input-wrap">
        <span class="search-icon" aria-hidden="true">🔍</span>
        <input type="search" id="search-input" class="search-input" placeholder="Buscar recursos, herramientas, librerías, formatos..." aria-label="Buscar recursos en la página" autocomplete="off">
        <kbd class="search-shortcut" title="Presiona / para buscar">/</kbd>
        <button type="button" id="search-clear" class="search-clear" aria-label="Limpiar búsqueda" hidden>&times;</button>
      </div>
      <div id="search-meta" class="search-meta" aria-live="polite"></div>
    </div>

    <div id="search-empty" class="search-empty" hidden>
      <p class="search-empty-icon">🗺️</p>
      <p class="search-empty-text">No se encontraron recursos que coincidan con "<span id="search-query-text"></span>".</p>
      <button type="button" class="search-reset-btn" id="search-reset-btn">Mostrar todos los recursos</button>
    </div>

    {body_html}
  </main>

  <button type="button" id="back-to-top" class="back-to-top" aria-label="Volver arriba" title="Volver arriba">
    ↑
  </button>

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

  <script>
    document.addEventListener('DOMContentLoaded', () => {{
      const searchInput = document.getElementById('search-input');
      const searchClear = document.getElementById('search-clear');
      const searchMeta = document.getElementById('search-meta');
      const searchEmpty = document.getElementById('search-empty');
      const searchQueryText = document.getElementById('search-query-text');
      const searchResetBtn = document.getElementById('search-reset-btn');
      const backToTopBtn = document.getElementById('back-to-top');
      const content = document.getElementById('contenido');

      if (!content || !searchInput) return;

      const resourceLists = Array.from(content.querySelectorAll('ul'));
      const resourceItems = Array.from(content.querySelectorAll('ul > li'));
      const allHeadings = Array.from(content.querySelectorAll('h2, h3, h4'));
      const totalCount = resourceItems.length;

      function normalize(str) {{
        return (str || '')
          .toLowerCase()
          .normalize('NFD')
          .replace(/[\u0300-\u036f]/g, '');
      }}

      const indexedItems = resourceItems.map(li => ({{
        el: li,
        text: normalize(li.textContent)
      }}));

      const levels = {{ 'H4': 4, 'H3': 3, 'H2': 2 }};

      function updateSearch() {{
        const rawQuery = searchInput.value;
        const query = normalize(rawQuery).trim();

        if (!query) {{
          searchClear.hidden = true;
          searchEmpty.hidden = true;
          searchMeta.innerHTML = '';

          indexedItems.forEach(item => {{ item.el.style.display = ''; }});
          resourceLists.forEach(ul => {{ ul.style.display = ''; }});
          allHeadings.forEach(h => {{ h.style.display = ''; }});
          content.querySelectorAll('p, blockquote, hr, ol').forEach(el => {{ el.style.display = ''; }});
          return;
        }}

        searchClear.hidden = false;
        let matchCount = 0;

        indexedItems.forEach(item => {{
          const match = item.text.includes(query);
          item.el.style.display = match ? '' : 'none';
          if (match) matchCount++;
        }});

        content.querySelectorAll('blockquote, ol, hr').forEach(el => {{ el.style.display = 'none'; }});

        resourceLists.forEach(ul => {{
          const visible = Array.from(ul.children).some(li => li.style.display !== 'none');
          ul.style.display = visible ? '' : 'none';
        }});

        allHeadings.slice().reverse().forEach(heading => {{
          const currentLevel = levels[heading.tagName];
          let sibling = heading.nextElementSibling;
          let hasVisibleContent = false;

          while (sibling) {{
            const sibLevel = levels[sibling.tagName];
            if (sibLevel && sibLevel <= currentLevel) break;
            if (sibling.style.display !== 'none') {{
              hasVisibleContent = true;
            }}
            sibling = sibling.nextElementSibling;
          }}

          heading.style.display = hasVisibleContent ? '' : 'none';

          let pSibling = heading.nextElementSibling;
          while (pSibling && !['H2', 'H3', 'H4', 'UL', 'OL', 'HR'].includes(pSibling.tagName)) {{
            pSibling.style.display = hasVisibleContent ? '' : 'none';
            pSibling = pSibling.nextElementSibling;
          }}
        }});

        if (matchCount === 0) {{
          searchEmpty.hidden = false;
          searchQueryText.textContent = rawQuery;
          searchMeta.innerHTML = '<span>0 resultados encontrados</span>';
        }} else {{
          searchEmpty.hidden = true;
          searchMeta.innerHTML = `<span>Mostrando <span class="count">${{matchCount}}</span> de ${{totalCount}} recursos</span>`;
        }}
      }}

      searchInput.addEventListener('input', updateSearch);

      searchClear.addEventListener('click', () => {{
        searchInput.value = '';
        searchInput.focus();
        updateSearch();
      }});

      if (searchResetBtn) {{
        searchResetBtn.addEventListener('click', () => {{
          searchInput.value = '';
          searchInput.focus();
          updateSearch();
        }});
      }}

      document.addEventListener('keydown', (e) => {{
        if (e.key === '/' && document.activeElement !== searchInput && !['INPUT', 'TEXTAREA'].includes(document.activeElement ? document.activeElement.tagName : '')) {{
          e.preventDefault();
          searchInput.focus();
          searchInput.select();
        }} else if (e.key === 'Escape' && document.activeElement === searchInput) {{
          searchInput.value = '';
          updateSearch();
          searchInput.blur();
        }}
      }});

      if (backToTopBtn) {{
        window.addEventListener('scroll', () => {{
          if (window.scrollY > 350) {{
            backToTopBtn.classList.add('is-visible');
          }} else {{
            backToTopBtn.classList.remove('is-visible');
          }}
        }}, {{ passive: true }});

        backToTopBtn.addEventListener('click', () => {{
          window.scrollTo({{ top: 0, behavior: 'smooth' }});
        }});
      }}
    }});
  </script>
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
