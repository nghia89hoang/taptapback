import webapp2
import urllib2
from google.appengine.ext import ndb
from protorpc import message_types
from endpoints_proto_datastore.ndb import EndpointsModel

# class TapUser(ndb.Model):
class TapUser(EndpointsModel):
  userID = ndb.StringProperty(indexed = False)
  email = ndb.StringProperty(indexed = True)
  signupDate = ndb.DateTimeProperty(auto_now_add = True)
  
  @staticmethod
  def insert(my_model):
    user_query = TapUser.query(TapUser.email == my_model.email)
    if user_query.count() == 0:
      my_model.put()
      # return my_model
      return message_types.StringMessage('Insert success')
    return message_types.StringMessage('Insert failed')
  