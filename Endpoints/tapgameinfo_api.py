import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote

from endpoints_proto_datastore.ndb import EndpointsModel
# from Model.ndbUser import TapUser
from Model.ndbTapGameInfo import TapGameInfo
import CustomType

@endpoints.api(name='tapGameInfoApi', version='v1', description='Tap Game API')
class TapGameInfoApi(remote.Service):

  @TapGameInfo.query_method(query_fields=('order',), path='gameinfoLst', name='gameinfo.list')
  def TapGameInfoList(self, query):
    return query


#   @TapGameInfo.query_method(query_fields=('order',),path='gameinfoLstByLevel', name='gameinfo.listbylevel')
#   def TapGameInfoListByLevel(self, query):
#     return query

  # @TapUser.method(path='tapgameinfo', http_method='POST', name='tapgameinfo.insert', response_message = CustomType.StringMessage)
  # def TapUserInsert(self, new_user):
    # if TapUser.insert(new_user) == True:
      # new_tapgameinfo = TapGameInfo(parent=new_user.key)
      # if TapGameInfo.insert(new_tapgameinfo) == True:
        # return CustomType.StringMessage(value = 'Insertion successed')
      # else:
        # return CustomType.StringMessage(value = 'Insertion Failed, can not insert TapGameInfor for user')
    # return CustomType.StringMessage(value = 'Insertion failed')

  # @TapUser.method(path='tapuser/del', http_method='POST', name='tapuser.del', response_message = CustomType.StringMessage)
  # def TapUserDelete(self, user_2del):
    # pass

# app = endpoints.api_server([
    # TapGameInfoApi
# ])