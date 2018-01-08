import tornado.web
import tornado.httpserver
import textwrap
import tornado.ioloop
import tornado.options

from tornado.options import define,options
define("port",default=8000,help="Set the Port default is 8000",type=int)

class ReverseHandler(tornado.web.RequestHandler):
    def get(self,input):
        self.write(input[::-1])

class WrapHandler(tornado.web.RequestHandler):
    def post(self):
        text = self.get_argument("text","nontext")
        len = self.get_argument("length",40)
        self.write(textwrap.fill(text,len))


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[
        (r"/reverse/(\w+)",ReverseHandler),
        (r"/wrap",WrapHandler)
    ])
    httpSever = tornado.httpserver.HTTPServer(app)
    httpSever.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()