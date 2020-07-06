import requests
from bs4 import BeautifulSoup
import urllib.request
import json
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options

chrome_options = Options() # 啟動無頭模式
chrome_options.add_argument('--headless')  #規避google bug
chrome_options.add_argument('--disable-gpu')
browser = webdriver.Chrome('C:\chromedriver.exe',options = chrome_options)
url = 'https://www.foodpanda.com.tw/restaurants/lat/24.178824/lng/120.6466926/city/%E8%A5%BF%E5%B1%AF%E5%8D%80/address/%25E9%2580%25A2%25E7%2594%25B2%25E5%25A4%25A7%25E5%25AD%25B8%252C%2520407%25E5%258F%25B0%25E7%2581%25A3%25E5%258F%25B0%25E4%25B8%25AD%25E5%25B8%2582%25E8%25A5%25BF%25E5%25B1%25AF%25E5%258D%2580%25E6%2596%2587%25E8%258F%25AF%25E8%25B7%25AF100%25E8%2599%259F/%25E6%2596%2587%25E8%258F%25AF%25E8%25B7%25AF/100%25E8%2599%259F%2520%25E9%2580%25A2%25E7%2594%25B2%25E5%25A4%25A7%25E5%25AD%25B8?postcode=407&verticalTab=restaurants'
browser.get(url)
sleep(3)
search_food = input()
# search_food = "義大利麵"
search_tag_name = "restaurants-search"
browser.find_element_by_class_name(search_tag_name).click()

search_type_tag = "restaurants-search-input"
print(browser.find_element_by_class_name(search_type_tag).text)
browser.find_element_by_class_name(search_type_tag).send_keys(search_food)
sleep(2)
for i in range(1,50):
    Y = i*50
    browser.execute_script("window.scrollTo(0,"+str(Y)+")")
    sleep(0.5)

html_source = browser.page_source
# print(html_source)
soup = BeautifulSoup(html_source,'html.parser')
print(soup)
img_tag_name = "div.vendor-picture"
shop_tag_name = "figcaption.vendor-info"
diliver_time_tag ="span.badge-info"
img = soup.select(img_tag_name)
tar = soup.select(shop_tag_name)
time = soup.select(diliver_time_tag)
# print(tar[0].text)
# print(str(img[0]).split("(\"")[1].split("\")")[0])
# print(time[0].text)
lis = []

for i in range(0,15):
#     print("shop-info:",tar[i].text)
    print("img:",str(img[i]).split("(\"")[1].split("\")")[0])
#     print("time:",time[i].text)
    dic= {
        'shop-info':tar[i].text,
        'img':str(img[i]).split("(\"")[1].split("\")")[0],
        'time':time[i].text
        }
    lis.append(dic)
print(lis)