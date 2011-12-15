#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2
import re

req = urllib2.Request("http://www.rssweather.com/wx/gr/athinai/rss.php")
response = urllib2.urlopen(req)
the_page = response.read()
result= re.search('Weather ::.*?<',the_page)
print result.group(0)[:len(result.group(0))-1]
