import webapp2
import urllib2
from google.appengine.ext import ndb
from protorpc import message_types
from protorpc import messages
from endpoints_proto_datastore.ndb import EndpointsModel
from endpoints_proto_datastore.ndb import EndpointsAliasProperty

from Model.ndbUser import TapUser


class Order(messages.Enum):
  HI_LEVEL_ASC    =1
  HI_LEVEL_DESC   =2
  TOTAL_PRES_ASC  =3
  TOTAL_PRES_DESC =4
  TOTAL_REL_ASC   =5
  TOTAL_REL_DESC  =6

DEFAULT_ORDER = Order.HI_LEVEL_DESC

class TapGameInfo(EndpointsModel):
  currLevel = ndb.IntegerProperty(indexed = True, default = 1)
  highestLevel = ndb.IntegerProperty(indexed = True, default = 1)
  # totalGold = ndb.StringProperty(indexed = False, default = 0)
  totalRelics = ndb.IntegerProperty(default = 0)
  totalPrestiges = ndb.IntegerProperty(default = 0)

  def OrderSet(self, value):
    if not isinstance(value, Order):
      raise TypeError('Expected an Enum, received: %s' % (value,))
    if value == Order.HI_LEVEL_ASC:
      super(TapGameInfo, self).OrderSet('highestLevel')
    elif value == Order.HI_LEVEL_DESC:
      super(TapGameInfo, self).OrderSet('-highestLevel')
    elif value == Order.TOTAL_PRES_ASC:
      super(TapGameInfo, self).OrderSet('totalPrestiges')
    elif value == Order.TOTAL_PRES_DESC:
      super(TapGameInfo, self).OrderSet('-totalPrestiges')
    elif value == Order.TOTAL_REL_ASC:
      super(TapGameInfo, self).OrderSet('totalRelics')
    elif value == Order.TOTAL_REL_DESC:
      super(TapGameInfo, self).OrderSet('-totalRelics')
    else:
      raise TypeError('Expected an Enum, received: %s' % (value,))

  @EndpointsAliasProperty(setter=OrderSet, property_type=Order, default=DEFAULT_ORDER)
  def order(self):
    return super(TapGameInfo, self).order

  @staticmethod
  def insert(new_tapgameinfo):
    query = TapGameInfo.query(ancestor = new_tapgameinfo.key.parent())
    if query.count() == 0:
      new_tapgameinfo.put()
      return True
    return False

  @staticmethod
  def getByUserId(uId):
#     gameInfo = TapGameInfo.query(ancestor = ndb.Key(TapUser, uId))
    user = TapUser.query(TapUser.userID == uId).get()
    if user is not None:
      gameInfo = TapGameInfo.query(ancestor = user.key)
      return gameInfo
    return None
