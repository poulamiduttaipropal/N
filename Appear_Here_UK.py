from selenium import webdriver
from time import sleep
import json
import traceback
from selenium.webdriver.firefox.options import Options


options = Options()
options.headless = True
profile = webdriver.FirefoxProfile()
profile.set_preference('permissions.default.stylesheet', 2)
profile.set_preference('permissions.default.image', False)
profile.set_preference("javascript.enabled", True)

n=25
while(n!=35):
    
    sleep(2)
    browser = webdriver.Firefox(options=options, executable_path = '/home/poulami/Downloads/geckodriver')
    url='https://www.appearhere.co.uk/spaces/search?search_campaign=available-now&search_medium=button&search_source=available-now&search_id=xlfou7x1dh&page=' + str(n) + '&type=space'
    
    browser.get(url)
    num=0
    for x in range(1, 7):
        try:
            expected_rent=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[1]/li[" + str(x) + "]/div/div/div[2]/a/div[1]/div/span[2]')
            title=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[1]/li[" + str(x) + "]/div/div/div[2]/a/div[2]')
            city=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[1]/li[" + str(x) + "]/div/div/div[2]/a/div[3]/span[1]/span')
            area_unit=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[1]/li[" + str(x) + "]/div/div/div[2]/a/div[3]/span[3]/span/span')
            image=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[1]/li[" + str(x) + "]/div/div/div[1]/div/div/div/div/ul/li[1]/a/div/img')
            i=image[num].get_attribute("data-src")
            country="UK"
            e=expected_rent[num].text + str('/day')
            # title[num].text=title[num].text.replace('\u2019','')
            # title[num].text=title[num].text.replace('\u2018','')
            # title[num].text=title[num].text.replace('\u2013','')
            # title[num].text=title[num].text.replace('\u2012','')

            t=title[num].text
            c=city[num].text
            au=area_unit[num].text
            link=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[1]/li[" + str(x) + "]/div/div/div[1]/div/div/div/div/ul/li[1]/a')
            l=link[num].get_attribute("href")
            print(l)
            browser1 = webdriver.Firefox(options=options, executable_path = '/home/poulami/Downloads/geckodriver')
            browser1.get(l)
            area=browser1.find_elements_by_xpath('/html/body/div[2]/div/div[3]/div/div[2]/div[1]/div[1]/span')
            
            description=browser1.find_elements_by_xpath('/html/body/div[2]/div/div[3]/div/div[2]/div[1]/div[2]/div/p')
            # description[0].text=description[0].text.replace('\u2019','')
            # description[0].text=description[0].text.replace('\u2018','')
            # description[0].text=description[0].text.replace('\u2013','')
            # description[0].text=description[0].text.replace('\u2012','')
            ae=area[0].text
            d=description[0].text
            browser1.quit()
            dict={"area":ae,"area_unit":au,"city":c,"country":country,"description":d,"expected_rent":e,"property_image":i,"title":t}
            print(dict)
            with open('/home/poulami/Project/data/AppearHere6.json', 'a') as file:
                file.write(json.dumps(dict))
            num=num+1
            
            print(num)
        except:
            print traceback.format_exc()
    num=0
    for x in range(1, 25):
        try:
            
            expected_rent=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[3]/li[" + str(x) + "]/div/div/div[2]/a/div[1]/div/span[2]')
            title=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[3]/li[" + str(x) + "]/div/div/div[2]/a/div[2]')
            city=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[3]/li[" + str(x) + "]/div/div/div[2]/a/div[3]/span[1]/span')
            area_unit=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[3]/li[" + str(x) + "]/div/div/div[2]/a/div[3]/span[3]/span/span')
            image=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[3]/li[" + str(x) + "]/div/div/div[1]/div/div/div/div/ul/li[1]/a/div/img')
            i=image[num].get_attribute("data-src")
            country="UK"
            e=expected_rent[num].text + str('/day')
            # title[num].text=title[num].text.replace('\u2019','')
            # title[num].text=title[num].text.replace('\u2018','')
            # title[num].text=title[num].text.replace('\u2013','')
            # title[num].text=title[num].text.replace('\u2012','')
            t=title[num].text
            c=city[num].text
            au=area_unit[num].text
            link=browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/ul[3]/li[" + str(x) + "]/div/div/div[1]/div/div/div/div/ul/li[1]/a')
            l=link[num].get_attribute("href")
            print(l)
            browser1 = webdriver.Firefox(options=options, executable_path = '/home/poulami/Downloads/geckodriver')
            browser1.get(l)
            area=browser1.find_elements_by_xpath('/html/body/div[2]/div/div[3]/div/div[2]/div[1]/div[1]/span')
            description=browser1.find_elements_by_xpath('/html/body/div[2]/div/div[3]/div/div[2]/div[1]/div[2]/div/p')
            # description[0].text=description[0].text.replace('\u2019','')
            # description[0].text=description[0].text.replace('\u2018','')
            # description[0].text=description[0].text.replace('\u2013','')
            # description[0].text=description[0].text.replace('\u2012','')
            ae=area[0].text
            d=description[0].text
            browser1.quit()
            dict={"area":ae,"area_unit":au,"city":c,"country":country,"description":d,"expected_rent":e,"property_image":i,"title":t}
            print(dict)
            with open('/home/poulami/Project/data/AppearHere6.json', 'a') as file:
                file.write(json.dumps(dict))
            num=num+1
            print(num)
        except:
            print traceback.format_exc()
    sleep(2)
    browser.quit()
    n=n+1