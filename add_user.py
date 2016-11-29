#!/usr/bin/env python
#
#title           :add_user.py
#description     :This is a sample script to demonstrate how to add a user to the Smart Communications API.
#author          :Michael Dodwell <michael@dodwell.us>
#date            :20161129
#version         :0.1
#usage           :python add_user.py
#notes           :See https://example.thunderhead.com/one/help/api/index.htm#22468.htm
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
# getUser()
# This function creates a array and turns it into a json object 
# containing an example user
# inputs: none
# returns: json object of a user
def getUser():
  #The request body is composed of an object in the following structure:
  #
  #{
  #	"userId": "name@yourtenancy",
  #	"authType": "AD",
  #	"emailAddress": "email@thunderhead.com",
  #	"forename": "firstname",
  #	"surname": "lastname",
  #	"groupNames": ["Default Group"],
  #	"roleIds": [1, 6]
  #}
  #
  # Here we specify the array and then turn it into a json object
  #
  # You could read the json object from a file with the following code:
  #
  # with open('user.json') as json_data:
  #   return json.load(json_data)
  #
  #
  user = {}
  user['userId'] = 'michael2@dodwell.us.trial'
  user['emailAddress'] = 'michael@dodwell.us'
  user['forename'] = 'Michael'
  user['surname'] = 'Dodwell'
  
  # groupNames
  #
  #The groups in the application that the user will be added to (if they exist).
  #
  #If a specified group does not exist, an exception will be thrown.
  #
  #If no groups are specified, the user will not be added to any groups.
  user['groupNames'] = ["Default Group"]
  
  # roleIds
  #
  # Roles assigned to the user in the Settings module:
  #
  # 1     System Administrator
  # 2     Templates User
  # 3     Salesforce User
  # 4     Documents Administrator
  # 5     Documents Creator
  # 6     Documents User
  # 7     Documents API
  # 8     Touchpoints User
  # 9     CMS Administrator
  # 10    Appliance Admin
  # 11    Appliance Manager
  # 12    Appliance Operator
  # 13    Appliance User
  # 14    Documents Operator
  # 15    User Administrator
  user['roleIds'] = [1,6]
  
  return json.dumps(user)


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
                API_ENDPOINT + "/users",
                method = "POST",
                body=getUser(),
                headers={'Content-type': 'application/json'}
                )

# The response will be HTTP Response 201 if the user is created successfully, and the user ID will be returned.
if resp['status'] != '201':
  exitPrint(resp, content)

print "User created successfullly:"
print "    - userId        = %s" % content
print 
