#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  22 19:11:51 2022

@author: margaritanazarian
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="/Users/margaritanazarian/opt/anaconda3/chromedriver")


# URLs

url_dishwasher = "https://www.but.fr/electromenager/lavage/tous-les-lave-vaisselle/index-c11201.html"
url_oven = "https://www.but.fr/electromenager/cuisson/four/index-c11167.html"
url_fridge = "https://www.but.fr/electromenager/froid/tous-les-refrigerateurs/index-c11184.html"
url_microwave = "https://www.but.fr/electromenager/cuisson/micro-ondes/index-c11168.html"
url_hob = "https://www.but.fr/electromenager/cuisson/plaque-de-cuisson/index-c11171.html"

# html code

class_name = "prix"

# DISHWASHER

url = url_dishwasher
driver.get(url)
for n in range(0,100):
    driver.find_element_by_tag_name("body").send_keys(Keys.PAGE_DOWN)
    
pages = driver.find_element_by_class_name("produits-page-definir").text
pages = pages.split("/")
last_page = int(pages[-1])

prices = []

for page in range(1,last_page+1): 
    driver.get(url+"?PageIndex="+str(page))
    doc = BeautifulSoup(driver.page_source, "html.parser")
    
    end = len(doc.find_all(class_=class_name))
    p = [doc.find_all(class_=class_name)[n].text for n in range(0,end)]
    prices.extend(p)
    print(p)

prices_only =[]

for element in prices: 
    price = element[:-2]
    prices_only.append(price)
    print(price)

final_prices = [item.replace(",", ".") for item in prices_only]

table_dishwasher = pd.DataFrame({"Price": final_prices})

table_dishwasher["Price"] = table_dishwasher['Price'].astype('float')

table_dishwasher = table_dishwasher.assign(Category = "Dishwasher")


# OVEN

url = url_oven
driver.get(url)
for n in range(0,100):
    driver.find_element_by_tag_name("body").send_keys(Keys.PAGE_DOWN)
    
pages = driver.find_element_by_class_name("produits-page-definir").text
pages = pages.split("/")
last_page = int(pages[-1])

prices = []

for page in range(1,last_page+1): 
    driver.get(url+"?PageIndex="+str(page))
    doc = BeautifulSoup(driver.page_source, "html.parser")
    
    end = len(doc.find_all(class_=class_name))
    p = [doc.find_all(class_=class_name)[n].text for n in range(0,end)]
    prices.extend(p)
    print(p)

prices_only =[]

for element in prices: 
    price = element[:-2]
    prices_only.append(price)
    print(price)

final_prices = [item.replace(",", ".") for item in prices_only]

table_oven = pd.DataFrame({"Price": final_prices})

table_oven["Price"] = table_oven['Price'].astype('float')

table_oven = table_oven.assign(Category = "Oven")


# FRIDGE

url = url_fridge
driver.get(url)
for n in range(0,100):
    driver.find_element_by_tag_name("body").send_keys(Keys.PAGE_DOWN)
    
pages = driver.find_element_by_class_name("produits-page-definir").text
pages = pages.split("/")
last_page = int(pages[-1])

prices = []

for page in range(1,last_page+1): 
    driver.get(url+"?PageIndex="+str(page))
    doc = BeautifulSoup(driver.page_source, "html.parser")
    
    end = len(doc.find_all(class_=class_name))
    p = [doc.find_all(class_=class_name)[n].text for n in range(0,end)]
    prices.extend(p)
    print(p)

prices_only =[]

for element in prices: 
    price = element[:-2]
    prices_only.append(price)
    print(price)

final_prices = [item.replace(",", ".") for item in prices_only]

table_fridge = pd.DataFrame({"Price": final_prices})

table_fridge["Price"] = table_fridge['Price'].astype('float')

table_fridge = table_fridge.assign(Category = "Fridge")

# MICROWAVE

url = url_microwave
driver.get(url)
for n in range(0,100):
    driver.find_element_by_tag_name("body").send_keys(Keys.PAGE_DOWN)
    
pages = driver.find_element_by_class_name("produits-page-definir").text
pages = pages.split("/")
last_page = int(pages[-1])

prices = []

for page in range(1,last_page+1): 
    driver.get(url+"?PageIndex="+str(page))
    doc = BeautifulSoup(driver.page_source, "html.parser")
    
    end = len(doc.find_all(class_=class_name))
    p = [doc.find_all(class_=class_name)[n].text for n in range(0,end)]
    prices.extend(p)
    print(p)

prices_only =[]

for element in prices: 
    price = element[:-2]
    prices_only.append(price)
    print(price)

final_prices = [item.replace(",", ".") for item in prices_only]

table_microwave = pd.DataFrame({"Price": final_prices})

table_microwave["Price"] = table_microwave['Price'].astype('float')

table_microwave = table_microwave.assign(Category = "Microwave")

# HOB

url = url_hob
driver.get(url)
for n in range(0,100):
    driver.find_element_by_tag_name("body").send_keys(Keys.PAGE_DOWN)
    
pages = driver.find_element_by_class_name("produits-page-definir").text
pages = pages.split("/")
last_page = int(pages[-1])

prices = []

for page in range(1,last_page+1): 
    driver.get(url+"?PageIndex="+str(page))
    doc = BeautifulSoup(driver.page_source, "html.parser")
    
    end = len(doc.find_all(class_=class_name))
    p = [doc.find_all(class_=class_name)[n].text for n in range(0,end)]
    prices.extend(p)
    print(p)

prices_only =[]

for element in prices: 
    price = element[:-2]
    prices_only.append(price)
    print(price)

final_prices = [item.replace(",", ".") for item in prices_only]

table_hob = pd.DataFrame({"Price": final_prices})

table_hob["Price"] = table_hob['Price'].astype('float')

table_hob = table_hob.assign(Category = "Hob")


# APPEND TABLES

table = table_dishwasher.append([table_oven, table_fridge, table_microwave, table_hob])
table.to_csv("table.csv")




