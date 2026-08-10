<!-- Este README es la ÚNICA fuente de la verdad. La web (index.html) se genera con build.py. -->

# Documentación Geomática

> Punto de acceso a **documentación**, **software de fuente abierta** y **recursos** útiles para la **Topografía** y la **Geomática**. El objetivo es ayudar a los **Ingenieros en Geomática y Topografía** a encontrar recursos necesarios para nuestra bonita profesión.

Este repositorio es un directorio vivo y curado de enlaces de interés en el ámbito de la Ingeniería Geomática. El propio `README.md` es la fuente desde la cual se genera automáticamente la web publicada en GitHub Pages.

---

## Documentación y referencia

Manuales, normativa y material formativo de referencia.

- [OSGeo — Open Source Geospatial Foundation](https://www.osgeo.org/) — Fundación que agrupa los principales proyectos geoespaciales libres.
- [Documentación oficial de QGIS](https://docs.qgis.org/) — Manual de usuario, guía de formación y manual de PyQGIS.
- [Documentación de GDAL/OGR](https://gdal.org/) — Librería de referencia para lectura/escritura de datos ráster y vectoriales.
- [PROJ — Transformaciones de coordenadas](https://proj.org/) — Biblioteca para proyecciones y transformaciones de sistemas de referencia.
- [EPSG](https://epsg.org/) — Registro EPSG de sistemas de referencia de coordenadas (CRS).
- [Instituto Geográfico Nacional (IGN España)](https://www.ign.es/) — Cartografía oficial, geodesia, nivelación y redes GNSS.
- [Centro Nacional de Información geográfica (CNIG)](https://www.cnig.es/) — Centro de descargas de datos geográficos oficiales de España.
- [OGC — Open Geospatial Consortium](https://www.ogc.org/) — Estándares abiertos geoespaciales (WMS, WFS, WMTS, GeoPackage, etc.).
- [OGC APIs](https://ogcapi.ogc.org/) — Nueva familia de estándares OGC basados en OpenAPI/REST (Features, Tiles, Maps, Coverages…), el futuro de los servicios geoespaciales.

## Software de fuente abierta

Herramientas libres para adquisición, procesado, análisis y publicación de datos geoespaciales.

### SIG de escritorio

- [QGIS](https://qgis.org/) — Sistema de Información Geográfica de escritorio, el estándar libre de facto.
- [GRASS GIS](https://grass.osgeo.org/) — SIG con potente análisis ráster, vectorial y geoespacial.
- [SAGA GIS](https://saga-gis.sourceforge.io/) — Análisis geocientífico, especialmente modelos digitales del terreno.
- [gvSIG Desktop](https://www.gvsig.com/) — SIG de escritorio con fuerte comunidad hispanohablante.

### Geodesia, GNSS y topografía

- [RTKLIB](https://www.rtklib.com/) — Posicionamiento GNSS de precisión (RTK, PPP) de código abierto.
- [GNSS-SDR](https://gnss-sdr.org/) — Receptor GNSS definido por software.
- [Emlid / documentación RTK](https://docs.emlid.com/) — Referencia sobre flujos de trabajo RTK/PPK.

### Fotogrametría, LiDAR y nubes de puntos

- [OpenDroneMap (ODM / WebODM)](https://www.opendronemap.org/) — Fotogrametría con drones de código abierto.
- [CloudCompare](https://www.cloudcompare.org/) — Edición y comparación de nubes de puntos 3D y mallas.
- [PDAL — Point Data Abstraction Library](https://pdal.io/) — Procesado de nubes de puntos LiDAR.
- [LAStools (open components)](https://rapidlasso.de/) — Herramientas para datos LiDAR en formato LAS/LAZ.
- [Meshroom (AliceVision)](https://alicevision.org/) — Reconstrucción 3D fotogramétrica.

### Bases de datos y servidores geoespaciales

- [PostGIS](https://postgis.net/) — Extensión geoespacial para PostgreSQL.
- [GeoServer](https://geoserver.org/) — Servidor de datos geoespaciales (WMS/WFS/WCS).
- [MapServer](https://mapserver.org/) — Servidor de mapas rápido y ligero.
- [pgRouting](https://pgrouting.org/) — Análisis de rutas sobre PostGIS.
- [pygeoapi](https://pygeoapi.io/) — Servidor geoespacial en Python que implementa las OGC APIs (Features, Tiles, Coverages, Processes…).

### Cartografía web y visualización

- [Leaflet](https://leafletjs.com/) — Librería JavaScript ligera para mapas interactivos.
- [OpenLayers](https://openlayers.org/) — Librería JavaScript avanzada para mapas web.
- [MapLibre GL](https://maplibre.org/) — Renderizado de mapas vectoriales por GPU (fork libre de Mapbox GL).
- [API-IDEE](https://github.com/IGN-CNIG/API-IDEE) — API de la Infraestructura de Datos Espaciales de España para crear visualizadores de mapas interoperables.
- [CesiumJS](https://cesium.com/platform/cesiumjs/) — Librería JavaScript de código abierto para visualizadores 3D.

### Librerías Python

- [GDAL (bindings de Python)](https://pypi.org/project/GDAL/) — Wrapper oficial de Python para GDAL/OGR (módulo `osgeo`); acceso completo a la librería desde Python.
- [pyogrio](https://pyogrio.readthedocs.io/) — Wrapper vectorial rápido sobre GDAL/OGR para leer/escribir datos vectoriales en Python.
- [Shapely](https://shapely.readthedocs.io/) — Geometría vectorial en Python.
- [GeoPandas](https://geopandas.org/) — Análisis de datos geoespaciales en Python.
- [Rasterio](https://rasterio.readthedocs.io/) — Lectura/escritura de datos ráster en Python.
- [Fiona](https://fiona.readthedocs.io/) — Acceso a formatos vectoriales en Python.

### Librerías JavaScript

- [Turf.js](https://turfjs.org/) — Motor modular de análisis geoespacial sobre GeoJSON en navegador y Node.js.
- [proj4js](https://proj4js.org/) — Transformación de coordenadas entre sistemas de referencia y proyecciones (paquete npm `proj4`).
- [JSTS](https://bjornharrtell.github.io/jsts/) — Port a JavaScript de JTS Topology Suite para predicados espaciales y operaciones geométricas.
- [Deck.gl](https://deck.gl/) — Framework de alto rendimiento sobre WebGL para explorar y analizar grandes conjuntos de datos geoespaciales.
- [geojson-vt](https://maplibre.org/geojson-vt/) — Corte eficiente de GeoJSON masivo en teselas vectoriales al vuelo en el navegador.
- [Terra Draw](https://terradraw.io/) — Dibujo y edición de geometrías compatible con Leaflet, MapLibre, OpenLayers y otros motores de mapas.
- [geotiff.js](https://geotiffjs.github.io/geotiff.js/) — Lectura y acceso a datos ráster GeoTIFF directamente en navegador o Node.js.
- [FlatGeobuf](https://flatgeobuf.org/) — Formato geoespacial binario de alto rendimiento para streaming y acceso aleatorio a grandes conjuntos de datos.

## Datos y recursos

Fuentes de datos abiertos y recursos de aprendizaje.

- [Directorio de Servicios de la IDEE](https://www.idee.es/segun-tipo-de-servicio) — Catálogo de servicios web geoespaciales (WMS, WFS, WMTS, CSW, etc.) de la Infraestructura de Datos Espaciales de España, organizados por tipo.
- [OpenStreetMap](https://www.openstreetmap.org/) — Cartografía colaborativa libre a escala mundial.
- [Copernicus / Sentinel Hub](https://www.copernicus.eu/) — Datos de observación de la Tierra del programa europeo Copernicus.
- [USGS EarthExplorer](https://earthexplorer.usgs.gov/) — Descarga de imágenes de satélite y modelos del terreno.
- [Natural Earth](https://www.naturalearthdata.com/) — Cartografía base de dominio público a varias escalas.
- [Awesome Geospatial](https://github.com/sacridini/Awesome-Geospatial) — Lista curada de recursos geoespaciales.

---

## Contribuir

¿Conoces un recurso que debería estar aquí? Edita el `README.md` y abre un *pull request*. Recuerda: **el `README.md` es la fuente de la verdad** y la web se regenera automáticamente a partir de él.

## Licencia

El contenido de este repositorio se publica bajo licencia [Creative Commons Attribution 4.0 (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.es).

La tipografía **Chulapa** utilizada en la web es obra del proyecto Madrid-Ferpal del Ayuntamiento de Madrid (Joan Carles Casasín y Pablo Gámez), publicada bajo licencia CC BY 4.0.
