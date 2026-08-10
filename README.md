<!-- Este README es la ÚNICA fuente de la verdad. La web (index.html) se genera con build.py. -->

# Documentación Geomática

> Punto de acceso a **documentación**, **software de fuente abierta** y **recursos** útiles para la **Topografía** y la **Geomática**. El objetivo es ayudar a los **Ingenieros en Geomática y Topografía** a encontrar recursos necesarios para nuestra bonita profesión.

[![Ver la web](https://img.shields.io/badge/Ver_la_web-1f4e79?style=for-the-badge&logo=github&logoColor=white)](https://ingenierogeomatico.github.io/Documentacion_Geomatica/)

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
- [Referencia de funciones PostGIS](https://postgis.net/docs/reference.html) — Documentación oficial de las funciones espaciales SQL (`ST_*`) y operadores de PostGIS.
- [Especificación 3D Tiles (OGC)](https://www.ogc.org/standard/3dtiles/) — Estándar abierto para streaming y renderizado de datos geoespaciales 3D masivos (mallas, nubes de puntos, edificios).

## Software de fuente abierta

Herramientas libres para adquisición, procesado, análisis y publicación de datos geoespaciales.

### SIG de escritorio y campo

- [QGIS](https://qgis.org/) — Sistema de Información Geográfica de escritorio, el estándar libre de facto.
- [GRASS GIS](https://grass.osgeo.org/) — SIG con potente análisis ráster, vectorial y geoespacial.
- [SAGA GIS](https://saga-gis.sourceforge.io/) — Análisis geocientífico, especialmente modelos digitales del terreno.
- [gvSIG Desktop](https://www.gvsig.com/) — SIG de escritorio con fuerte comunidad hispanohablante.
- [QField](https://qfield.org/) — Aplicación móvil basada en QGIS para la captura y edición de datos geoespaciales en campo.
- [Mergin Maps](https://merginmaps.com/) — Plataforma de captura de datos en campo colaborativa con sincronización, integrada con QGIS.
- [WhiteboxTools](https://www.whiteboxgeo.com/) — Plataforma avanzada de geoprocesado y análisis de terreno (geomorfometría, hidrología).

### Geodesia, GNSS y topografía

- [RTKLIB](https://www.rtklib.com/) — Posicionamiento GNSS de precisión (RTK, PPP) de código abierto.
- [RTKLIB-EX (demo5)](https://github.com/rtklibexplorer/RTKLIB) — Fork mantenido de RTKLIB, optimizado para receptores GNSS de bajo coste y constelaciones actuales.
- [GNSS-SDR](https://gnss-sdr.org/) — Receptor GNSS definido por software.
- [Ginan](https://gnss-geodesy.github.io/ginan/) — Toolkit de GNSS de alta precisión (PPP, órbitas/relojes, modelado atmosférico) de Geoscience Australia.
- [Anubis](https://www.pecny.cz/gop/index.php/gnss/anubis/) — Control de calidad y preprocesado de datos RINEX (2/3/4), reemplazo del difunto `teqc`.
- [Emlid / documentación RTK](https://docs.emlid.com/) — Referencia sobre flujos de trabajo RTK/PPK.
- [GNU Gama](https://www.gnu.org/software/gama/) — Ajuste riguroso de redes geodésicas y topográficas por mínimos cuadrados (línea de comandos).

#### Librerías

- 🐍 [pyproj](https://pyproj4.github.io/pyproj/) — Interfaz de Python para PROJ: proyecciones cartográficas y transformación de coordenadas.
- 🐍 [PyGeodesy](https://pypi.org/project/PyGeodesy/) — Cálculos geodésicos elipsoidales y esféricos (distancias, rumbos, intersecciones) en Python puro.
- 🐍 [georinex](https://github.com/geospace-code/georinex) — Lectura rápida de ficheros RINEX (2, 3, 4) de observación y navegación GNSS.
- 🐍 [gnss-lib-py](https://github.com/Stanford-NavLab/gnss_lib_py) — Marco modular para parsear, analizar y visualizar datos GNSS y estimar posición.
- 🟨 [proj4js](https://proj4js.org/) — Transformación de coordenadas entre sistemas de referencia y proyecciones (paquete npm `proj4`).

### Fotogrametría, LiDAR y nubes de puntos

- [OpenDroneMap (ODM / WebODM)](https://www.opendronemap.org/) — Fotogrametría con drones de código abierto.
- [CloudCompare](https://www.cloudcompare.org/) — Edición y comparación de nubes de puntos 3D y mallas.
- [PDAL — Point Data Abstraction Library](https://pdal.io/) — Procesado de nubes de puntos LiDAR.
- [LAStools (open components)](https://rapidlasso.de/) — Herramientas para datos LiDAR en formato LAS/LAZ.
- [Meshroom (AliceVision)](https://alicevision.org/) — Reconstrucción 3D fotogramétrica.
- [Entwine](https://entwine.io/) — Indexado y organización de nubes de puntos masivas para streaming web y escritorio.
- [e-foto](http://efoto.uerj.br/) — Estación fotogramétrica digital completa de código abierto (GPL), orientada a docencia e investigación.

#### Librerías

- 🐍 [COLMAP](https://colmap.github.io/) — Pipeline de Structure-from-Motion (SfM) y Multi-View Stereo (MVS) de propósito general, con bindings de Python (pycolmap).
- [OpenMVG](https://github.com/openMVG/OpenMVG) — Librería de geometría de vistas múltiples centrada en pipelines de SfM (C++).
- [OpenMVS](https://cdcseacave.github.io/openMVS/) — Librería de Multi-View Stereo para reconstrucción densa y mallado (C++), complemento habitual de COLMAP.
- [MicMac](https://micmac.ensg.eu/) — Suite fotogramétrica completa de reconstrucción 3D del IGN francés (C++).
- 🐍 [Open3D](https://www.open3d.org/) — Librería moderna de procesado de datos 3D, mallas y nubes de puntos (Python/C++).
- [PCL — Point Cloud Library](https://pointclouds.org/) — Librería de referencia para procesado de nubes de puntos 2D/3D (C++).
- 🐍 [laspy](https://laspy.readthedocs.io/) — Lectura y escritura de nubes de puntos LiDAR en formato LAS/LAZ desde Python.

### Bases de datos y servidores geoespaciales

- [PostGIS](https://postgis.net/) — Extensión geoespacial para PostgreSQL.
- [SpatiaLite](https://www.gaia-gis.it/fossil/libspatialite/index) — Extensión espacial para SQLite; base de datos geoespacial ligera de fichero único.
- [DuckDB (extensión spatial)](https://duckdb.org/docs/extensions/spatial) — Base de datos analítica en proceso con soporte espacial, muy eficiente para grandes volúmenes.
- [GeoServer](https://geoserver.org/) — Servidor de datos geoespaciales (WMS/WFS/WCS).
- [MapServer](https://mapserver.org/) — Servidor de mapas rápido y ligero.
- [QGIS Server](https://docs.qgis.org/latest/en/docs/server_manual/) — Servicio web OGC (WMS/WFS/WMTS/OGC API) que publica directamente proyectos de QGIS.
- [pgRouting](https://pgrouting.org/) — Análisis de rutas sobre PostGIS.
- [pygeoapi](https://pygeoapi.io/) — Servidor geoespacial en Python que implementa las OGC APIs (Features, Tiles, Coverages, Processes…).
- [Martin](https://martin.maplibre.org/) — Servidor de teselas vectoriales de alto rendimiento en Rust (PostGIS, MBTiles, PMTiles).
- [pg_tileserv](https://github.com/CrunchyData/pg_tileserv) — Servidor de teselas vectoriales MVT ligero, exclusivo para PostGIS, con capas dinámicas por funciones SQL.
- [TiTiler](https://developmentseed.org/titiler/) — Servidor dinámico de teselas ráster para datos cloud-optimized (COG).
- [GeoNetwork](https://geonetwork-opensource.org/) — Catálogo de metadatos geoespaciales (CSW) para infraestructuras de datos espaciales.
- [GeoNode](https://geonode.org/) — Plataforma/CMS geoespacial para gestionar y publicar datos y mapas.

#### Librerías

- 🐍 [psycopg](https://www.psycopg.org/) — Adaptador moderno de PostgreSQL para Python con soporte asyncio (sucesor de psycopg2); base para conectar con PostGIS.
- 🐍 [SQLAlchemy](https://www.sqlalchemy.org/) — Toolkit SQL y ORM estándar de Python.
- 🐍 [GeoAlchemy2](https://geoalchemy-2.readthedocs.io/) — Extensión geoespacial de SQLAlchemy para trabajar con bases de datos como PostGIS.

### Cartografía web y visualización

- [Leaflet](https://leafletjs.com/) — Librería JavaScript ligera para mapas interactivos.
- [OpenLayers](https://openlayers.org/) — Librería JavaScript avanzada para mapas web.
- [MapLibre GL](https://maplibre.org/) — Renderizado de mapas vectoriales por GPU (fork libre de Mapbox GL).
- [API-IDEE](https://github.com/IGN-CNIG/API-IDEE) — API de la Infraestructura de Datos Espaciales de España para crear visualizadores de mapas interoperables.
- [CesiumJS](https://cesium.com/platform/cesiumjs/) — Librería JavaScript de código abierto para visualizadores 3D.
- [iTowns](https://www.itowns-project.org/) — Framework del IGN francés para visualización geoespacial 3D/2D a gran escala en el navegador.
- [Terria.js](https://terria.io/) — Framework para crear catálogos y visores geoespaciales 3D interactivos (sobre Cesium/Leaflet).
- [MapStore](https://mapstore.geosolutionsgroup.com/) — Plataforma para crear aplicaciones WebGIS y geoportales sin programar.

#### Librerías

- 🟨 [Deck.gl](https://deck.gl/) — Framework de alto rendimiento sobre WebGL para explorar y analizar grandes conjuntos de datos geoespaciales.
- 🟨 [Terra Draw](https://terradraw.io/) — Dibujo y edición de geometrías compatible con Leaflet, MapLibre, OpenLayers y otros motores de mapas.
- 🟨 [geojson-vt](https://maplibre.org/geojson-vt/) — Corte eficiente de GeoJSON masivo en teselas vectoriales al vuelo en el navegador.
- 🟨 [geotiff.js](https://geotiffjs.github.io/geotiff.js/) — Lectura y acceso a datos ráster GeoTIFF directamente en navegador o Node.js.
- 🟨 [georaster](https://github.com/geotiffjs/georaster) — Parsea formatos ráster (GeoTIFF, etc.) a una estructura unificada para mapas web.
- 🟨 [PMTiles](https://pmtiles.org/) — Formato de archivo único para pirámides de teselas (ráster o vectoriales) servibles desde almacenamiento en la nube.

### 3D Tiles y visualización 3D

- [3D Tiles Tools (CesiumGS)](https://github.com/CesiumGS/3d-tiles-tools) — Herramientas oficiales para convertir, optimizar, procesar y analizar datos 3D Tiles.
- [Recursos y generadores de 3D Tiles](https://github.com/CesiumGS/3d-tiles/blob/main/RESOURCES.md#generators) — Catálogo oficial de herramientas y librerías para generar tilesets 3D Tiles.

## Librerías de propósito geoespacial

Librerías de programación de uso transversal que no encajan en una única categoría de software. El icono indica el lenguaje: 🐍 Python · 🟨 JavaScript.

### Datos vectoriales y ráster (base)

- 🐍 [GDAL (bindings de Python)](https://pypi.org/project/GDAL/) — Wrapper oficial de Python para GDAL/OGR (módulo `osgeo`); acceso completo a la librería desde Python.
- 🐍 [pyogrio](https://pyogrio.readthedocs.io/) — Wrapper vectorial rápido sobre GDAL/OGR para leer/escribir datos vectoriales en Python.
- 🐍 [Shapely](https://shapely.readthedocs.io/) — Geometría vectorial en Python.
- 🐍 [GeoPandas](https://geopandas.org/) — Análisis de datos geoespaciales en Python.
- 🐍 [Rasterio](https://rasterio.readthedocs.io/) — Lectura/escritura de datos ráster en Python.
- 🐍 [Fiona](https://fiona.readthedocs.io/) — Acceso a formatos vectoriales en Python.
- 🟨 [Turf.js](https://turfjs.org/) — Motor modular de análisis geoespacial sobre GeoJSON en navegador y Node.js.
- 🟨 [JSTS](https://bjornharrtell.github.io/jsts/) — Port a JavaScript de JTS Topology Suite para predicados espaciales y operaciones geométricas.

### Teledetección y análisis ráster

- 🐍 [rioxarray](https://corteva.github.io/rioxarray/) — Extensión geoespacial de Xarray que integra Rasterio con arrays multidimensionales etiquetados.
- 🐍 [xarray](https://docs.xarray.dev/) — Arrays N-dimensionales etiquetados, base para el análisis de datos climáticos y de teledetección.
- 🐍 [rasterstats](https://pythonhosted.org/rasterstats/) — Estadísticas zonales de datos ráster a partir de geometrías vectoriales.
- 🐍 [pystac / pystac-client](https://pystac.readthedocs.io/) — Trabajo con catálogos SpatioTemporal Asset Catalogs (STAC) para descubrir y acceder a datos de observación de la Tierra.
- 🐍 [stackstac](https://stackstac.readthedocs.io/) — Convierte ítems STAC en cubos de datos Xarray de carga perezosa con Dask.
- 🐍 [Satpy](https://satpy.readthedocs.io/) — Lectura, manipulación y escritura de datos de satélites meteorológicos.

### Cartografía temática y visualización

- 🐍 [Cartopy](https://scitools.org.uk/cartopy/) — Procesado de datos geoespaciales y creación de mapas de calidad para publicación.
- 🐍 [contextily](https://contextily.readthedocs.io/) — Añade mapas base de teselas de internet como fondo en gráficos.
- 🐍 [mapclassify](https://mapclassify.readthedocs.io/) — Esquemas de clasificación para mapas coropléticos.
- 🐍 [leafmap](https://leafmap.org/) — Mapas interactivos ligeros para diversos formatos y proveedores de datos geoespaciales.
- 🐍 [geemap](https://geemap.org/) — Análisis y cartografía interactiva específicos para Google Earth Engine.

### Formatos e indexación

- 🟨 [FlatGeobuf](https://flatgeobuf.org/) — Formato geoespacial binario de alto rendimiento para streaming y acceso aleatorio a grandes conjuntos de datos.
- 🟨 [TopoJSON](https://github.com/topojson/topojson) — Extensión de GeoJSON que codifica topología para reducir notablemente el tamaño de los ficheros.
- 🟨 [H3-js](https://uber.github.io/h3-js/) — Port a JavaScript del sistema de indexación geoespacial hexagonal jerárquico H3 de Uber.
- 🟨 [shpjs](https://github.com/calvinmetcalf/shpjs) — Lectura de Shapefiles (SHP, DBF, PRJ) directamente en el navegador o Node.js.
- 🟨 [wkx](https://github.com/cschwarz/wkx) — Parseo y serialización de geometrías en Well-Known Text (WKT) y Well-Known Binary (WKB).

## Herramientas de propósito general

Software libre y librerías que, aunque no son específicamente geomáticos, resultan muy útiles en el día a día: edición de imágenes y vídeo, maquetación de planos, cómputo científico, etc.

### Edición gráfica y multimedia

- [GIMP](https://www.gimp.org/) — Editor de imágenes rasterizadas (retoque fotográfico, texturas, mapas de bits).
- [Inkscape](https://inkscape.org/) — Editor de gráficos vectoriales SVG, ideal para planos, símbolos y maquetación cartográfica.
- [Krita](https://krita.org/) — Pintura digital e ilustración, útil para diseño y edición de texturas.
- [Blender](https://www.blender.org/) — Suite de creación 3D (modelado, renderizado, animación); útil para visualización de modelos y terreno.
- [Kdenlive](https://kdenlive.org/) — Editor de vídeo no lineal, para montar animaciones y presentaciones de resultados.
- [OBS Studio](https://obsproject.com/) — Grabación de pantalla y streaming, útil para tutoriales y documentación audiovisual.

### Cómputo científico (Python)

- [NumPy](https://numpy.org/) — Cálculo numérico con arrays N-dimensionales, base del ecosistema científico de Python.
- [SciPy](https://scipy.org/) — Algoritmos científicos (optimización, álgebra lineal, estadística, interpolación).
- [pandas](https://pandas.pydata.org/) — Análisis y manipulación de datos tabulares.
- [Matplotlib](https://matplotlib.org/) — Creación de gráficos y visualizaciones estáticas y de calidad para publicación.
- [Jupyter](https://jupyter.org/) — Cuadernos interactivos para análisis, prototipado y documentación reproducible.
- [scikit-learn](https://scikit-learn.org/) — Aprendizaje automático de propósito general (clasificación, regresión, clustering).

## Datos y recursos

Fuentes de datos abiertos y recursos de aprendizaje.

- [Directorio de Servicios de la IDEE](https://www.idee.es/segun-tipo-de-servicio) — Catálogo de servicios web geoespaciales (WMS, WFS, WMTS, CSW, etc.) de la Infraestructura de Datos Espaciales de España, organizados por tipo.
- [OpenStreetMap](https://www.openstreetmap.org/) — Cartografía colaborativa libre a escala mundial.
- [Copernicus / Sentinel Hub](https://www.copernicus.eu/) — Datos de observación de la Tierra del programa europeo Copernicus.
- [USGS EarthExplorer](https://earthexplorer.usgs.gov/) — Descarga de imágenes de satélite y modelos del terreno.
- [Natural Earth](https://www.naturalearthdata.com/) — Cartografía base de dominio público a varias escalas.
- [Wikidata](https://www.wikidata.org/) — Base de conocimiento libre con millones de entidades geolocalizadas (coordenadas) consultables vía SPARQL; útil para enriquecer datos SIG con identificadores autoritativos.
- [GeoNames](https://www.geonames.org/) — Base de datos geográfica libre con más de 25 millones de topónimos y sus coordenadas, códigos administrativos y de país.
- [Awesome Geospatial](https://github.com/sacridini/Awesome-Geospatial) — Lista curada de recursos geoespaciales.

---

## Contribuir

¿Conoces un recurso que debería estar aquí? Edita el `README.md` y abre un *pull request*. Recuerda: **el `README.md` es la fuente de la verdad** y la web se regenera automáticamente a partir de él.

## Licencia

El contenido de este repositorio se publica bajo licencia [Creative Commons Attribution 4.0 (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.es).

La tipografía **Chulapa** utilizada en la web es obra del proyecto Madrid-Ferpal del Ayuntamiento de Madrid (Joan Carles Casasín y Pablo Gámez), publicada bajo licencia CC BY 4.0.
