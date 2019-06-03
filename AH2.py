from selenium import webdriver
import json
browser = webdriver.Firefox(executable_path = '/home/poulami/Downloads/geckodriver')

browser.get('https://www.appearhere.us/spaces/search?search_source=home-page&search_medium=link&search_campaign=home-page-space-grid&search_id=uh6r6cemm9&page=1&type=space')
num=0
n=1
while(n!=15):
	for x in range(1, 7):
		#image=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[1]/li[" + str(x) + "]/div/div/div[1]/div/div/div/div/ul/li[1]/a/div/img')
		expected_rent=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[1]/li[" + str(x) + "]/div/div/div[2]/a/div[1]/div/span[2]')
		title=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[1]/li[" + str(x) + "]/div/div/div[2]/a/div[2]')
		city=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[1]/li[" + str(x) + "]/div/div/div[2]/a/div[3]/span[1]/span')
		area_unit=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[1]/li[" + str(x) + "]/div/div/div[2]/a/div[3]/span[3]/span/span')
		a="New York, NY, USA"
		#i=image.text
		e=expected_rent[num].text
		t=title[num].text
		c=city[num].text
		au=area_unit[num].text
		dict={"Area:":a,"Expected_Price:":e,"Title:":t,"State:":c,"Area_Unit:":au}
		with open('/home/poulami/Project/data/AppearHere1.json', 'a') as file:
			file.write(json.dumps(dict))
		num=num+1
	for x in range(1, 25):
		#image=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[1]/li[" + str(x) + "]/div/div/div[1]/div/div/div/div/ul/li[1]//a/div/img')
		expected_rent=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[2]/li[" + str(x) + "]/div/div/div[2]/a/div[1]/div/span[2]')
		title=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[2]/li[" + str(x) + "]/div/div/div[2]/a/div[2]')
		city=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[2]/li[" + str(x) + "]/div/div/div[2]/a/div[3]/span[1]/span')
		area_unit=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[2]/li[" + str(x) + "]/div/div/div[2]/a/div[3]/span[3]/span/span')
		a="New York, NY, USA"
		#i=image.text
		e=expected_rent[num].text
		t=title[num].text
		c=city[num].text
		au=area_unit[num].text
		dict={"Area:":a,"Expected_Price:":e,"Title:":t,"State:":c,"Area_Unit:":au}
		with open('/home/poulami/Project/data/AppearHere1.json', 'a') as file:
			file.write(json.dumps(dict))
		num=num+1
# 		WebElement textbox = driver.findElement(By.class("idOfElement"));
# textbox.sendKeys(Keys.ENTER);
	n=n+1
	# browser.find_element_by_class("Bloom__root_oj Bloom__fontSmallI_6").click()
	# link = browser.find_element_by_link_text('?href=2')
	# link.click()
	#browser.find_element_by_('Bloom__root_gt Bloom__arrow_fh Bloom__nextArrow_om').click()
	
   

