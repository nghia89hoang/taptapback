import webapp2
import urllib2
from google.appengine.api import urlfetch

class MainHandler(webapp2.RequestHandler):
  def get(self):
    url = "http://google.com"
    try:
      result = urlfetch.fetch(url)
      if result.status_code == 200:
        self.response.write(result.content)
    except urllib2.URLERROR, e:
      handleError(e)
    # self.response.write('Hello AppEngine')
    
app = webapp2.WSGIApplication([
    ('/',MainHandler)
], debug = True)