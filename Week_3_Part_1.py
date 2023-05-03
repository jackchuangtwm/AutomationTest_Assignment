# Assignment 1: Non-element Interaction (Selenium)
# Write a script to automate the below scenario in using Chrome browser.
# Scenario:
# Open the Chrome browser.
# Maximize the browser window.
# Navigate to AppWorks School Website (https://school.appworks.tw).
# Print “PASS” if the title of the page matches with “Code Your Future” else “FAIL”.
# Click the link “AppWorks” in top right corner
# Switch to new tabs to AppWorks website
# Print “PASS” if there is text “By Founders, For Founders” else “FAIL”.
# Navigate to https://appworks.tw/investments/
# Print “PASS” if there is text “We know you have a choice. We want you to choose us.” else “FAIL”.
# Navigate back to the AppWorks Website
# Print the URL of the current page.
# Navigate forward. 下一頁
# Close the current window
# Switch back to the original window and reload the page.
# Finally, Close the Browser.

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def selnium_lab():
    # Open the Chrome browser.
    driver = webdriver.Chrome()
    time.sleep(2)

    # Maximize the browser window.
    driver.maximize_window()

    # Navigate to AppWorks School Website (https://school.appworks.tw).
    driver.get("https://school.appworks.tw")
    time.sleep(2)

    # Print “PASS” if the title of the page matches with “Code Your Future” else “FAIL”.
    xpath = '//*[@id="page"]/div[1]/div/div[1]/div/div/div/h1/span'
    str = driver.find_element(By.XPATH, xpath).text

    if str == 'Code Your Future':
        print('PASS')
    else:
        print('FAIL')

    # Click the link “AppWorks” in top right corner
    xpath = '//*[@id="page-top"]/div[2]/div/div/div[2]/a/i'
    driver.find_element(By.XPATH, xpath).click()
    time.sleep(2)

    # Switch to new tabs to AppWorks website
    xpath = 'AppWorks'
    driver.find_element(By.LINK_TEXT, xpath).click()
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)

    # Print “PASS” if there is text “By Founders, For Founders” else “FAIL”.
    xpath = '//*[@id="main"]/div[1]/div[2]/div/div/div[3]/div/h3/span/em'
    str = driver.find_element(By.XPATH, xpath).text

    if str == 'By Founders, For Founders':
        print('PASS')
    else:
        print('FAIL')

    # Navigate to https://appworks.tw/investments/
    driver.get("https://appworks.tw/investments/")
    time.sleep(2)

    # Print “PASS” if there is text “We know you have a choice. We want you to choose us.” else “FAIL”.
    xpath = '//*[@id="main"]/div[1]/div[2]/div/div/div[3]/div/h3/span/em'
    str = driver.find_element(By.XPATH, xpath).text

    if str == 'We know you have a choice. We want you to choose us.':
        print('PASS')
    else:
        print('FAIL')

    # Navigate back to the AppWorks Website
    driver.back()
    time.sleep(2)

    # Print the URL of the current page.
    current_url = driver.current_url
    print(current_url)

    # Navigate forward. 回下一頁
    driver.forward()
    time.sleep(2)

    # Close the current window
    driver.close()
    time.sleep(2)

    # Switch back to the original window and reload the page.
    driver.switch_to.window(driver.window_handles[0])
    driver.refresh()
    time.sleep(2)

    # Finally, Close the Browser.
    driver.quit()

sel = selnium_lab()


# Assignment 2: Algorithm Practice (Advanced Optional)
# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

def plus_one(nums):
    n = len(nums)
    
    # 從右向左找，找出第1個不為9的數字
    for i in range(n-1, -1, -1):
        if nums[i] != 9:
            nums[i] += 1 #把值 +1 回傳
            
            return nums
        
        else:
            nums[i] = 0 #要進位
    
    #如果數字都是9，就要進位
    return [1] + [0] * n

print(plus_one([1, 2, 3])) # Should be [1, 2, 4] because 123 + 1 = 124 ==> [1, 2, 4]
print(plus_one([4, 3, 2, 1])) # Should be [4, 3, 2, 2]
print(plus_one([9])) # Should be [1, 0]
print(plus_one([9,9])) # Should be [1, 0, 0]

