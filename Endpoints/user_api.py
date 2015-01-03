import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote

from endpoints_proto_datastore.ndb import EndpointsModel
from Model.ndbUser import TapUser

@endpoints.api(name='userApi', version='v1', description='Tap user API')
class UserApi(remote.Service):
  
  @TapUser.query_method(path='tapusers', name='tapuser.list')
  def TapUserList(self, query):
    return query
  
  @TapUser.method(path='tapuser', http_method='POST', name='tapuser.insert', response_message = message_types.StringMessage)
  def TapUserInsert(self, my_model):
    return TapUser.insert(my_model)
    
    
app = endpoints.api_server([
    UserApi
])