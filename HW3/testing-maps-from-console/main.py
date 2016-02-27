import cgi
import datetime
import webapp2
import urllib2
import json

from google.appengine.ext import ndb
from google.appengine.api import users
from google.appengine.api import urlfetch

guestbook_key = ndb.Key('Guestbook', 'default_guestbook')

GMAPS_API_KEY = "AIzaSyB16N6RHY71J_sZlGupTntG4vvx1rF_rGc"

class Greeting(ndb.Model):
  nickname = ndb.UserProperty()
  location = ndb.TextProperty()
  date = ndb.DateTimeProperty(auto_now_add=True)


class MainPage(webapp2.RequestHandler):
  def get(self):
    self.response.out.write("""<html><body>
                            <h1>Chipotle Burnt My Chicken!</h1>
                            <strong>Are you fed up with burnt chicken at Chipotle? Let them know here!</strong><br />
                            Tell us which Chipotle location burnt your chicken, and we'll record the date and time to this map.<br /><br />""")

    interactions = ndb.gql('SELECT * '
                    'FROM Greeting '
                    'WHERE ANCESTOR IS :1 '
                    'ORDER BY date DESC LIMIT 10',
                    guestbook_key)

    interactionsArray = []
    coords = []
    						
    for interaction in interactions:
      if interaction != None:
        interactionsArray.append(interaction)
        
    ## GEOCODING
    stringSearchLocation = ""
    if interactionsArray[0].location != None:
      stringSearchLocation = interactionsArray[0].location.replace(" ", "+")
    geocodeRequestURL = """https://maps.googleapis.com/maps/api/geocode/json?address=""" + stringSearchLocation + """+Chipotle&key=""" + GMAPS_API_KEY
    
    geocodeRequest = urlfetch.fetch(geocodeRequestURL)
    data = json.loads(geocodeRequest.content)
    newInputCoord = []
    newInputCoord.append( data['results'][0]['geometry']['location']['lat'] )
    newInputCoord.append( data['results'][0]['geometry']['location']['lng'] )
    
    ## MAP IFRAME
    self.response.out.write("""
      <img width="600" src="http://maps.googleapis.com/maps/api/staticmap?center=united+states&zoom=3&scale=false&size=600x300&maptype=roadmap&key=AIzaSyB16N6RHY71J_sZlGupTntG4vvx1rF_rGc&format=png&visual_refresh=true
      &markers=size:large%7color:0xff0000%7c""" + str(newInputCoord[0]) + """,+""" + str(newInputCoord[1]) + """
      ">""") #It's 50 minutes before this is due. This should be in an array, and display multiple markers.
##    self.response.out.write("""
##      <iframe
##        width="600"
##        height="450"
##        frameborder="0" style="border:0"
##        src="https://www.google.com/maps/embed/v1/place?key=""" + GMAPS_API_KEY + """
##          &q=""" + str(newInputCoord[0]) + "," + str(newInputCoord[1]) + """+Chipotle" allowfullscreen>
##      </iframe><br />""")


    self.response.out.write("""
          <form action="/sign" method="post">
            <div>Name/Nickname<br />
            <input type="text" name="nickname"></input></div><br />
            <div>Location of restaurant (city or approximate address)<br />
            <textarea name="location" rows="3" cols="60" value="Chipotle location"></textarea></div>
            <div><input type="submit" value="They burnt my chicken!!!"></div>
          </form>""")

    self.response.out.write("""
          <br /><br /><br /><br />
          <div style="font-style:italic">
            Dear Chipotle, <br />
            It's just a homework assignment, bro. Please don't sue me for libel.<br />
            But seriously, please stop serving me blackened chicken.
          </div>
        </body>
      </html>""")


class Guestbook(webapp2.RequestHandler):
  def post(self):
    interaction = Greeting(parent=guestbook_key)

    if users.get_current_user():
      interaction.nickname = self.request.get('nickname')

    interaction.location = self.request.get('location')
    interaction.put()
    self.redirect('/')


app = webapp2.WSGIApplication([
  ('/', MainPage),
  ('/sign', Guestbook)
], debug=True)
