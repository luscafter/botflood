# Copyright (c) 2020, Lucas Araújo
# All rights reserved.

# GitHub:    https://www.github.com/luscafter
# Twitter:   https://twitter.com/spartancode_
# Instagram: https://www.instagram.com/luscafter
# YouTube:   https://www.youtube.com/spartancode

from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import os, time, getpass

clean  = "\033[0;0m"
cyan   = "\033[1;36m"
R      = "\033[1;91m"
G      = "\033[1;92m"
B      = "\033[1;34m"

def banner():
    os.system("clear")
    print(cyan + "           ______ _______ _______  " + clean + "    _______ __                 __   ")
    print(cyan + "          |   __ \       |_     _| " + clean + "   |    ___|  |.-----.-----.--|  |  ")
    print(cyan + "          |   __ <   -   | |   |   " + clean + "   |    ___|  ||  _  |  _  |  _  |  ")
    print(cyan + "          |______/_______| |___|   " + clean + "   |___|   |__||_____|_____|_____|\n")
    print("                 (　" + R + "-" + clean + "_" + R + "-" + clean + ")︻デ═一     -                   Version " + cyan + "1" + clean + "." + cyan + "0" + clean + "." + cyan + "0" + clean)
    print("                                                 github.com/" + B + "luscafter\n" + clean + "\nLogin with your [Facebook] credentials\n")

class Facebook:
    def __init__(self):
        banner()
        username = input("[" + B + "Email" + clean + "] > ")
        password = getpass.getpass("[" + B + "Password" + clean + "] > ")
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path="/bin/geckodriver")

    def login(self):
        try:
            driver = self.driver
            print("\n[" + G + "+" + clean + "] Accessing Facebook...")
            driver.get("https://www.facebook.com")
            time.sleep(1)

            username_field = driver.find_element_by_xpath("//input[@name='email']")
            username_field.click()
            print("[" + G + "+" + clean + "] Typing the email")
            username_field.send_keys(self.username)
            time.sleep(1)

            password_field = driver.find_element_by_xpath("//input[@name='pass']")
            password_field.click()
            print("[" + G + "+" + clean + "] Entering the password")
            password_field.send_keys(self.password)
            time.sleep(1)

            print("[" + G + "+" + clean + "] Signing in...")
            password_field.send_keys(Keys.RETURN)
            time.sleep(1)
            print("[" + G + "+" + clean + "] Successfully logged in!\n")
            time.sleep(1)

            print("[ATTENTION]\n\nFacebook blocks the user for a certain time, every 400 comments.")
            print("If you want to send more comments, wait a while.\n")
            print("Save the target publication, go to the saved publications, click on the publication and copy the URL.")
            print("Or click on the target publication and copy the URL (the first option is recommended).")
            print("Example: https://www.facebook.com/" + G + "jonatas.braz.9/posts/2707472182712483\n" + clean)
            target = input("Type here > ")

            comment = input("Enter the comment you want to flood > ")

            delay = 0
            while delay <= 0:
                delay = float(input("Enter the time delay to send messages [separate by points, example: 0.4] > "))
                if delay <= 0:
                    print("[" + R + "!" + clean + "] Invalid value! Enter a value greater than 0 (zero).\n")

            toggle = 0
            while toggle <= 0:
                toggle = int(input("Enter the maximum amount of the repeated comment range [10 is standard] > "))
                if toggle <= 0:
                    print("[" + R + "!" + clean + "] Invalid value! Enter a value greater than 0 (zero).\n")

            print("\n[" + G + "+" + clean + "] Redirecting to the target publication...\n")
            time.sleep(1)
            print("    (　" + R + "-" + clean + "_" + R + "-" + clean + ")︻デ═一     -     " + target[:25] + G + target[25:] + clean + "\n")
            self.publication_target(target, comment, delay, toggle)

        except Exception as error:
            print("\n[" + R + "!" + clean + "] An error has occurred.")
            print("You did not enter the data correctly or the page was closed unexpectedly. Try again!\n")

    def log_messages(self, delay, message):
        v = ['/', '—', '\\', '|']
        for i in range(4):
            print("\r[" + B + "!" + clean + "] Flooding    [ " + B + v[i] + clean + " ]    Sleep: " + str(delay) + "s    Message [ " + B + str(message) + clean + " ]    ", end="")
            time.sleep(delay/4)

    def publication_target(self, target, comment, delay, toggle):
        driver = self.driver
        driver.get(target)
        time.sleep(3)
        # Search for the field that contains "Write a comment..." and click
        driver.find_element_by_xpath("//div[contains(text(), 'Escreva um comentário...')]").click()

        limit    = 1
        message  = 1
        refresh  = 1
        addition = 1

        while message <= 400:
            try:
                # The "addition" variable is incremented and printed along with the comments so that Facebook doesn't block the flood
                if limit > toggle:
                    addition += 1
                    print("\n\n[" + G + "+" + clean + "] Toggling comment\n")
                    limit = 1

                # The page is updated every 50 comments to not crash
                if refresh > 50:
                    print("[" + G + "+" + clean + "] The page is being updated...\n")
                    time.sleep(3)
                    driver.refresh()
                    driver.find_element_by_xpath("//div[contains(text(), 'Escreva um comentário...')]").click()
                    refresh = 1

                # Scroll to the bottom of the page
                driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                # Look for the class "notranslate _5rpu"
                comment_field = driver.find_element_by_css_selector(".notranslate._5rpu")
                # Commenting on the post / photo
                comment_field.send_keys(comment + " [ " + str(addition) + " ]")
                self.log_messages(delay, message)
                # Enter key
                comment_field.send_keys(Keys.RETURN)
                refresh += 1
                limit   += 1
                message += 1
                if message == 400:
                    print("\n[" + R + "!" + clean + "] You have reached the maximum comment limit. Try later!\n")

            except Exception as error:
                if limit < toggle:
                    print("")

                print("\n[" + R + "!" + clean + "] An error has occurred.\nThe page can be updated!")
                time.sleep(3)
                driver.refresh()
                driver.find_element_by_xpath("//div[contains(text(), 'Escreva um comentário...')]").click()

luscas = Facebook()
luscas.login()
