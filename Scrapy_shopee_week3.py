#!/usr/bin/env python
# coding: utf-8

# ### Install library

# In[ ]:


get_ipython().system('pip install selenium')
get_ipython().system('pip install pandas')


# ### Import function ที่จำเป็น

# In[ ]:


import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import bs4
import time
import re


# ### สร้าง Web driver ของ Firefox

# In[ ]:


options = Options()
options.binary_location = r'/Applications/Firefox.app/Contents/MacOS/firefox-bin'
driver = webdriver.Firefox(executable_path=r'/Users/kanlayajhanpum/Desktop/DSI310/1', options=options)
driver.get('https://shopee.co.th/')


# ### เรียกใช้ Selenium

# In[ ]:


#เลือกภาษาไทยเป็น function ของเว็บไซต์ 
thai_button = driver.find_element("xpath",'/html/body/div[2]/div[1]/div[1]/div/div[3]/div[1]/button').click()
time.sleep(6)


# In[ ]:


#ปิดโฆษณาของตัวเว็บไซต์ 
close_adver = driver.execute_script('return document.querySelector("shopee-banner-popup-stateful").shadowRoot.querySelector("div.shopee-popup__close-btn")')
close_adver.click()


# In[ ]:


#Search ใน Search bar ของ Shopee
search = driver.find_element("xpath",'/html/body/div[1]/div/header/div[2]/div/div[1]/div[1]/div/form/input')
search.send_keys('ขมิ้นชัน')


# In[ ]:


#กด Enter
search.send_keys(Keys.ENTER)


# In[ ]:


#Zoom out เพื่อให้ load ทั่วหน้าจอ
driver.execute_script("document.body.style.MozTransform='scale(0.1)';")
driver.execute_script('document.body.style.MozTransformOrigin = "0 0";')


# ### Scraping Process

# In[ ]:


data = driver.page_source #ดึงข้อมูลจากหน้าเว็บ
soup = bs4.BeautifulSoup(data) #จัดในรูปแบบ BeautifulSoup


# In[ ]:


#ดึงข้อมูล
soup.select(".row>div") #css selector


# In[ ]:


#ดึงข้อมูลชื่อ
e.select_one("div.col-xs-2-4 > a:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)").text.strip()


# In[ ]:


#ดึงราคาเต็มของสินค้า
e.select_one("div.col-xs-2-4> a> div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1)").text.strip()


# In[ ]:


#ตัดและเลือกเลขด้านหน้า Range
try:
    start_price = float(p)
except:
    price = p.rpartition('-')[0]
    start_price = float(price)

start_price


# In[ ]:


#รวมราคาสินค้า
try:
    p = e.select_one("div.col-xs-2-4 > a > div > div > div:nth-child(2) > div:nth-child(2)> div:nth-child(2)").text.strip()
except:
    p = e.select_one("div.col-xs-2-4 > a:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1)").text.strip()
p = p.replace(",", "").replace("฿", "").replace(" ", "")
try:
    start_price = float(p)
except:
    price = p.rpartition('-')[0]
    start_price = float(price)

start_price


# In[ ]:


#ดึงยอดขายของสินค้า
sales = e.select_one("div.col-xs-2-4:nth-child(1) > a:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(2)").text.strip().replace("พัน","000").replace("ล้าน","000000")
try:
    sales = float(re.sub('\D','',sales))
except:
    sales = 0
sales


# In[ ]:


#ดึงจังหวัดของเจ้าของร้านที่ขาย
e.select_one("div.col-xs-2-4 > a:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4)").text.strip()


# ### นำขั้นตอนที่ดึงข้อมูลต่างๆมา Loop เพื่อให้เป็นระเบียบ

# In[ ]:


records=[]
for i in range(1):
    data = driver.page_source
    soup = bs4.BeautifulSoup(data)
    el=soup.select(".row>div")
    for e in el:
        name = e.select_one("div.col-xs-2-4 > a:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)").text.strip()
        try:
            p = e.select_one("div.col-xs-2-4 > a > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2)").text.strip()
            if p == '':
                print(1/0)
        except:
            p = e.select_one("div.col-xs-2-4 > a:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1)").text.strip()
        p = p.replace(",", "").replace("฿", "").replace(" ", "")
        try:
            start_price = float(p)
        except:
            price = p.rpartition('-')[0]
            start_price = float(price)

        sales = e.select_one("div.col-xs-2-4 > a:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3)").text.strip().replace("พัน","000").replace("ล้าน","000000")
        try:
            sales = float(re.sub('\D','',sales))
        except:
            sales = 0
        province = e.select_one("div.col-xs-2-4 > a:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4)").text.strip()
        #print(name, p)
        records.append([name, start_price,sales,province])


# In[ ]:


#แสดงจำนวนสินค้าในแต่ละหน้า
len(records)


# In[ ]:


#ใช้ Selenium ในการกดปุ่มเพื่อไปหน้าถัดไป
next_button = driver.find_element("xpath",'/html/body/div[1]/div/div[2]/div/div/div[2]/div[2]/div[3]/div/button[8]')
next_button.click()


# ### นำขั้นตอนการเก็บข้อมูลทั้งหมดมาเข้า Loop เพื่อทำการ Scrap สินค้าทั้งหมดในทุกหน้าที่ต้องการ

# In[ ]:


# การ Scrape ข้อมูลจากหลายหน้าของ Web Shopee
records=[]
for i in range(5):
    data = driver.page_source
    soup = bs4.BeautifulSoup(data)
    el=soup.select(".row>div")
    for e in el:
        name = e.select_one("div.col-xs-2-4 > a:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)").text.strip()
        try:
            p = e.select_one("div.col-xs-2-4 > a > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2)").text.strip()
            if p == '':
                print(1/0)
        except:
            p = e.select_one("div.col-xs-2-4 > a:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1)").text.strip()
        p = p.replace(",", "").replace("฿", "").replace(" ", "")
        try:
            start_price = float(p)
        except:
            price = p.rpartition('-')[0]
            start_price = float(price)
            
        sales = e.select_one("div.col-xs-2-4 > a:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(2)").text.strip().replace("พัน","000").replace("ล้าน","000000")
        try:
            sales = float(re.sub('\D','',sales))
        except:
            sales = 0

        #sales = e.select_one("div.col-xs-2-4 > a > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(3)").text.strip().replace("พัน","000").replace("ล้าน","000000")
        #try:
            #sales = float(re.sub('\D','',sales))
        #except:
            #sales = 0
        province = e.select_one("div.col-xs-2-4 > a:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4)").text.strip()
        #print(name, p)
        records.append([name, start_price,sales,province])


    time.sleep(5)
    next_button = driver.find_element("xpath",'/html/body/div[1]/div/div[2]/div/div/div[2]/div[2]/div[3]/div/button[8]')
    next_button.click()
    time.sleep(5)


# In[ ]:


len(records)


# ### นำข้อมูลที่ได้ใส่ลงใน DataFrame

# In[ ]:


#ทำเป็น DataFrame
df = pd.DataFrame(records, columns=['itemname','price','amount','province']) # ใส้ชื่อ Columns ทั้งหมด
df


# ### แปลงเป็นไฟล์ Excel 

# In[ ]:


df.to_csv('Shopee_Turmeric.csv', encoding='utf-8')

