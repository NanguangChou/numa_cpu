#coding:utf-8
import socket
from struct import unpack
from struct import pack

class socket_data():
	def __init__(self,ip="192.168.150.46",port=9876):
		self.s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.s.connect((ip,port))
		data      = pack("!L",1);
		event_num = pack("!L",60)
		type      = pack("!L",0)
		time      = pack("!L",1)
		recv=self.s.recv(4)
		self.s.send(data)
		self.s.send(time)
		self.s.send(data)
		self.s.send(event_num)
		self.s.send(data)
		self.s.send(data)
		self.s.send(type)
		self.s.recv(4)
	def recvive(self):
		a=unpack("!L",self.s.recv(4))
		b=unpack("!L",self.s.recv(4))
		return (a[0]<<30)+b[0]
	def __del__(self):
		self.s.close()
