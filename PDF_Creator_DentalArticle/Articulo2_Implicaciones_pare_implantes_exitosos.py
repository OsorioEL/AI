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
Resumen de los Riesgos para Implantes Dentales de Titanio Exitosos
Liberación de Partículas de Titanio:

Desprendimiento de Pequeñas Partículas: Incluso cuando los implantes funcionan bien, pequeñas piezas de titanio pueden desprenderse de la superficie del implante durante su uso normal o en limpiezas dentales regulares.
Desgaste de la Superficie: La capa protectora del titanio puede desgastarse con el tiempo, especialmente debido a los cambios en la acidez de la boca causados por la comida y las bacterias.
Respuesta del Sistema Inmunitario:

Reacción del Sistema Inmunitario: El sistema de defensa del cuerpo puede seguir reaccionando a estas pequeñas piezas de titanio, aunque no cause problemas obvios como una inflamación severa.
Reacción de las Células: Células inmunitarias especiales llamadas macrófagos pueden absorber estas partículas, posiblemente causando una inflamación leve y continua.
Inflamación Sutil:

Inflamación de Bajo Nivel: Puede haber una inflamación leve y continua alrededor del implante que no es perceptible, pero puede afectar la salud del tejido circundante con el tiempo.
Cambios a Nivel Genético:

Activación de Genes: Incluso sin problemas visibles, ciertos genes relacionados con la respuesta inmunitaria y la inflamación pueden estar más activos, indicando que el cuerpo está respondiendo al implante a nivel microscópico.
Actividad Inmunitaria Continua: Esta respuesta continua significa que el sistema inmunitario siempre está interactuando con el titanio, lo que podría tener efectos desconocidos a largo plazo.
Biocompatibilidad a Largo Plazo:

Potenciales Problemas Futuros: Podrían surgir problemas inesperados en el futuro a medida que el cuerpo continúe reaccionando al titanio. Esto podría incluir cambios sutiles en la salud del hueso o del tejido.
Interacción Inmunitaria Continua: La constante interacción con las partículas de titanio podría afectar la salud general de maneras que aún no se comprenden completamente.
"""

def replace_non_latin1_characters(text):
    return text.encode('latin-1', errors='replace').decode('latin-1')

# Use the function before adding text to the PDF
text = replace_non_latin1_characters(translated_text)
#pdf.cell(200, 10, txt=text, ln=True)

pdf.multi_cell(0, 10, text)

# Save the PDF
pdf_output_path = "/Users/master/Downloads/Articulo2_Implicaciones_para_Implantes_exitosos.pdf"
pdf.output(pdf_output_path)
pdf_output_path
