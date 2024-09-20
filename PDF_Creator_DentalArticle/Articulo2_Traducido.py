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
Partículas de Titanio Modulan la Polarización de Linfocitos y Macrófagos en Tejidos Gingivales Peri-Implante
Resumen: Los implantes dentales de titanio son una de las modalidades para reemplazar dientes faltantes. La liberación de partículas de titanio desde la superficie del implante puede modular las células inmunitarias, resultando en el fracaso del implante. Sin embargo, se sabe poco sobre el microambiente inmunitario que desempeña un papel en la inflamación peri-implante como consecuencia de las partículas de titanio. En este estudio, se recogieron tejidos gingivales peri-implante de pacientes con implantes fallidos, implantes exitosos y sin implantes, y luego se realizó un análisis del transcriptoma completo. El análisis de enriquecimiento de conjuntos génicos confirmó que la polarización de macrófagos M1/M2 y la proliferación de linfocitos se expresaron de manera diferencial entre los grupos de estudio. El agrupamiento funcional y el análisis de las vías de los genes expresados diferencialmente entre los implantes fallidos y exitosos frente a los que no tienen implantes revelaron que las vías de respuesta inmunitaria fueron las más comunes en ambas comparaciones, implicando el papel crítico de las células inmunitarias infiltrantes en los tejidos peri-implante. Las tinciones H&E e IHC confirmaron la presencia de partículas de titanio y células inmunitarias en las muestras de tejido, con un aumento en la infiltración de linfocitos y macrófagos en las muestras de implantes fallidos. La validación in vitro mostró un aumento significativo en el nivel de expresión de IL-1, IL-8 e IL-18 por macrófagos. Nuestros hallazgos mostraron evidencia de que las partículas de titanio modulan la polarización de linfocitos y macrófagos en los tejidos gingivales peri-implante, lo que puede ayudar a comprender el desequilibrio en la actividad osteoblástica-osteoclástica y el fracaso de la osteointegración del implante dental.

Palabras clave: implantes dentales, peri-implantitis, titanio, linfocitos, polarización de macrófagos, IL-1, IL-18, IL-8.

1. Introducción
El uso de implantes dentales para reemplazar dientes faltantes es beneficioso y está aumentando debido al rendimiento fiable y duradero de las prótesis soportadas por implantes. Se espera que esta modalidad de reemplazo de dientes faltantes continúe en el futuro como resultado del envejecimiento de la población global y los avances en tratamientos dentales. Aunque los implantes dentales muestran altas tasas de éxito, es importante señalar que los desafíos en este enfoque de tratamiento son el fracaso de aproximadamente el 5% al 11% de los implantes dentro de los 10 a 15 años y la necesidad de la eliminación de los implantes. Las causas principales de este fracaso se atribuyen a factores biológicos o biomecánicos; estos factores son complejos e interrelacionados. Sin embargo, la peri-implantitis es un proceso inflamatorio que afecta los tejidos peri-implante, conduciendo a la pérdida del hueso de soporte. Por lo tanto, las intervenciones clínicas tienen como objetivo preservar la integridad de los tejidos blandos y duros peri-implante y aumentar el éxito del tratamiento con implantes dentales.

El titanio es el metal de elección para implantes orales y maxilofaciales. Es un metal altamente reactivo que desarrolla una capa pasivadora de dióxido de titanio (TiO2) sobre su superficie al exponerse al aire o a fluidos. Esta capa de TiO2 actúa como una interfaz crucial entre el implante y el medio biológico, asegurando la biocompatibilidad al reducir la reactividad del material y prevenir parcialmente la corrosión. Sin embargo, la pérdida de esta capa protectora sin re-formación podría llevar a la corrosión similar a otros metales base. Las biopelículas producen ácidos como subproductos de sus actividades metabólicas, lo que puede llevar a la erosión de estructuras radiculares y al deterioro de materiales prostéticos dentales con el tiempo. Sin embargo, los productos basados en polímeros y adhesivos dentales están diseñados típicamente para liberar o generar sustancias alcalinas, que neutralizan los ácidos y crean un entorno menos ácido. Esto ayudará a contrarrestar los efectos de los ácidos de la biopelícula proporcionando una barrera protectora. Además, los adhesivos tienen el potencial de lograr reducciones superiores en el crecimiento de biopelículas, la adhesión temprana y la actividad metabólica.

Las partículas de titanio pueden liberarse en los tejidos gingivales peri-implante como resultado de la cirugía de colocación del implante, la corrosión de la superficie del implante, los micromovimientos entre el implante y su superestructura, y la instrumentación de la superficie del implante durante el mantenimiento del implante. En el entorno oral, el titanio enfrenta valores de pH fluctuantes debido a la presencia de biopelículas bacterianas, fluoruros y factores dietéticos. Esto puede inducir un medio ácido que a su vez activa la disolución de las partículas de titanio y la interrupción de la capa de TiO2 en la superficie del implante dental. Estas partículas actúan como cuerpos extraños para las células inmunitarias, desencadenando varias respuestas inmunitarias y promoviendo la activación de diferentes mediadores que están asociados con la resorción ósea y las enfermedades peri-implante.

Una amplia variedad de células inmunitarias están presentes en los tejidos gingivales peri-implante, tales como células plasmáticas, linfocitos, neutrófilos, granulocitos y/o macrófagos. Las partículas de titanio que se han desprendido de las superficies de los implantes dentales se han identificado como un cuerpo extraño predominante en las biopsias de tejido con peri-implantitis que están rodeadas por células inflamatorias. Esas partículas son fagocitadas por los macrófagos que liberan citoquinas proinflamatorias como IL-1β y TNF-α. Estas citoquinas están asociadas con la activación de osteoclastos a través de la vía de señalización del ligando del receptor activador del factor nuclear κB (RANKL)/receptor activador del factor nuclear κB (RANK)/osteoprotegerina (OPG). Esto finalmente conduce a la osteólisis y resorción ósea, que están fuertemente asociadas con el desarrollo y progresión de la peri-implantitis. Oliveira et al. mostraron que los macrófagos en los tejidos peri-implante fagocitaron productos de corrosión de micropartículas de titanio, lo que llevó a la estimulación de la actividad de los osteoclastos, y que la mayoría de la interacción entre las células del sistema inmunitario está modulada por citoquinas, factores de crecimiento y hormonas. Se ha propuesto que las citoquinas pro y antiinflamatorias influyen en la progresión de la peri-implantitis. Los desequilibrios en los niveles de liberación de citoquinas pueden inhibir la resolución de la inflamación y contribuir a la pérdida de hueso alveolar.

A pesar de las inconsistencias en las definiciones de peri-implantitis, la prevalencia de la enfermedad varía entre el 1% y el 47% de los pacientes. La infiltración de células inmunitarias afecta significativamente la biocompatibilidad y la función de los implantes dentales, lo que puede llevar a su fracaso. La lesión inicial de los tejidos peri-implante tras la colocación del implante desencadena una respuesta inflamatoria mediada por células de inmunidad innata, como macrófagos, células dendríticas, mastocitos y neutrófilos. Los macrófagos desempeñan un doble papel como macrófagos inflamatorios (M1) o alternativos (M2). Oliveira y colaboradores informaron que, en presencia de partículas de titanio, la actividad de los osteoclastos se activó y el número de macrófagos en el sitio aumentó, asociado con una mayor tasa de mutaciones en células humanas cultivadas en nanopartículas basadas en titanio. Además, la investigación in vitro mostró que la presencia de partículas de titanio resultó en un aumento de la expresión de citoquinas inflamatorias, activación de osteoclastos y alteraciones morfológicas, como neutrófilos y macrófagos. Los productos de degradación pueden causar alteraciones morfológicas en las células inflamatorias, aumentando consecuentemente la liberación de TNF-α. Además, se sabía que citoquinas como TNF-α e IL-1β inducen la expresión y activan el promotor de CCL3, que se informó que desempeña un papel crítico en la migración potencial de macrófagos. Durante la inflamación, el reclutamiento de leucocitos está regulado por varias citoquinas, incluidas IL-8/CXCL8, CCL2, IL-1β y TNFα, que actúan como prominentes quimioatrayentes.

Sin embargo, hay una brecha en el conocimiento sobre el papel de las partículas de titanio en el desarrollo de la peri-implantitis y el fracaso de la osteointegración de los implantes dentales. Explorar esta área de investigación puede arrojar luz sobre la relación entre la infiltración de partículas de titanio en los tejidos peri-implante y la modulación de las células inmunitarias, mejorando así nuestra comprensión del fracaso de la osteointegración del implante. Esto contribuirá a la comprensión del desequilibrio en la actividad osteoblástica-osteoclástica y el fracaso de la osteointegración del implante dental. Por lo tanto, el objetivo principal de este estudio es investigar la infiltración de partículas de titanio y células inmunitarias en los tejidos gingivales peri-implante mediante un análisis comparativo de la expresión génica utilizando un análisis del transcriptoma completo en tejidos gingivales que rodean implantes dentales exitosos y fallidos, en comparación con un grupo de referencia sin implantes. El paso subsiguiente fue la validación funcional utilizando líneas celulares de macrófagos derivados de monocitos THP-1 para confirmar los hallazgos y proporcionar información adicional.

2. Resultados
2.1. Perfil Transcripcional Distingue entre Muestras de Tejido Gingival de FI, SI y NI

El análisis diferencial de expresión génica mostró perfiles de expresión génica distintos entre FI y SI en comparación con las muestras de tejido gingival de NI. Después de la normalización y filtrado estándar, un total de 2185 y 5375 DEGs resultaron en FI en comparación con NI y SI en comparación con NI, respectivamente. Los genes expresados diferencialmente se seleccionaron con FC > 2 a un nivel de significancia del valor p ajustado (FDR) < 0.05 y se utilizaron para un análisis de agrupamiento jerárquico no supervisado. Los pacientes con FI y NI se agrupan como una sola rama, mostrando claramente subgrupos de FI y NI independientemente de su origen de diferentes pacientes con FI y NI (Figura 1A). Además, los pacientes con SI y NI se agrupan como una sola rama, mostrando claramente subgrupos de SI y NI independientemente de su origen de diferentes pacientes con SI y NI (Figura 1B). El árbol de genes en cada agrupamiento jerárquico no supervisado se ordenó de acuerdo con las vías biológicas enriquecidas por la herramienta de anotación Metascape, y se indican los grupos de genes enriquecidos para las vías enriquecidas principales. Por lo tanto, el perfil transcriptómico encontrado en los mapas de calor muestra una firma única entre FI vs. NI y SI vs. NI, lo que confirma la fracción inmunitaria y sus vías relacionadas en cada subgrupo.

2.2. Disregulación de la Respuesta Celular al Estrés Químico y Respuesta Inmunitaria en Tejidos Gingivales de SI y FI

Para investigar la relevancia funcional de los DEGs significativos en los tejidos gingivales de FI y SI en comparación con los tejidos de NI, se realizaron análisis funcionales y de vías (Tabla 1). Los análisis revelaron vías celulares clave como la respuesta celular al ion cadmio (p < 0.01) y la activación y proliferación de linfocitos B y T (p < 0.0001 y 0.01, respectivamente) que estaban sobreenriquecidas en FI en comparación con NI. En contraste, la respuesta celular al estrés químico (p < 0.0001) y la respuesta al alcohol estaban significativamente subreguladas en FI en comparación con NI. Curiosamente, diferentes vías relacionadas con la respuesta y el proceso inmunitario y la activación de células inmunitarias estaban sobreexpresadas en SI, como la migración de leucocitos (p < 0.0001), la activación de leucocitos mieloides (p < 0.00001), la degranulación de neutrófilos y leucocitos (p < 0.0001 y 0.001, respectivamente), además de la regulación de la producción de citoquinas (p < 0.001) y principalmente la regulación positiva de la producción de interleucina-10 (p < 0.001). Además, la respuesta de defensa celular (p < 0.001) y las vías de eliminación de células apoptóticas (p < 0.001) estaban altamente enriquecidas en SI en comparación con NI. Sin embargo, el agrupamiento funcional reveló significativamente que las respuestas celulares a estímulos (p < 1 × 10^-53) y la muerte celular programada (p < 1 × 10^-14) estaban subreguladas en SI en comparación con NI.

Tabla 1. Análisis funcional y de vías de los genes expresados diferencialmente en tejidos gingivales de SI y FI en comparación con NI.

Grupo	Expresión	Descripción	Categoría de Procesos Biológicos	Recuento de Genes	Valor p
Implantes exitosos (SI)	Arriba	Detección de estímulo químico	GO:0009593	55	1.12 × 10^-7
Arriba	Migración de leucocitos	GO:0050900	37	5.77 × 10^-5
Arriba	Activación de leucocitos mieloides	GO:0002274	26	6.33 × 10^-5
Arriba	Degranulación de neutrófilos	Conjuntos de Genes Reactoma: R-HSA-6798695	44	8.49 × 10^-5
Arriba	Regulación de la producción de citoquinas	GO:0001817	64	1.44 × 10^-4
Arriba	Respuesta de defensa celular	GO:0006968	10	2.3 × 10^-4
Arriba	Degranulación de leucocitos	GO:0043299	12	3.23 × 10^-4
Arriba	Regulación positiva de la producción de interleucina-10	GO:0032733	8	8.28 × 10^-4
Arriba	Eliminación de células apoptóticas	GO:0043277	9	9.91 × 10^-4
Abajo	Respuestas celulares a estímulos	Conjuntos de Genes Reactoma: R-HSA-8953897	422	3.88 × 10^-54
Abajo	Muerte celular programada	Conjuntos de Genes Reactoma: R-HSA-5357801	50	2.83 × 10^-15
Implantes fallidos (FI)	Arriba	Respuesta celular al ion cadmio	GO:0071276	10	1.9 × 10^-3
Arriba	Proliferación de linfocitos	GO:0002376	12	3.4 × 10^-4
Arriba	Activación de células B	GO:0042113	21	1.92 × 10^-5
Arriba	Activación de células T involucradas en la respuesta inmunitaria	GO:0002286	9	4.69 × 10^-3
Abajo	Respuesta celular al estrés químico	Conjuntos de Genes Reactoma: R-HSA-9711123	47	4.7 × 10^-6
Abajo	Respuesta al alcohol	GO:0097305	24	1.9 × 10^-6
2.3. GSEA Identifica las Vías Celulares Activadas en Tejidos Gingivales de SI y FI

Para identificar más vías detalladas y los DEGs relacionados en cada comparación de FI vs. NI y SI vs. NI, se realizó un exhaustivo GSEA. Las vías significativamente activadas fueron identificadas para cada comparación basadas en el corte nominal p < 0.05. Los detalles de los conjuntos de genes significativamente enriquecidos se listan en la Tabla 2.

Tabla 2. Vías significativamente enriquecidas activadas diferencialmente entre FI y SI en comparación con NI.

Comparación	Conjunto de Genes	Fuente	Tamaño	ES	NES	NOM p
FI vs. NI	M1 vs. M2	GSE5099	23	0.62	1.64	<0.001
CD4 EFF MEM VS PBMC DN	GSE11057	21	0.52	1.49	<0.05
PROLIFERACIÓN DE LINFOCITOS	GO:0008283	50	0.40	1.52	<0.05
CSF1 IFNG VS CSF1 IFNG PAM3CYS IN MAC UP	GSE11864	15	0.53	1.54	<0.05
UNTREATED VS CSF1 IFNG PAM3CYS IN MAC DN	GSE11864	16	0.53	1.82	<0.001
TFH VS TH17 CD4 TCELL DN	GSE11924	15	0.62	1.60	<0.001
IGD POS BLOOD VS NAIVE TONSIL BCELL DN	GSE12845	17	0.63	1.42	<0.001
IMM VS MATURE NKCELL DN	GSE13229	16	0.60	1.66	<0.05
SI vs. NI	NAIVE VS MEMORY CD8 TCELL DN	GSE10239	47	0.49	1.58	<0.001
CD4 TCELL VS LUPUS CD4 TCELL DN	GSE10325	35	0.56	1.59	<0.001
NAIVE VS CENT MEMORY CD4 TCELL UP	GSE11057	30	0.54	1.69	<0.001
NAIVE VS EFF MEMORY CD4 TCELL UP	GSE11057	41	0.54	1.71	<0.001
NAIVE VS DAY8 EFF CD8 TCELL UP	GSE1000001	41	0.59	1.38	<0.001
RESPUESTA A ESTÍMULO QUÍMICO	GO:0042221	63	0.44	1.64	<0.001
ES: Puntuación de Enriquecimiento; NES: Puntuación ES Normalizada; NOM: nominal.

Además, los análisis de vanguardia revelaron genes activados diferencialmente importantes que están involucrados en múltiples inflamaciones y respuestas inmunitarias relacionadas con procesos biológicos o vías moleculares, incluyendo IL1B, CDK3, IL27 y CD86 en la comparación FI vs. NI (Figura 2A,B), además de CXCL6, CXCL1, CCL7, CCL13 e IL18 en la comparación SI vs. NI (Figura 2C,D).

2.4. Polarización de Macrófagos en Tejidos Gingivales Peri-Implante

Se evaluó un análisis enfocado de la deconvolución de células inmunitarias para los DEGs en SI y FI en comparación con NI utilizando el método computacional CIBERSORT (Figura 3). El análisis de citometría digital mostró que el porcentaje de macrófagos M1 era del 9.9% en SI, ligeramente más alto que en FI (9.4%). Sin embargo, el porcentaje de macrófagos M2 era del 22.3% en FI, más que en SI (18.7%). Curiosamente, hubo una clara variación en los porcentajes de subtipos de células T entre las muestras de FI y SI; por ejemplo, los porcentajes de células T reguladoras eran del 16.4% en FI y del 3.15% en SI (Tabla 3).

Tabla 3. El porcentaje relativo de la distribución de subconjuntos de células inmunitarias en FI y SI. Los datos fueron extraídos del análisis de citometría de flujo in silico de CIBERSORT.

Células Inmunitarias	Implantes Exitosos SI (%)	Implantes Fallidos FI (%)
Células T CD8 de Memoria	6.8	6
Células T CD8	13.4	0
Células T Reguladoras (Tregs)	3.15	16.4
Macrófagos M1	9.9	9.4
Macrófagos M2	18.7	22.3
Células T CD4	19.6	45.9
2.5. Las Partículas de Titanio Resultan en el Desencadenamiento del Sistema Inmunitario en FI y SI

Se investigó el recuento de los DEGs a través de los dos tipos de tejidos gingivales peri-implante (FI y SI) (Figura 4A). El análisis funcional y de vías de los DEGs comunes en los tejidos gingivales peri-implante de FI y SI mostró un enriquecimiento significativo de transcripciones involucradas en la respuesta a estímulos, defensa del sistema inmunitario, desintoxicación y señalización (Figura 4B).

Figura 4. (A) Diagrama de Venn que representa la superposición de genes expresados diferencialmente significativamente entre los implantes fallidos y exitosos. (B) Análisis de agrupamiento funcional y de vías de los genes expresados diferencialmente comunes entre los implantes fallidos y exitosos.

2.6. Mayor Infiltración de Células Inmunitarias en Tejidos Gingivales Peri-Implante de FI en Comparación con SI o NI

Para confirmar la infiltración de células inmunitarias en los tejidos gingivales peri-implante de FI en comparación con SI y NI, se realizó una tinción H&E. El examen microscópico mostró una mayor infiltración de células inflamatorias en los tejidos gingivales recolectados de pacientes con FI, en comparación con los tejidos gingivales de SI. La predominancia de macrófagos y linfocitos es una indicación de inflamación crónica. De hecho, la especificación de las células inmunitarias se basó en la morfología de cada tipo de célula basada en el núcleo y el citoplasma. Además, las partículas de titanio eran evidentes en las imágenes H&E en los tejidos gingivales peri-implante recolectados de pacientes con FI y SI. Sin embargo, los tejidos gingivales recolectados de pacientes sin implantes dentales revelaron una mínima o nula infiltración de células inflamatorias (Figura 5). La identificación de partículas de titanio también se basó en la morfología; son completamente diferentes de las células inflamatorias ya que se ven como manchas negras.

Figura 5. Imágenes representativas de H&E que demuestran la infiltración de células inflamatorias en tejidos gingivales peri-implante (200×). (A) Imagen de H&E que muestra células inflamatorias en el área circundante de las partículas de titanio (círculos rojos) en implantes fallidos. (B) Imagen de H&E que muestra las partículas de titanio rodeadas por infiltrados celulares moderados en implantes exitosos. (C) Imagen de H&E que muestra tejidos gingivales compuestos por epitelio externo y una red interna de tejidos conectivos en muestras sin implantes.

2.7. Análisis de Inmunohistoquímica Valida la Infiltración de Macrófagos y Linfocitos en Tejidos Gingivales Peri-Implante

Para validar la infiltración de células inmunitarias representadas principalmente por macrófagos y linfocitos en los tejidos gingivales peri-implante, se realizó un puntaje inmunoreactivo (IRS) utilizando hallazgos de análisis IHC para evaluar la expresión de los marcadores CD68 y CD3 representativos de macrófagos y linfocitos, respectivamente. El análisis de imágenes IHC mostró una expresión positiva de CD68 y CD3 en casos de FI, que fue más pronunciada que en SI. Además, los tejidos gingivales recolectados de pacientes sin implantes dentales mostraron una expresión negativa de los mismos marcadores (Figura 6). El análisis estadístico de los marcadores inmunitarios entre los diversos grupos de implantes mostró que tanto CD68 como CD3 fueron significativamente más altos en el grupo FI en comparación con el grupo SI (p < 0.01), y ambos fueron ligeramente menos significativos al comparar el grupo NI con el grupo FI (p < 0.05), pero no fueron significativos al comparar NI con SI.

Figura 6. Imágenes representativas de la tinción IHC de CD68 y CD3 en tejidos gingivales peri-implante entre los diversos grupos de implantes (200×). (A) La tinción IHC revela una fuerte expresión de CD68 en presencia de partículas de titanio en FI. (B) La tinción IHC revela expresión positiva de CD68 en SI pero menos que en FI (A). (C) La tinción IHC mostró expresión negativa de CD68 en NI. (D) La tinción IHC revela expresión positiva de CD3 en FI. (E) La tinción IHC revela expresión positiva de CD3 en SI. Sin embargo, la proporción de CD3 es mayor en FI, y la intensidad de la tinción es más fuerte en SI. (F) La tinción IHC muestra expresión negativa de CD3 en los tejidos gingivales de NI. FI: Implantes fallidos; SI: Implantes exitosos; NI: Sin implantes. Las flechas rojas se refieren a la expresión de los macrófagos/linfocitos y/o a las partículas de titanio.

2.8. Expresión de Proteínas de Varias Citoquinas por Macrófagos M0 Tratados con TiO2

Se investigaron varias citoquinas asociadas a la inflamación de macrófagos tras el tratamiento de macrófagos M0 durante 24 horas con 20 y 100 µg/mL de TiO2 NPs y MPs. Curiosamente, hubo un aumento en la liberación de IL-1β, IL-8 e IL-18 por macrófagos M0 después de ser tratados durante 24 horas con 100 µg/mL de TiO2 NPs (p < 0.05, p < 0.01 y p < 0.0001, respectivamente) y MPs (p < 0.05, p < 0.01 y p < 0.001, respectivamente) en comparación con células no tratadas. Además, hubo un aumento significativo en los niveles de IL-1β, CCL3 e IL-8 entre los tratamientos de 20 y 100 µg/mL de TiO2 NPs y MPs. Sin embargo, TNF-α no mostró ningún cambio significativo tras diferentes tratamientos de TiO2 (Figura 7).

Figura 7. Expresión a nivel de proteínas de citoquinas por macrófagos M0 tratados con TiO2. (A) CCL3, (B) IL-1β, (C) TNF-α, (D) IL-8, y (E) IL-18 expresión de proteínas en macrófagos M0 después de ser tratados durante 24 horas con 20 y 100 µg/mL de TiO2 NPs y MPs usando Luminex/ELISA. La expresión de citoquinas se representa en términos de picogramas /mililitro en comparación con macrófagos M0 no tratados. Los datos se representan como media ± SEM de dos experimentos separados. * p < 0.05, ** p < 0.01, *** p < 0.001, y **** p < 0.0001.

2.9. Red de Interacción de Proteínas de las Citoquinas Significativamente Alteradas en los Tejidos Gingivales Peri-Implante con la Presencia de TiO2

Construimos redes de interacción de proteínas de las citoquinas significativamente alteradas en los tejidos gingivales peri-implante (CCL3, IL-1β, IL-8 e IL-18) que se validaron en los macrófagos M0 tratados con TiO2. El análisis de la red de interacción mostró que todas las citoquinas están funcionalmente interconectadas (Figura 8). El análisis de la red de interacción de proteínas mostró la presencia de varios DEGs en FI en comparación con NI, incluidos AKT1, GNA15, GNAI1, GNB2L1, GSDMD, NLRC4 y SMO que mostraron interacciones potenciales y afectaron comúnmente la expresión y función de cada uno. Por lo tanto, se puede suponer que la interrupción de las citoquinas CCL3, IL-1β, IL-8 e IL-18 desempeña un papel esencial en la osteointegración del implante dental.

Figura 8. Red de interacción proteína-proteína de citoquinas alteradas en los tejidos gingivales peri-implante. Los nodos de la red representan proteínas. Las líneas de diferentes colores representan seis tipos de indicadores utilizados para predecir las asociaciones de la red; línea roja: presencia de evidencia de fusión; línea verde: evidencia de vecindad; línea azul: evidencia de co-ocurrencia; línea púrpura: evidencia experimental; línea azul claro: evidencia de base de datos; línea negra: evidencia de coexpresión.

3. Discusión
Hasta donde sabemos, este es el primer estudio que utiliza el análisis del transcriptoma para comparar tejidos gingivales peri-implante de grupos de pacientes con FI, SI y NI. En el presente estudio, los perfiles de expresión génica distintos en el análisis del transcriptoma entre muestras de tejido de FI, SI y NI podrían considerarse una indicación del impacto de las partículas de titanio en los cambios de expresión génica. Además, esto puede estar correlacionado con la infiltración de células inflamatorias, lo que confirma la fracción inmunitaria única en cada subgrupo resultando en los análisis de agrupamiento jerárquico y mapas de calor. Además, los datos extraídos del análisis de citometría de flujo in silico confirmaron la profusión de macrófagos en los tejidos peri-implante con variaciones en el M1 con una proporción del 9.4% y 9.9% y el M2 con una proporción del 22.3% y 18.7%, respectivamente, en los tejidos FI y SI en comparación con las muestras NI. El porcentaje de macrófagos M2 y células T en el tejido de casos con FI era mayor que en SI, pero el porcentaje de macrófagos M1 era mayor en SI que en FI. Este hallazgo está de acuerdo con estudios ortopédicos que han informado una abundancia de macrófagos CD68 en tejidos ortopédicos periprotésicos que contienen desechos metálicos y un número aumentado de macrófagos CD68 en una prótesis ortopédica aflojada asépticamente. Yang et al. analizaron ratones implantados con tejidos periprotésicos humanos y reportaron células CD68 en cantidades mucho mayores cuando estaban presentes partículas de titanio en comparación con aquellas libres de partículas de titanio. Este aumento en las células CD68 se pensó que estaba asociado con un mayor número de monocitos fagocitados en sitios que contenían partículas de titanio y desechos. Nuestros hallazgos mostraron que los macrófagos M1 y M2 fueron detectados en los tejidos gingivales peri-implante de pacientes con FI y SI, lo que siguió a otros estudios donde la plasticidad y polarización de macrófagos se han reportado en el contexto de la peri-implantitis. Futuros estudios, que consideren el uso de CD163 y CD86, se llevarán a cabo para investigar la polarización de M2 y M1, respectivamente.

El agrupamiento funcional y el enriquecimiento de vías de los genes expresados diferencialmente en FI vs. NI, o SI vs. NI, identificaron varias vías moleculares y procesos biológicos. Sin embargo, las vías de respuesta inmunitaria fueron las más frecuentes en ambas comparaciones, sugiriendo los roles importantes de las células inmunitarias infiltrantes en los tejidos peri-implante. Para los DEGs en el grupo FI, mostramos que los procesos de activación y proliferación de células B y T estaban sobreexpresados, aunque las respuestas celulares al estrés químico y la respuesta al alcohol estaban subreguladas en FI en comparación con NI. De hecho, para los DEGs en el grupo SI, diferentes vías relacionadas con la respuesta inmunitaria, el proceso y la activación de células inmunitarias estaban sobreexpresadas, incluyendo la migración de leucocitos, la activación de leucocitos mieloides, la degranulación de neutrófilos y leucocitos, además de la regulación de la producción de citoquinas. Estos hallazgos son consistentes con resultados previos que muestran que en los tejidos peri-implante, los cambios de expresión génica están principalmente relacionados con respuestas inmunitarias y respuestas de defensa. Además, el GSEA mostró además que los conjuntos de genes relacionados con la polarización de macrófagos M1/M2, las respuestas inmunitarias, la activación y proliferación de células inmunitarias y la señalización de citoquinas estaban diferencialmente sobre-representados entre los diferentes subgrupos. Importante, los análisis de vanguardia revelaron genes activados diferencialmente importantes que están involucrados en múltiples inflamaciones y respuestas inmunitarias relacionadas con procesos biológicos o vías moleculares, incluyendo IL-1β, CDK3, IL-27 y CD86 en la comparación FI vs. NI, además de CXCL6, CXCL1, CCL7, CCL13 e IL18 en la comparación SI vs. NI. Estudios de transcriptómica previos que perfilan los genes expresados diferencialmente en peri-implantitis han señalado que las vías significativamente alteradas estaban relacionadas con moléculas de matriz extracelular, enzimas degradadoras de matriz y vías inflamatorias incluyendo la vía RANKL/OPG y la vía de la ciclooxigenasa2.

Por otro lado, el análisis de enriquecimiento funcional de los DEGs comunes a los tejidos gingivales peri-implante de FI y SI mostró que el enriquecimiento significativo de transcripciones está involucrado en la respuesta a estímulos, defensa del sistema inmunitario, desintoxicación y señalización, indicando que en ambos casos de implantes fallidos y exitosos, hay una liberación del titanio que se considera como estrés para las células en el área peri-implante y por lo tanto, resulta en el desencadenamiento del sistema inmunitario, activando principalmente la polarización de macrófagos M1, y quizás más tarde, la polarización de M2. Además, se puede suponer que un desequilibrio de la polarización de macrófagos M1-M2 a menudo está asociado con diversas condiciones inflamatorias, lo que lleva al fracaso del implante en algunos casos y al éxito en otros. Este hallazgo está de acuerdo con el estudio de Tilton et al., y apoya además la idea de que la exposición de monocitos THP-1 a partículas de TiO2 puede inducir los procesos biológicos y la regulación diferencial de la inflamación involucrada en la activación de neutrófilos y respuestas inmunitarias como la fagocitosis. Estos resultados están en buen acuerdo con nuestro estudio anterior que mostró que la fagocitosis de partículas de TiO2 por macrófagos es dependiente del tamaño y la dosis.

En el presente estudio, las imágenes de diapositivas H&E confirmaron la presencia de partículas de titanio y la infiltración de células inflamatorias en los tejidos gingivales peri-implante recolectados de pacientes con FI o SI. El examen visual de las imágenes mostró que las partículas de titanio estaban presentes en aproximadamente el 85% de las muestras de tejido, lo que significa que las partículas de titanio a menudo se desprenden de la superficie del implante. Sin embargo, la expresión de células inflamatorias en las muestras de FI fue mayor que en las muestras de SI. Este hallazgo se refiere al papel de las partículas de titanio para aumentar la inflamación en los tejidos gingivales peri-implante. Como lo propuso Tawse-Smith et al., las partículas de titanio se encontraron altamente abundantes en todos los tejidos de peri-implantitis en comparación con otras áreas de prueba y control utilizando el análisis SEM-EDS. Mostramos que las células inflamatorias que infiltraban los tejidos de peri-implantitis eran principalmente crónicas, lo cual es un hallazgo común para los tejidos de peri-implantitis. Esto está de acuerdo con un estudio de Dapunt et al. que encontró que la liberación de iones metálicos de la prótesis puede inducir una fase aguda de la enfermedad inflamatoria crónica con infiltrados de monocitos, células T y osteoclastos. No obstante, la influencia de factores microbianos nunca debe ser descuidada en el desarrollo de peri-implantitis, aunque el enfoque principal del estudio actual fue investigar la infiltración de partículas de titanio y células inflamatorias en los tejidos gingivales peri-implante y las consecuencias de este hecho. Por lo tanto, se realizarán evaluaciones adicionales en el tejido gingival para identificar el contenido de partículas de titanio en investigaciones futuras, lo que allanará el camino para una mejor comprensión de la asociación entre el contenido de partículas de titanio en los tejidos gingivales y la inflamación crónica, peri-implantitis y el fracaso de la osteointegración.

Las imágenes del análisis IHC mostraron una tinción positiva de CD68 y CD3 en presencia de partículas de titanio, y la expresión de la tinción positiva en casos de FI fue mayor que en casos de SI. Esto podría ser una indicación del aumento de la infiltración de macrófagos y linfocitos en los tejidos gingivales alrededor de FI en comparación con los tejidos de SI, lo que puede referirse al papel de las partículas de titanio en la polarización de macrófagos. Este hallazgo está de acuerdo con el estudio clínico de Rao et al. que declaró que el fracaso de los implantes ortopédicos estaba relacionado con la presencia de macrófagos M1 polarizados en exceso alrededor de las articulaciones de titanio. Además, Galarraga Vinueza et al. mostraron en el estudio IHC que hubo un aumento en la proporción de macrófagos M1/M2 en los tejidos gingivales peri-implante de pacientes con peri-implantitis. En consecuencia, esto puede considerarse un factor importante relacionado con el fracaso del implante y podría llevar a la absorción del hueso circundante y al aflojamiento de los implantes.

En el escenario clínico, todas las células en los tejidos gingivales peri-implante generalmente están expuestas a partículas de desgaste de titanio. Sin embargo, en los experimentos in vitro utilizados en el estudio de validación, se dirigió solo a los macrófagos como la principal célula inmunitaria incluida en la respuesta a las reacciones de cuerpo extraño. Vale la pena considerar que el análisis IHC confirmó la infiltración de macrófagos en los tejidos gingivales peri-implante recolectados de FI y SI con la presencia de partículas de titanio y los genes relacionados identificados por GSEA en ambas comparaciones. Por lo tanto, la validación funcional fue crucial para confirmar el impacto de las partículas de titanio en la polarización de los macrófagos M1, que son responsables de la expresión de citoquinas inflamatorias como Il-18, Il-1β, CCL3, TNF-α e IL-8.

En el presente estudio, no fue posible reconocer el tamaño de las partículas de titanio en las imágenes de IHC y H&E debido a la posible modificación causada por la técnica de corte con microtomo, que limita el grosor de las muestras. Por lo tanto, para replicar los escenarios clínicos, utilizamos diferentes concentraciones de partículas de TiO2 de tamaño nano y micro para tratar macrófagos M0 derivados de monocitos THP-1, validando así los hallazgos obtenidos del análisis IHC. Los resultados a nivel de proteínas confirmaron que las partículas de TiO2 inducen la secreción de IL-1β por los macrófagos. Este hallazgo estaba de acuerdo con evidencia previa que demuestra que IL-1 sirve como mediador proinflamatorio expresado por los macrófagos. Además, nuestros hallazgos mostraron una regulación al alza en la expresión de marcadores de macrófagos en las muestras de tejido de FI en comparación con SI. Vale la pena señalar que IL-1β se asoció con la diferenciación directa de pre-osteoclastos en osteoclastos, lo que potencialmente influye en el fracaso de la osteointegración del implante dental. Además, la activación de NF-κB involucra numerosas moléculas, incluyendo IL-1β y TNF-α. De manera emocionante, el promotor de IL-1β contiene un sitio funcional de unión a NF-κB, y esto indica que IL-1 autoregula positivamente su síntesis ya que actúa como un potencial inductor de la actividad de unión a NF-κB. En consecuencia, el gen IL-1β puede considerarse un importante miembro adicional de la familia de genes de citoquinas que se regula en parte por la familia de factores de transcripción NF-κB/rel.

La respuesta inmunitaria a las partículas de titanio es un proceso complejo influenciado por la interacción entre numerosas células inmunitarias. Estas células están expuestas a las partículas y producen diferentes citoquinas, que a su vez inducen la activación de macrófagos proinflamatorios. En nuestro presente estudio, hubo una regulación al alza de estas citoquinas proinflamatorias por los macrófagos, indicando el posible vínculo entre la liberación de partículas de titanio y el fracaso de los implantes dentales. Este hallazgo está en línea con investigaciones previas que demuestran que IL-1β y las citoquinas inflamatorias impactan la activación de osteoclastos y están asociadas con la regulación negativa del colágeno tipo 1. En consecuencia, la citoquina IL-1β está implicada en la resorción ósea y la peri-implantitis. TNF-α juega un papel crucial en la organización de la respuesta inflamatoria y la infiltración de células inmunitarias. Si bien no se observaron alteraciones significativas en el nivel de proteínas de TNF-α tras varios tratamientos con TiO2, se reconoce ampliamente que TNF-α, junto con IL-1β, provoca vías de señalización descendente, como las quinasas activadas por mitógenos (MAPKs) y el factor de transcripción NF-κB. Estas vías eventualmente llevan a la liberación de quimioquinas y citoquinas proinflamatorias adicionales.

CCL3 desempeña un papel crucial en el reclutamiento y activación de macrófagos, especialmente en sitios de inflamación y daño tisular. La liberación de CCL3 por los macrófagos tratados con partículas de TiO2 sugiere que estas partículas desencadenan una respuesta inmunitaria significativa que puede contribuir al fracaso de la osteointegración de los implantes dentales. Esta red de interacción entre citoquinas y macrófagos proinflamatorios subraya la complejidad del microambiente inmunitario peri-implante y su influencia en la biocompatibilidad y éxito de los implantes dentales. Estudios futuros deben enfocarse en la caracterización detallada de estas interacciones y sus implicaciones clínicas para mejorar los resultados de los tratamientos con implantes dentales y prevenir la peri-implantitis y el fracaso de la osteointegración.

"""

def replace_non_latin1_characters(text):
    return text.encode('latin-1', errors='replace').decode('latin-1')

# Use the function before adding text to the PDF
text = replace_non_latin1_characters(translated_text)
#pdf.cell(200, 10, txt=text, ln=True)

pdf.multi_cell(0, 10, text)

# Save the PDF
pdf_output_path = "/Users/master/Downloads/Particulas_de_Titanio_Articulo2.pdf"
pdf.output(pdf_output_path)
pdf_output_path
