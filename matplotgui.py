'''
Shows a matplotlib graph in a frame with y = a + bx + cx^2 + dx^3 in range (-1,1).
A,B,C, and D are pre-defined for now.

'''

import wx
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigCanvas

import numpy as np
 
a = float(0)
b = float(0)
c = float(0)
d = float(0)
 
class MyFrame(wx.Frame):
 def __init__(self, *args, **kwds):
	kwds["style"] = wx.DEFAULT_FRAME_STYLE
	wx.Frame.__init__(self, *args, **kwds)
	self.SetTitle("wx plot")
	self.__do_layout()
	self.draw_figure()    
   
 def __do_layout(self):
	sizer = wx.BoxSizer(wx.VERTICAL)
	self.SetSizer(sizer)

	# Create matplotlib figure
	self.fig = Figure(figsize=(5.0, 4.0), dpi=100)
	self.canvas = FigCanvas(self, -1, self.fig)
	self.ax = self.fig.add_subplot(111)
	
	# Set event when plot is clicked
   	self.canvas.mpl_connect('pick_event', self.on_pick)
	# Add figure
	sizer.Add(self.canvas, 1, wx.EXPAND)

	self.btn1 = wx.Button(self, -1, 'Graph')
	self.Bind(wx.EVT_BUTTON, self.draw_figure1, self.btn1)
		
	self.textbox1 = wx.TextCtrl(self, size=(1,-1), style=wx.TE_PROCESS_ENTER)
	self.Bind(wx.EVT_TEXT, self.draw_figure1, self.textbox1)
	
	self.textbox2 = wx.TextCtrl(self, size=(1,-1), style=wx.TE_PROCESS_ENTER)
	self.Bind(wx.EVT_TEXT, self.draw_figure1, self.textbox2)
	
	self.textbox3 = wx.TextCtrl(self, size=(1,-1), style=wx.TE_PROCESS_ENTER)
	self.Bind(wx.EVT_TEXT, self.draw_figure1, self.textbox3)
	
	self.textbox4 = wx.TextCtrl(self, size=(1,-1), style=wx.TE_PROCESS_ENTER)
	self.Bind(wx.EVT_TEXT, self.draw_figure1, self.textbox4)
	
	box = wx.BoxSizer(wx.HORIZONTAL)
	box.Add(self.btn1, 0 )
	box.Add(self.textbox1, 1)
	box.Add(self.textbox2, 1)
	box.Add(self.textbox3, 1)
	box.Add(self.textbox4, 1)

	sizer.Add(box,0, wx.EXPAND)
	self.Centre()
	sizer.Fit(self)
	self.Layout()

 def draw_figure1(self, event):
	global a
	global b
	global c
	global d
	try:
		if not(self.textbox1.IsEmpty()):
			a = float(self.textbox1.GetValue())
		else:
			a = float(self.textbox1.SetValue('0'))
		if not(self.textbox2.IsEmpty()):	
			b = float(self.textbox2.GetValue())
		else:
			b = float(self.textbox2.SetValue('0'))
		if not(self.textbox3.IsEmpty()):	
			c = float(self.textbox3.GetValue())
		else:
			c = float(self.textbox3.SetValue('0'))
		if not(self.textbox4.IsEmpty()):	
			d = float(self.textbox4.GetValue())
		else:
			d = float(self.textbox4.SetValue('0'))
	except ValueError:
		wx.MessageBox("Invalid input. Must be floating point numbers","Error",
                    wx.OK|wx.ICON_EXCLAMATION)
		return
	self.draw_figure()
	
 def draw_figure(self):
	self.ax.clear()
	x = np.arange(0,1,0.001)
	y = my_formula(x)
	i = 0
	print 'Line being graphed: ',a, '+',b,'x+',c,'x^2+',d,'x^3'
	print 'Every 100th plot of the line:'
	while i<len(x):
		print i, ':', x[i], ',', y[i]
		i = i + 100
	self.ax.plot(x,y,picker=5)
	self.canvas.draw()
 def on_pick(self, event):
	print 'hello world'

# end of class MyFrame
def my_formula(x):
	return a+b*x+c*x**2+d*x**3
 
if __name__ == "__main__":
 app = wx.PySimpleApp(0)
 frame = MyFrame(None, -1, "")
 app.SetTopWindow(frame)
 frame.Show()
 app.MainLoop()
