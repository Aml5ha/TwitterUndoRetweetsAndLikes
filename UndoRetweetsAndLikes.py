#Made by Arman Lokhandwala 07/2018
import os.path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import time


### This method waits for al elements on the page to load
def WaitForLoad(driver):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located
        )
    finally:
        time.sleep(.5)

### This method does the setup by handling the twitter login
def Setup():
    #the following two lines asks the user for username and password and keeps it for later use
    username = input("Enter Username: ")
    password = input("Enter password: ")


    directory = os.path.dirname(os.path.abspath(__file__))  # gets the path of where this file is saved
    location_of_driver = (os.path.join(directory,'chromedriver'))  # appends 'chromedriver' to the current file path - make sure chrome driver is in same directory as this file

    # print(locationOfDriver) #this line may be commented out to make sure its correctly reaching the location of the chromedriver

    driver = webdriver.Chrome(location_of_driver) #gets the chromedriver

    driver.get("https://twitter.com/login")  #navigates the driver to the twitter login page
    WaitForLoad(driver)

    login_list = driver.find_elements_by_name("session[username_or_email]")  # finds the elements on the page that have a matching name

    login_box = login_list[1]  # looking through the HTML, you can see that the second instance of "session[username_or_email]" corresponds to the actual login box
    login_box.send_keys(username, Keys.ARROW_DOWN)  # sending the username to the login box, and the down arrow key to indicate its finished

    password_list = driver.find_elements_by_name("session[password]")  # finds all elements relating to password
    password_box = password_list[1]  # second element mentioned on the page corresponds to the password box

    password_box.send_keys(password, Keys.ARROW_DOWN)  # send the password to the appropriate box

    password_box.send_keys(Keys.TAB, Keys.ENTER)  # navigating and 'clicking' the log in button

    driver.get("https://twitter.com/" + str(username)) #navigates to the twitter page that was logged into
    WaitForLoad(driver)
    return driver

### This method handles undoing *most* of the retweets and likes on the users profile
def undo_retweets_and_likes(driver):
    time_to_scroll = int(input("Scroll for how many seconds? (enter a number):  ")) #choose how long to scroll for
    end_time = time.time() + time_to_scroll
    while time.time() < end_time:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # scrolls down for 'time_to_scroll' seconds

        WaitForLoad(driver)

    list_of_retweets = driver.find_elements_by_class_name("ProfileTweet-actionButtonUndo") #finds a list of *clickable buttons
    num_buttons_found = list_of_retweets.__len__() #the number of buttons found

    i = 0
    count = 0
    not_clicked = 0

    ## This block of code tries to click on all of the buttons found, if it cannot be clicked it is added to the "not_clicked" counter
    while (i < num_buttons_found):
        string = list_of_retweets[i].find_element_by_xpath("..").find_element_by_xpath("..").find_element_by_xpath(
            "..").find_element_by_xpath(
            "..").find_element_by_xpath("..").get_attribute("innerHTML")
        if "js-retweet-text" in string:
            try:
                list_of_retweets[i].click()
                count += 1

            except WebDriverException:
                not_clicked +=1

        i += 1

    total_time = time.time() - (end_time - 5) #calculate how much time the process took

    print("Total time taken: " + "{0:.2f}".format(total_time))  #print how long it took
    print("Total buttons clicked (undoretweets or unlike): " + str(count)) #print how many buttons were clicked in total
    print("Buttons that weren't clickable: " + str(num_buttons_found - not_clicked)) #print how many weren't clickable for some reason


undo_retweets_and_likes(Setup())
