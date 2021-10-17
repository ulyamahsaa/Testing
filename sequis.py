from selenium import webdriver
# from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()
driver.get('https://sequis.co.id/')

drp1 = driver.find_element_by_class_name('jcf-select-text')
drp1.click()

opt1 = driver.find_element_by_xpath("//span[contains(text(),'Dana pensiun')]")
opt1.click()

nxt1 = driver.find_element_by_xpath("//body/main[1]/div[3]/section[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/button[1]/span[1]")
nxt1.click()

btn = driver.find_element_by_xpath("//body/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/section[1]/div[4]/button[1]")
btn.click()

# Page 2
jk = driver.find_element_by_xpath("//body/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/section[2]/div[3]/div[1]/div[1]/div[1]/div[1]/label[3]/span[1]/input[1]")
jk.click()

drp2 = driver.find_element_by_xpath("//body/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/section[2]/div[3]/div[1]/div[1]/div[2]/div[1]/span[1]/span[1]")
drp2.click()

opt2 = driver.find_element_by_xpath("//span[contains(text(),'17 - 25 tahun')]")
opt2.click()

stat = driver.find_element_by_xpath("//input[@id='single']")
stat.click()

btn2 = driver.find_element_by_xpath("//body/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/section[2]/div[4]/button[1]")
btn2.click()

# Page 3

pengeluaran = driver.find_element_by_xpath("//body/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/section[3]/div[3]/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]")
pengeluaran.click()

opt_peng = driver.find_element_by_xpath("//span[contains(text(),'5 - 10 juta')]")
opt_peng.click()

tabungan = driver.find_element_by_xpath("//body/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/section[3]/div[3]/div[1]/div[2]/div[1]/div[1]/span[1]/span[1]")
tabungan.click()

opt_tab = opt_peng = driver.find_element_by_xpath("//span[contains(text(),'1 - 2 juta')]")
opt_tab.click()

dana = driver.find_element_by_xpath("//body/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/section[3]/div[3]/div[1]/div[3]/div[1]/div[1]/span[1]/span[1]")
dana.click()

opt_dana = driver.find_element_by_xpath("//span[contains(text(),'kurang dari 1 juta')]")
opt_dana.click()

btn3 = driver.find_element_by_xpath("//body/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/section[2]/div[4]/button[1]")
btn3.click()

# Page 4 - Dapatkan hasil
hasil = driver.find_element_by_xpath("//a[contains(text(),'Dapatkan Hasil')]")
hasil.click()