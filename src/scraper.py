from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument("--incognito")

driver = webdriver.Chrome(options=options)  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/')

search_bar = driver.find_element_by_name("q")
search_bar.clear()
search_bar.send_keys("diego florez-estrada linkedin")
search_bar.send_keys(Keys.RETURN)

driver.current_url
#ricardo molina spain Information Technology & Services Internet Computer Software linkedin
users = driver.find_elements_by_partial_link_text("Diego")

for u in users:
    print(u.get_attribute('href'))
