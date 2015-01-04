import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote

from endpoints_proto_datastore.ndb import EndpointsModel
from Model.ndbUser import TapUser
from Model.ndbTapGameInfo import TapGameInfo
from Endpoints.tapgameinfo_api import TapGameInfoApi
import CustomType

@endpoints.api(name='userApi', version='v1', description='Tap user API')
class UserApi(remote.Service):
  
  @TapUser.query_method(path='tapuserLst', name='tapuser.list')
  def TapUserList(self, query):
    return query
  
  @TapUser.method(path='tapuser', http_method='POST', name='tapuser.insert', response_message = CustomType.StringMessage)
  def TapUserInsert(self, new_user):
    if TapUser.insert(new_user) == True:
      new_tapgameinfo = TapGameInfo(parent=new_user.key)
      if TapGameInfo.insert(new_tapgameinfo) == True:      
        return CustomType.StringMessage(value = 'Insertion successed')
      else:
        return CustomType.StringMessage(value = 'Insertion Failed, can not insert TapGameInfor for user')
    return CustomType.StringMessage(value = 'Insertion failed')

  # @TapUser.method(path='tapuser/del', http_method='POST', name='tapuser.del', response_message = CustomType.StringMessage)
  # def TapUserDelete(self, user_2del):
    # pass
    
app = endpoints.api_server([
    UserApi,
    TapGameInfoApi
])