import requests
from bs4 import BeautifulSoup
from numpy.core.defchararray import title
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import pandas as pd
import os
from csv import writer

url = "https://www.udemy.com/course/machinelearning/"

driver = webdriver.Chrome('/Users/carlosrueda/My Stuff/UBC/COSC 419C/project/chromedriver')
driver.implicitly_wait(30)
driver.get(url)

soup1 = BeautifulSoup(driver.page_source, 'lxml')
post = soup1.find(class_='clp-lead')
# grabs the title of the course
title = post.find(class_='clp-lead__title').get_text().replace('\n', '')
ratings = post.find(class_='tooltip-container')

print(ratings)

