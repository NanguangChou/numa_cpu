# -*- coding: utf-8 -*-
# Source:wxPython in action PDF P44
# Source:wxPython Demo->Cone windows Controls->SplitterWindow
# xwPython P249 上也有关地 SplitterWindow 的相关例子# 2010-04-20 中国广州天河
# 显示如果添加工具栏、菜单栏、及状态栏,使用分割窗口
# 使用 SplitterWindow 最大缺点是当你在 SplitterWindow 上继续旋转 Panel等控件时.
# 控件大少不会随着窗口的大小调整!import wx
# 这句跟书本上的例子是不同的
# See:http://www.manning-sandbox.com/thread.jspa?messageID=78899
import wx
from wx.lib import pydocview as images 
class ToolbarFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,"one base example",size=(300,200))
        statusBar=self.CreateStatusBar()
        
        splitter = wx.SplitterWindow(self, -1, style=wx.SP_LIVE_UPDATE)
        sty = wx.BORDER_SUNKEN
        p1 = wx.Window(splitter, style=sty)
        p1.SetBackgroundColour("pink")
        wx.StaticText(p1, -1, "Panel One", (5,5))
        p2 = wx.Window(splitter, style=sty)
        p2.SetBackgroundColour("sky blue")
        wx.StaticText(p2, -1, "Panel Two", (5,5))        
        splitter.SetMinimumPaneSize(20)
        splitter.SplitVertically(p1, p2, -100)
class MySplitter(wx.SplitterWindow):
    def __init__(self, parent, ID, log):
        wx.SplitterWindow.__init__(self, parent, ID,
                                   style = wx.SP_LIVE_UPDATE
                                   )
app = wx.PySimpleApp()
frame=ToolbarFrame(parent=None,id=-1)
frame.Show(True)
app.MainLoop()


"""
toolbar=self.CreateToolBar()
        toolbar.AddSimpleTool(wx.NewId(),images.New.GetBitmap(),'New',"Long help for 'New'")
        toolbar.Realize()
        menuBar= wx.MenuBar()
        menu1=wx.Menu()
        menuBar.Append(menu1,"&File")
        menu2=wx.Menu()
        menu2.Append(wx.NewId(),"&Copy","Show status")
        menu2.Append(wx.NewId(),"C&ut","")
        menu2.Append(wx.NewId(),"Paste","")
        menu2.AppendSeparator()
        menu2.Append(wx.NewId(),"&Options","Display Options")
        menuBar.Append(menu2,"&Edit")     
        
        self.SetMenuBar(menuBar)        # 创建分割窗口   
"""