import webapp2
import urllib2
from google.appengine.api import urlfetch
from google.appengine.ext import ndb

class TapGameInfo(ndb.Model):
  currLevel = IntProperty(indexed = True)
  highestLevel = IntProperty(indexed = True)
  totalGold = StringProperty(indexed = False)
  totalRelics = IntProperty()
  totalPrestiges = IntProperty()