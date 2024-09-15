import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from Testing_framework.framework.resources.helpers.report_builder import ReportBuilder
import sendgrid
import base64
from sendgrid.helpers.mail import Attachment, FileContent, FileName, Disposition, ContentId

class HTMLTestReportBuilder(ReportBuilder):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def build_and_send_report(self, test_data, images, log_file):
        """
        Costruisce e invia un report HTML per un test utilizzando SendGrid.

        Args:
            test_data (dict): Dizionario contenente i dati del test (es: Test_id, Test_description).
            images (list): Lista di tuple (nome_immagine, percorso_immagine).
            log_file (str): Percorso del file di log.
        """

        # Template HTML
        html_template = """
        <html>
        <body>
        <h1>Report Test</h1>
        <p><b>ID Test:</b> {Test_id}</p>
        <p><b>Description:</b> {Test_description}</p>
        <h2>CPU and RAM Usage</h2>
        {images}
        <h2>Log del Test</h2>
        <pre>{log}</pre>
        </body>
        </html>
        """

        # Costruisci la sezione delle immagini
        images_html = ""
        for name, path in images:
            images_html += f"<img src='cid:{name}'>"

        # Leggi il contenuto del file di log
        with open(log_file, 'rb') as f:
            log_content = f.read()

        # Sostituisci i placeholder nel template
        html_content = html_template.format(**test_data, images=images_html, log=log_content.decode('utf-8'))

        # After formatting the template (step 4)
        with open("test_report.html", "w", encoding="utf-8") as f:
            f.write(html_content)
        # Crea il messaggio email SendGrid
        email_data = self.create_email(f"Report Test {test_data['Test_id']}", html_content)
        sendgrid_message = email_data['sendgrid_message']

        # Aggiungi le immagini come allegati convertiti in base64
        for name, path in images:
            with open(path, 'rb') as f:
                img_data = f.read()
                encoded_img = base64.b64encode(img_data).decode()  # Converti in base64 e decodifica in stringa
                attachment = Attachment(
                    file_content=FileContent(encoded_img),
                    file_name=FileName(name),
                    disposition=Disposition("inline"),
                    content_id=ContentId(name)
                )
                sendgrid_message.add_attachment(attachment)


        # Aggiungi il file di log come allegato
        with open(log_file, 'rb') as f:
            log_data = f.read()
            encoded_log = base64.b64encode(log_data).decode()  # Converti in base64 e decodifica in stringa
            attachment = Attachment(
                file_content=FileContent(encoded_log),
                file_name=FileName(log_file),
                disposition=Disposition("attachment")
            )
            sendgrid_message.add_attachment(attachment)

        # Invia il messaggio SendGrid
        self.send_email(sendgrid_message)