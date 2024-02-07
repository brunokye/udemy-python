import os
import pathlib
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template
from dotenv import load_dotenv

load_dotenv()

# Caminho arquivo HTML
CAMINHO_HTML = pathlib.Path(__file__).parent / "aula185.html"

# Dados do remetente e destinatário
remente = os.getenv("FROM_EMAIL", "")
destinatario = remente

# Configurações SMTP
smtp_server = os.getenv("SMTP_SERVER", "")
smtp_port = os.getenv("SMTP_PORT", "")
smtp_username = os.getenv("FROM_EMAIL", "")
smtp_password = os.getenv("EMAIL_PASSWORD", "")

# Mensagem de texto
with open(CAMINHO_HTML, "r", encoding="UTF-8") as arquivo:
    texto_arquivo = arquivo.read()
    template = Template(texto_arquivo)
    texto_email = template.substitute(nome="João")

# Transformar nossa mensagem em MIMEMultipart
mime_multipart = MIMEMultipart()
mime_multipart["from"] = remente
mime_multipart["to"] = destinatario
mime_multipart["subject"] = "Este é o assunto do email"

corpo_email = MIMEText(texto_email, "html", "UTF-8")
mime_multipart.attach(corpo_email)

with smtplib.SMTP(smtp_server, int(smtp_port)) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.send_message(mime_multipart)

    print("E-mail enviado com sucesso.")
