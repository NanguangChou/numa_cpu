#coding=utf-8
import wx
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
import matplotlib.font_manager as font_manager
import numpy as nu

TIMER_ID = wx.NewId()
POINTS = 300

class PlotFigure(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self,None,-1,"Cpu Status Monitor",size=(800,600))
		#button和label都建立在Panel上
		panel         = wx.Panel(self,-1) 
		#初始化label.输入框.按钮
		self.IPLabel       = wx.StaticText(panel,-1,"IP Address:")
		self.IPText        = wx.TextCtrl(panel,-1,"192.168.150.46",size=(100,-1))
		self.portLabel     = wx.StaticText(panel,-1,"Port:",)
		self.portText      = wx.TextCtrl(panel,-1,"9876",size=(100,-1))
		self.button        = wx.Button(panel,-1,"Start")
		self.button_record = False
		#初始化sizer对象
		sizer              = wx.FlexGridSizer(cols=5,hgap=6,vgap=6)
		sizer.AddMany([self.IPLabel,self.IPText,self.portLabel,self.portText,self.button])
		panel.SetSizer(sizer)
		#事件绑定
		self.Bind(wx.EVT_BUTTON,self.OnClick,self.button)
		#初始化canvas
		
		self.fig    = Figure((8,6),100)
		self.canvas = FigureCanvas(self,-1,self.fig)
		self.ax     = self.fig.add_subplot(221)
		self.ax.set_ylim([0,100])
		self.ax.set_xlim([0,POINTS])
		self.ax.set_autoscale_on(True)
		self.ax.set_xticks([])
		self.ax.set_yticks(range(0,101,10))
		self.ax.grid(True)
		self.user   = [None] * POINTS
		self.l_user,=self.ax.plot(range(POINTS),self.user,label="User %")
		self.ax.legend(loc='upper center',
							ncol=4,
							prop=font_manager.FontProperties(size=10))
		self.canvas.draw()
		self.bg     = self.canvas.copy_from_bbox(self.ax.bbox)
		
	def OnClick(self,event):
		exit()

if __name__=='__main__':
	app=wx.PySimpleApp()
	frame=PlotFigure()
	frame.Show()
	app.MainLoop()


