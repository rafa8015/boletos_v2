from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

navegador = webdriver.Chrome()

navegador.get(
    "https://auth.netcombo.com.br/web/login.html?client_id=MINHA_CLARO_RESIDENCIAL&redirect_uri=https%3A%2F%2Fminhaclaroresidencial.claro.com.br%2Flogin&response_type=code&scope=openid+minha_net&authMs=UP,EP,DOCP,OTP")

navegador.find_element(By.XPATH,
                       '/html/body/div[1]/div[2]/main/div/div[1]/section/div/div[2]/div[1]/div/form/div[1]/div/input').send_keys(
    "10406738807")
navegador.find_element(By.XPATH,
                       '/html/body/div[1]/div[2]/main/div/div[1]/section/div/div[2]/div[1]/div/form/div[3]/button').click()

navegador.find_element(By.XPATH, '//*[@id="password"]').send_keys("Rafael159357")

navegador.find_element(By.XPATH, '//*[@id="FormLogin"]/div[3]/button').click()

WebDriverWait(navegador, 40).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mcr-list-radio-157427817"]')))

botao = navegador.find_element(By.XPATH, '//*[@id="mcr-list-radio-157427817"]')

navegador.execute_script("arguments[0].click();", botao)

WebDriverWait(navegador, 20).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/article/div/div[2]/div/div[3]/button')))

botao1 = navegador.find_element(By.XPATH, '//*[@id="app"]/article/div/div[2]/div/div[3]/button')

navegador.execute_script("arguments[0].click();", botao1)

try:
    botao2 = WebDriverWait(navegador, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="consentimento-lgpd"]/div/div/div[1]/button')))
    botao2.click()
    botao2 = WebDriverWait(navegador, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="consentimento-lgpd"]/div/div/div[1]/button')))
    botao2.click()

except:
    pass

WebDriverWait(navegador, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id=\"invoiceAmount\"]')))

ValorClaro = navegador.find_element(By.XPATH, '//*[@id=\"invoiceAmount\"]')

print(ValorClaro.accessible_name)
