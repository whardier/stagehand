
#!/usr/bin/env python
import os
import wx

app = wx.App(False)


menuBar = wx.MenuBar()
file_menu = wx.Menu()
app.SetMacExitMenuItemId(wx.ID_EXIT)
exit_item = file_menu.Append(wx.ID_EXIT, "E&xit\tCtrl-Q", "Exit NodeMCU PyFlasher")
menuBar.Append(file_menu, "&File")

scale = dir(app.GetTopWindow())

frame = wx.Frame(None, wx.ID_ANY, "stagehand")

frame.SetIcon(wx.Icon("../resource/icon-app.ico"))
frame.Show(True)

frame.SetMenuBar(menuBar)

print('hi')

app.MainLoop()