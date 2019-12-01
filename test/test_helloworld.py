"""Hello World class test"""

import cherrypy
from cherrypy.test import helper

from app.helloworld import Helloworld

class HelloWorldTest(helper.CPWebCase):
    """Hello World class signature."""

    @staticmethod
    def setup_server():
        """Setup test class method"""
        cherrypy.tree.mount(Helloworld(), '/', {})

    def test_helloworld(self):
        """Hello world endpoint test"""
        self.getPage("/helloworld")
        self.assertBody('Hello World!')

    def test_byebyeworld(self):
        """Bye bye world endpoint test"""
        self.getPage("/byebyeworld")
        self.assertBody('Bye bye World!')
