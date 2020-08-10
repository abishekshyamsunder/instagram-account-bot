import pdb
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import os
import pyautogui


print(pyautogui.size())
path = 'chromedriver84'
driver = webdriver.Chrome(executable_path = path)

time.sleep(10)
print(pyautogui.position())
