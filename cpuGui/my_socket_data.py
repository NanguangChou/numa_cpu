#coding:utf-8
import socket
from struct import unpack
from struct import pack
from pdb import set_trace
from numpy import zeros
class socket_data():
	def __init__(self,ip="192.168.150.46",port=9873):
		self.s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.s.connect((ip,port))
		number    = 2
		event_num = pack("!L",number)
		data      = pack("!L",1 ) #usr和os的值都是1
		cpuid     = pack("!L",1 )
		evt       = pack("!L",60)
		type      = pack("!L",0 )
		time      = pack("!L",1 )
		recv=self.s.recv(4)
		#
		#set_trace() #断点调试工具
		#
		self.s.send(event_num)
		self.s.send(time)
		
		for i in range(number):
			cpu = pack("!L",i)
			self.s.send(cpu)
			self.s.send(evt)
			self.s.send(data) #usr
			self.s.send(data) #os
			self.s.send(type)

		'''
		self.s.send(data)
		self.s.send(evt )
		self.s.send(data)
		self.s.send(data)
		self.s.send(type)

		self.s.send(cpuid)
		self.s.send(evt )
		self.s.send(data)
		self.s.send(data)
		self.s.send(type)
		'''
		self.s.recv(4)
	def recvive(self):
		a=unpack("!L",self.s.recv(4))
		b=unpack("!L",self.s.recv(4))
		return (a[0]<<30)+b[0]
	def __del__(self):
		self.s.close()

if __name__=="__main__":
	socket_test = socket_data()
	temp = zeros(2)
	while 1:
		for i in range(2):
			temp[i] = socket_test.recvive()
			print temp[i]