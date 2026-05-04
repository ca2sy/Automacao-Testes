from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
class LoginPage:
   
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
 
    def preencher_usuario(self, username):
        campo = self.wait.until(EC.presence_of_element_located((By.ID, "user-name")))
        campo.send_keys(username)
 
    def preencher_senha(self, password):
        campo = self.wait.until(EC.presence_of_element_located((By.ID, "password")))
        campo.send_keys(password)
 
    def clicar_login(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()
 
    def fazer_login(self, username, password):
        self.preencher_usuario(username)
        self.preencher_senha(password)
        self.clicar_login()
 
    def obter_mensagem_erro(self):
        elemento = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='error']")))
        return elemento.text