#hello.py
def application(environ,start_response):
	start_response('200 OK',[('Content-type','text/html')])
	return "<h1>Hello,sb %s</h1>" %(environ['PATH_INFO'][1:] or 'sb') + environ['SERVER_PORT']