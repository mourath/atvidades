
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

class TestLogin():
  def setup_method(self):
    #google chrome navegador padrão, selecione firefox ou phantonjs caso headless, é preciso que o selenium grid esteja configurado
    self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
    self.vars = {}
  
  def teardown_method(self):
    self.driver.quit()
  
  def test_login(self):
    self.driver.get("http://automationpractice.com/index.php")
    self.driver.set_window_size(1247, 686)
    self.driver.find_element(By.LINK_TEXT, "Sign in").click()
    self.driver.find_element(By.ID, "email").send_keys("teste2651@gmail.com")
    self.driver.find_element(By.ID, "passwd").send_keys("pass123")
    self.driver.find_element(By.CSS_SELECTOR, "#SubmitLogin > span").click()
  
test = TestLogin()
test.setup_method()
test.test_login()
test.teardown_method()
