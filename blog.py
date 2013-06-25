import os
import webapp2
import jinja2
from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)
    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)
    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class MainPage(Handler):
    def get(self):
        self.render("front.html")

class NewPost(Handler):
    def render_post(self, subject="", blog="", error=""):
        self.render("post.html",subject=subject, blog=blog, error=error)

    def get(self):
        self.render_post()

    def post(self):

        subject = self.request.get("subject")
        blog = self.request.get("blog")
        error = self.request.get("error")

        render_post()


application = webapp2.WSGIApplication([('/blog', MainPage),
                                       ('/blog/newpost', NewPost)

                                       ], debug=True)

