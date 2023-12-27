from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui  
from selenium.webdriver.support.ui import Select
from verifyBD import NomeInst
from time import sleep

servico= Service(ChromeDriverManager().install())

navegador=webdriver.Chrome(service=servico)

#Entrando no site
navegador.get("http://homologa.siga.fapesb.ba.gov.br/cadastro_inst_novo/login.wsp")
#Logando
navegador.find_element('xpath','//*[@id="tudo"]/table[2]/tbody/tr/td/table/tbody/tr[2]/td[2]/form/table/tbody/tr[1]/td[2]/input').send_keys('jefferson.amorim')
navegador.find_element('xpath','//*[@id="tudo"]/table[2]/tbody/tr/td/table/tbody/tr[2]/td[2]/form/table/tbody/tr[2]/td[2]/input').send_keys("Processo2016")
navegador.find_element('xpath','//*[@id="tudo"]/table[2]/tbody/tr/td/table/tbody/tr[2]/td[2]/form/table/tbody/tr[3]/td/input').click()
#Selecionando Insts e mostrando detalhes
select_element = navegador.find_element('xpath','//*[@id="tmp.inst_tmp"]')
# Criar um objeto Select
select = Select(select_element)
# Texto a ser procurado
texto_procurado = 'Campus dos Males'

navegador.find_element('xpath','/html/body/table[1]/tbody/tr/td/form/table/tbody/tr/td[1]/table[2]/tbody/tr/td/table/tbody/tr/td/input').click()
#Ecluir Instituição dos pedidos

# navegador.find_element('xpath','//*[@id="tmp.cgc_tmp_inst"]').send_keys(Keys.CONTROL + "a")
# navegador.find_element('xpath','//*[@id="tmp.cgc_tmp_inst"]').send_keys(Keys.CONTROL + "c")


sleep(200)