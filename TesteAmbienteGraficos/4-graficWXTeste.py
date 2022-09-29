import wx

app = wx.App(redirect=True)
top = wx.Frame(None, title="Teste de Aplicação gráfica com WX", size=(800,600))
top.Show()
app.MainLoop()