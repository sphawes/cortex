#Scrape HackPGH for Open Status
import requests, bs4, os, re
import urllib.request
import shutil

def isHackPghOpen():

    url = "http://www.hackpittsburgh.org/"


    #sweep categories page, bring up each category link
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    #page is now soup-ified in BS4 element 'soup'
    lightStatusPanel = soup.find("div", {"id": "light_status"});

    if lightStatusPanel['style'] == "width: 209px; height: 76px; margin-bottom: 0px; background: url('http://www.hackpittsburgh.org/wp-content/uploads/2016/12/shopClosed2.png'); display:none;":
        return False;
    elif lightStatusPanel['style'] == "width: 209px; height: 76px; margin-bottom: 0px; background: url('http://www.hackpittsburgh.org/wp-content/uploads/2016/12/shopClosed2.png'); display:none;":
        
    else:
        return True;
