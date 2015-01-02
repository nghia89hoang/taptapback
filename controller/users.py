import webapp2
import urllib2
from google.appengine.api import urlfetch

from Model.ndbUser import gUser

class UserHandler(webapp2.RequestHandler):
  def get(self):    
    self.response.write('Users page')
    
app = webapp2.WSGIApplication([
    ('/users',UserHandler)
], debug = True)