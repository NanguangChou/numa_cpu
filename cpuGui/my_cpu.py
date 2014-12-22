#-*-coding:utf-8 -*-
import wx  
from matplotlib.figure import Figure  
import matplotlib.font_manager as font_manager  
import numpy as np  
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas  
from my_socket_data import socket_data
import math
# wxWidgets object ID for the timer  
TIMER_ID = wx.NewId()  
# number of data points  
POINTS = 300  
LOG_FREQUENCE = math.log(2.4*1024*1024*1024)

class PlotFigure(wx.Frame):
    def __init__(self,data):
        wx.Frame.__init__(self, None, wx.ID_ANY, title="CPU Usage Monitor", size=(600, 400))
        # Matplotlib Figur
        self.fig = Figure((6, 4), 100)
        self.canvas = FigureCanvas(self, wx.ID_ANY, self.fig)
        # add a subplot  
        self.ax = self.fig.add_subplot(111)
        self.data=data;
        self.ax.set_ylim([0,100])
        self.ax.set_xlim([0, POINTS])
        
        self.ax.set_autoscale_on(False)
        self.ax.set_xticks([])
        self.ax.set_yticks(range(0,100, 5))


        # disable autoscale, since we don't want the Axes to ad  
        # draw a grid (it will be only for Y)  
        self.ax.grid(True)  
        # generates first "empty" plots  
        self.user = [None] * POINTS  
        self.l_user,=self.ax.plot(range(POINTS),self.user,label=u'CPU percentage')  
    
        # add the legend  
        self.ax.legend(loc='upper center',  
                           ncol=4,  
                           prop=font_manager.FontProperties(size=10))  
        self.canvas.draw()  
        self.bg = self.canvas.copy_from_bbox(self.ax.bbox)  
        wx.EVT_TIMER(self, TIMER_ID, self.onTimer)  
        self.Bind(wx.EVT_CLOSE,self.frame_close,self)
      
    def onTimer(self, evt):  
        self.canvas.restore_region(self.bg)
        temp = (math.log(self.data.recvive())/LOG_FREQUENCE)*100
        #temp =np.random.randint(60,80)  

        self.user = self.user[1:] + [temp]  
            # update the plot  
        self.l_user.set_ydata(self.user)  
            # just draw the "animated" objects  
        self.ax.draw_artist(self.l_user)# It is used to efficiently update Axes data (axis ticks, labels, etc are not updated)  
        self.canvas.blit(self.ax.bbox) 
        #print self.data.recvive()
    
    def frame_close(self,event):
        self.Show(False)

    def __del__(self):
        exit()


class ButtonFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,title="Cpu Usage Monitor",size=(300,200))
        panel = wx.Panel(self,-1)
        self.button = wx.Button(panel,-1,"Start")
        self.Bind(wx.EVT_BUTTON,self.OnClick,self.button)
        self.button.SetDefault()
        #Ip和端口输入窗口
        self.Ip =wx.StaticText(panel,-1,"IP:")
        self.IpText=wx.TextCtrl(panel,-1,"192.168.150.46",size=(100,-1))
        self.IpText.SetInsertionPoint(0)
        self.Port=wx.StaticText(panel,-1,"Port:")
        self.PortText=wx.TextCtrl(panel,-1,"9876",size=(100,-1))
        ##
        sizer=wx.FlexGridSizer(cols=2,hgap=6,vgap=6)
        sizer.AddMany([self.Ip,self.IpText,self.Port,self.PortText,self.button])
        panel.SetSizer(sizer)
        self.button_record=False
        #self.Bind(EVT_CLOSE,frame_close,self)
        ##

    def OnClick(self,event):
        self.button_record = not self.button_record
        if self.button_record:
            self.button.SetLabel("Stop")
            app=wx.PySimpleApp()
            data1=socket_data(ip=self.IpText.GetValue(),port=int(self.PortText.GetValue(),10))
            frame=PlotFigure(data=data1)
            t = wx.Timer(frame,TIMER_ID)  
            t.Start(50)
            frame.Show()
            app.MainLoop()
        else:
            self.button.SetLabel("Start")
            #TIMER_ID=wx.NewId()
            ##
    def frame_close(self,event):
        self.Destroy()

    def __del__(self):
        exit()

if __name__ == '__main__':
    app2 = wx.PySimpleApp() 
    button = ButtonFrame()
    button.Show()
    app2.MainLoop()  
