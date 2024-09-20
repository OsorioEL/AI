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
Resumen del artículo: Impurezas en implantes dentales comerciales de titanio
Objetivo:
El estudio analizó las impurezas presentes en quince sistemas comerciales de implantes dentales de titanio utilizando espectrometría de masas con plasma acoplado inductivamente (ICP-MS) y espectrometría de emisión óptica (ICP-OES), con un enfoque en los posibles riesgos para el paciente.

Resultados:

Se detectaron contaminantes metálicos exógenos en todos los implantes investigados, incluyendo níquel (Ni), cromo (Cr), antimonio (Sb) y niobio (Nb).
Algunos implantes contenían arsénico (As) y radionúclidos uranio-238 (U-238) y torio-232 (Th-232) en niveles ultra traza.
La composición elemental de los implantes fabricados a partir de titanio puro comercial (CpTi), Ti-6Al-4V y la aleación TiZr (Roxolid) se ajustó a las normas ISO/ASTM o a los datos del fabricante.
Implicaciones para el paciente:

Inflamación periimplantaria: La evidencia sugiere que los iones y partículas de titanio liberados de los implantes pueden estar asociados con reacciones inflamatorias locales. La liberación de estas partículas puede inducir inflamación en los tejidos circundantes, lo que podría comprometer la osteointegración del implante.
Reacciones inmunológicas: Los metales potencialmente alergénicos, como el níquel y el cromo, pueden desencadenar respuestas inmunológicas en algunos pacientes, provocando reacciones alérgicas o hipersensibilidad. Estas reacciones pueden llevar a la periimplantitis, una inflamación que afecta los tejidos alrededor del implante y puede resultar en la pérdida del implante.
Toxicidad y cáncer: La presencia de arsénico, aunque en niveles traza, es preocupante debido a su toxicidad y potencial cancerígeno. La exposición crónica al arsénico inorgánico está asociada con varios efectos adversos para la salud, incluyendo un mayor riesgo de cáncer.
Radionúclidos: La detección de uranio-238 y torio-232, aunque en niveles muy bajos, plantea preguntas sobre la posible radioactividad y sus efectos a largo plazo en el cuerpo humano. Aunque la relevancia clínica de estos radionúclidos no está completamente entendida, su presencia subraya la necesidad de evaluaciones de seguridad más rigurosas.
Conclusión:
Este estudio resalta la presencia de impurezas en los implantes dentales comerciales de titanio, destacando los posibles riesgos de inflamación y efectos inmunológicos para los pacientes. Se recomienda realizar investigaciones adicionales para comprender mejor las implicaciones clínicas de estas contaminaciones y adaptar las normas industriales para minimizar los riesgos asociados.
"""

def replace_non_latin1_characters(text):
    return text.encode('latin-1', errors='replace').decode('latin-1')

# Use the function before adding text to the PDF
text = replace_non_latin1_characters(translated_text)
#pdf.cell(200, 10, txt=text, ln=True)

pdf.multi_cell(0, 10, text)

# Save the PDF
pdf_output_path = "/Users/master/Downloads/Impurezas_Implantes_Titaneo_Resultados.pdf"
pdf.output(pdf_output_path)
pdf_output_path
