from random import randint
from teste.test_login import TestLogin
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestUntitled():
  def setup_method(self):
    #google chrome navegador padrão, selecione firefox ou phantonjs caso headless, é preciso que o selenium grid esteja configurado
    self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
    self.vars = {}
  s
  def teardown_method(self):
    self.driver.quit()

  def test_login(self):
    self.driver.get("http://automationpractice.com/index.php")
    self.driver.set_window_size(1247, 686)
    self.driver.find_element(By.LINK_TEXT, "Sign in").click()
    self.driver.find_element(By.ID, "email").send_keys("teste2651@gmail.com")
    self.driver.find_element(By.ID, "passwd").send_keys("pass123")
    self.driver.find_element(By.CSS_SELECTOR, "#SubmitLogin > span").click()

  def test_untitled(self):
    self.driver.get("http://automationpractice.com/index.php")
    self.driver.set_window_size(1247, 686)
    self.driver.find_element(By.XPATH, f"//ul[@id=\'homefeatured\']/li[{randint(0,6)}]/div/div[2]/div[2]/a/span").click()# escolhe entre 7 produtos disponiveis na home
    self.driver.find_element(By.CSS_SELECTOR, ".button-medium > span").click()
    self.driver.find_element(By.CSS_SELECTOR, ".standard-checkout > span").click()
    self.driver.find_element(By.CSS_SELECTOR, ".button:nth-child(4) > span").click()
    self.driver.find_element(By.ID, "cgv").click()
    self.driver.find_element(By.CSS_SELECTOR, ".standard-checkout > span").click()
    payments = self.driver.find_element(By.ID,"HOOK_PAYMENT")
    payment = payments[randint(0,1)]#escolhe entre os dois metodos de pagamento
    assert payment.click()
    assert self.driver.find_element(By.CSS_SELECTOR, "#cart_navigation span").click()
  
teste = TestUntitled()
teste.setup_method()
teste.test_login()
teste.test_untitled()
teste.teardown_method()