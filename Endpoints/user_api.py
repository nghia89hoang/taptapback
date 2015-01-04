import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote

from endpoints_proto_datastore.ndb import EndpointsModel
from Model.ndbUser import TapUser
import CustomType

@endpoints.api(name='userApi', version='v1', description='Tap user API')
class UserApi(remote.Service):
  
  @TapUser.query_method(path='tapusers', name='tapuser.list')
  def TapUserList(self, query):
    return query
  
  @TapUser.method(path='tapuser', http_method='POST', name='tapuser.insert', response_message = CustomType.StringMessage)
  def TapUserInsert(self, my_model):
    if TapUser.insert(my_model) == True:
      return CustomType.StringMessage(value = 'Insert success')
    return CustomType.StringMessage(value = 'Insert failed')
    
    
app = endpoints.api_server([
    UserApi
])