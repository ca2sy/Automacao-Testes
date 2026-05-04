import os
import unittest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage
from pages.produtos_page import ProdutosPage
from pages.carrinho_page import CarrinhoPage
from pages.checkout_page import CheckoutPage

load_dotenv()


class TestSauceDemo(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

        self.url = os.getenv("SAUCE_URL")
        self.username = os.getenv("SAUCE_USERNAME")
        self.password = os.getenv("SAUCE_PASSWORD")

    def test_login_com_sucesso(self):
        self.driver.get(self.url)

        login_page = LoginPage(self.driver)
        login_page.fazer_login(self.username, self.password)

        self.assertIn("inventory", self.driver.current_url)
        print("Login realizado com sucesso!")

    def test_fluxo_compra(self):
        self.driver.get(self.url)

        login_page = LoginPage(self.driver)
        login_page.fazer_login(self.username, self.password)

        produtos_page = ProdutosPage(self.driver)
        produtos_page.adicionar_primeiro_produto()
        self.assertEqual(produtos_page.obter_quantidade_carrinho(), "1")

        self.assertEqual(produtos_page.obter_quantidade_carrinho(), "1")

        produtos_page.ir_para_carrinho()

        carrinho_page = CarrinhoPage(self.driver)
        self.assertEqual(carrinho_page.obter_quantidade_itens(), 1)
        carrinho_page.ir_para_checkout()

        checkout_page = CheckoutPage(self.driver)
        checkout_page.preencher_dados("QA", "Tester", "12345")
        checkout_page.clicar_continuar()
        checkout_page.clicar_finalizar()

        mensagem = checkout_page.obter_mensagem_sucesso()
        self.assertEqual(mensagem, "Thank you for your order!")
        print("Compra finalizada com sucesso!")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()