
import wx  
      
class Border(wx.Frame):  
    def __init__(self, parent, id, title):  
        wx.Frame.__init__(self, parent, id, title, size=(250, 200))  
      
        panel = wx.Panel(self, -1,size=(250,200))  
        panel.SetBackgroundColour('white')  
        boxsizer1 = wx.BoxSizer(wx.VERTICAL)  
              
        btn1 = wx.Button(panel, -1, 'Botton1')     
              
        btn2 = wx.Button(panel, -1, 'Botton2')     
              
        btn3 = wx.Button(panel, -1, 'Botton3')  
              
        boxsizer1.Add(btn1, proportion=-1, flag=wx.ALL, border=1)  
        boxsizer1.Add(btn2, proportion=-1, flag=wx.ALL, border=0)  
        boxsizer1.Add(btn3, proportion=-1, flag=wx.ALL, border=0)  
              
        self.SetSizer(boxsizer1)  
              
        self.Centre()  
        self.Show(True)  
      
app = wx.App()  
Border(None, -1, '')  
app.MainLoop()  
