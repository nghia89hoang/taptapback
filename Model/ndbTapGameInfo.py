import webapp2
import urllib2
from google.appengine.ext import ndb
from protorpc import message_types
from endpoints_proto_datastore.ndb import EndpointsModel

class TapGameInfo(EndpointsModel):
  currLevel = ndb.IntegerProperty(indexed = True)
  highestLevel = ndb.IntegerProperty(indexed = True)
  # totalGold = ndb.StringProperty(indexed = False)
  totalRelics = ndb.IntegerProperty()
  totalPrestiges = ndb.IntegerProperty()
  
  @staticmethod
  def insert(new_tapgameinfo):
    query = TapGameInfo.query(ancestor = new_tapgameinfo.key.parent())
    if query.count() == 0:
      new_tapgameinfo.put()
      return True
    return False
    