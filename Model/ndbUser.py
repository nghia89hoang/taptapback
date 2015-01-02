import webapp2
import urllib2
from google.appengine.ext import ndb
from endpoints_proto_datastore.ndb import EndpointsModel

# class TapUser(ndb.Model):
class TapUser(EndpointsModel):
  userID = ndb.StringProperty(indexed = True)
  email = ndb.StringProperty(indexed = False)
  signupDate = ndb.DateTimeProperty(auto_now_add = True)

