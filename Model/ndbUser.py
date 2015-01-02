import webapp2
import urllib2
from google.appengine.api import urlfetch
from google.appengine.ext import ndb

class gUser(ndb.Model):
  userID = ndb.StringProperty(indexed = True)
  email = ndb.StringProperty(indexed = True)
  signupDate = ndb.DateTimeProperty(auto_now_add = True)

