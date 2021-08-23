# -*- coding: utf-8 -*-

# Imports
import requests
import smtplib
import time
import urllib
from bs4 import BeautifulSoup

## UserAgent and URL

Head = 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0'

HEADER = {'User-Agent': Head}
#URL = str(input("Enter URL: "))
URL = 'https://www.flipkart.com/adidas-solid-men-round-neck-white-t-shirt/p/itmfefdzn3f7w8e7?pid=TSHFEFDNDHQT7BYA&lid=LSTTSHFEFDNDHQT7BYATVVBA7&marketplace=FLIPKART&sattr[]=color&st=color'
Price_Expecc = 800

page = requests.get(URL,
                    headers=Head)
suup = BeautifulSoup(page.content, 'html.parser')
title = str(suup.find("span", {"class": "B_NuCI"}).get_text())[:10].strip()
price = float(suup.find("div", {"class": "_30jeq3 _16Jk6d"}).get_text()[
              1:].replace(',', ''))

"""##URL Shortening"""


def URL_Short(Ze_URL):
    key = '4423d86605cc556762e0229b8254d1d9004f5'
    url = urllib.parse.quote(Ze_URL)

    api_call = ('http://cutt.ly/api/api.php?key={}&short={}'.format(key, url))
    data = requests.get(api_call).json()["url"]
    if data["status"] == 7:
        # get shortened URL
        return data["shortLink"]
    else:
        print("[!] Error Shortening URL:", data)
        return Ze_URL


"""## Parse Price"""


def check_price():

    if(price < Price_Expecc):
        Send_Mail()
        print("Price Below {0} and is {1}".format(Price_Expecc, price))


print(title)

"""## Emailing"""


def Send_Mail():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()     # servers identify the client
    server.starttls()  # start an SMTP connection in TLS
    server.ehlo()     # re-send
    # Generate app password on Gmail ("Email", "App Password")
    server.login('eminate894567@gmail.com', "mnlcctzfhsmpeknb")
    # EMAILS
    FROM = "eminate894567@gmail.com"
    TO = "midann534@gmail.com"
    # BODY of mail
    Subj = ('Price of {} is below {}'.format(title, Price_Expecc))
    Txt = ('Check the link: ' + URL_Short(URL))
    # Body = " ".join((
    #        "From: %s" % FROM,
    #        "To: %s" % TO,
    #        "Subject: %s" % Subj,
    #        "",
    #        Txt,
    #        ))
    Body = f"Subject: {Subj}\n\n{Txt}"

    # Sending Mail
    server.sendmail(FROM, TO, Body)
    print('Email Sent')
    print(Body)
    server.quit()


"""# Running every hour"""

while(True):
    check_price()
    time.sleep(60*60)
