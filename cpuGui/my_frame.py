#Boa:Frame:Frame1

import wx
import wx.gizmos
from matplotlib.backends import backend_wxagg
from matplotlib.figure import Figure

class my_window(wx.SplitterWindow):
    def __init(self):
        wx.SplitterWindow(self, id=None)
        self.panel=backend_wxagg.FigureCanvasWxAgg(self,-1,Figure())
        axes=self.panel.figure.gca()
        axes.cla()
        axes.plot([1,2,3],[1,2,3])
        self.panel.draw()
        
def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BUTTON1, wxID_FRAME1PANEL1, 
 wxID_FRAME1SPLITTERWINDOW1, wxID_FRAME1SPLITTERWINDOW2, 
 wxID_FRAME1STATICLINE1, wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT2, 
 wxID_FRAME1TEXTCTRL1, wxID_FRAME1TEXTCTRL2, 
] = [wx.NewId() for _init_ctrls in range(10)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(0, 0), size=wx.Size(1091, 800),
              style=wx.DEFAULT_FRAME_STYLE, title='Frame1')
        self.SetClientSize(wx.Size(1075, 761))

        self.splitterWindow1 = wx.SplitterWindow(id=wxID_FRAME1SPLITTERWINDOW1,
              name='splitterWindow1', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(128, 760), style=wx.SP_3D)

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1',
              parent=self.splitterWindow1, pos=wx.Point(0, 0), size=wx.Size(128,
              760), style=wx.TAB_TRAVERSAL)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label=u'IP Server Address', name='staticText1',
              parent=self.panel1, pos=wx.Point(16, 16), size=wx.Size(97, 14),
              style=1)

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL1, name='textCtrl1',
              parent=self.panel1, pos=wx.Point(16, 48), size=wx.Size(100, 22),
              style=1, value=u'192.168.150.46')

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label=u'Port', name='staticText2', parent=self.panel1,
              pos=wx.Point(16, 96), size=wx.Size(23, 14), style=0)

        self.textCtrl2 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL2, name='textCtrl2',
              parent=self.panel1, pos=wx.Point(16, 120), size=wx.Size(100, 22),
              style=0, value=u'9876')

        self.button1 = wx.Button(id=wxID_FRAME1BUTTON1, label='button1',
              name='button1', parent=self.panel1, pos=wx.Point(24, 328),
              size=wx.Size(75, 24), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_FRAME1BUTTON1)

        self.staticLine1 = wx.StaticLine(id=wxID_FRAME1STATICLINE1,
              name='staticLine1', parent=self.panel1, pos=wx.Point(129, 0),
              size=wx.Size(1, 752), style=0)

        self.splitterWindow2 = my_window(id=wxID_FRAME1SPLITTERWINDOW2,
              name='splitterWindow2', parent=self, pos=wx.Point(128, 0),
              size=wx.Size(944, 760), style=wx.SP_3D)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnButton1Button(self, event):
        event.Skip()
