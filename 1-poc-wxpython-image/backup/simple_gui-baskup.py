import wx
import wx.html2
import time
import locale

URL = "https://www.facebook.com"

class MyBrowser(wx.Frame):
    def __init__(self, *args, **kwds):
        wx.Frame.__init__(self, *args, **kwds)
        self.url = URL
        self.browser = wx.html2.WebView.New(self, -1, size=(900,600))
        self.browser.Bind(wx.html2.EVT_WEBVIEW_ERROR, self.on_webview_error)
        self.browser.Bind(wx.html2.EVT_WEBVIEW_LOADED, self.on_webview_load)
        self.retries = 0
        self.max_retries = 10

    def OnInit(self):
        busy = wx.BusyInfo("Loading plese wait...")
        # locale.setlocale
      

    def on_webview_error(self, evt):
        self.URL = evt.GetURL()
        print(self.URL)
        self.retries += 1
        if self.retries > self.max_retries: # Give up
            self.Destroy()
        print("Error {} of {} attempts to load {}, trying again in 3 seconds.".format(self.retries,self.max_retries,self.URL))
        if self.retries > 5: # Try alternate
            self.URL = "http://wxPython.org"
            print("Swapping to alternate Url "+self.URL)
        self.browser.Destroy()

        

        self.browser = wx.html2.WebView.New(self, -1, size=(900,600))
        self.browser.Bind(wx.html2.EVT_WEBVIEW_ERROR, self.on_webview_error)
        self.browser.Bind(wx.html2.EVT_WEBVIEW_LOADED, self.on_webview_load)
        time.sleep(3)
        self.browser.LoadURL(self.URL)
        time.sleep(3)
        self.browser.ReLoadURL()

    def on_webview_load(self, evt):
        print(self.url, "Load complete")

if __name__ == '__main__':
  app = wx.App()
  wx.Locale(wx.LANGUAGE_GERMAN)
  dialog = MyBrowser(None, -1)
  dialog.browser.LoadURL(URL)
  dialog.Show()
  app.MainLoop()