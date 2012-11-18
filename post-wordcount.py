#!/usr/bin/env python

"""a script for fetching posts from wordpress, and then doing a wordcount. here i do it for a specific user, but it could be for all users. fill in username and password, domain, as well as the desired user to fetch, 
as their name is displayed, as opposed to their username."""


from __future__ import division
import xmlrpclib
 
MAX_POSTS = 500
#adjust for your own domain
url = 'http://DOMAINCOM/xmlrpc.php'
#input your blog username and pw
myusername = ''
mypassword = ''
#type the wordpress user whose posts you want to fetch here, 
#and month expressed as a number#
user_to_fetch = ''
month = ''
 
server = xmlrpclib.ServerProxy(url)
result = server.metaWeblog.getRecentPosts(url, myusername, mypassword, MAX_POSTS)
 
postwordcount = 0

postwordcount = 0

for post in result:
  description = post['description']
  desc_minus_image = BeautifulSoup(description).get_text()
  postwordcount = len(desc_minus_image.split())
  post_date = str(post['date_created_gmt'])
  post_title = post['title']
  post_author = post['wp_author_display_name']
  if post_author == user_to_fetch and post_date[4:6] == month:
    print """%d, %s/%s, %s""" % (postwordcount, post_date[4:6], post_date[6:8], post_title)
