
import pytest
from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException



def test_button_availability(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(5)
    try:
        browser.find_element_by_css_selector("button.btn-add-to-basket")
        result = True
    except NoSuchElementException:
        result = False

    assert result == True, "button is not available"
    
    
    
    
    
    
    
