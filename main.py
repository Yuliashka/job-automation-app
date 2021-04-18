
# TO CREATE A FORM: https://docs.google.com/forms/
# MY_FORM = https://docs.google.com/forms/d/1KrIbgmLlXD5fCKADBrvCzM-djNGGF5wh9NQT1fQD0D8/edit

from selenium import webdriver
chrom_driver_path = "C:\Development\chromedriver.exe"
from selenium.webdriver.common.keys import Keys
import time

GOOGLE_ENTER = "https://www.google.com/"
GOOGLE_ACCOUNT = "your google account"
GOOGLE_PASSWORD = "password from you account"
FORM_LINK = "https://docs.google.com/forms/d/e/1FAIpQLSf2SYXpDQUGt8W_Ltj6bJPYHk6DDx3G1FFrACw3g2hgNYsR_w/viewform?usp=sf_link"
WEBSITE_LINK = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.33371235881715%2C%22east%22%3A-122.198786516532%2C%22south%22%3A37.815107779798836%2C%22north%22%3A37.89309730643784%7D%2C%22mapZoom%22%3A13%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"

driver = webdriver.Chrome(executable_path=chrom_driver_path)

# TO OPEN GOOGLE:
driver.get(GOOGLE_ENTER)
time.sleep(3)
accept_button = driver.find_element_by_xpath('//*[@id="zV9nZe"]')
time.sleep(3)
accept_button.click()
time.sleep(3)
enter_button = driver.find_element_by_xpath('//*[@id="gb"]/div/div[2]/a')
time.sleep(5)
enter_button.click()
time.sleep(3)
email_input = driver.find_element_by_xpath('//*[@id="identifierId"]')
time.sleep(3)
email_input.send_keys(GOOGLE_ACCOUNT)
time.sleep(3)
proceed_button = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]')
time.sleep(3)
proceed_button.click()
time.sleep(3)
password_input = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
time.sleep(3)
password_input.send_keys(GOOGLE_PASSWORD)
time.sleep(3)
proceed_button2 = driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]')
time.sleep(3)
proceed_button2.click()
time.sleep(5)


# TO MAKE OUR DRIVER TO OPEN RENT PAGE:
driver.get(WEBSITE_LINK)

# TO SCROLL DOWN THE RENT OFFERS INFO:
modal = driver.find_element_by_xpath('//*[@id="search-page-list-container"]')
time.sleep(3)
for i in range(2):
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
    time.sleep(2)

# GETTING <UL> WITH ALL <LI> WITH RENT INFO:
time.sleep(3)
list_with_links = driver.find_element_by_xpath('//*[@id="grid-search-results"]/ul')
time.sleep(5)

# IN <UL> FINDING ALL <A> AND GETTING THEIR "HREFS"
hrefs = []
all_links = list_with_links.find_elements_by_xpath("//div[contains(@class,'list-card-info')]//a[contains(@class,'list-card-link')]")
time.sleep(3)
for link in all_links:
    every_href = link.get_attribute("href")
    hrefs.append(every_href)

print(hrefs)
print(f"The length of links massive is: {len(hrefs)}")

# IN <UL> FINDING ALL <DIV> WITH PRICES AND GETTING THEIR PRICE VALUE:
prices = []
all_prices = list_with_links.find_elements_by_xpath("//div[contains(@class,'list-card-info')]//div[contains(@class,'list-card-heading')]//div[contains(@class,'list-card-price')]")
time.sleep(5)
for price in all_prices:
    every_price = price.text
    prices.append(every_price)

print(prices)
print(f"The length of prices massive is: {len(prices)}")


# IN <UL> FINDING ALL <DIV> WITH PRICES AND GETTING THEIR PRICE VALUE:
addresses = []
all_addresses = list_with_links.find_elements_by_xpath("//div[contains(@class,'list-card-info')]//address[contains(@class,'list-card-addr')]")
time.sleep(3)
for address in all_addresses:
    every_address = address.text
    addresses.append(every_address)

print(addresses)
print(f"The length of addresses massive is: {len(addresses)}")


time.sleep(2)
# TO MAKE OUR DRIVER TO OPEN FORM PAGE:
driver.get(FORM_LINK)
time.sleep(2)


# FILLING IN FORM:
x = range(0, 3)
for n in x:
    # TO GET ADDRESS INPUT:
    address_input = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    time.sleep(2)
    address_input.send_keys(addresses[n])
    time.sleep(2)

    # TO GET PRICE INPUT:
    price_input = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    time.sleep(2)
    price_input.send_keys(prices[n])
    time.sleep(2)

    # TO GET LINK INPUT:
    link_input = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    time.sleep(2)
    link_input.send_keys(hrefs[n])
    time.sleep(2)

    # PRESS THE BUTTON "SEND FORM":
    send_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
    time.sleep(2)
    send_button.click()
    time.sleep(2)

    # SEND ONE MORE ANSWER:
    send_answer_link = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    time.sleep(2)
    send_answer_link.click()
    time.sleep(2)

# CHANGE FORM:
change_button = driver.find_element_by_xpath('/html/body/div/div[1]/div')
time.sleep(2)
change_button.click()
time.sleep(2)

# SEE ANSWERS:
answers = driver.find_element_by_xpath('//*[@id="tJHJj"]/div[3]/div[1]/div/div[2]/span/div')
time.sleep(2)
answers.click()
time.sleep(2)

# CREATE A TABLE:
create_button = driver.find_element_by_xpath('//*[@id="ResponsesView"]/div/div[1]/div[1]/div[2]/div[1]/div/div/span/span/div')
time.sleep(2)
create_button.click()
time.sleep(2)




