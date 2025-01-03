import os
from flask import Flask, request, render_template, send_file, flash, redirect, url_for
from werkzeug.utils import secure_filename
from xml_to_pdf_functions.xml_to_pdf_functions import sii_doc_XMLtoPDF

# Configuración de la app
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './uploads'  # Carpeta donde se guardan los archivos subidos
app.config['GENERATED_PDF_FOLDER'] = './output/pdf'  # Carpeta para los PDFs generados
app.config['SECRET_KEY'] = 'your_secret_key'

# Extensiones permitidas
ALLOWED_EXTENSIONS = {'xml'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No se seleccionó ningún archivo.')
        return redirect(url_for('index'))

    file = request.files['file']

    if file.filename == '':
        flash('No se seleccionó ningún archivo.')
        return redirect(url_for('index'))

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        try:
            # Procesa el XML para generar el PDF
            sii_doc_XMLtoPDF(filepath)
            flash('Archivo procesado correctamente.')
            # Encuentra el archivo PDF generado
            pdf_files = [
                f for f in os.listdir(app.config['GENERATED_PDF_FOLDER']) if f.endswith('.pdf')
            ]
            if not pdf_files:
                flash('No se pudo encontrar el PDF generado.')
                return redirect(url_for('index'))

            pdf_path = os.path.join(app.config['GENERATED_PDF_FOLDER'], pdf_files[-1])
            return send_file(pdf_path, as_attachment=True)
        except Exception as e:
            flash(f'Error al procesar el archivo: {e}')
            return redirect(url_for('index'))
    else:
        flash('Archivo no permitido. Solo se admiten archivos XML.')
        return redirect(url_for('index'))

if __name__ == '__main__':
    # Crear las carpetas necesarias si no existen
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    os.makedirs(app.config['GENERATED_PDF_FOLDER'], exist_ok=True)
    app.run(debug=True)
