"""Hello World test application module"""
import cherrypy

class Helloworld():
    """Hello World class signature"""
    @cherrypy.expose
    def helloworld(self):
        """Hello world endpoint method."""
        return "Hello World!"

    @cherrypy.expose
    def byebyeworld(self):
        """Bye bye world endpoint method."""
        return "Bye bye World!"

if __name__ == '__main__':
    cherrypy.quickstart(Helloworld())
