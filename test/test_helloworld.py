import sys
import importlib

import cherrypy
from cherrypy.test import helper

from app.helloworld import Helloworld

class HelloWorldTest(helper.CPWebCase):

    @staticmethod
    def setup_server():
        cherrypy.tree.mount(Helloworld(), '/', {})

    def test_generate(self):
        self.getPage("/helloworld")
        self.assertBody('Hello World!')
