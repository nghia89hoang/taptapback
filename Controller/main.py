import webapp2
import urllib2
from google.appengine.api import urlfetch

from Model.ndbUser import TapUser
from Controller.users import UserHandler
from Controller.tapgame import TapGameHandler

class MainHandler(webapp2.RequestHandler):
  def get(self):
    self.response.write('Home page')
    
app = webapp2.WSGIApplication([
    ('/',MainHandler)
], debug = True)