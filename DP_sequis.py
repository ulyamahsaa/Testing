from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://sequis.co.id/id/solution-finder/')

drp1 = driver.find_element_by_xpath("//body/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/section[1]/div[3]/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]")
drp1.click()

opt1 = driver.find_element_by_xpath("//span[contains(text(),'Dana pensiun')]")
opt1.click()

btn = driver.find_element_by_xpath("//body/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/section[1]/div[4]/button[1]")
btn.click()

# jk = driver.find_element_by_xpath("//body/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/section[2]/div[3]/div[1]/div[1]/div[1]/div[1]/label[3]/span[1]/input[1]")
# jk.click()

# drp2 = driver.find_element_by_xpath("//body/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/section[2]/div[3]/div[1]/div[1]/div[2]/div[1]/span[1]/span[1]")
# drp2.click()

# opt2 = driver.find_element_by_xpath("//span[contains(text(),'17 - 25 tahun')]")
# opt2.click()

stat = driver.find_element_by_xpath("//input[@id='single']")
stat.click()

# btn2 = driver.find_element_by_xpath("//body/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/section[2]/div[4]/button[1]")
# btn2.click()
