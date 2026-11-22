# Conversor XML a PDF 🧾

¡Bienvenido! Este proyecto está desarrollado en Python utilizando Flask para convertir documentos XML (como facturas electrónicas) a formato PDF, siguiendo el diseño preestablecido en plantillas HTML/CSS.

## 🎯 Funcionalidades

- Subida de archivos XML para procesarlos y generar documentos PDF.
- Generación de códigos de barras en el PDF basados en información extraída del XML.
- Plantilla profesional y personalizable con Bootstrap.
- Interfaz moderna y responsiva.
- Descarga automática del archivo PDF generado.

---

## 📸 Vista Previa
### Página Principal

### PDF Generado


---

## 🚀 Tecnologías Utilizadas


    Python 3.8+
    Flask (Framework web)
    WeasyPrint (Conversión de HTML a PDF)
    Bootstrap 5 (Estilo y diseño responsivo)
    Jinja2 (Motor de plantillas)

---

## 📂 Estructura del Proyecto

```plaintext
.
├── app.py                     # Archivo principal de la aplicación Flask
├── templates/                 # Plantillas HTML
│   ├── index.html             # Página principal
│   ├── invoice.html           # Plantilla para generar el PDF
│   ├── invoice.css            # Estilos para el PDF
├── output/                    # Carpeta donde se almacenan los PDFs generados
├── uploads/                   # Carpeta para archivos XML subidos
├── xml_to_pdf_functions/      # Funciones para procesar XML
│   ├── __init__.py
│   ├── xml_to_pdf_functions.py
├── requirements.txt           # Dependencias del proyecto
├── README.md                  # Este archivo

```
---

## 🛠️ Instalación y Configuración

### Requisitos Previos
        Python 3.8 o superior
        Gestor de paquetes pip

1. Clonar el Repositorio

```plaintext
git clone https://github.com/tu-usuario/conversor-xml-to-pdf.git
cd conversor-xml-to-pdf

```

2. Instalar Dependencias

```plaintext
pip install -r requirements.txt
```

3. Ejecutar la Aplicación
```plaintext
    python app.py
```
Abrir en el Navegador Accede a la aplicación en: http://127.0.0.1:5000/

---

## 🎨 Personalización

Plantilla HTML/CSS del PDF: Modifica templates/invoice.html y templates/invoice.css para personalizar el diseño del PDF.
Carpeta de Almacenamiento:
    Cambia la carpeta de subida de archivos (uploads/) o la carpeta de PDFs generados (output/) modificando las variables UPLOAD_FOLDER y GENERATED_PDF_FOLDER en app.py.

---

## 🖼️ Ejemplo de Uso

    Paso 1: Sube un archivo XML desde la página principal.
    Paso 2: El sistema procesa el XML y genera un PDF con el diseño predefinido.
    Paso 3: Descarga automáticamente el archivo PDF generado.

---

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si deseas mejorar este proyecto, sigue estos pasos:

    Haz un fork del repositorio.
    Crea una rama con tu funcionalidad:

git checkout -b mi-nueva-funcionalidad

Realiza los cambios y haz un commit:

git commit -m 'Añadí nueva funcionalidad'

Sube los cambios:

    git push origin mi-nueva-funcionalidad

    Crea un pull request.

---

## 📝 Licencia

Este proyecto está bajo la [licencia MIT](LICENSE), a nombre de Israel Ubeda.
Código interno de registro: [IU-OSS-0003](LICENSE_ID.txt).

---
## ✨ Autor

Desarrollado por Israel Ubeda
📧 Contacto: israel.ubedabravo@gmail.com

inspirada en el desarrollo de ![tonicanada](https://github.com/tonicanada/sii_chile_xml_to_pdf)

¡Gracias por usar este conversor XML a PDF! 🎉
