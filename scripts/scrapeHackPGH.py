#Scrape HackPGH for Open Status
import requests, bs4, os, re
import urllib.request
import shutil


url = "http://www.hackpittsburgh.org/"


#sweep categories page, bring up each category link
res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
#page is now soup-ified in BS4 element 'soup'

soup.find("div", {"id": "page_status"})
