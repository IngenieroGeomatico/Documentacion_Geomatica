# Tipografía Chulapa

Los títulos de la web usan la tipografía **Chulapa**, publicada por el
**Ayuntamiento de Madrid** (proyecto Madrid-Ferpal) bajo licencia
**Creative Commons Attribution 4.0 (CC BY 4.0)**.

## ⚠️ Falta añadir los archivos de fuente

La descarga automática desde la web oficial está bloqueada (error 403), así que
los archivos deben añadirse **manualmente** una sola vez. El sitio funciona sin
ellos (los títulos usan una fuente de sistema como alternativa), pero para ver
la estética chulapa real hay que colocarlos aquí.

### Pasos

1. Descarga la tipografía desde la fuente oficial:
   - https://diario.madrid.es/chulapa/
   - (alternativa) https://identidad.madrid.es/tipografias/
2. Descomprime el `.zip`. Obtendrás los pesos **Light**, **Regular** y **Bold**
   en formato `.ttf` (u `.otf`).
3. Copia/renombra los archivos en esta carpeta (`assets/fonts/`) con **estos
   nombres exactos** (los que espera `assets/css/style.css`):

   ```
   assets/fonts/Chulapa-Light.ttf
   assets/fonts/Chulapa-Regular.ttf
   assets/fonts/Chulapa-Bold.ttf
   ```

4. (Recomendado, opcional) Genera versiones `.woff2` para carga más rápida.
   Puedes usar [fonttools](https://github.com/fonttools/fonttools):

   ```bash
   pip install fonttools brotli
   fonttools ttLib.woff2 compress Chulapa-Light.ttf
   fonttools ttLib.woff2 compress Chulapa-Regular.ttf
   fonttools ttLib.woff2 compress Chulapa-Bold.ttf
   ```

   El CSS ya prioriza `.woff2`, luego `.woff` y finalmente `.ttf`, así que con
   solo los `.ttf` ya funciona.

5. Regenera la web:

   ```bash
   python build.py
   ```

## Atribución (obligatoria por CC BY 4.0)

> Tipografía **Chulapa**, con licencia CC BY 4.0.
> Diseñada por Joan Carles Casasín y Pablo Gámez para el Ayuntamiento de Madrid
> (proyecto Madrid-Ferpal), sobre una idea original de Silvia Fernández Palomar.

Ver `LICENSE-Chulapa.txt` en esta misma carpeta.
