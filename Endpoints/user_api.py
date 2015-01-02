import endpoints
from protorpc import messages
from protorpc import message_type
from protorpc import remote

from endpoints_proto_datastore.ndb import EndpointsModel
from Model.ndbUser import TapUser

@endpoints.api(name='userApi', version='v1', description='Tap user API')
class UserApi(remote.Service):
  
  @TapUser.query_method(path='tapusers', name='tapuser.list')
  def TapUserList(self, query):
    return query
  
  @TapUser.method(path='tapuser', http_method='POST', name='tapuser.insert')
  def TapUserInsert(self, my_model):
    my_model.put
    return my_model
    
    
app = endpoints.api_server([
    UserApi
], debug = True)