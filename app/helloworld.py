"""Hello World test application module"""
import cherrypy
import os

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
    cherrypy.config.update({
        'server.socket_host': '0.0.0.0',
	    'server.socket_port': os.environ["PORT"]
        })
    cherrypy.quickstart(Helloworld())
