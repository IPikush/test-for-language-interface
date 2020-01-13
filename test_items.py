
import pytest
from selenium import webdriver
import time
import math



def test_button_availability(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(5)
    
    assert (browser.find_element_by_css_selector("button.btn-add-to-basket"))   , "button is not available"
    
    
    
    
    
