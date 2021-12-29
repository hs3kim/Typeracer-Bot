from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

PATH = "./driver/chromedriver.exe"
URL = "https://play.typeracer.com/"
WPM = 100

def input_text(wpm):
    text_container = []
    str = ""

    print("Awaiting next race...")
    # Wait to start a new race after a race has been completed
    while (True):
        try:
            # Waiting for "Typing review" page to disappear
            time.sleep(1)
            driver.find_element_by_xpath('//span[@class="remainingChars"]')
        except NoSuchElementException:
            break

    # Locate element that takes user text input
    while (True):
        try:
            input = driver.find_element_by_xpath('//input[@class="txtInput"]')
            break
        except NoSuchElementException:
            # Waiting to find text input location
            time.sleep(0.5)
    
    while(text_container == []):
        text_container = driver.find_elements_by_xpath('//table[@class="inputPanel"]')
    print("Race start!")

    text = text_container[0].find_elements_by_xpath('//span[@unselectable="on"]')

    # Input first word of text
    if len(text) == 2:
        str = text[1].text
        if str[0] == ",":
            input.send_keys(text[0].text)
        else:
            input.send_keys(text[0].text + " ")
    else:
        str = text[2].text
        if str[0] == ",":
            input.send_keys(text[0].text + text[1].text)
        else:
            input.send_keys(text[0].text + text[1].text + " ")
    # Input remaining text
    for x in str:
        input.send_keys(x)
        time.sleep(10/wpm)

# Set target WPM with user input
def input_wpm():
    while(True):
        try:
            wpm = input("Enter a desired WPM(Default 100):")
            if wpm == "":
                wpm = WPM
                print("WPM set to " + str(wpm))
                break
            elif int(wpm) <= 0:
                print("Enter an integer value greater than 0")
            else:
                wpm = int(wpm)
                print("WPM set to " + str(wpm))
                break
        except ValueError:
            print("Invalid argument")
    return wpm

def main():
    global driver

    wpm = input_wpm()

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path=PATH, options=options)
    driver.get(URL)

    while(True):
        input_text(wpm)

if __name__ == "__main__":
    main()
