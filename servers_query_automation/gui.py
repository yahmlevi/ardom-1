import wx
import wx.lib.mixins.listctrl as listmix

class TestListCtrl(wx.ListCtrl, listmix.CheckListCtrlMixin, listmix.ListCtrlAutoWidthMixin):
    def __init__(self, *args, **kwargs):
        wx.ListCtrl.__init__(self, *args, **kwargs)
        listmix.CheckListCtrlMixin.__init__(self)
        listmix.ListCtrlAutoWidthMixin.__init__(self)

    def OnCheckItem(self, index, flag):
        print(index, flag)

class MainWindow(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        self.panel = wx.Panel(self)
        self.list = TestListCtrl(self.panel, style=wx.LC_REPORT)
        self.list.InsertColumn(0, "")
        self.list.InsertColumn(1, "Query Description")
        self.list.Arrange()
        for i in range(1, 6):
            self.list.Append(["", "%d query" % (i)])        
        self.button = wx.Button(self.panel, label="Submit")
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.list, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)
        self.sizer.Add(self.button, flag=wx.EXPAND | wx.ALL, border=5)
        self.panel.SetSizerAndFit(self.sizer)
        self.Show()

app = wx.App(False)
win = MainWindow(None)
app.MainLoop()