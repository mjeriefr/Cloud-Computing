import cgi
import datetime
import webapp2

from google.appengine.ext import ndb
from google.appengine.api import users

guestbook_key = ndb.Key('Guestbook', 'default_guestbook')

class Greeting(ndb.Model):
  author = ndb.UserProperty()
  content = ndb.TextProperty()
  date = ndb.DateTimeProperty(auto_now_add=True)


class MainPage(webapp2.RequestHandler):
  def get(self):
    self.response.out.write("""<html><body>
                            <h1>Chipotle Burnt My Chicken!</h1>
                            <strong>Are you fed up with burnt chicken at Chipotle? Let them know here!</strong><br />
                            Tell us which Chipotle location burnt your chicken, and we'll save the date and time to this map.<br /><br />""")

    GMAPS_API_KEY = "AIzaSyB16N6RHY71J_sZlGupTntG4vvx1rF_rGc"
    self.response.out.write("""
      <iframe
        width="600"
        height="450"
        frameborder="0" style="border:0"
        src="https://www.google.com/maps/embed/v1/place?key=""" + GMAPS_API_KEY + """
          &q=Space+Needle,Seattle+WA" allowfullscreen>
      </iframe><br />""")
	
    greetings = ndb.gql('SELECT * '
                        'FROM Greeting '
                        'WHERE ANCESTOR IS :1 '
                        'ORDER BY date DESC LIMIT 10',
                        guestbook_key)

	
						
    for greeting in greetings:
      if greeting.author:
        self.response.out.write('<b>%s</b> wrote:' % greeting.author.nickname())
      else:
        self.response.out.write('An anonymous person wrote:')
      self.response.out.write('<blockquote>%s</blockquote>' %
                              cgi.escape(greeting.content))


    self.response.out.write("""
          <form action="/sign" method="post">
            <div><textarea name="content" rows="3" cols="60" value="Chipotle location"></textarea></div>
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
    greeting = Greeting(parent=guestbook_key)

    if users.get_current_user():
      greeting.author = users.get_current_user()

    greeting.content = self.request.get('content')
    greeting.put()
    self.redirect('/')


app = webapp2.WSGIApplication([
  ('/', MainPage),
  ('/sign', Guestbook)
], debug=True)
