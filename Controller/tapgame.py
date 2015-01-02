import webapp2
import urllib2
from google.appengine.api import urlfetch

from Model.ndbUser import TapUser
class TapGameHandler(webapp2.RequestHandler):
  def get(self):
    self.response.write('TapGame Page')
    
app = webapp2.WSGIApplication([
    ('/tapgame/',TapGameHandler)
], debug = True)