from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from verifyBD import nuInst
from selenium.webdriver.support import expected_conditions as EC
from verifyBD import NomeInst
from time import sleep

servico= Service(ChromeDriverManager().install())

navegador=webdriver.Chrome(service=servico)

#Entrando no site
navegador.get("http://chamados.intranet.fapesb.ba.gov.br/index.php")
#Logando
navegador.find_element('xpath','//*[@id="login_name"]').send_keys('jefferson.amorim')
navegador.find_element('xpath','//*[@id="login_password"]').send_keys('jeo2016@')
navegador.find_element('xpath','//*[@id="boxlogin"]/form/p[5]/input').click()
#Assistencia > abrir chamado
navegador.find_element('xpath','//*[@id="menu_all_button"]').click()
navegador.find_element('xpath','//*[@id="show_all_menu"]/dl[1]/dd[2]/a').click()

navegador.find_element('xpath','//*[@id="mainformtable4"]/tbody/tr[1]/td/input').click()

# navegador.find_element('value','501').click()

sleep(200)