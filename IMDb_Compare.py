#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Victoria Wingo

Created: 24 Jan 2022

Purpose: Scrub information from IMDb to compare
the actors of two pieces of media
"""

from bs4 import BeautifulSoup
import requests


def util_func(element):
    try:
        return element['title']
    except KeyError:
        pass


# Scrape The Sopranos page and make list of cast
sop_page = requests.get(
    "https://www.imdb.com/title/tt0141842/fullcredits/?ref_=tt_ql_cl")
sop_soup = BeautifulSoup(sop_page.content, "html.parser")

# Scrape Goodfellas page and make list of cast
gf_page = requests.get(
    "https://www.imdb.com/title/tt0099685/fullcredits/?ref_=tt_cl_sm")
gf_soup = BeautifulSoup(gf_page.content, 'html.parser')

sop_cast = [util_func(element) for index, element 
            in enumerate(sop_soup.select('.cast_list img'))]
sop_cast = [x for x in sop_cast if x]
print("Actors in The Sopranos: ", sop_cast[:9])
gf_cast = [util_func(element) for index, element 
           in enumerate(gf_soup.select('.cast_list img'))]
print("Actors in Goodfellas: ", gf_cast[:9])
print('Actors in both "The Sopranos" and "Goodfellas":', 
      list(set(sop_cast) & set(gf_cast)))