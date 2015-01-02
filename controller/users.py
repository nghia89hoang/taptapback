import webapp2
import urllib2
import ndbUser
from google.appengine.api import urlfetch

class UserHandler(webapp2.RequestHandler):
  def get(self):    
    self.response.write('Users page')
    
app = webapp2.WSGIApplication([
    ('/users/',UserHandler)
], debug = True)