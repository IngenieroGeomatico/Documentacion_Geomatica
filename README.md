<!-- Este README es la ÚNICA fuente de la verdad. La web (index.html) se genera con build.py. -->

# Documentación Geomática

> Punto de acceso a **documentación**, **software de fuente abierta** y **recursos** útiles para la **Topografía** y la **Geomática**. El objetivo es ayudar a los **Ingenieros en Geomática y Topografía** a encontrar recursos necesarios para nuestra bonita profesión.

<!-- WEB-EXCLUDE:START -->
[![Ver la web](https://img.shields.io/badge/Ver_la_web-1f4e79?style=for-the-badge&logo=github&logoColor=white)](https://ingenierogeomatico.github.io/Documentacion_Geomatica/)
<!-- WEB-EXCLUDE:END -->

Este repositorio es un directorio vivo y curado de enlaces de interés en el ámbito de la Ingeniería Geomática. El propio `README.md` es la fuente desde la cual se genera automáticamente la web publicada en GitHub Pages.

---

### 📑 Índice de contenidos

1. [Documentación y referencia oficial](#1-documentación-y-referencia-oficial)
2. [Estándares, formatos y servicios web](#2-estándares-formatos-y-servicios-web)
3. [Software SIG, topografía y 3D](#3-software-sig-topografía-y-3d)
4. [Bases de datos, servidores y backend geoespacial](#4-bases-de-datos-servidores-y-backend-geoespacial)
5. [Cartografía web, visualizadores y movilidad](#5-cartografía-web-visualizadores-y-movilidad)
6. [Ecosistema de librerías de desarrollo](#6-ecosistema-de-librerías-de-desarrollo)
7. [Herramientas de propósito general](#7-herramientas-de-propósito-general)
8. [Datos y recursos abiertos](#8-datos-y-recursos-abiertos)
9. [Aprendizaje y práctica de programación](#9-aprendizaje-y-práctica-de-programación)
10. [Inteligencia artificial (IA) de fuente abierta](#10-inteligencia-artificial-ia-de-fuente-abierta)
11. [Proyectos propios](#11-proyectos-propios)

---

## 1. Documentación y referencia oficial

Organismos, fundaciones, especificaciones y manuales técnicos de referencia.

- [OSGeo — Open Source Geospatial Foundation](https://www.osgeo.org/) — Fundación que agrupa y da soporte a los principales proyectos geoespaciales libres.
- [OGC — Open Geospatial Consortium](https://www.ogc.org/) — Organización internacional que define los estándares abiertos de interoperabilidad geoespacial.
- [Instituto Geográfico Nacional (IGN España)](https://www.ign.es/) — Organismo oficial responsable de geodesia, cartografía oficial, nivelación y redes GNSS en España.
- [Centro Nacional de Información Geográfica (CNIG)](https://www.cnig.es/) — Centro de descargas y difusión de datos geográficos oficiales de España.
- [Documentación oficial de QGIS](https://docs.qgis.org/) — Manuales de usuario, guías de formación y documentación de PyQGIS.
- [Documentación de GDAL/OGR](https://gdal.org/) — Librería de referencia para lectura, transformación y escritura de datos ráster y vectoriales.
- [PROJ — Transformaciones de coordenadas](https://proj.org/) — Biblioteca base para conversiones y transformaciones de sistemas de referencia de coordenadas.
- [Referencia de funciones PostGIS](https://postgis.net/docs/reference.html) — Documentación oficial de las funciones SQL espaciales (`ST_*`) y operadores de PostGIS.
- [Cloud-Native Geospatial Guide](https://guide.cloudnativegeo.org/) — Guía de referencia sobre la arquitectura y formatos geoespaciales optimizados para la nube.

---

## 2. Estándares, formatos y servicios web

Especificaciones de formatos de datos, sistemas de referencia y protocolos de intercambio geoespacial.

### Formatos vectoriales

- [GeoJSON](https://geojson.org/) — Formato de intercambio geoespacial abierto basado en JSON (IETF, RFC 7946).
- [GeoPackage](https://www.geopackage.org/) — Contenedor abierto y ligero basado en SQLite para almacenar datos vectoriales y ráster (OGC).
- [FlatGeobuf](https://flatgeobuf.org/) — Formato binario de alto rendimiento basado en FlatBuffers para streaming y acceso espacial indexado (cloud-native).
- [GeoParquet](https://geoparquet.org/) — Formato columnar binario optimizado para analítica geoespacial masiva sobre Apache Parquet.
- [Vector Tiles (MVT)](https://github.com/mapbox/vector-tile-spec) — Especificación binaria de teselas vectoriales para renderizado web eficiente por GPU (Mapbox / de facto).
- [Shapefile](https://www.esri.com/library/whitepapers/pdfs/shapefile.pdf) — Formato clásico multiactivo de Esri para geometría y atributos (estándar de facto).
- [GML](https://www.ogc.org/standards/gml/) — Geography Markup Language: codificación XML para modelar y transportar entidades geográficas (OGC/ISO).
- [KML](https://www.ogc.org/standards/kml/) — Keyhole Markup Language: gramática XML para visualización en globos virtuales y visualizadores (OGC).
- [WKT / WKB](https://www.ogc.org/standards/sfa/) — Well-Known Text y Well-Known Binary para representación textual y binaria de geometrías (OGC/ISO).

### Formatos ráster y multidimensionales

- [GeoTIFF](https://www.ogc.org/standards/geotiff/) — Formato TIFF extendido con metadatos de georreferenciación (OGC).
- [Cloud Optimized GeoTIFF (COG)](https://www.cogeo.org/) — GeoTIFF organizado internamente en teselas y pirámides para lectura por rangos HTTP en la nube.
- [NetCDF](https://www.unidata.ucar.edu/software/netcdf/) — Formato autodescriptivo para matrices y datos científicos multidimensionales (Unidata).
- [Zarr](https://zarr.dev/) — Formato de almacenamiento de arrays N-dimensionales comprimidos en bloques particionados (OGC Community Standard).

### Nubes de puntos y 3D

- [LAS/LAZ](https://www.asprs.org/divisions-committees/lidar-division/laser-file-format-exchange-activities) — Formato binario estándar para el intercambio de datos LiDAR y su variante comprimida LAZ (ASPRS).
- [COPC](https://copc.io/) — Cloud Optimized Point Cloud: nube de puntos LAS/LAZ estructurada espacialmente para streaming en la nube.
- [3D Tiles](https://www.ogc.org/standard/3dtiles/) — Especificación para streaming y renderizado jerárquico (LOD) de modelos 3D, mallas, nubes de puntos y Gaussian/Triangle Splats mediante glTF (OGC).
- [glTF / KHR_gaussian_splatting](https://www.khronos.org/news/press/gltf-gaussian-splatting-press-release) — Estándar de transmisión de escenas 3D (glTF 2.0) y extensión oficial para splatting y radiometría.

### Servicios web OGC clásicos

- [WMS](https://www.ogc.org/standards/wms/) — Web Map Service: solicitud de imágenes de mapa prerrenderizadas georreferenciadas.
- [WMTS](https://www.ogc.org/standards/wmts/) — Web Map Tile Service: servicio de teselas de imagen de mapa en cuadrículas predefinidas.
- [TMS](https://wiki.osgeo.org/wiki/Tile_Map_Service_Specification) — Tile Map Service: especificación de la OSGeo para servicio de teselas mediante estructura de URLs predecibles.
- [WFS](https://www.ogc.org/standards/wfs/) — Web Feature Service: consulta y descarga de datos vectoriales a nivel de entidad/geometría.
- [WCS](https://www.ogc.org/standards/wcs/) — Web Coverage Service: acceso a datos ráster brutos y coberturas multidimensionales con sus valores numéricos.
- [CSW](https://www.ogc.org/standards/cat/) — Catalogue Service for the Web: publicación y consulta de catálogos de metadatos geoespaciales.
- [WPS](https://www.ogc.org/standards/wps/) — Web Processing Service: ejecución de procesos y análisis espaciales en remoto.
- [SOS](https://www.ogc.org/standards/sos/) — Sensor Observation Service: consulta e intercambio de observaciones y lecturas de sensores.

### OGC APIs y catálogos modernos

- [OGC APIs](https://ogcapi.ogc.org/) — Familia modular de estándares RESTful basados en OpenAPI y JSON (Features, Tiles, Maps, Coverages, Processes, Records).
- [STAC — SpatioTemporal Asset Catalog](https://stacspec.org/) — Especificación comunitaria moderna para catalogar, buscar e indexar imágenes de satélite y datos de observación.

### Sistemas de referencia y metadatos

- [EPSG](https://epsg.org/) — Registro oficial y autoritativo de sistemas de referencia de coordenadas (CRS), elipsoides, datums y transformaciones.
- [WKT-CRS (ISO 19162)](https://www.iso.org/standard/74039.html) — Estándar para la representación textual de sistemas de referencia de coordenadas.
- [ISO 19115](https://www.iso.org/standard/53798.html) — Estándar internacional que define el esquema de metadatos para la información geográfica.
- [INSPIRE](https://inspire.ec.europa.eu/) — Directiva europea que establece las normas para la Infraestructura de Información Espacial en la UE.

---

## 3. Software SIG, topografía y 3D

Aplicaciones de escritorio, herramientas de campo y suites de procesado técnico.

### SIG de escritorio

- [QGIS](https://qgis.org/) — El Sistema de Información Geográfica de escritorio de referencia en el mundo de código abierto.
- [GRASS GIS](https://grass.osgeo.org/) — SIG avanzado con potente motor de modelado espacial, análisis ráster y vectorial.
- [SAGA GIS](https://saga-gis.sourceforge.io/) — SIG orientado al análisis geocientífico, geomorfometría y modelos digitales del terreno (MDT).
- [gvSIG Desktop](https://www.gvsig.com/) — SIG de escritorio libre con amplia trayectoria y fuerte comunidad hispanohablante.
- [WhiteboxTools](https://www.whiteboxgeo.com/) — Plataforma de geoprocesamiento de alto rendimiento para análisis geoespacial, hidrológico y de relieve.
- [Orfeo ToolBox (OTB)](https://www.orfeo-toolbox.org/) — Suite para procesado digital de imágenes de teledetección (clasificación, segmentación y ortorrectificación).
- [Marble](https://marble.kde.org/) — Globo virtual y atlas interactivo de escritorio (KDE), ideal para docencia y visualización.
- [GeoLibre](https://geolibre.app/) — Plataforma SIG ligera y cloud-native que corre en navegador, escritorio, móvil y Jupyter para visualizar, explorar y analizar datos geoespaciales (MapLibre GL JS, DuckDB-WASM, deck.gl).
- [RustGIS](https://github.com/opengeos/RustGIS) — SIG rápido y de código abierto escrito en Rust puro para cartografía, análisis y compartición de datos geoespaciales (escritorio y navegador web).

### Trabajo de campo y movilidad

- [QField](https://qfield.org/) — Aplicación móvil para Android e iOS basada en el motor de QGIS para toma de datos y edición en campo.
- [Mergin Maps](https://merginmaps.com/) — Plataforma de captura y sincronización colaborativa de datos de campo integrada con QGIS.

### Geodesia, GNSS y topografía

- [RTKLIB](https://www.rtklib.com/) — Paquete de programas para posicionamiento GNSS de precisión (RTK, DGPS, PPP) de código abierto.
- [RTKLIB-EX (demo5)](https://github.com/rtklibexplorer/RTKLIB) — Fork mantenido de RTKLIB, optimizado para receptores GNSS de bajo coste y constelaciones modernas.
- [GNSS-SDR](https://gnss-sdr.org/) — Receptor GNSS de radio definida por software (SDR) multiconstelación y multifrecuencia.
- [Ginan](https://gnss-geodesy.github.io/ginan/) — Toolkit de procesamiento GNSS de alta precisión (PPP, órbitas, relojes y troposfera) de Geoscience Australia.
- [Anubis](https://www.pecny.cz/gop/index.php/gnss/anubis/) — Herramienta para control de calidad, análisis y preprocesado de ficheros RINEX (versiones 2, 3 y 4).
- [GNU Gama](https://www.gnu.org/software/gama/) — Ajuste riguroso de redes geodésicas y topográficas 1D, 2D y 3D por mínimos cuadrados.
- [Emlid RTK Docs](https://docs.emlid.com/) — Guías y documentación práctica sobre flujos de trabajo con receptores GNSS RTK/PPK.

### Fotogrametría, LiDAR y mallas 3D

- [OpenDroneMap (ODM / WebODM)](https://www.opendronemap.org/) — Ecosistema completo para fotogrametría con drones (ortomosaicos, modelos 3D y nubes de puntos).
- [COLMAP](https://colmap.github.io/) — Pipeline y suite de Structure-from-Motion (SfM incremental y global GLOMAP) con Multi-View Stereo (MVS) de alta precisión.
- [CloudCompare](https://www.cloudcompare.org/) — Software de referencia para visualización, edición, registro y comparación de nubes de puntos 3D y mallas.
- [MeshLab](https://www.meshlab.net/) — Sistema avanzado de procesamiento, filtrado, limpieza, inspección y renderizado de mallas 3D y nubes de puntos.
- [Meshroom (AliceVision)](https://alicevision.org/) — Suite de reconstrucción 3D fotogramétrica basada en pipelines nodales de Structure-from-Motion.
- [Regard3D](https://www.regard3d.org/) — Programa de fotogrametría de escritorio con interfaz gráfica intuitiva basado en OpenMVG/OpenMVS.
- [PDAL — Point Data Abstraction Library](https://pdal.io/) — Librería y suite CLI para filtrado, conversión y procesado de nubes de puntos LiDAR.
- [LAStools (open components)](https://rapidlasso.de/) — Herramientas para manipulación y compresión de datos LiDAR en formato LAS/LAZ.
- [Entwine](https://entwine.io/) — Indexador y generador de pirámides octree para nubes de puntos masivas (base de EPT/COPC).
- [e-foto](http://efoto.uerj.br/) — Estación fotogramétrica digital completa (GPL) orientada a la enseñanza e investigación.
- [PerfectTIN](https://github.com/phma/perfecttin) — Herramienta para convertir nubes de puntos en mallas de triángulos irregulares (TIN).
- [Hugin](https://hugin.sourceforge.io/) — Software de ensamblado panorámico con calibración de parámetros ópticos y corrección de distorsión de lentes.
- [Triangle Splatting](https://trianglesplatting.github.io/) — Representación de campos de radiancia (*radiance fields*) mediante microtriángulos; optimizada para renderizado en tiempo real y compatibilidad directa con mallas poligonales y motores gráficos.
- [nerfstudio](https://docs.nerf.studio/) — Framework modular para reconstrucción 3D y renderizado volumétrico mediante NeRF, 3D Gaussian Splatting (3DGS) y exportación a mallas/splats.
- [3D Tiles Tools](https://github.com/CesiumGS/3d-tiles-tools) — Utilidades oficiales de Cesium para optimizar, validar y convertir conjuntos de datos 3D Tiles.
- [obj23dtiles](https://github.com/PrincessGod/obj23dtiles) — Conversor de modelos 3D (OBJ, glTF, GLB) a 3D Tiles (`b3dm` / `tileset.json`) con optimización de cajas envolventes (*bounding boxes*) y LOD.
- [Recursos y generadores de 3D Tiles](https://github.com/CesiumGS/3d-tiles/blob/main/RESOURCES.md#generators) — Catálogo curado de herramientas para generar tilesets 3D Tiles.

### Calibración de cámaras y visión por computador

- [mrcal](https://mrcal.secretsauce.net/) — Toolkit del NASA JPL para calibración rigurosa de cámaras, modelado de incertidumbre y optimización fotogramétrica.
- [Kalibr](https://github.com/ethz-asl/kalibr) — Toolbox del ETH Zurich para calibración precisa intrínseca/extrínseca multicámara y sincronización visual-inercial (cámara-IMU).
- [Camodocal](https://github.com/hengli/camodocal) — Calibración para modelos de cámara omnidireccionales, gran angular y ojos de pez (*fisheye*).
- [AprilTag](https://april.eecs.umich.edu/software/apriltag) — Sistema de dianas y marcadores visuales fiduciales para calibración de alta precisión, orientación y seguimiento.

### Entornos y distribuciones preparadas

- [OSGeoLive](https://live.osgeo.org/) — Distribución Linux en vivo (Lubuntu) con todo el stack de software geoespacial preinstalado y configurado.
- [OSGeo4W](https://trac.osgeo.org/osgeo4w/) — Instalador modular para Windows de paquetes OSGeo (QGIS, GDAL/OGR, GRASS, Python...).

---

## 4. Bases de datos, servidores y backend geoespacial

Infraestructura backend para almacenamiento, consulta, publicación y geoprocesamiento de datos espaciales.

### Bases de datos espaciales

- [PostGIS](https://postgis.net/) — Extensión espacial para PostgreSQL; el motor de base de datos relacional geoespacial de referencia.
- [SpatiaLite](https://www.gaia-gis.it/fossil/libspatialite/index) — Extensión que añade capacidades espaciales a SQLite; base de datos ligera en un único archivo.
- [DuckDB (extensión spatial)](https://duckdb.org/docs/extensions/spatial) — Base de datos OLAP embebida de alto rendimiento con soporte vectorial y ráster.
- [MobilityDB](https://mobilitydb.com/) — Extensión de PostGIS/PostgreSQL para la gestión de objetos móviles, trayectorias y series temporales.
- [rasdaman](https://rasdaman.org/) — Motor de base de datos y servidor de análisis para cubos de datos ráster multidimensionales masivos.

### Servidores de mapas, datos y APIs

- [GeoServer](https://geoserver.org/) — Servidor de datos geoespaciales en Java de referencia; implementa WMS, WFS, WCS, WMTS y OGC APIs.
- [MapServer](https://mapserver.org/) — Servidor de mapas en C/C++ reconocido por su alta velocidad, bajo consumo y estabilidad.
- [pygeoapi](https://pygeoapi.io/) — Servidor geoespacial en Python que implementa los estándares RESTful de la familia OGC APIs.
- [QGIS Server](https://docs.qgis.org/latest/en/docs/server_manual/) — Servidor que publica proyectos `.qgz` de QGIS como servicios web estándar (WMS, WFS, OGC API).
- [deegree](https://www.deegree.org/) — Framework Java para servicios web OGC e infraestructuras de datos espaciales corporativas.
- [pgRouting](https://pgrouting.org/) — Extensión de PostGIS para análisis de rutas, caminos mínimos y problemas de grafos espaciales.

### Servidores de teselas y optimización en nube

- [Martin](https://martin.maplibre.org/) — Servidor de teselas vectoriales y ráster ultrarrápido escrito en Rust (PostGIS, MBTiles, PMTiles).
- [pg_tileserv](https://github.com/CrunchyData/pg_tileserv) — Servidor ligero en Go para servir teselas vectoriales MVT directamente desde funciones y tablas de PostGIS.
- [TiTiler](https://developmentseed.org/titiler/) — Servidor dinámico en Python para generación y visualización de teselas a partir de formatos COG, STAC y Zarr.
- [GeoWebCache](https://www.geowebcache.org/) — Servidor de caché y aceleración de teselas para servicios WMS/WMTS.
- [VersaTiles](https://versatiles.org/) — Formato de archivo único y servidor de teselas vectoriales de alto rendimiento sin dependencias pesadas.

### Servidores de geoprocesamiento

- [ZOO-Project](https://zoo-project.org/) — Plataforma de geoprocesos de código abierto compatible con WPS y OGC API - Processes con soporte multilenguaje.
- [PyWPS](https://pywps.org/) — Servidor en Python para la publicación y ejecución remota de algoritmos de geoprocesado vía OGC WPS.
- [actinia](https://actinia.mundialis.de/) — API REST de geoprocesado en la nube de alto rendimiento impulsada por el motor de GRASS GIS.

### Catálogos y plataformas integrales

- [GeoNetwork](https://geonetwork-opensource.org/) — Plataforma de catálogo de metadatos espaciales (CSW, ISO 19115/19139, DCAT) para IDEs.
- [GeoNode](https://geonode.org/) — Sistema de gestión de contenidos (CMS) geoespacial para compartir mapas, capas y datos colaborativos.
- [Giswater](https://www.giswater.org/) — Plataforma libre para la gestión de redes de abastecimiento, saneamiento y drenaje urbano sobre PostGIS y EPANET/SWMM.
- [GeoHealthCheck](https://geohealthcheck.org/) — Aplicación de monitorización de disponibilidad, rendimiento y calidad de servicios web OGC.

---

## 5. Cartografía web, visualizadores y movilidad

Librerías cliente para la creación de mapas interactivos en el navegador, motores de enrutamiento y herramientas de estilos.

### Visualizadores y clientes de mapas web

- [Leaflet](https://leafletjs.com/) — Librería JavaScript ligera, modular y amigable para mapas interactivos 2D.
- [OpenLayers](https://openlayers.org/) — Librería JavaScript avanzada y completa para cartografía web con soporte de proyecciones, vectoriales y ráster.
- [MapLibre GL](https://maplibre.org/) — Motor de mapas vectoriales por GPU para web (JS) y móvil (iOS/Android), fork comunitario y libre de Mapbox GL.
- [API-IDEE](https://github.com/IGN-CNIG/API-IDEE) — API oficial del IGN-CNIG para crear visualizadores web interoperables con capas de la IDEE de España.
- [CesiumJS](https://cesium.com/platform/cesiumjs/) — Motor de visualización 3D geoespacial para globos terráqueos interactivos y visualización de 3D Tiles en el navegador.
- [iTowns](https://www.itowns-project.org/) — Framework 3D/2D del IGN francés sobre Three.js para visualización de datos espaciales masivos.
- [Terria.js](https://terria.io/) — Framework para construir portales y visualizadores de datos espaciales complejos sobre CesiumJS y Leaflet.
- [MapStore](https://mapstore.geosolutionsgroup.com/) — Plataforma WebGIS modular para crear geoportales y paneles de control sin programar.
- [GeoMoose](https://geomoose.org/) — Framework ligero para portales cartográficos basados en OpenLayers.
- [Mapbender](https://mapbender.org/) — Framework en PHP/Symfony para administrar y publicar geoportales seguros.

### Geocodificación, rutas y herramientas de OSM

- [Nominatim](https://nominatim.org/) — Motor de geocodificación directa e inversa basado en datos de OpenStreetMap.
- [Photon](https://photon.komoot.io/) — Geocodificador de autocompletado rápido tolerante a erratas basado en Elasticsearch y OSM (Komoot).
- [OSRM (Open Source Routing Machine)](https://project-osrm.org/) — Motor de cálculo de rutas y matrices de distancia ultrarrápido en C++ sobre OpenStreetMap.
- [Valhalla](https://valhalla.github.io/valhalla/) — Motor de enrutamiento multimodal de código abierto (vehículo, bicicleta, peatón, transporte público).
- [osm2pgsql](https://osm2pgsql.org/) — Herramienta esencial para importar y transformar datos de OpenStreetMap a bases de datos PostgreSQL/PostGIS.
- [Overpass API](https://overpass-api.de/) — API de consulta y extracción de subconjuntos específicos de datos de OpenStreetMap.

### Generación de teselas y editores de estilos

- [Maputnik](https://maplibre.org/maputnik/) — Editor visual de hojas de estilo JSON para MapLibre GL y Mapbox GL.
- [Tippecanoe](https://github.com/felt/tippecanoe) — Herramienta CLI de referencia para generar teselas vectoriales multiescala a partir de GeoJSON masivo.
- [Planetiler](https://github.com/onthegomap/planetiler) — Generador en Java capaz de crear un fichero MBTiles planetario completo a partir de OpenStreetMap en pocas horas.
- [OpenMapTiles](https://openmaptiles.org/) — Conjunto de esquemas abiertos y herramientas para generar teselas de base cartográfica mundial.
- [Spreet](https://github.com/maplibre/spreet) — Generador de sprites y atlas de iconos para estilos de MapLibre GL a partir de archivos SVG.
- [Charites](https://github.com/unvt/charites) — Herramienta para diseñar y validar estilos de mapas en formato YAML legible.
- [MapLibre Style Spec](https://maplibre.org/maplibre-style-spec/) — Especificación técnica del formato JSON de estilos cartográficos vectoriales.

---

## 6. Ecosistema de librerías de desarrollo

Librerías y paquetes de programación para construir aplicaciones, análisis y flujos de datos.

> **Iconos de lenguaje:** 🐍 Python · 🟨 JavaScript / TypeScript · ⚙️ C / C++ · 🦀 Rust · ☕ Java

### Manipulación vectorial, geometría y análisis base

- 🐍 [GDAL / OGR (Python)](https://pypi.org/project/GDAL/) — Bindings oficiales del módulo `osgeo` para acceso completo a la librería GDAL/OGR.
- 🐍 [pyogrio](https://pyogrio.readthedocs.io/) — Interfaz vectorial rápida construida sobre GDAL/OGR con soporte directo de DataFrames.
- 🐍 [Shapely](https://shapely.readthedocs.io/) — Manipulación y análisis de geometrías vectoriales 2D y 3D en Python (basado en GEOS).
- 🐍 [GeoPandas](https://geopandas.org/) — Extensión geoespacial de `pandas` para operar con GeoDataFrames y geometrías vectoriales.
- 🐍 [Fiona](https://fiona.readthedocs.io/) — Lectura y escritura ordenada de datos vectoriales en Python basada en OGR.
- 🟨 [Turf.js](https://turfjs.org/) — Colección modular de algoritmos y análisis geoespacial espacial sobre GeoJSON en navegador y Node.js.
- 🟨 [JSTS](https://bjornharrtell.github.io/jsts/) — Port a JavaScript de JTS Topology Suite para predicados espaciales y operaciones de geometría.
- ☕ [GeoTools](https://geotools.org/) — Toolkit estándar de Java para manipulación de datos espaciales, motor base de GeoServer.
- ⚙️ [MDAL](https://mdal.xyz/) — Librería C++ para lectura y procesado de mallas multidimensionales y series temporales (usada por QGIS).
- ⚙️ [SFCGAL](https://sfcgal.org/) — Librería C++ de geometría 3D sobre CGAL; backend del soporte 3D avanzado de PostGIS.
- 🟨 [wkx](https://github.com/cschwarz/wkx) — Parseo y serialización bidireccional de formatos WKT y WKB en JavaScript.
- 🟨 [shpjs](https://github.com/calvinmetcalf/shpjs) — Librería para parsear archivos Shapefile (.zip, .shp, .dbf) en el navegador o backend.
- 🟨 [TopoJSON](https://github.com/topojson/topojson) — Extensión de GeoJSON que codifica topología compartida, reduciendo drásticamente el tamaño de los datos.
- 🟨 [H3-js](https://uber.github.io/h3-js/) — Bindings de JavaScript para el sistema de indexación geoespacial hexagonal jerárquico H3 de Uber.

### Ráster, teledetección y cubos de datos

- 🐍 [Rasterio](https://rasterio.readthedocs.io/) — Lectura, escritura y manipulación de datos ráster en Python basada en GDAL.
- 🐍 [rioxarray](https://corteva.github.io/rioxarray/) — Extensión geoespacial que une Rasterio con arrays multidimensionales etiquetados de xarray.
- 🐍 [xarray](https://docs.xarray.dev/) — Estructuras de datos N-dimensionales etiquetadas, pilar del análisis climático y satelital.
- 🐍 [rasterstats](https://pythonhosted.org/rasterstats/) — Cálculo de estadísticas zonales ráster a partir de geometrías vectoriales.
- 🐍 [pystac / pystac-client](https://pystac.readthedocs.io/) — Librerías en Python para interactuar con catálogos y APIs STAC de imágenes satelitales.
- 🐍 [stackstac](https://stackstac.readthedocs.io/) — Transforma colecciones STAC en cubos de datos xarray con computación distribuida perezosa vía Dask.
- 🐍 [Satpy](https://satpy.readthedocs.io/) — Lectura, calibración y composición de imágenes procedentes de satélites meteorológicos y de observación.
- 🐍 [Open Data Cube](https://www.opendatacube.org/) — Arquitectura abierta para la gestión y análisis temporal de colecciones masivas de observación de la Tierra.
- 🐍 [TorchGeo](https://torchgeo.readthedocs.io/) — Librería de PyTorch con datasets, transformaciones y modelos preentrenados de deep learning geoespacial.
- 🟨 [geotiff.js](https://geotiffjs.github.io/geotiff.js/) — Parser e intérprete de metadatos e imágenes GeoTIFF/COG directamente en JavaScript.
- 🟨 [georaster](https://github.com/geotiffjs/georaster) — Estructura estandarizada para cargar y visualizar formatos ráster en aplicaciones web.

### Geodesia, proyecciones y GNSS

- 🐍 [pyproj](https://pyproj4.github.io/pyproj/) — Interfaz de Python para la librería PROJ: proyecciones cartográficas y transformaciones geodésicas.
- 🐍 [PyGeodesy](https://pypi.org/project/PyGeodesy/) — Funciones trigonométricas y cálculos geodésicos esféricos y elipsoidales en Python puro.
- 🐍 [georinex](https://github.com/geospace-code/georinex) — Lectura y parseo estructurado de ficheros GNSS RINEX (2, 3 y 4) a DataFrames.
- 🐍 [gnss-lib-py](https://github.com/Stanford-NavLab/gnss_lib_py) — Marco modular en Python para procesar, visualizar y resolver estimaciones de posición GNSS.
- 🟨 [proj4js](https://proj4js.org/) — Puerto de PROJ a JavaScript para cálculo de proyecciones y transformación de coordenadas en cliente web.

### Nubes de puntos, fotogrametría y 3D

- 🐍 [laspy](https://laspy.readthedocs.io/) — Lectura, creación y edición de nubes de puntos LiDAR en formato LAS y LAZ desde Python.
- 🐍 [Open3D](https://www.open3d.org/) — Librería moderna para el procesado, registro, filtrado y renderizado de geometrías 3D y nubes de puntos (Python/C++).
- 🐍 [py3dtiles](https://py3dtiles.org/) — Generación, lectura y conversión de conjuntos 3D Tiles y nubes de puntos desde Python.
- 🐍 [triangle-splatting](https://github.com/trianglesplatting/triangle-splatting) — Implementación oficial de Triangle Splatting en Python/CUDA para optimización y renderizado de radiance fields con triángulos.
- 🐍 [gsplat](https://docs.gsplat.studio/) — Librería abierta acelerada en CUDA para rasterización y optimización de 3D Gaussian Splatting (base de nerfstudio y pipelines 3D).
- 🟨 [gltf-pipeline](https://github.com/CesiumGS/gltf-pipeline) — Optimización, compresión Draco y conversión de modelos glTF/GLB para su integración en tilesets 3D Tiles.
- 🐍 [pycolmap](https://github.com/colmap/pycolmap) — Bindings oficiales de Python para el pipeline de reconstrucción de COLMAP.
- 🐍 [OpenSfM](https://github.com/mapillary/OpenSfM) — Pipeline de Structure-from-Motion en Python (Mapillary) para reconstrucción fotogramétrica a gran escala.
- 🐍 [pyRANSAC-3D](https://github.com/leomariga/pyRANSAC-3D) — Ajuste y detección de primitivas geométricas 3D (planos, cilindros, esferas) en nubes de puntos con RANSAC.
- ⚙️ [OpenCV](https://opencv.org/) — Librería de visión artificial de referencia (módulo `calib3d` para calibración con tableros CharuCo/Checkerboard, estéreo y homografías).
- ⚙️ [Ceres Solver](http://ceres-solver.org/) — Optimizador no lineal de Google, motor de Bundle Adjustment y ajuste de haces en COLMAP y herramientas de SfM.
- ⚙️ [OpenMVG](https://github.com/openMVG/OpenMVG) — Librería C++ para geometría de vistas múltiples (Structure-from-Motion).
- ⚙️ [OpenMVS](https://cdcseacave.github.io/openMVS/) — Librería C++ para Multi-View Stereo, densificación y generación de mallas texturizadas 3D.
- ⚙️ [TheiaSfM](https://theia-sfm.org/) — Librería C++ para Structure-from-Motion escalable y rápida con ajuste de haces multithreading.
- ⚙️ [GTSAM](https://gtsam.org/) — Factor graphs en C++ y Python para SLAM visual, estimación de trayectoria y calibración de sensores.
- ⚙️ [MicMac](https://micmac.ensg.eu/) — Suite fotogramétrica libre desarrollada por el IGN francés (ENSG) para investigación y aplicaciones de precisión.
- ⚙️ [PCL — Point Cloud Library](https://pointclouds.org/) — Librería clásica de algoritmos 2D/3D para visión artificial y nubes de puntos.
- ⚙️ [OSSIM](https://ossimlabs.github.io/) — Librería C++ de alto rendimiento para procesamiento fotogramétrico y corrección de imágenes de teledetección.

### Visualización interactiva y cartografía temática

- 🟨 [Deck.gl](https://deck.gl/) — Framework de visualización geoespacial acelerado por GPU (WebGL) para conjuntos de datos masivos.
- 🟨 [Terra Draw](https://terradraw.io/) — Motor de dibujo y edición vectorial de geometrías compatible con Leaflet, MapLibre, OpenLayers y Google Maps.
- 🟨 [geojson-vt](https://maplibre.org/geojson-vt/) — Generador de teselas vectoriales en cliente al vuelo a partir de grandes volúmenes de GeoJSON.
- 🟨 [PMTiles](https://pmtiles.org/) — Implementación JS/TS del formato de archivo único para visualización de pirámides de teselas sin servidor.
- 🟨 [GeoStyler](https://geostyler.org/) — Librería e interfaz gráfica para conversión y edición de estilos cartográficos (SLD, OpenLayers, MapLibre).
- 🐍 [Cartopy](https://scitools.org.uk/cartopy/) — Librería de Python para producción de mapas temáticos de alta calidad cartográfica sobre Matplotlib.
- 🐍 [leafmap](https://leafmap.org/) — Paquete de Python para análisis y visualización interactiva de datos geoespaciales con múltiples backends.
- 🐍 [geemap](https://geemap.org/) — Paquete de Python para análisis interactivo y cartografía con Google Earth Engine.
- 🐍 [contextily](https://contextily.readthedocs.io/) — Descarga y añade mapas base de teselas de internet como capas de fondo en gráficos.
- 🐍 [mapclassify](https://mapclassify.readthedocs.io/) — Clasificación estadística de datos para la elaboración de mapas coropléticos.

### Conexión a bases de datos, APIs y metadatos

- 🐍 [psycopg](https://www.psycopg.org/) — Conector de referencia de PostgreSQL para Python con soporte asíncrono y base para consultas PostGIS.
- 🐍 [SQLAlchemy](https://www.sqlalchemy.org/) — Toolkit SQL y ORM de referencia en Python.
- 🐍 [GeoAlchemy2](https://geoalchemy-2.readthedocs.io/) — Extensión espacial para SQLAlchemy que facilita el modelado de datos geográficos en PostGIS y SpatiaLite.
- 🐍 [OWSLib](https://geopython.github.io/OWSLib/) — Cliente en Python para interactuar y consumir servicios web OGC (WMS, WFS, WCS, CSW, WMTS).
- 🐍 [pygeometa](https://pygeometa.readthedocs.io/) — Generación de metadatos geoespaciales normalizados a partir de esquemas simples en YAML.
- 🐍 [mappyfile](https://mappyfile.readthedocs.io/) — Parseo, modificación y formateo programático de archivos Mapfile de MapServer.

---

## 7. Herramientas de propósito general

Software y librerías transversales que complementan el flujo de trabajo en ingeniería, maquetación, visualización y análisis de datos.

### Edición gráfica, multimedia y 3D

- [ArtCraft (Crafting Apps)](https://getartcraft.com/) — Suite de apps creativas de código abierto escritas en Rust (alternativa a Adobe): edición de imagen, vector, vídeo, PDF, maquetación, CAD, hojas de cálculo y más; funcionan en escritorio y navegador.
- [Inkscape](https://inkscape.org/) — Editor de gráficos vectoriales SVG, indispensable para pulir maquetación de planos, simbología y rotulación.
- [GIMP](https://www.gimp.org/) — Editor de imágenes matriciales para retoque fotográfico, ajuste de texturas y edición de mapas de bits.
- [Krita](https://krita.org/) — Programa de pintura e ilustración digital, útil para retoque artístico y diseño de texturas de terreno.
- [Blender](https://www.blender.org/) — Suite integral de creación 3D (modelado, renderizado y animación); ideal para renders de relieve y modelos de ciudades.
- [Kdenlive](https://kdenlive.org/) — Editor de vídeo no lineal de código abierto para montaje de animaciones, vuelos virtuales y presentaciones.
- [OBS Studio](https://obsproject.com/) — Software de grabación de pantalla y emisión en directo para tutoriales y formación.

### Cómputo científico y análisis de datos

- [NumPy](https://numpy.org/) — Paquete fundamental para computación numérica con arrays multidimensionales en Python.
- [SciPy](https://scipy.org/) — Algoritmos científicos avanzados para optimización, álgebra lineal, transformadas, estadística e interpolación.
- [pandas](https://pandas.pydata.org/) — Librería esencial de análisis y manipulación de datos tabulares en Python.
- [Matplotlib](https://matplotlib.org/) — Creación de visualizaciones estáticas, animadas e interactivas con calidad de publicación.
- [Jupyter](https://jupyter.org/) — Entorno interactivo de cuadernos para cálculo reproducible, prototipado y divulgación técnica.
- [scikit-learn](https://scikit-learn.org/) — Algoritmos de aprendizaje automático clásico (clasificación, regresión, agrupamiento y reducción dimensional).
- [PSPP](https://www.gnu.org/software/pspp/) — Software de análisis estadístico descriptivo e inferencial, alternativa libre a SPSS.

---

## 8. Datos y recursos abiertos

Portales, repositorios de datos geográficos libres y catálogos comunitarios.

- [Directorio de Servicios de la IDEE](https://www.idee.es/segun-tipo-de-servicio) — Directorio oficial de servicios web interoperables (WMS, WFS, WMTS, CSW...) de las administraciones públicas españolas.
- [OpenStreetMap (OSM)](https://www.openstreetmap.org/) — Proyecto cartográfico colaborativo y abierto que proporciona cobertura geográfica global.
- [Copernicus / Sentinel Hub](https://www.copernicus.eu/) — Programa europeo de observación de la Tierra con acceso libre a las constelaciones satelitales Sentinel.
- [USGS EarthExplorer](https://earthexplorer.usgs.gov/) — Portal oficial del USGS para búsqueda y descarga de imágenes Landsat, datos satelitales y modelos de elevación.
- [Natural Earth](https://www.naturalearthdata.com/) — Colección de datos cartográficos vectoriales y ráster de dominio público a múltiples escalas globales.
- [Wikidata](https://www.wikidata.org/) — Base de conocimiento libre con millones de entidades geolocalizadas consultables mediante SPARQL.
- [GeoNames](https://www.geonames.org/) — Base de datos geográfica con más de 25 millones de topónimos, coordenadas y códigos administrativos mundiales.
- [Awesome Geospatial](https://github.com/sacridini/Awesome-Geospatial) — Lista comunitaria internacional con cientos de proyectos y librerías geoespaciales.

---

## 9. Aprendizaje y práctica de programación

Sitios web, plataformas y retos para aprender a programar, practicar algoritmos y mejorar tus habilidades de código.

### Referencia y tutoriales

- [W3Schools](https://www.w3schools.com/) — Tutoriales y referencia de HTML, CSS, JavaScript, SQL, Python y más, con ejemplos interactivos "Try it Yourself".
- [MDN Web Docs](https://developer.mozilla.org/) — Documentación web de referencia mantenida por Mozilla (HTML, CSS, JavaScript, Web APIs).
- [freeCodeCamp](https://www.freecodecamp.org/) — Currículo interactivo gratuito basado en proyectos, con certificaciones.
- [The Odin Project](https://www.theodinproject.com/) — Currículo full-stack gratuito y de código abierto basado en proyectos reales.
- [Codecademy](https://www.codecademy.com/) — Lecciones interactivas en el navegador para decenas de lenguajes y tecnologías.
- [Programiz](https://www.programiz.com/) — Tutoriales y compilador online para Python, C, C++, Java y otros lenguajes.
- [GeeksforGeeks](https://www.geeksforgeeks.org/) — Artículos, tutoriales, problemas de programación y preparación de entrevistas.
- [Khan Academy — Computación](https://www.khanacademy.org/computing) — Informática y programación para principiantes con ejercicios interactivos.
- [CS50 (Harvard)](https://cs50.harvard.edu/) — Curso de introducción a la informática y la programación, gratuito y de código abierto.
- [Exercism](https://exercism.org/) — Ejercicios de código con mentoría humana en más de 60 lenguajes.
- [Sololearn](https://www.sololearn.com/) — Aprendizaje interactivo y móvil de programación.
- [Codedex](https://www.codedex.io/) — Aprendizaje gamificado de programación con estética retro.
- [Boot.dev](https://www.boot.dev/) — Currículo backend (Python, Go) basado en proyectos y gamificación.
- [Egghead](https://egghead.io/) — Screencasts cortos y concisos para desarrolladores web.

### Práctica y retos de código

- [Codewars](https://www.codewars.com/) — Katas de programación en muchos lenguajes con ranking y comunidad.
- [LeetCode](https://leetcode.com/) — Problemas de algoritmos y estructuras de datos; preparación de entrevistas técnicas.
- [HackerRank](https://www.hackerrank.com/) — Desafíos de código, concursos y certificaciones por lenguaje.
- [HackerEarth](https://www.hackerearth.com/) — Desafíos, hackathons y problemas de programación competitiva.
- [Edabit](https://edabit.com/) — Retos cortos de código organizados por dificultad.
- [CodingBat](https://codingbat.com/) — Ejercicios de lógica en Java y Python.
- [CheckiO](https://checkio.org/) — Juego de programación en Python y JavaScript resolviendo misiones.
- [CodinGame](https://www.codingame.com/) — Juegos y desafíos multilenguaje para practicar algoritmia de forma lúdica.
- [Project Euler](https://projecteuler.net/) — Problemas matemáticos/computacionales que requieren programación.
- [Advent of Code](https://adventofcode.com/) — Calendario anual de retos de programación (diciembre).
- [Brilliant](https://brilliant.org/) — Matemáticas, ciencia e informática interactiva con problemas guiados.
- [AtCoder](https://atcoder.jp/) — Plataforma de programación competitiva con concursos regulares.
- [Codeforces](https://codeforces.com/) — Comunidad y competiciones de programación competitiva.
- [TopCoder](https://www.topcoder.com/) — Competición algorítmica y desafíos de desarrollo.
- [Kaggle](https://www.kaggle.com/) — Competición y aprendizaje de ciencia de datos y machine learning.

### Code golf (mínimo número de caracteres/bytes)

- [CSSBattle](https://cssbattle.dev/) — Reproducir diseños con el mínimo CSS posible (retos de code golf visual).
- [code.golf](https://code.golf/) — Resolver problemas usando el menor número de bytes en múltiples lenguajes.
- [Code Golf (Stack Exchange)](https://codegolf.stackexchange.com/) — Comunidad y retos de code golf con soluciones explicadas.
- [JS1k](http://js1k.com/) — Demos JavaScript en menos de 1024 bytes (archivo histórico).

### Entornos y editores online

- [VS Code for the Web (vscode.dev)](https://vscode.dev/) — Versión web de Visual Studio Code, editable directamente en el navegador sin instalación.
- [github.dev](https://github.dev/) — Abre cualquier repositorio de GitHub en VS Code web con un atajo de teclado (tecla `.`).
- [StackBlitz](https://stackblitz.com/) — IDE online basado en VS Code para proyectos web y Node.js, con arranque instantáneo.
- [CodeSandbox](https://codesandbox.io/) — Entorno online para prototipado y desarrollo web colaborativo.
- [Gitpod](https://www.gitpod.io/) — Entornos de desarrollo en la nube listos al instante para repositorios.
- [Replit](https://replit.com/) — IDE online colaborativo para múltiples lenguajes.
- [CodePen](https://codepen.io/) — Playground online para HTML, CSS y JavaScript.
- [JSFiddle](https://jsfiddle.net/) — Editor online para prototipado web rápido.
- [Scratch](https://scratch.mit.edu/) — Programación visual por bloques para principiantes y educación.

---

## 10. Inteligencia artificial (IA) de fuente abierta

Recursos, herramientas, modelos y guías para aprovechar la IA en abierto: asistentes y agentes de código, creación de agentes/herramientas/habilidades, servidores MCP (incluidos los geoespaciales), modelos gratuitos, inferencia compatible con OpenAI, *fine-tuning* y fuentes para mantenerse al día.

### Asistentes y agentes de código (fuente abierta)

- [OpenCode](https://opencode.ai/) — Agente de código para terminal con soporte de múltiples proveedores y modelos; permite definir agentes, herramientas y habilidades (skills) en archivos de configuración.
- [Aider](https://aider.chat/) — Asistente de programación en terminal que edita repositorios directamente y se integra con Git.
- [Continue](https://continue.dev/) — Extensión de VS Code/JetBrains para autocompletado y chat con modelos locales o remotos.
- [Cline](https://github.com/cline/cline) — Agente autónomo para VS Code con uso de herramientas, terminal y navegador.
- [Roo Code](https://github.com/RooVetGit/Roo-Code) — Fork evolucionado de Cline con modos/roles personalizables y soporte MCP.
- [Tabby](https://tabbyml.com/) — Asistente de código autoalojado y de código abierto (autocompletado y chat).
- [OpenHands](https://github.com/All-Hands-AI/OpenHands) — Plataforma de agentes de software autónomos (antes OpenDevin) para resolver tareas de desarrollo.
- [SWE-agent](https://github.com/princeton-nlp/SWE-agent) — Framework académico para agentes que resuelven incidencias de repositorios (SWE-bench).
- [GPT Engineer](https://github.com/AntonOsika/gpt-engineer) — Generación de proyectos completos a partir de un prompt.
- [smolagents (Hugging Face)](https://github.com/huggingface/smolagents) — Biblioteca ligera para construir agentes con herramientas y ejecución de código.
- [DSPy](https://github.com/stanfordnlp/dspy) — Framework para programar (no solo *promptear*) sistemas basados en LLMs con optimización automática de prompts.
- [LangChain](https://www.langchain.com/) — Framework para cadenas, agentes, herramientas y RAG sobre LLMs.
- [LangGraph](https://www.langchain.com/langgraph) — Orquestación de agentes con estado y grafos de control (human-in-the-loop, persistencia).
- [LlamaIndex](https://www.llamaindex.ai/) — Framework centrado en ingesta de datos, índices y agentes para RAG y flujos de trabajo.
- [CrewAI](https://www.crewai.com/) — Orquestación de equipos de agentes con roles, tareas y herramientas.
- [AutoGen (Microsoft)](https://github.com/microsoft/autogen) — Framework multiagente conversacional con human-in-the-loop.
- [Semantic Kernel (Microsoft)](https://github.com/microsoft/semantic-kernel) — SDK para integrar LLMs, plugins y memoria en aplicaciones.
- [Haystack (deepset)](https://haystack.deepset.ai/) — Framework para pipelines RAG, agentes y búsqueda semántica.
- [Pydantic AI](https://ai.pydantic.dev/) — Framework de agentes con validación tipada y herramientas declarativas en Python.
- [Mastra](https://mastra.ai/) — Framework de agentes en TypeScript/JavaScript.
- [Agno (Phidata)](https://www.agno.com/) — Framework para agentes con memoria, conocimiento y herramientas.
- [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) — SDK abierto de OpenAI para agentes con *handoffs*, guardrails y trazabilidad.

### Cómo crear agentes, herramientas y habilidades (skills)

- [Documentación de OpenCode](https://opencode.ai/docs) — Guía para configurar agentes, herramientas (tools), habilidades (skills), comandos y MCP en OpenCode.
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) — Especificación abierta para conectar LLMs con herramientas y fuentes de datos externas.
- [MCP — Quickstart (servidores)](https://modelcontextprotocol.io/quickstart/server) — Cómo crear un servidor MCP en Python/TypeScript.
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) — SDK oficial para implementar servidores y clientes MCP en Python.
- [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) — SDK oficial para implementar servidores y clientes MCP en TypeScript.
- [Anthropic — Building effective agents](https://www.anthropic.com/research/building-effective-agents) — Patrones y buenas prácticas para diseñar agentes (workflows vs. agentes, tool use).
- [OpenAI — Function calling / Tools](https://platform.openai.com/docs/guides/function-calling) — Guía de uso de herramientas (function calling) con la API de OpenAI.
- [LangChain — Tools](https://python.langchain.com/docs/concepts/tools/) — Conceptos y creación de herramientas en LangChain.
- [LlamaIndex — Tools](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/tools/) — Herramientas y agentes en LlamaIndex.
- [CrewAI — Tools](https://docs.crewai.com/concepts/tools) — Creación y uso de herramientas en CrewAI.
- [Pydantic AI — Tools](https://ai.pydantic.dev/tools/) — Definición de herramientas tipadas en Pydantic AI.
- [Hugging Face — smolagents tools](https://huggingface.co/docs/smolagents/en/tools) — Cómo definir herramientas para smolagents.
- [DSPy — Signatures & Modules](https://dspy.ai/) — Programación declarativa de módulos y firmas para LLMs.

### Servidores MCP de fuente abierta (incluidos los geoespaciales)

- [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) — Colección de referencia de servidores MCP (filesystem, git, fetch, memory, sequential-thinking, etc.).
- [Awesome MCP Servers](https://github.com/punkpeye/awesome-mcp-servers) — Lista comunitaria de servidores MCP por categoría.
- [MCP Registry / Inspector](https://github.com/modelcontextprotocol/inspector) — Herramienta para inspeccionar y depurar servidores MCP.
- [sparkgeo/geo-mcp-servers](https://github.com/sparkgeo/geo-mcp-servers) — Registro curado de 80+ servidores MCP geoespaciales (geocodificación, rutas, imágenes satelitales, SIG de escritorio, etc.).
- [mahdin75/gis-mcp](https://github.com/mahdin75/gis-mcp) — Servidor MCP de código abierto para operaciones SIG y geoespaciales (geoprocesamiento, geometrías, ráster).
- [jjsantos01/qgis_mcp](https://github.com/jjsantos01/qgis_mcp) — Conecta QGIS con LLMs mediante MCP para controlar una sesión de QGIS.
- [nkarasiak/qgis-mcp](https://github.com/nkarasiak/qgis-mcp) — Alternativa de integración QGIS + MCP.
- [mapbox/mcp-server](https://github.com/mapbox/mcp-server) — Servidor MCP de Mapbox para geocodificación, isocronas, direcciones y mapas.
- [geoserver-mcp](https://github.com/modelcontextprotocol/servers) — Integración con GeoServer vía MCP (gestión de workspaces, capas y estilos) (ver registro de geo-mcp).
- [PostGIS MCP servers](https://github.com/sparkgeo/geo-mcp-servers) — Servidores MCP para consultar bases de datos espaciales PostGIS (ver registro geo-mcp).
- [OSM MCP servers](https://github.com/sparkgeo/geo-mcp-servers) — Servidores MCP para geocodificación, rutas y datos de OpenStreetMap (ver registro geo-mcp).

### Dónde encontrar modelos gratuitos / de código abierto

- [Hugging Face Hub](https://huggingface.co/models) — El mayor repositorio de modelos abiertos (LLMs, visión, audio, embeddings, difusión).
- [Ollama Library](https://ollama.com/library) — Catálogo de modelos listos para ejecutar en local con Ollama.
- [OpenRouter](https://openrouter.ai/models) — Agregador de modelos con modelos gratuitos (free tier) y enrutado unificado.
- [Groq](https://groq.com/) — Inferencia ultrarrápida con capa gratuita (Llama, Mixtral, etc.).
- [Google AI Studio](https://aistudio.google.com/) — Acceso gratuito a modelos Gemini (con límites de uso).
- [Mistral (La Plateforme)](https://mistral.ai/) — Modelos abiertos y API con nivel gratuito.
- [Kaggle Models](https://www.kaggle.com/models) — Modelos preentrenados y datasets para experimentación.
- [ModelScope (Alibaba)](https://modelscope.cn/models) — Repositorio de modelos (especialmente chino) con descarga abierta.
- [LM Studio](https://lmstudio.ai/) — App de escritorio para descargar y ejecutar modelos GGUF locales.
- [Hugging Face — Open LLM Leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard) — Ranking de modelos abiertos por benchmarks.
- [Chatbot Arena / LMSYS](https://lmarena.ai/) — Comparativa ciega de modelos (incluye modelos abiertos).
- [Artificial Analysis](https://artificialanalysis.ai/) — Comparativa de calidad, velocidad y precio de modelos.
- [OSI — Open Source AI Definition](https://opensource.org/ai) — Definición de "IA de código abierto" (OSAID) y criterios.

### Crear tu propio servidor compatible con OpenAI (inferencia local/remota)

- [Ollama](https://ollama.com/) — Ejecuta modelos en local y expone una API compatible con OpenAI (`/v1`).
- [vLLM](https://github.com/vllm-project/vllm) — Motor de inferencia de alto rendimiento con API compatible con OpenAI (PagedAttention, batching).
- [SGLang](https://github.com/sgl-project/sglang) — Motor de inferencia rápido con API compatible con OpenAI y RadixAttention.
- [LocalAI](https://localai.io/) — Reemplazo drop-in de la API de OpenAI que corre modelos locales (LLM, imágenes, audio, embeddings).
- [llama.cpp (llama-server)](https://github.com/ggerganov/llama.cpp) — Inferencia en CPU/GPU con servidor HTTP compatible con OpenAI.
- [text-generation-inference (TGI)](https://github.com/huggingface/text-generation-inference) — Servidor de inferencia de Hugging Face para modelos grandes (API compatible).
- [OpenLLM (BentoML)](https://github.com/bentoml/OpenLLM) — Servir LLMs de código abierto con API compatible con OpenAI y empaquetado Bento.
- [Aphrodite Engine](https://github.com/PygmalionAI/aphrodite-engine) — Motor de inferencia derivado de vLLM con API compatible.
- [TabbyAPI (ExLlamaV2)](https://github.com/theroyallab/tabbyAPI) — API compatible con OpenAI para modelos GGUF/ExLlama.
- [KoboldCpp](https://github.com/LostRuins/koboldcpp) — Servidor local de inferencia con interfaz web y API compatible.
- [text-generation-webui (oobabooga)](https://github.com/oobabooga/text-generation-webui) — Interfaz web y API para ejecutar modelos locales.

### Fine-tuning y entrenamiento

- [Hugging Face Transformers](https://huggingface.co/docs/transformers/) — Librería base para cargar y entrenar modelos.
- [PEFT](https://huggingface.co/docs/peft/) — Métodos eficientes de fine-tuning (LoRA, QLoRA, adapters, prefix tuning).
- [TRL (Transformer Reinforcement Learning)](https://huggingface.co/docs/trl/) — SFT, DPO, PPO, GRPO y RLHF sobre LLMs.
- [Unsloth](https://github.com/unslothai/unsloth) — Fine-tuning 2-5x más rápido y con menos memoria (LoRA/QLoRA) para Llama, Mistral, Gemma, etc.
- [Axolotl](https://github.com/axolotl-ai-cloud/axolotl) — Framework de fine-tuning flexible por configuración YAML.
- [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory) — Interfaz web y CLI para fine-tuning de 100+ LLMs (LoRA, QLoRA, full).
- [torchtune (Meta)](https://github.com/pytorch/torchtune) — Recetas de fine-tuning nativas en PyTorch.
- [MLX (Apple)](https://github.com/ml-explore/mlx) — Framework de Apple para entrenamiento/inferencia en Apple Silicon (incluye MLX-LM).
- [MLX-LM](https://github.com/ml-explore/mlx-examples/tree/main/llms) — Fine-tuning e inferencia de LLMs en Mac.
- [OpenAI Fine-tuning API](https://platform.openai.com/docs/guides/fine-tuning) — Fine-tuning gestionado (no abierto, pero útil para comparar).
- [Together AI — Fine-tuning](https://www.together.ai/) — Fine-tuning gestionado sobre modelos abiertos.
- [Weights & Biases](https://wandb.ai/) — Seguimiento de experimentos y métricas de entrenamiento.
- [MLflow](https://mlflow.org/) — Gestión del ciclo de vida de ML (tracking, modelos, despliegue).
- [DeepSpeed (Microsoft)](https://github.com/microsoft/DeepSpeed) — Optimización de entrenamiento distribuido y ZeRO.

### Bases de datos vectoriales y RAG

- [Chroma](https://www.trychroma.com/) — Base de datos vectorial embebida y de código abierto.
- [Qdrant](https://qdrant.tech/) — Base de datos vectorial de alto rendimiento escrita en Rust.
- [Milvus](https://milvus.io/) — Base de datos vectorial escalable para producción.
- [Weaviate](https://weaviate.io/) — Base de datos vectorial con módulos de IA integrados.
- [LanceDB](https://lancedb.com/) — Base de datos vectorial embebida sobre Apache Arrow/Lance.
- [pgvector](https://github.com/pgvector/pgvector) — Extensión de PostgreSQL para búsqueda vectorial (complementa PostGIS).
- [FAISS (Meta)](https://github.com/facebookresearch/faiss) — Biblioteca de búsqueda de similitud de vectores.
- [RAGFlow](https://github.com/infiniflow/ragflow) — Motor RAG de código abierto con orquestación de flujos.
- [Kotaemon](https://github.com/Cinnamon/kotaemon) — Herramienta de RAG local con interfaz de chat.

### Evaluación, observabilidad y prompts

- [Langfuse](https://langfuse.com/) — Observabilidad y trazabilidad de LLMs (traces, costes, evaluaciones) de código abierto.
- [Arize Phoenix](https://phoenix.arize.com/) — Observabilidad y evaluación de LLMs/RAG de código abierto.
- [Promptfoo](https://www.promptfoo.dev/) — Evaluación y red-teaming de prompts y modelos en CLI.
- [RAGAS](https://docs.ragas.io/) — Métricas de evaluación para pipelines RAG.
- [DeepEval](https://github.com/confident-ai/deepeval) — Framework de evaluación de LLMs (unit tests para IA).
- [Inspect AI (UK AISI)](https://inspect.ai-safety-institute.org.uk/) — Framework de evaluación de capacidades y seguridad de modelos.
- [LiteLLM](https://github.com/BerriAI/litellm) — Proxy unificado compatible con OpenAI para 100+ proveedores (enrutado, costes, fallbacks).
- [OpenRouter](https://openrouter.ai/) — Enrutador de modelos con fallbacks y modelos gratuitos.

### Para estar al día en IA de código abierto

- [Hugging Face Daily Papers](https://huggingface.co/papers) — Papers recientes destacados por la comunidad.
- [Papers With Code](https://paperswithcode.com/) — Papers con código y benchmarks.
- [arXiv (cs.AI, cs.CL, cs.LG)](https://arxiv.org/) — Preprints de investigación en IA.
- [The Batch (DeepLearning.AI)](https://www.deeplearning.ai/the-batch/) — Newsletter semanal de Andrew Ng.
- [Import AI (Jack Clark)](https://importai.substack.com/) — Newsletter sobre avances en IA.
- [Latent Space](https://www.latent.space/) — Podcast y newsletter sobre IA aplicada.
- [r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/) — Comunidad de modelos locales y open source.
- [r/MachineLearning](https://www.reddit.com/r/MachineLearning/) — Investigación y discusión académica.
- [Hugging Face Blog](https://huggingface.co/blog) — Anuncios y guías del ecosistema abierto.
- [Epoch AI](https://epochai.org/) — Análisis de tendencias de cómputo y modelos.
- [LM Arena](https://lmarena.ai/) — Ranking y comparativas actualizadas de modelos.

### IA geoespacial (modelos y herramientas)

- [TorchGeo](https://torchgeo.readthedocs.io/) — Datasets, transformaciones y modelos preentrenados de deep learning geoespacial (PyTorch).
- [segment-anything (SAM / SAM 2)](https://github.com/facebookresearch/segment-anything) — Segmentación de imágenes de propósito general aplicable a ortofotos y satélite.
- [Prithvi (IBM/NASA)](https://huggingface.co/ibm-nasa-geospatial) — Modelos fundacionales para observación de la Tierra.
- [Clay Foundation Model](https://clay-foundation.github.io/model/) — Modelo fundacional para datos de observación de la Tierra.
- [openEO](https://openeo.org/) — API abierta para procesamiento de datos de observación de la Tierra en la nube.
- [Google Earth Engine](https://earthengine.google.com/) — Plataforma de análisis geoespacial (acceso gratuito para investigación/educación).
- [eo-learn](https://github.com/sentinel-hub/eo-learn) — Pipelines de machine learning para datos de observación de la Tierra.

---

## 11. Proyectos propios

Proyectos y herramientas de código abierto desarrollados y mantenidos por [IngenieroGeomatico](https://github.com/IngenieroGeomatico).

- [QGIS2API-IDEE](https://github.com/IngenieroGeomatico/QGIS2API-IDEE) — Complemento para QGIS que exporta y genera un visualizador web interactivo basado en la API-IDEE.
- [serviciosIDEE2QGIS](https://github.com/IngenieroGeomatico/serviciosIDEE2QGIS) — Complemento de QGIS para cargar de forma rápida y sencilla los servicios web de la IDEE (IGN-CNIG).
- [apiidee-agent](https://github.com/IngenieroGeomatico/apiidee-agent) — Asistente y agente en Python para interactuar con las capacidades de la API-IDEE.
- [descarga_limites_administrativos](https://github.com/IngenieroGeomatico/descarga_limites_administrativos) — Flujo automatizado de descarga y homogeneización de límites territoriales de fuentes oficiales.
- [Galeria_de_mapas](https://github.com/IngenieroGeomatico/Galeria_de_mapas) — Catálogo de visualizadores cartográficos web temáticos desarrollados con distintas tecnologías.
- [pygeoapi_complementos](https://github.com/IngenieroGeomatico/pygeoapi_complementos) — Colección de plugins, proveedores y extensiones personalizadas para el servidor pygeoapi.
- [pygdal_PG_datasource](https://github.com/IngenieroGeomatico/pygdal_PG_datasource) — Ejemplos y utilidades para interactuar con orígenes de datos PostGIS mediante GDAL en Python.
- [dockerInstall_PostGIS_GDAL_Pygeoapi_andMore](https://github.com/IngenieroGeomatico/dockerInstall_PostGIS_GDAL_Pygeoapi_andMore) — Entorno de despliegue reproducible en Docker con un stack geoespacial completo (PostGIS, GDAL, pygeoapi...).

---

## Contribuir

¿Conoces un recurso o herramienta de código abierto que debería estar aquí? Edita el `README.md` y abre un *pull request*. Recuerda: **el `README.md` es la única fuente de la verdad** y la web se regenera automáticamente a partir de él.

## Licencia

El contenido de este repositorio se publica bajo licencia [Creative Commons Attribution 4.0 (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.es).

La tipografía **Chulapa** utilizada en la web es obra del proyecto Madrid-Ferpal del Ayuntamiento de Madrid (Joan Carles Casasín y Pablo Gámez), publicada bajo licencia CC BY 4.0.
