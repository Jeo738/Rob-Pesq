import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.message import EmailMessage
from verifyBD import nuInst
from verifyBD import Em_pesq
from verifyBD import NomeInstcadas
from verifyBD import NomeInst
from datetime import datetime
from rich import print
from sg import senhaEm
# Configurações do remetente
sender_email = "jefferson.amorim@fapesb.ba.gov.br"
sender_password = senhaEm

# Configurações do destinatário
recipient_email = "testesfapesb@outlook.com"

# Configurações do servidor SMTP do Outlook para Office 365
smtp_server = "smtp.office365.com"
smtp_port = 587

# Criar mensagem
message = MIMEMultipart()
# 'sistemas@fapesb.ba.gov.br'
message["From"] = "jefferson.amorim@fapesb.ba.gov.br"  
message["To"] = recipient_email
message["Subject"] = "Cadastro de " + nuInst
#Hora do dia
agora = datetime.now()
hora_atual = agora.hour

if 6 <= hora_atual < 12:
    saudacao = "bom dia"
elif 12 <= hora_atual < 18:
    saudacao = "boa tarde"
else:
    saudacao = "boa noite"

print(f"{saudacao}!")
# Adicionar conteúdo ao email
body = "Prezado(a), "+ saudacao + '.' +'\n'+ '\n' +"O pré-cadastro "+ nuInst + ' ' +  NomeInst + ", não pôde ser aceito, pois já consta na nossa base de dados como " + NomeInstcadas +"." + '\n' + '\n'+ "Cordialmente, "
message.attach(MIMEText(body, "plain"))

# Iniciar a conexão SMTP
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()  # Iniciar conexão segura
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient_email, message.as_string())
    print("Email enviado com sucesso!")
