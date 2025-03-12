from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("file:///C:/Users/claus_katzer/Documents/cadastro-de-produto/produto.html")

iCodProd = driver.find_element(By.ID, "iCodProd")
iCodProd.send_keys("12345678901")

iProd = driver.find_element(By.ID, "iProd")
iProd.send_keys("Araras")

iCat = driver.find_element(By.ID, "iCat")
iCat.send_keys("Camisetas")

iVal = driver.find_element(By.ID, "iVal")
iVal.send_keys("5,99")

iQtd = driver.find_element(By.ID, "iQtd")
iQtd.send_keys("9.00")

iDescProd = driver.find_element(By.ID, "iDescProd")
iDescProd.send_keys("Muitas coisa escritras aqui")

iForn = driver.find_element(By.ID, "iForn")
iForn.send_keys("Coca-Cola")

iCodBar = driver.find_element(By.ID, "iCodBar")
iCodBar.send_keys("19876543211987654321198765432119876543211987654321")

iPeso = driver.find_element(By.ID, "iPeso")
iPeso.send_keys("6.000")

iDimen = driver.find_element(By.ID, "iDimen")
iDimen.send_keys("12000")

iStatus = driver.find_element(By.ID, "iStatus")
iStatus.send_keys("Inativo")

iDescVal = driver.find_element(By.ID, "iDescVal")
iDescVal.send_keys("10")

iDatVal = driver.find_element(By.ID, "iDatVal")
iDatVal.send_keys("2025-02-18")

iSKU = driver.find_element(By.ID, "iSKU")
iSKU.send_keys("1657984546588")

submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
submit_button.click()

time.sleep(3)

driver.quit()