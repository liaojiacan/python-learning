# -*- coding:utf-8 -*-
def application(environ,start_response):
    start_response("200 OK",[('Content-type',"text/html")])
    return [b'<h1>hello,world</h1>']
