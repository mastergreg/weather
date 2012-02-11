#!/usr/bin/python
# -*- coding: utf-8 -*-
from urllib2 import Request, urlopen
from re import search

def main(): 
    req = Request("http://www.rssweather.com/wx/gr/athinai/rss.php")
    response = urlopen(req)
    the_page = response.read()
    result = search('Weather ::.*?<',the_page)
    print result.group(0)[:len(result.group(0))-1]

if __name__=="__main__":
    main()
