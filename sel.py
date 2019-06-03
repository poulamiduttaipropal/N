from selenium import webdriver
import json

browser = webdriver.Firefox(executable_path = '/home/poulami/Downloads/geckodriver')
# browser.get('https://www.appearhere.us/spaces/search?q=Nolita%2C%20Manhattan%2C%20New%20York%2C%20NY%2C%20USA&place_id=ChIJd9PLRY9ZwokRk9g2ewaGdEI&search_id=nr23j15ky7c&page=1&type=space&search_source=search%20results')


class Spider:
	browser.get('https://www.appearhere.us/spaces/search?q=Nolita%2C%20Manhattan%2C%20New%20York%2C%20NY%2C%20USA&place_id=ChIJd9PLRY9ZwokRk9g2ewaGdEI&search_id=nr23j15ky7c&page=1&type=space&search_source=search%20results')
	num=0
	for x in range(1, 7):
		#area=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[1]/div/div[1]/div/div/div/button/div/text()[1]')
		expected_rent=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div[2]/ul[1]/li[" + str(x) + "]/div/div/div[2]/a/div[1]/div/span[2]')
		# /html/body/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div[2]/ul[2]/li[1]/div/div/div[2]/a/div[1]/div/span[2]
		# /html/body/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div[2]/ul[2]/li[17]/div/div/div[2]/a/div[1]/div/span[2]
		title=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div[2]/ul[1]/li[" + str(x) + "]/div/div/div[2]/a/div[2]')
		city=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div[2]/ul[1]/li[" + str(x) + "]/div/div/div[2]/a/div[3]/span[1]/span')
		area_unit=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div[2]/ul[1]/li[" + str(x) + "]/div/div/div[2]/a/div[3]/span[3]/span/span')
		# print("Area:" + area[num].text)
		# print("Expected_Price:" + expected_rent[num].text + "/day")
		# print("Title:" + title[num].text)
		# print("State:" + city[num].text)
		# print("Area_Unit:" + area_unit[num].text)
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
		# area=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[1]/div/div[1]/div/div/div/button/div/text()[1]')
		expected_rent=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div[2]/ul[2]/li[" + str(x) + "]/div/div/div[2]/a/div[1]/div/span[2]')
		# /html/body/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div[2]/ul[2]/li[1]/div/div/div[2]/a/div[1]/div/span[2]
		# /html/body/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div[2]/ul[2]/li[17]/div/div/div[2]/a/div[1]/div/span[2]
		title=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div[2]/ul[2]/li[" + str(x) + "]/div/div/div[2]/a/div[2]')
		city=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div[2]/ul[2]/li[" + str(x) + "]/div/div/div[2]/a/div[3]/span[1]/span')
		area_unit=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div[2]/ul[2]/li[" + str(x) + "]/div/div/div[2]/a/div[3]/span[3]/span/span')
		# print("Area:" + area[num].text)
		# print("Expected_Price:" + expected_rent[num].text +"/day")
		# print("Title:" + title[num].text)
		# print("State:" + city[num].text)
		# print("Area_Unit:" + area_unit[num].text)
		a="Nolita, Manhattan, New York, NY, USA"
		e=expected_rent[num].text
		t=title[num].text
		c=city[num].text
		au=area_unit[num].text
		dict={"Area:":a,"Expected_Price:":e,"Title:":t,"State:":c,"Area_Unit:":au}
		with open('/home/poulami/Project/data/AppearHere.json', 'a') as file:
			file.write(json.dumps(dict))
		num=num+1

	# browser.get('https://www.appearhere.us/spaces/search?q=SoHo%2C%20Manhattan%2C%20New%20York%2C%20NY%2C%20USA&place_id=ChIJ8-JRXoxZwokRGPiQ9Ek0L84&search_id=saow7ydjgv&page=1&type=space&search_source=search%20results')
	# for x in range(1, 7):
	# 	#area=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[1]/div/div[1]/div/div/div/button/div/text()[1]')
	# 	expected_rent=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[2]/div[1]/div[2]/ul[1]/li[" + str(x) + "]/div/div/div[2]/a/div[1]/div/span[2]')
	# 	# /html/body/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div[2]/ul[2]/li[1]/div/div/div[2]/a/div[1]/div/span[2]
	# 	# /html/body/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div[2]/ul[2]/li[17]/div/div/div[2]/a/div[1]/div/span[2]
	# 	title=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[2]/div[1]/div[2]/ul[1]/li[" + str(x) + "]/div/div/div[2]/a/div[2]')
	# 	city=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[2]/div[1]/div[2]/ul[1]/li[" + str(x) + "]/div/div/div[2]/a/div[3]/span[1]/span')
	# 	area_unit=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[2]/div[1]/div[2]/ul[1]/li[" + str(x) + "]/div/div/div[2]/a/div[3]/span[3]/span/span/text()[1]')
	# 	# print("Area:" + area[num].text)
	# 	# print("Expected_Price:" + expected_rent[num].text + "/day")
	# 	# print("Title:" + title[num].text)
	# 	# print("State:" + city[num].text)
	# 	# print("Area_Unit:" + area_unit[num].text)
	# 	a="SoHo, Manhattan, New York, NY, USA"
	# 	e=expected_rent[num].text
	# 	t=title[num].text
	# 	c=city[num].text
	# 	au=area_unit[num].text

	# 	dict={"Area:":a,"Expected_Price:":e,"Title:":t,"State:":c,"Area_Unit:":au}
	# 	with open('/home/poulami/Project/data/AppearHere.json', 'a') as file:
	# 		file.write(json.dumps(dict))
	# 	num=num+1
	# for x in range(1, 25):
	# 	# area=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[1]/div/div[1]/div/div/div/button/div/text()[1]')
	# 	expected_rent=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div[2]/ul[2]/li[" + str(x) + "]/div/div/div[2]/a/div[1]/div/span[2]')
	# 	# /html/body/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div[2]/ul[2]/li[1]/div/div/div[2]/a/div[1]/div/span[2]
	# 	# /html/body/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div[2]/ul[2]/li[17]/div/div/div[2]/a/div[1]/div/span[2]
	# 	title=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div[2]/ul[2]/li[" + str(x) + "]/div/div/div[2]/a/div[2]')
	# 	city=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div[2]/ul[2]/li[" + str(x) + "]/div/div/div[2]/a/div[3]/span[1]/span')
	# 	area_unit=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div[2]/ul[2]/li[" + str(x) + "]/div/div/div[2]/a/div[3]/span[3]/span/span')
	# 	# print("Area:" + area[num].text)
	# 	# print("Expected_Price:" + expected_rent[num].text +"/day")
	# 	# print("Title:" + title[num].text)
	# 	# print("State:" + city[num].text)
	# 	# print("Area_Unit:" + area_unit[num].text)
	# 	a="SoHo, Manhattan, New York, NY, USA"
	# 	e=expected_rent[num].text
	# 	t=title[num].text
	# 	c=city[num].text
	# 	au=area_unit[num].text
	# 	dict={"Area:":a,"Expected_Price:":e,"Title:":t,"State:":c,"Area_Unit:":au}
	# 	with open('/home/poulami/Project/data/AppearHere.json', 'a') as file:
	# 		file.write(json.dumps(dict))
	# 	num=num+1

#                                 

	# for x in range(1, 18):
		# expected_rent=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div[2]/ul[1]/li[1]/div/div/div[2]/a/div[1]/div/span[2]')
		# print(expected_rent[x].text)
		# area=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[1]/div/div[1]/div/div/div/button/div/text()[1]')
		# print(area[x].text)





# with open('/home/poulami/Project/data/data1.json', 'a') as file:
#                                 file.write(json.dumps(list))
	

# x=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[1]/li[1]/div/div/div[2]/a/div[1]/div/span[2]')
# # /html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[1]/li[2]/div/div/div[2]/a/div[1]/div/span[2]
# # /html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[3]/li[24]/div/div/div[2]/a/div[1]/div/span[2]
# # /html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[3]/li[24]/div/div/div[2]/a/div[1]/div/span[2]
# /html/body/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div[2]/ul[2]/li[17]/div/div/div[2]/a/div[1]/div/span[2]


# for i in range(num):
# 	print(x[i].text)
# 	print("hello")
	
	
# browser.find_element_by_id("next_achive_button").click()
