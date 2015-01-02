import endpoints
from protorpc import messages
from protorpc import message_type
from protorpc import remote

import Model.ndbUser


class UserApi(remote.Service):
  pass
    
app = endpoints.api_server([
    UserApi
], debug = True)