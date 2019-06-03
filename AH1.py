from selenium import webdriver
import json
import pandas as pd

browser = webdriver.Firefox(executable_path = '/home/poulami/Downloads/geckodriver')
browser.get('https://www.appearhere.us/spaces/search?q=Nolita%2C%20Manhattan%2C%20New%20York%2C%20NY%2C%20USA&place_id=ChIJd9PLRY9ZwokRk9g2ewaGdEI&search_id=4abcf8adj91&page=1&type=space&search_source=search%20results')
num=0
for x in range(1, 7):
	expected_rent=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div[2]/ul[1]/li[" + str(x) + "]/div/div/div[2]/a/div[1]/div/span[2]')
	title=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div[2]/ul[1]/li[" + str(x) + "]/div/div/div[2]/a/div[2]')
	city=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div[2]/ul[1]/li[" + str(x) + "]/div/div/div[2]/a/div[3]/span[1]/span')
	area_unit=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div[2]/ul[1]/li[" + str(x) + "]/div/div/div[2]/a/div[3]/span[3]/span/span')
	a="Nolita, Manhattan, New York, NY, USA"
	e=expected_rent[num].text
	t=title[num].text
	c=city[num].text
	au=area_unit[num].text
	dict={"Area:":a,"Expected_Price:":e,"Title:":t,"State:":c,"Area_Unit:":au}
	with open('/home/poulami/Project/data/AppearHere.json', 'a') as file:
		file.write(json.dumps(dict))
	num=num+1
for x in range(1, 18):
	expected_rent=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div[2]/ul[2]/li[" + str(x) + "]/div/div/div[2]/a/div[1]/div/span[2]')
	title=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div[2]/ul[2]/li[" + str(x) + "]/div/div/div[2]/a/div[2]')
	city=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div[2]/ul[2]/li[" + str(x) + "]/div/div/div[2]/a/div[3]/span[1]/span')
	area_unit=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div[2]/ul[2]/li[" + str(x) + "]/div/div/div[2]/a/div[3]/span[3]/span/span')
	a="Nolita, Manhattan, New York, NY, USA"
	e=expected_rent[num].text
	t=title[num].text
	c=city[num].text
	au=area_unit[num].text
	dict={"Area:":a,"Expected_Price:":e,"Title:":t,"State:":c,"Area_Unit:":au}
	with open('/home/poulami/Project/data/AppearHere.json', 'a') as file:
		file.write(json.dumps(dict))
	num=num+1
