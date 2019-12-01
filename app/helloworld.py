"""Hello World test application module"""
import cherrypy

class Helloworld():
    """Hello World class signature"""
    @cherrypy.expose
    def helloworld(self):
        """Hello world endpoint method."""
        return "Hello World!"

if __name__ == '__main__':
    cherrypy.quickstart(Helloworld())
