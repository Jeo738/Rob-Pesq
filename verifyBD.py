import psycopg2
from sg import senhaBD
from rich.text import Text

# Configuração da conexão com o banco de dados
dbname = 'cad20'
user = 'jefferson'
password = senhaBD
host = '10.78.246.100'  # Endereço do servidor PostgreSQL
port = '5432'  # Porta padrão do PostgreSQL

# Conectando ao banco de dados
conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
cursor = conn.cursor()

# Executando uma consulta SQL

query1 = 'select  ti2.cgc_tmp_inst,i.cgc_inst,niv_tmp_inst, niv_inst, cep_tmp_inst,cep_inst,bairro_tmp_inst, bairro_inst ,email_pesq, nme_tmp_inst, nme_inst  from tmp_instituicao ti2 join instituicao i on  ti2.nme_tmp_inst=i.nme_inst  and ti2.niv_tmp_inst=i.niv_inst and cep_tmp_inst=cep_inst ;'
cursor.execute(query1)

# Obtendo os resultados
results = cursor.fetchall()

for row in results:

    quant=row
    with open('quant.txt','w') as arquivo:
     for quantidade in quant:
        arquivo.write(str(quantidade)+ '\n')
     Registro=quant
    with open('Registro.txt','w') as arquivo:
     for quantidade in Registro:
        arquivo.write(str(quantidade)+', ' + '\n')


# Definindo o nome do arquivo
nome_arquivo = "quant.txt"

# Mapeamento de valores para nomes de unidades
mapeamento_instituicoes = {
    "1": "da Instituição",
    "2": "da Unidade",
    "3": "do Departamento"
}

# Abrindo o arquivo em modo de leitura
with open(nome_arquivo, "r") as arquivo:
    # Leia todas as linhas do arquivo
    linhas = arquivo.readlines()
    
    # Verifique se a terceira linha está no mapeamento
    valor_quarta_linha = linhas[3].strip()
    if valor_quarta_linha in mapeamento_instituicoes:
        nuInst = mapeamento_instituicoes[valor_quarta_linha]
    else:
        nuInst = "Nivel Inst não encontrado"
    
    print("Valor do nivel Inst:", nuInst)
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

    print("Nome da Instituicao pesq:", NomeInst)

    if len(linhas) >= 9:
        NomeInstcadas = linhas[10].strip()
        
    else:
        NomeInstcadas = "Linha não encontrada"

    print("Nome da Inst que ja consta:", NomeInstcadas)

    if len(linhas) >= 9:
        cgctmpInst = linhas[0].strip()
    else:
        cgctmpInst = "Linha não encontrada"

    print("CNPJ da Instituicao pesq:", cgctmpInst)


    

# Fechando a conexão
cursor.close()
conn.close()
# filename = "quant.txt"
#  # Abre o arquivo em modo de escrita para limpar seu conteúdo
# with open(filename, "w") as file:
#     file.write("")  # Escreve uma string vazia para substituir o conteúdo existente

# print("Arquivo limpo com sucesso.")