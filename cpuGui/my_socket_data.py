#coding:utf-8
import socket
from struct import unpack
from struct import pack
from pdb import set_trace
from numpy import zeros
class socket_data():
	def __init__(self,ip="192.168.150.46",port=9876,type=0):
		self.s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.s.connect((ip,port))
		if type == 0:
			number    = 8
			event_num = pack("!L",number)
			data      = pack("!L",1 ) #usr和os的值都是1
			evt       = pack("!L",60)
			type      = pack("!L",type )
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
		elif type == 2:
			number    = 4
			event_num = pack("!L",number)
			data      = pack("!L",1 ) #usr和os的值都是1
			evt_r     = pack("!L",1836)
			evt_w     = pack("!L",1839)
			type      = pack("!L",type )
			time      = pack("!L",1 )
			recv=self.s.recv(4)
			#
			#set_trace() #断点调试工具
			#

			self.s.send(event_num)
			self.s.send(time)
			cpu_1     = pack("!L",0)
			cpu_2     = pack("!L",15)
			self.s.send(cpu_1)
			self.s.send(evt_r)
			self.s.send(data)#usr
			self.s.send(data)#os
			self.s.send(type)
			self.s.send(cpu_1)
			self.s.send(evt_w)
			self.s.send(data)#usr
			self.s.send(data)#os
			self.s.send(type)
			
			self.s.send(cpu_2)
			self.s.send(evt_r)
			self.s.send(data)#usr
			self.s.send(data)#os
			self.s.send(type)
			self.s.send(cpu_2)
			self.s.send(evt_w)
			self.s.send(data)#usr
			self.s.send(data)#os
			self.s.send(type)
			

		self.s.recv(4)
	def recvive(self):
		a=unpack("!L",self.s.recv(4))
		b=unpack("!L",self.s.recv(4))
		return (a[0]<<30)+b[0]
	def __del__(self):
		self.s.close()

###################
###测试用#########
##################
if __name__=="__main__":
	socket_test = socket_data(type=2)
	temp = zeros(2)
	while 1:
		for i in range(2):
			temp[i] = socket_test.recvive()
			print temp[i]