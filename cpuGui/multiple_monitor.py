# -*- coding: utf-8 -*-

from my_socket_data import socket_data
import wx

import numpy as np

import matplotlib

import time
# matplotlib采用WXAgg为后台,将matplotlib嵌入wxPython中
matplotlib.use("WXAgg")

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wxagg import NavigationToolbar2WxAgg as NavigationToolbar
from matplotlib.ticker import MultipleLocator, FuncFormatter

import pylab
from matplotlib import pyplot

import math

POINTS        = 100  
CPU_NUMBER    = 8
LOG_FREQUENCE = math.log(2.4*1024*1024*1024,2)
FREQUENCE     = 2.4*1024*1024*1024
from pdb import set_trace
######################################################################################

class MPL_Panel_base(wx.Panel):
    ''' #MPL_Panel_base面板,可以继承或者创建实例'''
    def __init__(self,parent):
        wx.Panel.__init__(self,parent=parent, id=-1)

        self.Figure = matplotlib.figure.Figure(figsize=(4,3))
        self.axes = self.Figure.add_axes([0.1,0.1,0.8,0.8])
        self.FigureCanvas = FigureCanvas(self,-1,self.Figure)
        
        self.NavigationToolbar = NavigationToolbar(self.FigureCanvas)

        self.StaticText = wx.StaticText(self,-1,label='Show Help String')

        self.SubBoxSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.SubBoxSizer.Add(self.NavigationToolbar,proportion =0, border = 2,flag = wx.ALL | wx.EXPAND)
        self.SubBoxSizer.Add(self.StaticText,proportion =-1, border = 2,flag = wx.ALL | wx.EXPAND)

        self.TopBoxSizer = wx.BoxSizer(wx.VERTICAL)
        self.TopBoxSizer.Add(self.SubBoxSizer, proportion = -1, border = 2,flag = wx.ALL | wx.EXPAND)
        self.TopBoxSizer.Add(self.FigureCanvas,proportion =-10, border = 2,flag = wx.ALL | wx.EXPAND)

        self.SetSizer(self.TopBoxSizer)

        ###方便调用
        self.pylab=pylab
        self.pl=pylab
        self.pyplot=pyplot
        self.numpy=np
        self.np=np
        self.plt=pyplot
        
        self.bg = self.FigureCanvas.copy_from_bbox(self.axes.bbox)
        #self.xticker()
        #self.axes.set_autoscale_on(True)
        
        self.xlim(0,POINTS)
        self.ylim(0,100)

    def UpdatePlot(self):
        '''#修改图形的任何属性后都必须使用self.UpdatePlot()更新GUI界面 '''
        self.grid(True)

        self.xlim(0,POINTS)
        self.ylim(0,100)
        self.FigureCanvas.draw()


    def plot(self,*args,**kwargs):
        '''#最常用的绘图命令plot '''
        self.axes.plot(*args,**kwargs)
        self.UpdatePlot()


    def semilogx(self,*args,**kwargs):
        ''' #对数坐标绘图命令 '''
        self.axes.semilogx(*args,**kwargs)
        self.UpdatePlot()

    def semilogy(self,*args,**kwargs):
        ''' #对数坐标绘图命令 '''
        self.axes.semilogy(*args,**kwargs)
        self.UpdatePlot()

    def loglog(self,*args,**kwargs):
        ''' #对数坐标绘图命令 '''
        self.axes.loglog(*args,**kwargs)
        self.UpdatePlot()


    def grid(self,flag=True):
        ''' ##显示网格  '''
        if flag:
            self.axes.grid()
        else:
            self.axes.grid(False)


    def title_MPL(self,TitleString="wxMatPlotLib Example In wxPython"):
        ''' # 给图像添加一个标题   '''
        self.axes.set_title(TitleString)


    def xlabel(self,XabelString="X"):
        ''' # Add xlabel to the plotting    '''
        self.axes.set_xlabel(XabelString)


    def ylabel(self,YabelString="Y"):
        ''' # Add ylabel to the plotting '''
        self.axes.set_ylabel(YabelString)


    def xticker(self,major_ticker=5,minor_ticker=5):
        ''' # 设置X轴的刻度大小 '''
        self.axes.xaxis.set_major_locator( MultipleLocator(major_ticker) )
        self.axes.xaxis.set_minor_locator( MultipleLocator(minor_ticker) )


    def yticker(self,major_ticker=5,minor_ticker=5):
        ''' # 设置Y轴的刻度大小 '''
        self.axes.yaxis.set_major_locator( MultipleLocator(major_ticker) )
        self.axes.yaxis.set_minor_locator( MultipleLocator(minor_ticker) )


    def legend(self,*args,**kwargs):
        ''' #图例legend for the plotting  '''
        self.axes.legend(*args,**kwargs)


    def xlim(self,x_min,x_max):
        ''' # 设置x轴的显示范围  '''
        self.axes.set_xlim(x_min,x_max)


    def ylim(self,y_min,y_max):
        ''' # 设置y轴的显示范围   '''
        self.axes.set_ylim(y_min,y_max)


    def savefig(self,*args,**kwargs):
        ''' #保存图形到文件 '''
        self.Figure.savefig(*args,**kwargs)


    def cla(self):
        ''' # 再次画图前,必须调用该命令清空原来的图形  '''
        self.axes.clear()
        #self.Figure.set_canvas(self.FigureCanvas)
        #self.UpdatePlot()
        
    def ShowHelpString(self,HelpString="Show Help String"):
        ''' #可以用它来显示一些帮助信息,如鼠标位置等 '''
        self.StaticText.SetLabel(HelpString)

###############################################################################
#  MPL_Frame添加了MPL_Panel的1个实例
###############################################################################
class MPL_Frame(wx.Frame):
    """MPL_Frame可以继承,并可修改,或者直接使用"""
    def __init__(self,title="Numa CPU Monitor",size=(1300,760)):
        wx.Frame.__init__(self,parent=None,title = title,size=size)

        self.BoxSizer=wx.BoxSizer(wx.HORIZONTAL)
        
        #####对象表属性测试
        '''self.MPL_ALL=[]
        for num in range(CPU_NUMBER):
            self.MPL_ALL += [MPL_Panel_base(self)]
        self.BoxSizerHorizon = []
        self.BoxSizerFigure = wx.BoxSizer(wx.VERTICAL)

        box_row = int( math.ceil( math.sqrt( CPU_NUMBER ) ) )
        box_col = int(math.sqrt(CPU_NUMBER))
        for n in range(box_row):
            self.BoxSizerHorizon += [wx.BoxSizer(wx.HORIZONTAL)]
            for j in range(box_col):
                if n*box_col+j <= CPU_NUMBER:
                    self.BoxSizerHorizon[n].Add(self.MPL_ALL[n*box_col+j], proportion = -1, border = 2, flag = wx.ALL | wx.EXPAND)
                    print n*box_col+j
                    #print len(self.BoxSizerHorizon)
            self.BoxSizerFigure.Add(self.BoxSizerHorizon[n])
            
        for n in range(len(self.BoxSizerHorizon)):
            for j in range(box_col):
                if n*box_col +j <= CPU_NUMBER:
                    self.BoxSizerHorizon[n].Add(self.MPL_ALL[n*box_col+j], proportion = -1, border = 2, flag = wx.ALL | wx.EXPAND)
            self.BoxSizerFigure.Add(self.BoxSizerHorizon[n])        

        '''
        self.draw_8_axes()
        
        #创建FlexGridSizer
        self.FlexGridSizer=wx.FlexGridSizer( rows=9, cols=1, vgap=5,hgap=5)
        self.FlexGridSizer.SetFlexibleDirection(wx.BOTH)

        self.RightPanel = wx.Panel(self,-1)

        #测试按钮1
        self.Button1 = wx.Button(self.RightPanel,-1,"TestButton",size=(100,40),pos=(10,10))
        self.Button1.Bind(wx.EVT_BUTTON,self.Button1Event)

        #测试按钮2
        self.Button2 = wx.Button(self.RightPanel,-1,"CloseButton",size=(100,40),pos=(10,10))
        self.Button2.Bind(wx.EVT_BUTTON,self.Button2Event)

        self.ip_text   = wx.StaticText(self.RightPanel,-1,"Ip Server:",size=(100,-1))
        self.ip_ctl    = wx.TextCtrl(self.RightPanel,-1,"192.168.150.46",size=(100,-1))
        self.port_text = wx.StaticText(self.RightPanel,-1,"Server Port",size=(100,-1))
        self.port_ctl  = wx.TextCtrl(self.RightPanel,-1,"9876",size=(100,-1))
        
        #加入Sizer中
        self.FlexGridSizer.Add(self.Button1, proportion =   0, border = 5,flag = wx.ALL | wx.EXPAND)
        self.FlexGridSizer.Add(self.Button2, proportion =   0, border = 5,flag = wx.ALL | wx.EXPAND)

        self.FlexGridSizer.Add(self.ip_text,   proportion = 0, border = 5,flag = wx.ALL | wx.EXPAND)
        self.FlexGridSizer.Add(self.ip_ctl,    proportion = 0, border = 5,flag = wx.ALL | wx.EXPAND)
        self.FlexGridSizer.Add(self.port_text, proportion = 0, border = 5,flag = wx.ALL | wx.EXPAND)
        self.FlexGridSizer.Add(self.port_ctl,  proportion = 0, border = 5,flag = wx.ALL | wx.EXPAND)

        
        #self.BoxSizer.Add(self.BoxSizerFigure,proportion = -1, border = 2,flag = wx.ALL | wx.EXPAND)
        self.BoxSizer.Add(self.BoxSizer_hh, proportion = -1, border = 2,flag = wx.ALL | wx.EXPAND)
        self.BoxSizer.Add(self.RightPanel,  proportion =  0, border = 2,flag = wx.ALL | wx.EXPAND)
        
        self.SetSizer(self.BoxSizer)
        self.RightPanel.SetSizer(self.FlexGridSizer)	

        #连接判断
        self.start_button_click = False
        self.stop_button_click  = False

        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER,self.draw_canvas,self.timer)
        #状态栏
        self.StatusBar()

        #MPL_Frame界面居中显示
        self.Centre(wx.BOTH)  

    #按钮事件,用于测试
    def Button1Event(self,event):
        #socket获取服务器数据
        #
        if not self.start_button_click:
            self.socket_data=socket_data(ip=self.ip_ctl.GetValue(),port=int(self.port_ctl.GetValue()))
            #if self.socket_data <0:
            #    return -1
            self.start_button_click = True
            self.timer.Start(100)

            #print self.t_1
        #清理初始化每个MPL对象
        #self.MPL1.cla()#必须清理图形,才能显示下一幅图
        self.y=[None]*CPU_NUMBER
        for i in range(CPU_NUMBER):
            self.y[i] = [None] * POINTS
        #print self.y
        #self.l_user_1,=self.MPL1.axes.plot(range(POINTS),self.y1)
        #self.MPL1.UpdatePlot()
        #while self.start_button_click:
            #self.MPL.cla()
            
            
            #time.sleep(1)
            #self.MPL.UpdatePlot()#必须刷新才能显示

    def draw_canvas(self,evt):
        #self.MPL.FigureCanvas.restore_region(self.MPL.bg)
        #print "ok"
        #clear canvas
        self.MPL1.cla()
        self.MPL2.cla()
        self.MPL3.cla()
        self.MPL4.cla()
        self.MPL5.cla()
        self.MPL6.cla()
        self.MPL7.cla()
        self.MPL8.cla()
        '''
        self.MPL9.cla()
        self.MPL10.cla()
        self.MPL11.cla()
        self.MPL12.cla()
        self.MPL13.cla()
        self.MPL14.cla()
        self.MPL15.cla()
        self.MPL16.cla()
        '''

        temp=[None]*CPU_NUMBER
        for i in range(CPU_NUMBER):
            #temp[i]=math.log(self.socket_data.recvive(),2)/LOG_FREQUENCE*100
            temp[i] = (self.socket_data.recvive())/FREQUENCE*100
        #print temp
        for j in range(CPU_NUMBER):
            self.y[j]=self.y[j][1:]+[temp[j]]
            print self.y[j]
            #set_trace()
        #self.y[i] = self.y[1:] +[temp]
        self.MPL1.plot(range(POINTS),self.y[0])
        self.MPL2.plot(range(POINTS),self.y[1])
        self.MPL3.plot(range(POINTS),self.y[2])
        self.MPL4.plot(range(POINTS),self.y[3])
        self.MPL5.plot(range(POINTS),self.y[4])
        self.MPL6.plot(range(POINTS),self.y[5])
        self.MPL7.plot(range(POINTS),self.y[6])
        self.MPL8.plot(range(POINTS),self.y[7])

        '''
        self.MPL9.plot(range(POINTS),self.y[9])
        self.MPL10.plot(range(POINTS),self.y[10])
        self.MPL11.plot(range(POINTS),self.y[11])
        self.MPL12.plot(range(POINTS),self.y[12])
        self.MPL13.plot(range(POINTS),self.y[13])
        self.MPL14.plot(range(POINTS),self.y[14])
        self.MPL15.plot(range(POINTS),self.y[15])
        self.MPL16.plot(range(POINTS),self.y[16])
        '''
        #self.l_user.set_ydata(self.y)
        #self.l_user,=self.MPL.axes.plot(range(POINTS),self.y,"--^g")
        #self.MPL.axes.draw_artist(self.l_user)
        #self.MPL.UpdatePlot()
        #self.MPL.FigureCanvas.blit(self.MPL.axes.bbox)

    def Button2Event(self,event):
        self.socket_data.__del__()
        self.timer.Stop()
        self.start_button_click=False
        self.AboutDialog()


    #打开文件,用于测试
    def DoOpenFile(self):
        wildcard = r"Data files (*.dat)|*.dat|Text files (*.txt)|*.txt|ALL Files (*.*)|*.*"
        open_dlg = wx.FileDialog(self,message='Choose a file',wildcard = wildcard, style=wx.OPEN|wx.CHANGE_DIR)
        if open_dlg.ShowModal() == wx.ID_OK:
            path=open_dlg.GetPath()
            try:
                file = open(path, 'r')
                text = file.read()
                file.close()
            except IOError, error:
                dlg = wx.MessageDialog(self, 'Error opening file\n' + str(error))
                dlg.ShowModal()

        open_dlg.Destroy()



    #自动创建状态栏
    def StatusBar(self):
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetFieldsCount(3)
        self.statusbar.SetStatusWidths([-2, -2, -1])


    #About对话框
    def AboutDialog(self):
        dlg = wx.MessageDialog(self, '\tPackages Used, Stop Ok', wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    #生成8个监控图像
    def draw_8_axes(self):
        self.MPL1 = MPL_Panel_base(self)
        self.MPL2 = MPL_Panel_base(self)
        self.MPL3 = MPL_Panel_base(self)
        self.MPL4 = MPL_Panel_base(self)
        self.MPL5 = MPL_Panel_base(self)
        self.MPL6 = MPL_Panel_base(self)
        self.MPL7 = MPL_Panel_base(self)
        self.MPL8 = MPL_Panel_base(self)
        self.BoxSizer1 = wx.BoxSizer( wx.HORIZONTAL )
        self.BoxSizer2 = wx.BoxSizer( wx.HORIZONTAL )
        self.BoxSizer_hh = wx.BoxSizer( wx.VERTICAL )
        self.BoxSizer1.Add(self.MPL1  ,proportion = -1, border = 2, flag = wx.ALL|wx.EXPAND)
        self.BoxSizer1.Add(self.MPL2  ,proportion = -1, border = 2, flag = wx.ALL|wx.EXPAND)
        self.BoxSizer1.Add(self.MPL3  ,proportion = -1, border = 2, flag = wx.ALL|wx.EXPAND)
        self.BoxSizer1.Add(self.MPL4  ,proportion = -1, border = 2, flag = wx.ALL|wx.EXPAND)
        self.BoxSizer2.Add(self.MPL5  ,proportion = -1, border = 2, flag = wx.ALL|wx.EXPAND)
        self.BoxSizer2.Add(self.MPL6  ,proportion = -1, border = 2, flag = wx.ALL|wx.EXPAND)
        self.BoxSizer2.Add(self.MPL7  ,proportion = -1, border = 2, flag = wx.ALL|wx.EXPAND)
        self.BoxSizer2.Add(self.MPL8  ,proportion = -1, border = 2, flag = wx.ALL|wx.EXPAND)
        self.BoxSizer_hh.Add(self.BoxSizer1, proportion = -1, border = 2, flag = wx.ALL|wx.EXPAND)
        self.BoxSizer_hh.Add(self.BoxSizer2, proportion = -1, border = 2, flag = wx.ALL| wx.EXPAND)

########################################################################

#主程序测试
if __name__ == '__main__':
    app = wx.PySimpleApp()
    #frame = MPL2_Frame()
    frame =MPL_Frame()
    frame.Center()
    frame.Show()
    app.MainLoop()
