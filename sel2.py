from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import json
import logging
import traceback


# browser = webdriver.Firefox(executable_path = '/home/poulami/Downloads/geckodriver')
# browser.get('https://www.appearhere.us/spaces/search?search_source=home-page&search_medium=link&search_campaign=home-page-space-grid&search_id=uh6r6cemm9&page=1&type=space')

# x=browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[2]/div[1]/span[2]/a').get_attribute('href')
# browser.execute_script(x)
# list=["3"]
# pagination = browser.find_element_by_link_text('list[0]')
# pagination.click()

# browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[2]/div[1]/span[2]/a/span[1]/svg').click()
# element = browser.find_element_by_css_selector('li.Bloom__page_i2:nth-child(2)')
# webdriver.ActionChains(browser).move_to_element(element ).click(element ).perform()
# element = browser.find_element_by_css_selector('li.Bloom__page_i2:nth-child(2)')
# browser.execute_script("arguments[0].click();", element)
# btn = browser.find_element_by_class_name("Bloom__page_i2").find_element_by_css_selector("li.Bloom__page_i2:nth-child(1)")
# btn.click()
	
# btn=browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[2]/div[1]/span[2]/a/span[1]/svg')
# btn.click()
# pagination = browser.find_element_by_link_text('"5"')
# pagination.click()
#browser = webdriver.Firefox(executable_path = '/home/poulami/Downloads/geckodriver')
n=1
# num=0
# num1=0
while(n!=15):
	sleep(2)
	browser = webdriver.Firefox(executable_path = '/home/poulami/Downloads/geckodriver')
	url='https://www.appearhere.us/spaces/search?search_source=home-page&search_medium=link&search_campaign=home-page-space-grid&search_id=uh6r6cemm9&page=' + str(n) + '&type=space'
	
	browser.get(url)
	try:
		num=0
		for x in range(1, 7):
			
			expected_rent=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[1]/li[" + str(x) + "]/div/div/div[2]/a/div[1]/div/span[2]')
			
			title=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[1]/li[" + str(x) + "]/div/div/div[2]/a/div[2]')
			city=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[1]/li[" + str(x) + "]/div/div/div[2]/a/div[3]/span[1]/span')
			area_unit=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[1]/li[" + str(x) + "]/div/div/div[2]/a/div[3]/span[3]/span/span')
			#image=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[1]/li[" + str(x) + "]/div/div/div[1]/div/div/div/div/ul/li[1]/a/div/img')
			# a=browser.find_elements_by_xpath('')
			country="USA"
			# print(num1)
			e=expected_rent[num].text
			# print(num1)
			t=title[num].text
			c=city[num].text
			au=area_unit[num].text

			dict={"Area_Unit:":au,"City:":c,"Country:":country,"Expected_Price:":e,"Title:":t}
			print(dict)
			with open('/home/poulami/Project/data/AppearHere.json', 'a') as file:
				file.write(json.dumps(dict))
			num=num+1
			print(num)
		# num1=num1+1
		# print(num1)
	except:
		print traceback.format_exc()


	

	try:
		num=0
        # Output expected IndexErrors.
        # Logging.log_exception(error)
		for x in range(1, 25):
			
			expected_rent=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[2]/li[" + str(x) + "]/div/div/div[2]/a/div[1]/div/span[2]')
			
			title=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[2]/li[" + str(x) + "]/div/div/div[2]/a/div[2]')
			city=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[2]/li[" + str(x) + "]/div/div/div[2]/a/div[3]/span[1]/span')
			area_unit=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[2]/li[" + str(x) + "]/div/div/div[2]/a/div[3]/span[3]/span/span')
			image=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[2]/li[" + str(x) + "]/div/div/div[1]/div/div/div/div/ul/li[1]/a/div/img')
			
			# a="Nolita, Manhattan, New York, NY, USA"
			country="USA"
			e=expected_rent[num].text
			t=title[num].text
			c=city[num].text
			au=area_unit[num].text

			dict={"Area_Unit:":au,"City:":c,"Country:":country,"Expected_Price:":e,"Title:":t}
			print(dict)
			with open('/home/poulami/Project/data/AppearHere.json', 'a') as file:
				file.write(json.dumps(dict))
			num=num+1
			print(num)
		# num=num+1
		
		
		
		# for x in range(1, 7):
		# 	expected_rent[num]=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[1]/li[" + str(x) + "]/div/div/div[2]/a/div[1]/div/span[2]')
		# 	title[num]=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[1]/li[" + str(x) + "]/div/div/div[2]/a/div[2]')
		# 	city[num]=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[1]/li[" + str(x) + "]/div/div/div[2]/a/div[3]/span[1]/span')
		# 	area_unit[num]=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[1]/li[" + str(x) + "]/div/div/div[2]/a/div[3]/span[3]/span/span')
		# 	#image=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[1]/li[" + str(x) + "]/div/div/div[1]/div/div/div/div/ul/li[1]/a/div/img')
		# 	# a=browser.find_elements_by_xpath('')
		# 	country="USA"
		# 	e=expected_rent[num].text
		# 	t=title[num].text
		# 	c=city[num].text
		# 	au=area_unit[num].text
		# 	dict={"Area_Unit:":au,"City:":c,"Country:":country,"Expected_Price:":e,"Title:":t}
		# 	with open('/home/poulami/Project/data/AppearHere.json', 'a') as file:
		# 		file.write(json.dumps(dict))
		# 	num=num+1
	# try:
	# 	num1=0
	# 	for x in range(1, 7):
			
	# 		expected_rent=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[1]/li[" + str(x) + "]/div/div/div[2]/a/div[1]/div/span[2]')
			
	# 		title=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[1]/li[" + str(x) + "]/div/div/div[2]/a/div[2]')
	# 		city=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[1]/li[" + str(x) + "]/div/div/div[2]/a/div[3]/span[1]/span')
	# 		area_unit=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[1]/li[" + str(x) + "]/div/div/div[2]/a/div[3]/span[3]/span/span')
	# 		#image=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[1]/li[" + str(x) + "]/div/div/div[1]/div/div/div/div/ul/li[1]/a/div/img')
	# 		# a=browser.find_elements_by_xpath('')
	# 		country="USA"
	# 		# print(num1)
	# 		e=expected_rent[num1].text
	# 		# print(num1)
	# 		t=title[num1].text
	# 		c=city[num1].text
	# 		au=area_unit[num1].text

	# 		dict={"Area_Unit:":au,"City:":c,"Country:":country,"Expected_Price:":e,"Title:":t}
	# 		print(dict)
	# 		with open('/home/poulami/Project/data/AppearHere.json', 'a') as file:
	# 			file.write(json.dumps(dict))
	# 		num1=num1+1
	# 		print(num1)
	# 	# num1=num1+1
	# 	print(num1)
	# except:
	# 	print traceback.format_exc()


	

	# try:
	# 	num=0
 #        # Output expected IndexErrors.
 #        # Logging.log_exception(error)
	# 	for x in range(1, 25):
			
	# 		expected_rent=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[2]/li[" + str(x) + "]/div/div/div[2]/a/div[1]/div/span[2]')
			
	# 		title=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[2]/li[" + str(x) + "]/div/div/div[2]/a/div[2]')
	# 		city=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[2]/li[" + str(x) + "]/div/div/div[2]/a/div[3]/span[1]/span')
	# 		area_unit=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[2]/li[" + str(x) + "]/div/div/div[2]/a/div[3]/span[3]/span/span')
	# 		image=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[2]/li[" + str(x) + "]/div/div/div[1]/div/div/div/div/ul/li[1]/a/div/img')
			
	# 		# a="Nolita, Manhattan, New York, NY, USA"
	# 		country="USA"
	# 		e=expected_rent[num].text
	# 		t=title[num].text
	# 		c=city[num].text
	# 		au=area_unit[num].text

	# 		dict1={"Area_Unit:":au,"City:":c,"Country:":country,"Expected_Price:":e,"Title:":t}
	# 		print(dict1)
	# 		with open('/home/poulami/Project/data/AppearHere2.json', 'a') as file:
	# 			file.write(json.dumps(dict1))
	# 		num=num+1
	# 		print(num)
	# 	# num=num+1
	# 	print(num)
		# for x in range(1, 25):
		# 	expected_rent[num]=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[2]/li[" + str(x) + "]/div/div/div[2]/a/div[1]/div/span[2]')
		# 	title[num]=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[2]/li[" + str(x) + "]/div/div/div[2]/a/div[2]')
		# 	city[num]=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[2]/li[" + str(x) + "]/div/div/div[2]/a/div[3]/span[1]/span')
		# 	area_unit[num]=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[2]/li[" + str(x) + "]/div/div/div[2]/a/div[3]/span[3]/span/span')
		# 	image[num]=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[2]/li[" + str(x) + "]/div/div/div[1]/div/div/div/div/ul/li[1]/a/div/img')
			
		# 	# a="Nolita, Manhattan, New York, NY, USA"
		# 	country="USA"
		# 	e=expected_rent[num].text
		# 	t=title[num].text
		# 	c=city[num].text
		# 	au=area_unit[num].text
		# 	dict={"Area_Unit:":au,"City:":c,"Country:":country,"Expected_Price:":e,"Title:":t}
		# 	with open('/home/poulami/Project/data/AppearHere.json', 'a') as file:
		# 		file.write(json.dumps(dict))
		# 	num=num+1
	# except IndexError:
	# 	continue

    	
	
	except:
	 	print traceback.format_exc()
		
			
	# except IndexError as error:
	# 	logging.error('This is an error message')

	sleep(2)
	browser.quit()
	n=n+1
# x=browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[1]/li[1]/div/div/div[2]/a/div[1]/div/span[2]')
# print(x.text)
# n=0
# while(n!=2):
# 	sleep(2)
# 	btn=browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[2]/div[1]/span[2]/a/span[1]/svg")
# 	btn.click()
# 	sleep(5)
# 	n=n+1

# javaScript = "document.getElementsByClassName('Bloom__root_oj Bloom__fontSmallI_6');"

# browser.execute_script(javaScript[0].onclick())
# content = browser.find_element_by_css_selector('Bloom__root_oj Bloom__fontSmallI_6')
# content.click()

# browser.find_elements_by_xpath('')
# browser.find_element_by_class_name('Bloom__root_oj Bloom__fontSmallI_6').click()
# browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[2]/div[1]/ul/li[2]/a[2]').click()

# browser.find_element_by_class_name('SpaceListing__image___2Z0KX lazyloaded').click()
# userName = browser.find_element_by_class_name('Bloom__root_oj Bloom__fontSmallI_6').click()
# browser.execute_script("arguments[1].click();", userName)
# try:
#     element = WebDriverWait(browser, 10).until(
#         EC.presence_of_element_located((By.CssSelector, "span.Bloom__page_i2:nth-child(3) > a:nth-child(1)"))
#     )
# finally:
#     browser.quit()

