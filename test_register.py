
from random import randint
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

dados = [{"email":"test1@gmail.com","first_name":"first1", "second_name":"second1", "address":"add1","Passwd":"pass123", "city":"city1", "post_code":"post1", "phone":"12345"},
          {"email":"test2@gmail.com","first_name":"first2", "second_name":"second2", "address":"add2","Passwd":"pass1234", "city":"city2", "post_code":"post2", "phone":"123456"},
          {"email":"test3@gmail.com","first_name":"first3", "second_name":"second3", "address":"add3", "Passwd":"pass12345", "city":"city3", "post_code":"post3", "phone":"1234567"}]

index = randint(0,len(dados)-1)
user = dados[index]
class TestUntitled():
  def setup_method(self):
    #google chrome navegador padrão, selecione firefox ou phantonjs caso headless, é preciso que o selenium grid esteja configurado
    self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
    self.vars = {}  
  
  def teardown_method(self):
    self.driver.quit()
  
  def test_untitled(self):
    self.driver.get("http://automationpractice.com/index.php")
    self.driver.set_window_size(1246, 682)
    self.driver.find_element(By.LINK_TEXT, "Sign in").click()
    self.driver.find_element(By.ID, "email_create").send_keys(user.email)
    self.driver.find_element(By.CSS_SELECTOR, "#SubmitCreate > span").click()
    self.driver.find_element(By.ID, "customer_firstname").send_keys(user.first_name)
    self.driver.find_element(By.ID, "customer_lastname").send_keys(user.second_name)
    self.driver.find_element(By.ID, "passwd").send_keys(user.passwd)
    self.driver.find_element(By.ID, "address1").send_keys(user.address)
    self.driver.find_element(By.ID, "city").send_keys(user.city)
    self.driver.find_element(By.CSS_SELECTOR, ".account_creation:nth-child(2)").click()
    self.driver.find_element(By.ID, "id_state").click()
    dropdown = self.driver.find_element(By.ID, "id_state")
    dropdown.find_element(By.XPATH, "//option[. = 'Alaska']").click()
    self.driver.find_element(By.ID, "postcode").send_keys(user.post_code)
    self.driver.find_element(By.ID, "phone_mobile").send_keys(user.phone)
    self.driver.find_element(By.ID, "alias").click()
    self.driver.find_element(By.CSS_SELECTOR, "#submitAccount > span").click()
  
teste = TestUntitled()
teste.setup_method()
teste.test_untitled()
teste.teardown_method()