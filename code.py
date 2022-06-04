''' (BeautifulSoup) is a python
module, which is famously used for
parsing text as HTML and then
performing actions in it, such as
finding specific HTML tags with a
particular class/id, or listing out all the
li tags inside the ul tags.'''

'''Selenium, on the other hand, is used
to interact with the webpage. It is
famously used for automation testing,
such as testing the functionality of a
website (Login/Logout/etc.) but can
be also used to interact with the page
such as clicking a button, etc.'''

from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

browser = webdriver.Chrome(r'C:\Users\hp\OneDrive\Desktop\python\C-127\chromedriver.exe')
browser.get(START_URL)
time.sleep(10)

def scrape():
    headers = ["Proper name","Distance","Mass","Radius"]
    planet_data = []
   

    for i in range(0,10):
        soup = BeautifulSoup(browser.page_source,"html.parser")
        for ul_tag in soup.find_all("ul", attrs = {"class","stars"}):
            temp_list = []
            li_tags = ul_tag.find_all("li")
            for index,li_tag in enumerate(li_tags):
                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:

                        temp_list.append(li_tag.contents[0])

                    except:
                        temp_list.append("")
            
            planet_data.append(temp_list)
        browser.find_element_by_xpath('//*[@id="mw-content-text"]/div[1]/table/tbody/tr[1]/td[2]/a').click()

    with open("scrapper.csv" , "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerow(planet_data)



scrape()






