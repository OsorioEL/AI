# Description: This script translates the text from English to French and saves the translated text in a PDF file.
from fpdf import FPDF
# Create instance of FPDF class
pdf = FPDF()

# Add a page
pdf.add_page()

# Set font
pdf.set_font("Arial", size = 12)

# Add the translated text
translated_text = """
Disponible en línea en www.sciencedirect.com

Página principal de la revista: www.elsevier.com/locate/dental

Impurezas en implantes dentales comerciales de titanio: un análisis elemental mediante espectrometría de masa y emisión óptica

Andres Strickera, Thomas Bergfeldtb, Tobias Fretwursta, Owen Addisonc, Rainer Schmelzeisena, René Rothweilera, Katja Nelsona, Christian Grossa,⁎

a Departamento de Cirugía Oral y Maxilofacial, Centro Médico – Universidad de Friburgo, Facultad de Medicina, Universidad de Friburgo, Hugstetter Str. 55, 79106 Friburgo de Brisgovia, Alemania
b Instituto de Materiales Aplicados - Física de Materiales Aplicados (IAM-AWP), Instituto de Tecnología de Karlsruhe (KIT), Hermann-von-Helmholtz-Platz 1, 76344 Eggenstein-Leopoldshafen, Alemania
c Centro de Ciencias Orales, Clínicas y Translacionales, Facultad de Odontología, Ciencias Orales y Craneofaciales, King's College London, Guy's Hospital, Great Maze Pond, SE1 9RT Londres, Reino Unido

Información del artículo

Historial del artículo:
- Recibido: 19 de febrero de 2022
- Recibido en forma revisada: 19 de junio de 2022
- Aceptado: 22 de junio de 2022

Palabras clave:
- Titanio
- Implantes dentales
- Implantes de titanio
- Análisis elemental

Resumen

Objetivo: El titanio (Ti) es considerado bioinerte y sigue siendo considerado el material “estándar de oro” para implantes dentales. Sin embargo, incluso el Ti ‘puro comercial’ contendrá fracciones menores de impurezas elementales. La evidencia que demuestra la liberación de iones y partículas de Ti de superficies de implantes ‘pasivas’ está aumentando y se ha atribuido a procesos de biocorrosión que pueden provocar reacciones inmunológicas. Sin embargo, se ha demostrado que el Ti observado en los tejidos periimplantarios está colocalizado con elementos considerados impurezas en aleaciones biomédicas. En consecuencia, este estudio tuvo como objetivo cuantificar la composición de impurezas en implantes dentales comerciales de Ti.

Métodos: Se analizaron quince sistemas comerciales de implantes dentales de titanio utilizando espectrometría de masas con plasma acoplado inductivamente (ICP-MS) y espectrometría de emisión óptica (ICP-OES).

Resultados: La composición elemental de los implantes fabricados a partir de grados puros comerciales de Ti, Ti-6Al-4V y la aleación TiZr (Roxolid) se ajustó a las normas ISO/ASTM respectivas o a los datos del fabricante (TiZr/Roxolid). Sin embargo, todos los implantes investigados incluían contaminantes metálicos exógenos, incluidos Ni, Cr, Sb y Nb en diferentes grados. Otros contaminantes detectados en una fracción de los implantes incluyeron As y los radionúclidos U-238 y Th-232.

Importancia: Aunque todos los estudios de implantes de Ti se ajustaron a sus composiciones estándar, se detectaron metales potencialmente alergénicos, nocivos e incluso radionúclidos. Dado que existen diferencias en el grado de contaminación entre los sistemas de implantes, parece técnicamente evitable una cierta fracción de impurezas. La relevancia clínica de estos hallazgos debe investigarse más a fondo, y se debe discutir una adaptación de las normas de la industria.

© 2022 The Authors. Publicado por Elsevier Inc. en nombre de The Academy of Dental Materials.

CC_BY_NC_ND_4.0

1. Introducción

El titanio (Ti) puro comercial (Cp) y las formas aleadas de Ti han sido consideradas los biomateriales "estándar de oro" para los implantes dentales endoóseos desde que se introdujo la modalidad de tratamiento en la década de 1960 [1,2]. Las características mecánicas y fisicoquímicas de estos materiales están especificadas por la norma 5832 de la Organización Internacional de Normalización (ISO) y la norma ASTM F67-13 de la Sociedad Americana para Pruebas y Materiales (ASTM) [3–5]. Las normas detallan las composiciones elementales requeridas para las diferentes presentaciones de Ti junto con los requisitos técnicos. Actualmente, el Ti biomédico está disponible en cuatro grados comerciales puros (ASTM I-IV) y varias aleaciones, incluida Ti-6Aluminio(Al)-4Vanadio(V) (Ti6Al4V; ASTM Grado V). Para los cuatro grados de CpTi, ISO 5832-2 y F67-13 especifican, junto con Ti, las fracciones máximas de masa elemental de nitrógeno (N) (máx.: 0.012–0.05 % de masa), carbono (C) (máx.: 0.03–0.08 % de masa), hidrógeno (H) (máx.: 0.0125 % de masa), oxígeno (O) (máx.: 0.1–0.4 % de masa) y contenido de hierro (Fe) (máx.: 0.1–0.5 % de masa). Las fracciones de Fe y O aumentan de Grado I a Grado IV Ti y se correlacionan con la mejora de la dureza, el rendimiento y las resistencias a la tracción, pero una disminución en la resistencia a la corrosión. La composición elemental de Grado IV Ti, el grado más comúnmente utilizado comercialmente de Ti en implantes dentales, está estandarizada de la siguiente manera: N: máx. 0.05 % de masa; C: máx. 0.08 % de masa; H: máx. 0.0125 % de masa; Fe: máx. 0.5 % de masa; O: máx. 0.4 % de masa; Ti: balance. Ninguna otra fracción de elemento metálico está especificada o limitada para CpTi en las respectivas normas [3,5].

La aleación alfa-beta Ti6Al4V (Grado V) exhibe mayor resistencia a la tracción y rendimiento (≥ 860 MPa y ≥ 780 MPa, respectivamente) y también se utiliza para la fabricación de implantes dentales comerciales. Cuando una aleación Ti6Al4V cumple con límites inferiores para las fracciones de O (máx. 0.13 % de masa) y Fe (máx. 0.25 % de masa), se denomina "Intersticiales Extra Bajas" (ELI), posee una mayor tenacidad a la fractura y está estandarizada por ASTM F-136 [6]. También se ha introducido en el mercado de implantes dentales una aleación binaria de ~ 85 % de masa de Ti y ~ 15 % de masa de circonio (Zr) para lograr valores más altos de resistencia a la fatiga y a la tracción (Roxolid ®, Straumann). Sin embargo, su composición no está actualmente estandarizada por normas ISO o ASTM [7–9].

Aunque se considera que el Ti y sus aleaciones tienen una alta resistencia a la corrosión bajo condiciones fisiológicas, existe una creciente evidencia de que los iones y partículas de Ti se liberan de los implantes dentales de Ti y pueden estar asociados con reacciones inmunológicas locales y sistémicas, como la inflamación periimplantaria [10–15]. La declaración final de la Conferencia de Consenso de la Asociación Europea de Osteointegración (EAO) de 2018 concluyó a partir de estudios in vitro que las partículas de Ti liberadas en los tejidos periimplantarios en un entorno ácido, como el inducido localmente dentro de biofilms bacterianos acidogénicos, pueden interferir con la homeostasis ósea mediante la activación de osteoclastos y osteoblastos y la secreción de citoquinas por linfocitos y macrófagos [16]. Los datos clínicos sobre alergias asociadas con implantes dentales de titanio se limitan a informes de casos y series de casos como se revisa actualmente [10].

Un estudio reciente investigó la distribución y especiación química de partículas metálicas exógenas encontradas en tejidos inflamados adyacentes a implantes dentales comerciales de Ti y cerámica utilizando fluorescencia de rayos X de radiación sincrotrón (SR-XRF) y espectroscopía de absorción de rayos X (SR-XAS) [17]. Junto con la detección de partículas de Ti y cerámica en el tejido periimplantario de los implantes de Ti y cerámica, los autores informaron la presencia de elementos potencialmente contaminantes como el plomo (Pb) y el arsénico (As). Se ha aceptado ampliamente que las modificaciones topográficas de los implantes dentales, como la abrasión de partículas suspendidas en aire o el grabado ácido utilizado para aumentar la rugosidad de la superficie y mejorar la osteointegración, pueden llevar a la contaminación de la superficie de Ti [18–20]. Varios estudios han utilizado técnicas no destructivas como la microscopía electrónica de barrido (SEM) y la espectroscopía de rayos X dispersiva en energía (EDX) para detectar una variedad de contaminantes orgánicos e inorgánicos en superficies de implantes dentales comerciales [21–23]. Se ha prestado menos atención a la caracterización de la composición elemental del cuerpo del implante. Sin embargo, los análisis de Ti biomédico y aleaciones de Ti han mostrado la presencia de elementos metálicos no descritos en las normas, como el cromo (Cr), molibdeno (Mo) y cobre (Cu) [24].

En un estudio previo, se realizó un análisis elemental de implantes dentales comerciales de zirconia estabilizada con itria utilizando digestión química y una combinación de espectrometría de masas con plasma acoplado inductivamente (ICP-MS) y espectrometría de emisión óptica con plasma acoplado inductivamente (ICP-OES). Las técnicas permitieron determinar la composición elemental de los implantes, incluidos niveles ultra traza (ppb) de contaminantes [25]. Además del Zr, se detectaron varios elementos metálicos, incluidos los radionúclidos torio (Th-232) y uranio (U-238).

En consecuencia, el presente estudio tuvo como objetivo caracterizar las composiciones elementales principales, menores y de traza de una gama de implantes dentales modernos basados en Ti comercial.

Métodos

2.1. Adquisición de muestras

Se examinaron quince sistemas comerciales de implantes dentales de Ti de doce marcas de implantes dentales. Se adquirieron dos implantes por sistema de implante directamente de las respectivas empresas (implantes n = 30; sistemas de implantes n = 15, marcas n = 12). Después de recibir los implantes empaquetados estériles documentados, los implantes se desempacaron bajo un flujo de aire laminar, se desprendieron de los postes o tornillos de inserción con pinzas de plástico, se transfirieron a contenedores de vidrio roscados (AR-GLAS®, Schott AG, Mainz, Alemania) y se indexaron mediante un código de tres dígitos. La metodología analítica fue diseñada y llevada a cabo por el Instituto de Materiales Aplicados - Física de Materiales Aplicados (IAM-AWP) del Instituto de Tecnología de Karlsruhe (KIT). Durante el análisis, los investigadores del IAM-AWP fueron cegados a la designación de la muestra (solo código de tres dígitos = índice ciego de muestra). La Tabla 1 resume los detalles de los implantes investigados.

2.2. Procesamiento preanalítico y digestión de muestras

Para la digestión química, las muestras se cortaron utilizando una cizalla de corte de acero (1 BR/6, Peddinghaus, Alemania) y luego se grabaron con un ácido mezclado (HCl 35 % subhervido, HNO3 65 % subhervido, agua ultrapura (OmniaPure, stakpure GmbH, Niederahr, Alemania)) y HF 40 % suprapuro durante un minuto. Las muestras se subdividieron en tres porciones de 80-190 mg (precisión de pesaje ± 0.25 mg (XP205, Mettler-Toledo, Gießen, Alemania), TiMed1, TiIMed2 y TiZrRox2: debido a la falta de material, solo se realizaron dos réplicas para cada muestra). Cada submuestra se disolvió completamente en 9 mL de ácido mezclado (HCl 35 % subhervido, HNO3 subhervido, agua ultrapura) y 1 mL de HF 40 % suprapuro. Todos los reactivos fueron de grado de espectrometría de masas ultrapura. Cada contenedor de muestra (PFA 50 mL) se calentó en un horno de grafito a 80 °C durante dos horas. Después del calentamiento, la solución acidificada resultante se diluyó a aproximadamente 50 mL con agua ultrapura con el peso exacto de la solución equilibrado. Debido al gran número de submuestras (n = 87) y la composición química parcialmente diferente de algunas muestras, las mediciones cuantitativas se realizaron en cinco series de mediciones (ver diferentes límites de cuantificación (LOQ) en la Tabla B del Apéndice).

2.3. Espectrometría de emisión óptica con plasma acoplado inductivamente (ICP-OES)

Cada solución de muestra se diluyó varias veces según la concentración de los elementos objetivo para el análisis. En lugar de usar métodos de dilución volumétrica, se pesaron la solución de muestra y el agua ultrapura (XP 205, Mettler-Toledo, Gießen, Alemania) para mejorar la precisión. La cuantificación elemental se logró utilizando cuatro soluciones de calibración diferentes y un estándar interno (escandio (Sc)) mediante ICP-OES (iCAP 7600 ICP-OES Duo, Thermo Fisher Scientific Inc., Waltham, MA, EE. UU.). Para elementos menores y de traza, la solución se adaptó a la matriz (Al, Ti, V, Zr, ácido). El rango de las soluciones de calibración se extendió de 0 a 0.2 mg/L. Se utilizaron dos o tres longitudes de onda de emisión de cada elemento para el cálculo de la fracción de masa. Los ajustes del instrumento para el ICP-OES se informan en la Tabla A.1.

2.4. Espectrometría de masas con plasma acoplado inductivamente (ICP-MS)

Se realizó ICP-MS (7500ce ICP-MS, Agilent Technologies Inc., Santa Clara, CA, EE. UU.) para medir la concentración de elementos con menor sensibilidad de detección con ICP-OES. El análisis elemental se logró con cuatro soluciones de calibración adaptadas a la matriz (Al, Ti, V, Zr, ácido) y dos estándares internos (Sc, indio (In)). El rango de la calibración se extendió de 0.01 a 4.0 µg/L (variando según cada elemento) e involucró el área de la concentración de las muestras. Se utilizaron una, dos o tres masas de los elementos para el cálculo. Los ajustes del instrumento para el ICP-MS se informan en la Tabla A.2.

2.5. Control de calidad

Las soluciones de calibración ICP certificadas (Aesar, Thermo Fisher (Kandel) GmbH, Karlsruhe, Alemania) se controlaron con otra solución ICP certificada de un productor diferente (Merck, Darmstadt, Alemania). La recuperación de estos estándares en soluciones adaptadas a la matriz estuvo entre 90 % y 110 %.

2.6. Cálculos y estadísticas descriptivas

Los resultados de ICP-MS/OES se informan como media, desviación estándar (SD) e incertidumbre de medición (±). Se da el límite de cuantificación (LOQ) respectivo para cada muestra (Tabla C del Apéndice). Los resultados se visualizaron en mg/kg (ppm) y porcentaje en masa (masa%) en gráficos de barras apiladas. Se utilizó IBM SPSS Statistics (versión 25.0, lanzada en 2017, IBM Corp., Armonk, NY, EE. UU.) para estadísticas descriptivas. Los resultados (media, SD) se han redondeado para una mejor visión general.

3. Resultados

Todos los resultados de los análisis elementales ICP-MS y ICP-OES se muestran en las Tablas B.1–6 y se visualizan selectivamente en las Figuras 1–4. Las abreviaturas de los elementos se presentan en la lista de abreviaturas.

3.1. Componentes principales

El Ti fue el componente principal; sin embargo, se detectaron múltiples otros elementos metálicos en todas las muestras. La fracción no normalizada de Ti en las muestras de implantes comercialmente puros promedió 1009 ppm (SD: 534). Las muestras de implantes de aleación binaria TiZr TiZrRox1 y TiZrRox2 (Roxolid) presentaron una fracción normalizada de Zr con una media del 14.2 % de masa (media: 142,000 ppm, SD: 6530) y una fracción normalizada no de Ti, no de Zr que promedió 493 ppm. Las muestras de implantes Ti6Al4V Ti6Al4VMis1 y Ti6Al4VMis2 (MIS C1B) presentaron una fracción normalizada de Al que promedió 6.16 % de masa (media: 61,600 ppm, SD: 44 ppm), una fracción normalizada de V con una media del 4.01 % de masa (media: 40,100 ppm, SD: 29 ppm) y una fracción normalizada de impurezas que promedió 2260 ppm. Los valores absolutos de resultados para los componentes principales y las fracciones de impurezas se dan en las Tablas B.1–6.

3.2. Contaminación menor, traza y ultra-traza con elementos metálicos

La fracción más grande de los constituyentes menores fue Fe, encontrado en todas las muestras de implantes investigadas y promedió un 0.071 % de masa (absoluto; media: 708 ppm; SD: 548 ppm). La fracción de Fe de todas las muestras de implantes fue menor del 0.5 % de masa según lo especificado por ISO 5832-2 y F67-13 [3,5]. Todas las muestras de implantes investigadas contenían fracciones de níquel (Ni) (absoluto; media: 56 ppm, SD: 46 ppm), cromo (Cr) (absoluto; media: 47 ppm, SD: 53 ppm), antimonio (Sb) (absoluto; media: 5.6, SD 3.7 ppm) y niobio (Nb) (absoluto; media: 4.2, SD: 2.9 ppm). 12 de 28 muestras de implantes no dopadas con vanadio incluyeron una fracción de V (absoluto; media: 26.6 ppm, SD: 47.5 ppm). Las fracciones encontradas de Fe, Cr, Ni y V se visualizan en las Figuras 1 y 2. 26 de 28 muestras no dopadas con aluminio contenían Al (absoluto; media: 36.1 ppm, SD: 33.9 ppm). No se detectó Al por encima del LOQ en las muestras TiCon1 y TiCon2 (implantes Conelog Screwline) (ver Figura 2). 24 de 28 muestras de implantes no dopadas con circonio contenían una fracción de Zr (absoluto; media: 3.4 ppm, SD: 3.5 ppm). Cuatro implantes (implantes Nobel Active: TiNoA1, TiNoA2, TiNoU1, TiNoU2) presentaron una fracción de fósforo (P) (absoluto; media: 241 ppm; SD: 40 ppm) (ver Figura 1). El arsénico (As) se encontró en cuatro muestras de dos marcas (absoluto; media: 35.5 ppm, SD: 5.2 ppm) (ver Figura 2). Otros elementos detectados incluyeron manganeso (Mn) (28/30 muestras), estaño (Sn) (26/30 muestras), tungsteno (W) (13/30 muestras), cobre (Cu) (12/30 muestras), cobalto (Co) (10/30 muestras), molibdeno (Mo) (9/30 muestras), plomo (Pb) (4/30 muestras), potasio (K) (5/30 muestras), tantalio (Ta) (5/30 muestras), galio (Ga) (2/30 muestras) y hafnio (Hf) (2/30 muestras). La Figura 1 (Fe, P, V), Figura 2 (Ni, Cr, Sn, As, Cu, Al) y Figura 3 (Nb, Co, Hf, Ta, Pb, Mn, Sb, Ga, W, Mo) visualizan selectivamente las contaminaciones encontradas. Para todos los resultados absolutos, ver la Tabla B.

3.3. Contaminación a nivel ultra-traza con Torio (Th-232) y Uranio (U-238)

El análisis ICP-MS reveló que 5 de 30 muestras de implantes contenían contaminación con U-238 en el rango de partes por billón (absoluto; media: 69 ppb, SD: 4 ppb), y 3 de 30 muestras presentaron contaminación con Th-232 (absoluto; media: 39 ppb, SD: 36 ppb) en el nivel ultra-traza por encima del LOQ. La Figura 4 visualiza las fracciones de Th-232 y U-238 de todas las muestras investigadas.

4. Discusión

Para ayudar a la interpretación de los resultados presentados, es importante reconocer que los análisis ICP-MS/OES cuantificaron la composición elemental promedio de todo el cuerpo del implante. En contraste, la mayoría de los informes previos que describen impurezas en implantes de Ti han utilizado solo técnicas de caracterización de la superficie [21–23]. El Ti es un metal altamente reactivo que forma rápidamente una capa de óxido superficial robusta que confiere su pasividad química protegiendo el implante contra la corrosión bajo condiciones fisiológicas [26,27]. Sin embargo, clínicamente, se ha demostrado la liberación de Ti de implantes dentales [17] y de implantes de anclaje óseo extraorales [28], con el tamaño y la especiación química de los productos de Ti liberados consistentes con los formados por corrosión. Para explicar estas observaciones, se han propuesto mecanismos donde se mantienen localmente altas concentraciones de especies reactivas de oxígeno (ROS) asociadas con inflamación [29] o entornos ácidos [30] [12,14,31–33]. La biocorrosión debida a la liberación local de ROS o biofilms acidogénicos y la corrosión de hendidura asistida mecánicamente asociada con micromovimientos relativos de componentes modulares, llevan a la ruptura de la capa pasiva superficial. Las regiones de impureza, como la agregación de Fe en los límites de grano en CpTi, presentan ubicaciones con menor resistencia a la corrosión que es más probable que se propaguen antes de que ocurra la repasivación [34]. De esta manera, la composición general y la heterogeneidad de la distribución de elementos menores y de traza dentro de la aleación a granel pueden influir directamente en la resistencia a la corrosión.

Un estudio previo de SR-XRF/XAS mostró que las partículas de Ti presentes en los tejidos periimplantarios son predominantemente de especiación de óxidos y se atribuyen a la liberación debido a la socavación y el desprendimiento de la superficie de óxido de Ti o, a través de una ruta de precipitación cuando los iones de Ti liberados rápidamente reaccionan con oxígeno o agua para formar TiO2 insoluble [17]. La abundancia de concentraciones relativamente altas de elementos 'contaminantes' en la misma ubicación que el Ti observado en el estudio [17] podría interpretarse como consistente con distribuciones no homogéneas de impurezas dentro del metal a granel que representan puntos de mayor riesgo de corrosión.

4.1. Conformidad con las normas ISO/ASTM y especificaciones del fabricante

Todos los implantes investigados fabricados a partir de CpTi se ajustaron a ISO 5832-2 y ASTM F67-13 (Grado II: máx. 0.3 % de masa de Fe; Grado IV: máx. 0.5 % de masa de Fe). Además, los dos implantes fabricados a partir de Ti6Al4V ELI (MIS Implant Systems) cumplieron con la norma ASTM F136 (máx. Fe: 0.25 % de masa, Al: 5.5–6.50 % de masa, V: 3.5–4.5 % de masa). Los implantes fabricados a partir de la aleación binaria TiZr (Roxolid, Straumann) no están sujetos a ninguna estandarización con respecto a la composición del material, pero se ajustaron a las especificaciones del fabricante (Ti: ~ 85 % de masa, Zr: ~ 15 % de masa) y a los estándares de CpTi Grado IV con respecto a la fracción de Fe.

4.2. Contaminación con múltiples elementos metálicos en todos los implantes

Aunque todos los sistemas de implantes dentales investigados se ajustaron a las normas ISO/ASTM respectivas o a las especificaciones del fabricante, todos contenían contaminación con múltiples elementos. Los contaminantes encontrados incluían elementos traza endógenos inofensivos (por ejemplo, Cu, Zn) pero también metales potencialmente alergénicos (por ejemplo, Ni, Co, Cr), metales potencialmente tóxicos (por ejemplo, As) e incluso radionúclidos (Th-232, U-238) [35]. El Ni, Co y Cr son potentes alérgenos de contacto con tasas de sensibilización estandarizadas por edad estimadas del 14.5 %, 2.1 % y 0.8 %, respectivamente, en países europeos [36]. Debido a una constante dieléctrica baja, es más probable que los óxidos de Ni y Co interactúen con electrolitos tisulares que el óxido de Ti o los óxidos del grupo refractario (por ejemplo, Nb, Ta, V) [24]. Estudios previos han identificado su presencia en sustratos de Ti biomédicos [24], y en este estudio, se observaron Ni y Cr en todas las muestras. El Co se encontró en un tercio de las muestras medidas. Sin embargo, el grado de contaminación con Ni (media: 56 ppm, SD: 46 ppm !), Cr (media: 47 ppm, SD: 53 ppm !) y Co (media: 1.7 ppm, SD: 2.7 ppm !) difirió entre los sistemas de implantes, lo que indica una diferencia en la calidad de los materiales de origen y que la reducción de impurezas aún no se implementa técnicamente a nivel estandarizado en el mercado de implantes dentales.

Según la Organización Mundial de la Salud (OMS), la exposición al As es una gran preocupación para la salud pública [37]. Aunque la evidencia está creciendo de que trazas de As, un componente natural de la corteza terrestre, podrían desempeñar un papel en el metabolismo humano, se asume que es tóxico y cancerígeno cuando la exposición crónica ocurre a sus formas inorgánicas [38,39]. Por lo tanto, la OMS recomienda un límite de 10 μg/L (= 10 ppm) de As en el agua potable [37]. El presente estudio encontró contaminación consistente de As de 30 y 40 ppm, respectivamente, en dos sistemas de implantes, lo que no puede extrapolarse a una concentración de liberación. Sin embargo, las cinéticas de cualquier liberación requieren una aclaración científica adicional. Cabe mencionar que a partir del análisis elemental ICP-MS/OES presente, no es posible deducir si el As está concentrado localmente o actúa como un elemento intersticial dentro del Ti a granel. No obstante, dado que la OMS recomienda mantener la contaminación de As lo más baja técnicamente posible y en relación con las observaciones de que la mayoría de los sistemas de implantes se fabricaron sin contaminación detectable de As, las impurezas de As en los implantes dentales pueden considerarse evitables.

Se ha demostrado que incluso las cerámicas de zirconia médicamente purificadas pueden estar contaminadas con los radionúclidos U y Th [40–43]. Un análisis ICP-MS/OES anterior sobre implantes dentales comerciales de zirconia demostró que la mayoría de los implantes investigados presentaban contaminación a nivel ultra-traza (en ppb) con U-238 y Th-232 [25]. Por lo tanto, se esperaba la contaminación a nivel ultra-traza con U-238 del sistema de implantes de aleación TiZr (Roxolid) encontrado en el presente estudio. Sin embargo, tres implantes dentales de Ti también presentaron contaminación con radionúclidos, lo que no se asocia con una fracción mayor de zirconia. No se espera una radioactividad clínicamente relevante de esto. Sin embargo, se requiere un análisis radiológico adicional para escanear otros radionúclidos y determinar no solo la radioactividad estimada sino la real.

4.3. Fuentes de contaminación

Aunque abundante en la corteza terrestre, debido a una extracción que consume tiempo y es costosa de varios minerales, el Ti se considera un "metal raro". Muchas impurezas, por ejemplo, Cu, Mn y Mo, pueden persistir en el Ti comercial [44]. Sin embargo, también puede surgir una mayor contaminación en el curso de las modificaciones topográficas de la superficie, como el grabado químico, la abrasión de partículas suspendidas en aire, la anodización, la ablación con láser y el recubrimiento de la superficie [45,46]. Al anodizar la superficie del implante en ácido fosfórico, se puede aumentar la rugosidad de la superficie, y se propone que la producción de citoquinas se puede modular y mejorar la osteointegración [46,47]. El presente estudio encontró una contaminación exclusiva de todos los implantes NobelActive con P, que probablemente se deba al tratamiento de la superficie con ácido fosfórico. Un estudio de SEM/EDX de Duddeck et al. también describió una señal de fósforo en la superficie de los implantes NobelActive [21].

Excepto por un sistema de implantes (Conelog Screwline), todos los implantes investigados hechos de CpTi exhibieron una fracción de Al. El Al residual es un contaminante potencial conocido en la superficie de los implantes dentales de Ti [21,22,45], que resulta más comúnmente de los residuos de óxido de aluminio utilizados para la abrasión de la superficie con aire en la superficie de Ti [48,49]. Sin embargo, el impacto de este aluminio(óxido) residual en la osteointegración del implante todavía se discute de manera controvertida [50–52].

El presente estudio proporciona una visión general única e independiente del fabricante de la composición elemental de una fracción (< 10 %) de implantes de Ti disponibles comercialmente. Se debe investigar más a fondo la posible formación de clústeres de impurezas dentro del cuerpo del implante y entre lotes. Además, se debe aclarar en qué medida las impurezas son clínicamente relevantes y si pueden jugar un papel en las intolerancias a los implantes dentales de Ti. El mercado de implantes dentales está creciendo rápidamente y está sujeto a alta fluctuación (entradas y salidas del mercado); por lo tanto, una investigación completa de todos los implantes en el mercado es limitada. En cambio, con el conocimiento de la composición elemental existente de los sistemas de implantes investigados, se debe evaluar y discutir una adaptación de las normas relevantes, en particular valores límite adicionales para contaminantes específicos.

5. Conclusión

Basado en los resultados del presente análisis ICP-MS/OES, se pueden extraer las siguientes conclusiones:

1. Aunque todos los implantes dentales de Ti investigados cumplen con las normas respectivas y las especificaciones del fabricante, todos contienen contaminación rastreable con varios elementos metálicos.
2. Los contaminantes diferían entre los sistemas de implantes e incluían elementos traza esenciales inofensivos y metales potencialmente nocivos, como As y radionúclidos.
3. Se necesita más investigación para probar la generalización en otros sistemas de implantes y la relevancia biológica de estas contaminaciones. Especialmente, el papel de los contaminantes potencialmente alergénicos, como el Ni, es de interés clínico.
4. Dado que existen diferencias relevantes en el grado de contaminación con elementos metálicos entre los sistemas de implantes, parece técnicamente evitable una cierta fracción de impurezas. Se debe discutir una adaptación de las normas relevantes, en particular valores límite adicionales para los contaminantes.

Aprobación ética y consentimiento para participar

No se necesita aprobación ética ya que no se estudiaron pacientes/animales.

Consentimiento para publicación

No se necesita consentimiento ya que no se utilizaron datos/material de pacientes.

Financiación

Los recursos para la parte experimental fueron apoyados por Karlsruhe Nano Micro Facility (KNMF, http://www.knmf.kit.edu), una infraestructura de investigación Helmholtz en el Instituto de Tecnología de Karlsruhe (KIT) (Propuesta 2019-023-028249). Los implantes dentales de Ti fueron adquiridos comercialmente de los respectivos fabricantes/vendedores sin ninguna financiación y sin el conocimiento de los fabricantes.

Disponibilidad de datos y material

Todos los datos generados o analizados durante este estudio están incluidos en este artículo publicado.

Agradecimientos

Los autores agradecen al Instituto de Materiales Aplicados - Física de Materiales Aplicados (IAM-AWP) del Instituto de Tecnología de Karlsruhe (KIT) y a Karlsruhe Nano Micro Facility (KNMF, http://www.knmf.kit.edu, una infraestructura de investigación Helmholtz en el KIT), por proporcionar y ejecutar la metodología de este estudio. Muchas gracias a KNMF por financiar la parte experimental de este proyecto.

Apéndice A. Información de soporte

Los datos suplementarios asociados con este artículo se pueden encontrar en la versión en línea en doi:10.1016/j.dental.2022.06.028.

Referencias

1. Branemark PI, Hansson BO, Adell R, Breine U, Lindstrom J, Hallen O, et al. Implantes osteointegrados en el tratamiento de la mandíbula edéntula. Experiencia de un período de 10 años. Scand J Plast Reconstr Surg Suppl 1977;16:1–132.
2. Osman R, Swain M. Una revisión crítica de los materiales de implantes dentales con énfasis en titanio versus zirconia. Materials 2015;8:932–58. https://doi.org/10.3390/ma8030932
3. ISO 5832-2:2018 (Implantes para cirugía – materiales metálicos – Parte 2: titanio no aleado). Ginebra, Suiza: Organización Internacional para la Estandarización; 2018.
4. ISO 5832-3:2020 (Implantes para cirugía – materiales metálicos – Parte 3: aleación de titanio forjado 6-aluminio 4-vanadio). Ginebra, Suiza: Organización Internacional para la Estandarización; 2020.
5. ASTM F67-13, 2017, Especificación estándar para titanio no aleado, para aplicaciones de implantes quirúrgicos (UNS R50250, UNS R50400, UNS R50550, UNS R50700). West Conshohocken, PA, EE. UU.: ASTM International; 2017.
6. ASTM F136-13, 2021, e1, Especificación estándar para aleación de titanio-6aluminio-4vanadio ELI (intersticial extra bajo) forjado para aplicaciones de implantes quirúrgicos (UNS R56401). West Conshohocken, PA, EE. UU.: ASTM International; 2013.
7. Karl M, Krafft T, Kelly J. Fractura de un implante Roxolid de diámetro estrecho: consideraciones clínicas y fractográficas. Int J Oral Maxillofac Implants 2014;29:1193–6. https://doi.org/10.11607/jomi.3573
8. Grandin HM, Berner S, Dard M. Una revisión de las aleaciones de titanio-zirconio (TiZr) para su uso en implantes dentales endoóseos. Materials 2012;5:1348–60. https://doi.org/10.3390/ma5081348
9. Barter S, Stone P, Brägger U. Un estudio piloto para evaluar la tasa de éxito y supervivencia de implantes de titanio-zirconio en pacientes parcialmente edéntulos: resultados después de 24 meses de seguimiento. Clin Oral Implants Res 2012;23:873–81. https://doi.org/10.1111/j.1600-0501.2011.02231.x
10. Comino-Garayoa R, Cortés-Bretón Brinkmann J, Peláez J, López-Suárez C, Martínez-González JM, Suárez MJ. Alergias a implantes dentales de titanio: ¿qué sabemos realmente sobre ellas? Una revisión de alcance. Biology 2020:9. https://doi.org/10.3390/biology9110404
11. Mombelli A, Hashim D, Cionca N. ¿Cuál es el impacto de las partículas de titanio y la biocorrosión en la supervivencia y complicaciones de los implantes? Una revisión crítica. Clin Oral Implants Res 2018;29:37–53. https://doi.org/10.1111/clr.13305
12. Fretwurst T, Nelson K, Tarnow DP, Wang HL, Giannobile WV. ¿Está la liberación de partículas metálicas asociada con la destrucción ósea periimplantaria? Un concepto emergente. J Dent Res 2017;97:259–65. https://doi.org/10.1177/0022034517740560
13. Wilson TG. Pérdida ósea alrededor de implantes: ¿es metalosis? J Periodontol 2020;92:181–5. https://doi.org/10.1002/jper.20-0208
14. Suárez-López del Amo F, Garaicoa-Pazmiño C, Fretwurst T, Castilho RM, Squarize CH. Liberación de partículas de titanio asociada con implantes dentales: una revisión sistemática. Clin Oral Implants Res 2018;29:1085–100. https://doi.org/10.1111/clr.13372
15. Fretwurst T, Muller J, Larsson L, Bronsert P, Hazard D, Castilho RM, et al. Composición inmunohistológica del tejido afectado por periimplantitis alrededor de implantes cerámicos: un estudio piloto. J Periodontol 2021;92:571–9. https://doi.org/10.1002/JPER.20-0169
16. Schliephake H, Sicilia A, Nawas BA, Donos N, Gruber R, Jepsen S, et al. Drogas y enfermedades: resumen y declaraciones de consenso del grupo 1. La 5ª Conferencia de Consenso de EAO 2018. Clin Oral Implants Res 2018;29:93–9. https://doi.org/10.1111/clr.13270
17. Nelson K, Hesse B, Addison O, Morrell AP, Gross C, Lagrange A, et al. Distribución y especiación química de micro y nanopartículas exógenas en tejido blando inflamado adyacente a implantes dentales de titanio y cerámica. Anal Chem 2020;92:14432–43. https://doi.org/10.1021/acs.analchem.0c02416
18. Ameen AP, Short RD, Johns R, Schwach G. El análisis de superficie de materiales de implantes. 1. La composición superficial de un material de implante dental de titanio. Clin Oral Implants Res 1993;4:144–50. https://doi.org/10.1034/j.1600-0501.1993.040305.x
19. Velasco-Ortega E, Ortiz-Garcia I, Jiménez-Guerra A, Núñez-Márquez E, Moreno-Muñoz J, Rondón-Romero JL, et al. Osteointegración de superficies de implantes grabadas con chorro de arena y ácido. un estudio histológico e histomorfométrico en el conejo. Int J Mol Sci 2021:22. https://doi.org/10.3390/ijms22168507
20. Cervino G, Fiorillo L, Iannello G, Santonocito D, Risitano G, Cicciù M. Superficies de implantes dentales de titanio grabadas con chorro de arena y ácido: revisión sistemática y evaluación con microscopía confocal. Materials 2019:12. https://doi.org/10.3390/ma12111763
21. Duddeck, Albrektsson, Wennerberg, Larsson, Beuer. Sobre la limpieza de diferentes sistemas de implantes orales: un estudio piloto. J Clin Med 2019:8. https://doi.org/10.3390/jcm8091280
22. Dias FJ, Fuentes R, Navarro P, Weber B, Borie E. Evaluación de la composición química en diferentes tipos de implantes dentales: un análisis a través del sistema EDX. Coatings 2020:10. https://doi.org/10.3390/coatings10090882
23. Semez G, Todea C, Mocuta D, Sas IT, Luca R. Análisis químico y morfológico de implantes dentales de titanio: técnicas de fotoemisión de rayos X (XPS) y microscopía electrónica de barrido (SEM) con análisis EDX. Rev Chim 2018;69:474–7. https://doi.org/10.37358/rc.18.2.6130
24. Harloff T, Hönle W, Holzwarth U, Bader R, Thomas P, Schuh A. ¿Alergia al titanio o no? "Impureza" de los materiales de implantes de titanio. Health 2010;02:306–10. https://doi.org/10.4236/health.2010.24045
25. Gross C, Bergfeldt T, Fretwurst T, Rothweiler R, Nelson K, Stricker A. Análisis elemental de implantes dentales comerciales de zirconia: ¿"sin metal" está libre de metales? J Mech Behav Biomed Mater 2020:107. https://doi.org/10.1016/j.jmbbm.2020.103759
26. Souza JCM, Apaza-Bedoya K, Benfatti CAM, Silva FS, Henriques B. Una revisión completa sobre las vías de corrosión de implantes dentales de titanio y sus efectos biológicos adversos. Metals 2020:10. https://doi.org/10.3390/met10091272
27. Noronha Oliveira M, Schunemann WVH, Mathew MT, Henriques B, Magini RS, Teughels W, et al. ¿Pueden los productos de degradación liberados de los implantes dentales afectar los tejidos periimplantarios? J Periodontal Res 2017;53:1–11. https://doi.org/10.1111/jre.12479
28. Addison O, Davenport AJ, Newport RJ, Kalra S, Monir M, Mosselmans JFW, et al. ¿Se deterioran las superficies médicas de titanio "pasivas" en servicio en ausencia de desgaste? J R Soc Interface 2012;9:3161–4. https://doi.org/10.1098/rsif.2012.0438
29. Zhang Y, Addison O, Yu F, Troconis BCR, Scully JR, Davenport AJ. Corrosión mejorada dependiente del tiempo de Ti6Al4V en presencia de H2O2 y albúmina. Sci Rep 2018:8. https://doi.org/10.1038/s41598-018-21332-x
30. Yu F, Addison O, Baker SJ, Davenport AJ. El lipopolisacárido inhibe o acelera la corrosión del titanio biomédico según la acidez ambiental. Int J Oral Sci 2015;7:179–86. https://doi.org/10.1038/ijos.2014.76
31. Apaza-Bedoya K, Tarce M, Benfatti CAM, Henriques B, Mathew MT, Teughels W, et al. Interacciones sinérgicas entre la corrosión y el desgaste en las conexiones de implantes dentales de titanio: una revisión exploratoria. J Periodontal Res 2017;52:946–54. https://doi.org/10.1111/jre.12469
32. Fretwurst T, Buzanich G, Nahles S, Woelber JP, Riesemeier H, Nelson K. Elementos metálicos en tejido con periimplantitis dental: un estudio piloto. Clin Oral Implants Res 2016;27:1178–86. https://doi.org/10.1111/clr.12718
33. Blum K, Wiest W, Fella C, Balles A, Dittmann J, Rack A, et al. Cambios inducidos por fatiga en conexiones de implante-abutment cónicas. Dent Mater 2015;31:1415–26. https://doi.org/10.1016/j.dental.2015.09.004
34. Virtanen S, Curty C. Corrosión por picaduras estable e inestable del titanio en soluciones de haluros. Corrosion 2004;60:643–9. https://doi.org/10.5006/1.3287839
35. Zoroddu MA, Aaseth J, Crisponi G, Medici S, Peana M, Nurchi VM. Los metales esenciales para los humanos: una breve visión general. J Inorg Biochem 2019;195:120–9. https://doi.org/10.1016/j.jinorgbio.2019.03.013
36. Schuttelaar MLA, Ofenloch RF, Bruze M, Cazzaniga S, Elsner P, Gonçalo M, et al. Prevalencia de alergia de contacto a metales en la población general europea con un enfoque en níquel y piercings: el Estudio de Fragrance EDEN. Contact Dermat 2018;79:1–9. https://doi.org/10.1111/cod.12983
37. Directrices para la calidad del agua potable. 4ª edición con 1er addendum. OMS Ginebra; 2017.
38. Hunter P. Una mezcla tóxica de la que no podemos vivir sin. EMBO Rep 2008;9:15–8. https://doi.org/10.1038/sj.embor.7401148
39. Nurchi VM, Buha Djordjevic A, Crisponi G, Alexander J, Bjørklund G, Aaseth J. Toxicidad del arsénico: objetivos moleculares y agentes terapéuticos. Biomolecules 2020:10. https://doi.org/10.3390/biom10020235
40. Nielsen RH, Wilfing G. Zirconio y compuestos de zirconio. Enciclopedia Ullmann de química industrial. Lanzamiento electrónico. Weinheim: Wiley-VCH; 2010.
41. Vagkopoulou T, Koutayas SO, Koidis P, Strub JR. Zirconia en odontología: Parte 1. Descubriendo la naturaleza de una biocerámica en ascenso. Eur J Esthet Dent 2009;4:130–51.
42. Piconi C, Maccauro G. Zirconia como biomaterial cerámico. Biomaterials 1999;20:1–25.
43. Hurley PM, Fairbairn HW. Abundancia y distribución de uranio y torio en circonio, esfena, apatita, epidota y monacita en rocas graníticas. Trans Am Geophys Union 1957:38. https://doi.org/10.1029/TR038i006p00939
44. Takeda O, Ouchi T, Okabe TH. Progreso reciente en la extracción y reciclaje de titanio. Metall Mater Trans B 2020;51:1315–28. https://doi.org/10.1007/s11663-020-01898-6
45. Dhaliwal JS, David SRN, Zulhilmi NR, Sodhi Dhaliwal SK, Knights J, de Albuquerque Junior RF. Contaminación de implantes dentales de titanio: una revisión narrativa. SN Appl Sci 2020:2. https://doi.org/10.1007/s42452-020-2810-4
46. Yeo I-SL. Modificaciones de las superficies de implantes dentales a nivel micro y nano para mejorar la osteointegración. Materials 2019:13. https://doi.org/10.3390/ma13010089
47. França FL, Honorio-França AC, Honorio MS, Silva FHd, Fujimori M, França EL, et al. Las superficies de implantes dentales tratadas con ácido fosfórico pueden modular la producción de citoquinas por células MN de sangre. Braz Oral Res 2019:33. https://doi.org/10.1590/1807-3107bor-2019.vol33.0040
48. Bahraminasab M, Bozorg M, Ghaffari S, Kavakebian F. Corrosión electroquímica de biocompuestos Ti-Al2O3 en solución de Ringer. J Alloy Compd 2019;777:34–43. https://doi.org/10.1016/j.jallcom.2018.09.313
49. Yurttutan ME, Keskin A. Evaluación de los efectos de diferentes partículas de arena que se utilizan en el implante dental para mejorar la osteointegración. BMC Oral Health 2018:18. https://doi.org/10.1186/s12903-018-0509-3
50. Lukaszewska-Kuska M, Wirstlein P, Majchrowski R, Dorocka-Bobkowska B. Comportamiento de células osteoblásticas en superficies de titanio modificadas. Micron 2018;105:55–63. https://doi.org/10.1016/j.micron.2017.11.010
51. Canabarro A, Diniz MG, Paciornik S, Carvalho L, Sampaio EM, Beloti MM, et al. Alta concentración de óxido de aluminio residual en la superficie de titanio inhibe la mineralización de la matriz extracelular. J Biomed Mater Res Part A 2008;87A:588–97. https://doi.org/10.1002/jbm.a.31810
52. Piattelli A. El óxido de aluminio residual en la superficie de los implantes de titanio no tiene efecto en la osteointegración. Biomaterials 2003;24:4081–9. https://doi.org/10.1016/s0142-9612(03)00300-4

"""

def replace_non_latin1_characters(text):
    return text.encode('latin-1', errors='replace').decode('latin-1')

# Use the function before adding text to the PDF
text = replace_non_latin1_characters(translated_text)
#pdf.cell(200, 10, txt=text, ln=True)

pdf.multi_cell(0, 10, text)

# Save the PDF
pdf_output_path = "/Users/master/Downloads/Impurities_in_Titanium_Translated.pdf"
pdf.output(pdf_output_path)
pdf_output_path
