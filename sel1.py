# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome()
# driver.get("https://www.gmail.com")

# # To open a link in a new tab
# actions = ActionChains(driver)
# # find = driver.find_element_by_link_text('ABC')
# actions.key_down(Keys.CONTROL).click(find).key_up(Keys.CONTROL).perform()

# driver.switch_to.window(driver.window_handles[-1])
# driver.get("https://stackoverflow.com")

from selenium import webdriver
# import json
# import pandas as pd

browser = webdriver.Firefox(executable_path = '/home/poulami/Downloads/geckodriver')
browser.get('https://www.appearhere.us/spaces/search?q=Nolita%2C%20Manhattan%2C%20New%20York%2C%20NY%2C%20USA&place_id=ChIJd9PLRY9ZwokRk9g2ewaGdEI&search_id=4abcf8adj91&page=1&type=space&search_source=search%20results')
browser.quit()
browser = webdriver.Firefox(executable_path = '/home/poulami/Downloads/geckodriver')
browser.get('https://www.appearhere.us/spaces/search?destination_id=5a49fabe-af5f-4f7a-9a36-1c359e9ec9aa&place_id=ChIJ8-JRXoxZwokRGPiQ9Ek0L84&q=SoHo&search_campaign=destination-page&search_medium=link&search_source=destinations&search_id=gtsl004pvmg&page=1&type=space')
