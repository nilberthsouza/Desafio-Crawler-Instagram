# coding: utf-8
 
 
from bs4 import BeautifulSoup

import requests
 
 class Page:
     def __init__(self,link):
         self.link = link
         self.site = requests.get(link).text
             
     def title(self):
         res = BeautifulSoup(self.site,'html.parser')
         pageTitle = res.find(class_='header-title-content')
         return pageTitle.text
 
 
 
 page = Page('https://g1.globo.com/bemestar/')
 
 class Convert(Page):
 
     @staticmethod
     def from_string_to_text(arg):
         return arg.text
 
 class Feed(Page):
     posts = []
 
     def post(self):
         response = []
         soup = BeautifulSoup(self.site, 'html.parser')
         result = soup.find_all(class_='feed-post-link')
         for res in result:
             response.append(Convert.from_string_to_text(res))
         return response
 
 feed = Feed('https://g1.globo.com/bemestar/')
 
 feed.link
 
 
 feed.post()
 
