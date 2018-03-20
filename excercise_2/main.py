from google.appengine.ext import db
import webapp2

class Greeting(db.Model):
    content = db.StringProperty(multiline=True)
    date = db.DateTimeProperty(auto_now_add=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')
        self.response.write('<h1>My GuestBook</h1><ol>')
        #greetings = db.GqlQuery("SELECT * FROM Greeting")
        greetings = Greeting.all()
        for greeting in greetings:
            self.response.write('<li> %s' % greeting.content)
        self.response.write('''
            </ol><hr>
            <form action="/sign" method=post>
            <textarea name=content rows=3 cols=60></textarea>
            <br><input type=submit value="Sign Guestbook">
            </form>
        ''')

class GuestBook(webapp2.RequestHandler):
    def post(self):
        greeting = Greeting()
        greeting.content = self.request.get('content')
        greeting.put()
        self.redirect('/')

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/sign', GuestBook),
], debug=True)
