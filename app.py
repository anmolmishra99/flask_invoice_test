from flask import Flask, send_file
import pdfkit

app = Flask(__name__)

@app.route('/download_pdf')
def download_pdf():
    options = {
        'page-size': 'Letter',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'custom-header': [
            ('Accept-Encoding', 'gzip')
        ],
        'no-outline': None
    }

    # Define the path to the HTML file
    html_file_path = 'invoice.html'
    
    # Save the PDF to a temporary file
    pdf_file_path = 'shaurya.pdf'
    pdfkit.from_file(html_file_path, pdf_file_path, options=options)
    
    # Send the file for download
    return send_file(pdf_file_path, as_attachment=True, download_name='shaurya.pdf')

if __name__ == '__main__':
    app.run(debug=True)
