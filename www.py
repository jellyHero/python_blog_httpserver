#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:Shelly
# time:2017-08-23

from  BaseHTTPServer import HTTPServer,BaseHTTPRequestHandler

class ServerHTTP(BaseHTTPRequestHandler):

	host = 'http://167.88.178.51:8888'
	server_root = '/var/www'
	white_list = ['html','js']
	index_header = '''
	<!DOCTYPE html>
	<html>
	<head>
	<style>
	#header {
    	background-color:black;
    	color:white;
    	text-align:center;
    	padding:5px;
	}
	#nav {
    	line-height:30px;
    	background-color:#eeeeee;
    	height:300px;
    	width:100px;
    	float:left;
    	padding:5px;	      
	}
	#section {
    	width:350px;
    	float:left;
    	padding:10px;	 	 
	}
	#footer {
    	background-color:black;
    	color:white;
    	clear:both;
    	text-align:center;
   	padding:5px;	 	 
	}
	</style>
	</head>
	<body>
	<div id="header">
	<h1>韩飞的博客</h1>
	</div>
	'''
	index_nav = "<div id='nav'><a href="+host+"/hacker/index.html>黑客是画家</a><br/><a href="+host+"/hobby/index.html>经济的智慧</a><br/><a href="+host+"/economy/index.html>最爱张国荣</a><br/></div>"
	index_section = '''
	<div id="section">
	<h2>韩飞想要：</h2>
	<p>
	嗨，我是韩飞。一个学过经济学、喜爱张国荣、名不见经传的黑客。我的博客里会分享一些黑客知识、发表一些经济见解、还会有一些乱七八糟的个人爱好或者广告。总之，这是个纯粹的个人网站！
	</p>
	<h2>你可以获取到：</h2>
	<p>
	或许你可以从其中的某篇文章获益匪浅。因为毕竟是个人网站，内容至上！
	</p>
	</div>
	'''
	index_footer= '''
	<div id="footer">
	你以目光感受   浪漫宁静宇宙
	</div>
	</body>
	</html>
	'''
	index_html =  index_header + index_nav + index_section + index_footer

	def creat_wfile(self):
		if self.path == '/':
			#print '==2=='
			data = self.index_html
			#print '==2=='
		else:
			try:
				if self.path.split('.')[-1] not in self.white_list:
					data = self.index_html
				else:
					#print '==3=='
					data = open(self.server_root+self.path,'rb').read()
					#print data
					#print '==3=='
			except:
				#print '==4=='
				data = self.index_html
				#print '==4=='
		self.send_response(200)
		self.send_header('Content-type','text/html; charset=utf-8')
		self.send_header('Content-Length',str(len(data)))
		self.end_headers()
		self.wfile.write(data)

	def do_GET(self):
		self.creat_wfile()

	def do_POST(self):
		self.do_GET()

def start_server(port):
	http_server = HTTPServer(('', int(port)),ServerHTTP)
	http_server.serve_forever() 

if __name__ == "__main__":
    start_server(8888)