import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Union

class PyMail:

    """
    PyMail class to send emails using different SMTP servers with HTML templates.

    Args:
        server_type (Union[str, "GMAIL"]): The type of email server to use. Valid options are:
            - 'GMAIL'
            - 'OUTLOOK'
        user (Union[str, None]): The username for the email account. Must be provided.
        password (Union[str, None]): The password for the email account. Must be provided.
        from_email (Union[str, None]): The email address to send from. Must be provided.
        to_email (Union[str, None]): The email address to send to. Must be provided.
        subject (Union[str, None]): The subject of the email. Must be provided.
        template_path (Union[str, "."]): The file path to the HTML email template. Must be provided.

    Attributes:
        server_type (str): The chosen email server type.
        smtp_server (str): The SMTP server address.
        smtp_port (int): The SMTP server port.
        smtp_user (str): The SMTP username.
        smtp_password (str): The SMTP password.
        from_email (str): The sender's email address.
        to_email (str): The recipient's email address.
        subject (str): The email subject.
        html_template (str): The HTML template content for the email body.
    """
    
    @staticmethod
    def __version__():
        return '0.1.0'

    def __init__(self, 
                 server_type: Union[str, None] = 'GMAIL', 
                 user: Union[str, None] = None,
                 password: Union[str, None] = None, 
                 from_email: Union[str, None] = None,
                 to_email: Union[str, None] = None, 
                 subject: Union[str, None] = None,
                 template_path: Union[str, None] = None
                ) -> None:
        
        if server_type == 'GMAIL':
            self.smtp_server = 'smtp.gmail.com'
        elif server_type == 'OUTLOOK':
            self.smtp_server = 'smtp.outlook.com'
        else: 
            raise ValueError(f"Currently {server_type} server type is not supported. Please select a valid option")

        self.smtp_port = 587
        
        if user is None or password is None:
            raise ValueError("Please provide valid username and password to continue")
        
        self.smtp_user = user
        self.smtp_password = password

        self.from_email = from_email
        self.to_email = to_email
        self.subject = subject

        if isinstance(template_path, str):
            with open(template_path, 'r') as file:
                self.html_template = file.read()
        else:
            raise FileNotFoundError("File does not exist, please check the path again")
    
    def send(self):
        """Send the email using the provided details and HTML template."""

        # Replace placeholders in the HTML template with actual values
        html_content = self.html_template.replace('{{name}}', 'John Doe')

        # Create a MIMEText object
        message = MIMEMultipart('alternative')
        message['From'] = self.from_email
        message['To'] = self.to_email
        message['Subject'] = self.subject

        # Attach the HTML content to the email
        message.attach(MIMEText(html_content, 'html'))

        try:
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(self.smtp_user, self.smtp_password)
            server.sendmail(self.from_email, self.to_email, message.as_string())
            print('Email sent successfully.')
        except Exception as e:
            raise RuntimeError(f'Failed to send email: {e}')
        finally:
            server.quit()