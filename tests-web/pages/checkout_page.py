from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
class CheckoutPage:
    """Page Object para as páginas de checkout do SauceDemo."""
 
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
 
    def preencher_dados(self, nome, sobrenome, cep):
        self.wait.until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys(nome)
        self.driver.find_element(By.ID, "last-name").send_keys(sobrenome)
        self.driver.find_element(By.ID, "postal-code").send_keys(cep)
 
    def clicar_continuar(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, "continue"))).click()
 
    def clicar_finalizar(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, "finish"))).click()
 
    def obter_mensagem_sucesso(self):
        elemento = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "complete-header")))
        return elemento.text
 