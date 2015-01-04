import webapp2
import urllib2
from google.appengine.ext import ndb
from protorpc import message_types
from endpoints_proto_datastore.ndb import EndpointsModel

class TapGameInfo(EndpointsModel):
  currLevel = ndb.IntegerProperty(indexed = True, default = 1)
  highestLevel = ndb.IntegerProperty(indexed = True, default = 1)
  # totalGold = ndb.StringProperty(indexed = False, default = 0)
  totalRelics = ndb.IntegerProperty(default = 0)
  totalPrestiges = ndb.IntegerProperty(default = 0)

  @staticmethod
  def insert(new_tapgameinfo):
    query = TapGameInfo.query(ancestor = new_tapgameinfo.key.parent())
    if query.count() == 0:
      new_tapgameinfo.put()
      return True
    return False

#   @staticmethod
#   def update()
