import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from Testing_framework.framework.resources.helpers.logger import logger
import os

class ReportBuilder:
    def __init__(self, sender_email, sender_password, recipient_email, smtp_server, smtp_port):
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.recipient_email = recipient_email
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

    def create_email(self, subject, html_content):
        """
        Crea un oggetto email compatibile sia con l'uso di `MIMEMultipart` che con `sendgrid.Mail`.

        Args:
            subject (str): Oggetto dell'email.
            html_content (str): Contenuto HTML dell'email.

        Returns:
            dict: Contiene il messaggio creato come MIMEMultipart e come Mail per SendGrid.
        """
        # Crea il messaggio MIMEMultipart per email normale
        mime_message = MIMEMultipart()
        mime_message['From'] = self.sender_email
        mime_message['To'] = self.recipient_email
        mime_message['Subject'] = subject
        mime_message.attach(MIMEText(html_content, 'html'))

        # Crea il messaggio Mail per SendGrid
        sendgrid_message = Mail(
            from_email=self.sender_email,
            to_emails=self.recipient_email,
            subject=subject,
            html_content=html_content
        )

        # Ritorna entrambi i formati
        return {
            'mime_message': mime_message,
            'sendgrid_message': sendgrid_message
        }

    def send_email(self, message):
        """
        Invia un'email utilizzando SendGrid.

        Args:
            message (Mail): Oggetto Mail contenente le informazioni dell'email.
        """
        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(message)
            logger.info(response.status_code)
            logger.info(response.body)
            logger.info(response.headers)
        except Exception as e: 
            logger.error(str(e))

