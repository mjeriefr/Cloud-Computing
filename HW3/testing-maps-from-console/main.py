import cgi
import datetime
import webapp2

from google.appengine.ext import ndb
from google.appengine.api import users

guestbook_key = ndb.Key('Guestbook', 'default_guestbook')

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
    						
    for interaction in interactions:
      if interaction.nickname != None:
        self.response.out.write(interaction.nickname + " ")
      if interaction.location != None:
        self.response.out.write(interaction.location + "<br />")
      if interaction != None:
        interactionsArray.append(interaction)
##      if interaction.author:
##        self.response.out.write('<b>%s</b> wrote:' % interaction.author.nickname())
##      else:
##        self.response.out.write('An anonymous person wrote:')
##      self.response.out.write('<blockquote>%s</blockquote>' %
##                              cgi.escape(interaction.location))

    GMAPS_API_KEY = "AIzaSyB16N6RHY71J_sZlGupTntG4vvx1rF_rGc"
    self.response.out.write("""
      <iframe
        width="600"
        height="450"
        frameborder="0" style="border:0"
        src="https://www.google.com/maps/embed/v1/place?key=""" + GMAPS_API_KEY + """
          &q=""" + interactionsArray[0].location + """+Chipotle" allowfullscreen>
      </iframe><br />""")


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
