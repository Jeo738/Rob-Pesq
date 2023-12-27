from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui  
from verifyBD import NomeInst
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep

servico = Service(GeckoDriverManager().install())
navegador = webdriver.Firefox(service=servico)

#Entrando no site
navegador.get("http://homologa.siga.fapesb.ba.gov.br/cadastro_inst_novo/login.wsp")
#Logando
navegador.find_element('xpath','/html/body/div/table[2]/tbody/tr/td/table/tbody/tr[2]/td[2]/form/table/tbody/tr[1]/td[2]/input').send_keys('jefferson.amorim')
navegador.find_element('xpath','/html/body/div/table[2]/tbody/tr/td/table/tbody/tr[2]/td[2]/form/table/tbody/tr[2]/td[2]/input').send_keys("Processo2016")
navegador.find_element('xpath','/html/body/div/table[2]/tbody/tr/td/table/tbody/tr[2]/td[2]/form/table/tbody/tr[3]/td/input').click()
#Selecionando Insts e mostrando detalhes
navegador.find_element('xpath',f'//*[contains(text(), "{NomeInst}")]').click()
# navegador.find_element('xpath','/html/body/table[1]/tbody/tr/td/form/table/tbody/tr/td[1]/table[2]/tbody/tr/td/table/tbody/tr/td/input').click()
# #Excluir Instituição dos pedidos
# navegador.find_element('xpath','//*[@id="div1"]/fieldset/table[4]/tbody/tr/td[1]/table[4]/tbody/tr/td/input[2]').click()
# navegador.find_element('xpath','/html/body/table/tbody/tr[2]/td/input').click()


sleep(200)