import cherrypy

class Helloworld(object):
    @cherrypy.expose
    def helloworld(self):
        return "Hello World!"

if __name__ == '__main__':
    cherrypy.quickstart(Helloworld())