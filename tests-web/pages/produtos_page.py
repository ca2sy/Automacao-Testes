from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProdutosPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20) 

    def adicionar_primeiro_produto(self):
        botao = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".inventory_item button"))
        )
        botao.click()

    def adicionar_produto_por_indice(self, indice):
        botoes = self.wait.until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".inventory_item button"))
        )
        botoes[indice].click()

    def ir_para_carrinho(self):
        self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
        ).click()

    def obter_quantidade_carrinho(self):
        elemento = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        )
        return elemento.text