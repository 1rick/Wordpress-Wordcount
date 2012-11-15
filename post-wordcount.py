#!/usr/bin/env python

"""a script for fetching posts from wordpress, and then doing a wordcount. here i do it for a specific user, but it could be for all users. fill in username and password, domain, as well as the desired user to fetch, as their name is displayed, as opposed to their username."""


from __future__ import division
import xmlrpclib
 
MAX_POSTS = 500
#adjust for your own domain
url = 'http://DOMAINCOM/xmlrpc.php'
#input your blog username and pw
myusername = ''
mypassword = ''
#type the wordpress user whose posts you want to fetch here
user_to_fetch = ''
 
server = xmlrpclib.ServerProxy(url)
result = server.metaWeblog.getRecentPosts(url, myusername, mypassword, MAX_POSTS)
 
numPosts = len(result)
postwordcount = 0

for post in result:
  postwordcount = len(post['description'].split())
  post_title = post['title']
  post_author = post['wp_author_display_name']
  post_date = post['date_created_gmt']
  if post_author == user_to_fetch:
    print (postwordcount, post_author, post_title, post_date)

