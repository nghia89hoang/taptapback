import webapp2
import urllib2
import ndbUser
from google.appengine.api import urlfetch

class TapGameHandler(webapp2.RequestHandler):
  def get(self):
    self.response.write('TapGame Page')
    
app = webapp2.WSGIApplication([
    ('/tapgame',TapGameHandler)
], debug = True)