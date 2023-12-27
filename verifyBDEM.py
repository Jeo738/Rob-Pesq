import psycopg2
from sg import senhaBD
from rich.text import Text
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.message import EmailMessage
from datetime import datetime
from rich import print
from sg import senhaEm
# Configuração da conexão com o banco de dados
dbname = 'cad20'
user = 'jefferson'
password = senhaBD
host = '10.78.246.4'  # Endereço do servidor PostgreSQL
port = '5432'  # Porta padrão do PostgreSQL

# Conectando ao banco de dados
conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
cursor = conn.cursor()

# Executando uma consulta SQL
query = 'select  ti2.cgc_tmp_inst,i.cgc_inst,niv_tmp_inst, niv_inst, cep_tmp_inst,cep_inst,bairro_tmp_inst, bairro_inst ,email_pesq, nme_tmp_inst, nme_inst  from tmp_instituicao ti2 join instituicao i on  ti2.cgc_tmp_inst=i.cgc_inst and ti2.niv_tmp_inst=i.niv_inst and cep_tmp_inst=cep_inst ;'
cursor.execute(query)

# Obtendo os resultados
results = cursor.fetchall()

for row in results:

    quant=row
    with open('quant.txt','w') as arquivo:
     for quantidade in quant:
        arquivo.write(str(quantidade)+ '\n')
     Registro=quant
    with open('Registro.txt','a') as arquivo:
     for quantidade in Registro:
        arquivo.write(str(quantidade)+', ' + '\n')


# Defina o nome do arquivo
nome_arquivo = "quant.txt"

# Mapeamento de valores para nomes de unidades
mapeamento_instituicoes = {
    "1": "da Instituição",
    "2": "da Unidade",
    "3": "do Departamento"
}

# Abra o arquivo em modo de leitura
with open(nome_arquivo, "r") as arquivo:
    # Leia todas as linhas do arquivo
    linhas = arquivo.readlines()
    
    # Verifique se a terceira linha está no mapeamento
    valor_quarta_linha = linhas[3].strip()
    if valor_quarta_linha in mapeamento_instituicoes:
        nuInst = mapeamento_instituicoes[valor_quarta_linha]
    else:
        nuInst = "Outro Valor"
    
    print("Valor da nuInst:", nuInst)
 #Por e-mail em variável
    if len(linhas) >= 9:
        Em_pesq = linhas[8].strip()
    else:
        Em_pesq = "Linha não encontrada"

    print("E-mail pesq:", Em_pesq)
 #Por nme_tmp_inst em variável
    if len(linhas) >= 9:
        NomeInst = linhas[9].strip()
    else:
        NomeInst = "Linha não encontrada"

    print("Nome da Instituicao:", NomeInst)

    if len(linhas) >= 9:
        NomeInstcadas = linhas[10].strip()
        
    else:
        NomeInstcadas = "Linha não encontrada"

    print("Nome da Instituicao:", NomeInstcadas)



    print(row)

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


# Fechando a conexão
cursor.close()
conn.close()
