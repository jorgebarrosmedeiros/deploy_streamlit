
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 

driver = webdriver.Chrome("/home/jorge/jorge/chromedriver")

driver.get('https://fcalatam.manusis4.com/')

#preencher usuario
usuario_input = driver.find_element_by_name("login")
usuario_input.send_keys("f03967d")
senha_input = driver.find_element_by_name("password")
senha_input.send_keys("Pallet@20")
senha_input.send_keys(Keys.ENTER)

#entrando na área de exports
exportador =  driver.find_element_by_id("tool-1121-toolEl").click()
#exportador.click()
entrada_ss = driver.find_element_by_id("td_menu-Suite:view:DataExportMaintReq-btnIconEl").click()

#marcar z4
z4 = driver.find_element_by_id("gridview-1343-record-26").click()

#adicionar data
data_inicial = driver.find_element_by_id("datefield-1392-inputEl")
data_inicial.send_keys("02/04/2020")
data_final  = driver.find_element_by_id("datefield-1394-inputEl")
data_final.send_keys("01/10/2020")

#exportar 
exportar = driver.find_element_by_id("button-1485").click()

#dar o ok
ok = driver.find_element_by_id("button-1005").click()
<img id="tool-1121-toolEl" src="data:image/gif;base64,R0lGODlhAQABAID/AMDAwAAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==" class="x-tool-img x-tool-expand-bottom" role="presentation">
