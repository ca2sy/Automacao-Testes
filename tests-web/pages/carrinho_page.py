from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
 
class CarrinhoPage:
  
 
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
 
    def obter_quantidade_itens(self):
        itens = self.wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "cart_item")))
        return len(itens)
 
    def ir_para_checkout(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()