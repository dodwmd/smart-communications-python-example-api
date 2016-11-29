#!/usr/bin/env python
#
#title           :list_users.py
#description     :This is a sample script to demonstrate how to list users from the Smart Communications API.
#author          :Michael Dodwell <michael@dodwell.us>
#date            :20161129
#version         :0.1
#usage           :python list_users.py
#notes           :See https://example.thunderhead.com/one/help/api/index.htm#22460.htm
#python_version  :2.7.12 
#==============================================================================

##############################################################
# IMPORT MODULES
##############################################################
# Import required modules
import oauth2
import time
import urllib2
import json
import sys
import xml.dom.minidom

##############################################################
# ENVIRONMENT SECTION
##############################################################
# oauth_consumer_key
#
# <API Key>!<User ID for Smart Communications>
# 
# For example:
#
# e90bea0d-ead9-45cc-9d48-f779f1d89050!jsmith@ONEURL
#
OAUTH_CONSUMER_KEY = '' # Fill this in with your client ID

# oauth_token_secret
#
# <Shared Secret>
#
# For example:
# 18441c0c-5a97-4d5d-8423-f0b7c80681e5
OAUTH_CONSUMER_SECRET = '' # Fill this in with your client secret

# ENDPOINT is for User Management
API_ENDPOINT = 'https://example.thunderhead.com/one/oauth1/userManagement/v4'

##############################################################
# FUNCTIONS SECTION
##############################################################
# exitPrint(resp, content)
# This function loops thru the headers and prints their vaules 
# with the body of a web response
# inputs:  resp, content are the response headers and the body 
#          content of a web request.
# returns: outputs slightly formmatted header values and the 
#          body of content returned
def exitPrint(resp, content):
  for header, value in resp.iteritems():
    print '%s: %s' % (header, value)
  print content
  print "Error code: %s" % resp['status']
  sys.exit(1)

##############################################################
# MAIN
##############################################################
# Lets start
#
# First Generate OAuth tokens
#
consumer = oauth2.Consumer(OAUTH_CONSUMER_KEY,OAUTH_CONSUMER_SECRET)
client = oauth2.Client(consumer)

# Send request
resp, content = client.request(
                API_ENDPOINT + "/users/michael@dodwell.us.trial",
                method = "GET",
                headers={'Content-type': 'application/json'}
                )

# The response will be HTTP Response 201 if the user is created successfully, and the user ID will be returned.
if resp['status'] != '200':
  exitPrint(resp, content)

# Response is XML lets make a little more pretty
contentXml = xml.dom.minidom.parseString(content)

print contentXml.toprettyxml()
