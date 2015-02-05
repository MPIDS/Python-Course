#===============================================================================
# File: BoltzmannPowerFit.py
# Language: Python 3
# Aims:
#	Create a control panel.
#	Plot the target Boltzmann curve.
#	Plot the fit.
#	Plot the first power Boltzmann curve.

#===============================================================================
# Figure

# Import modules
from matplotlib import *
from pylab import *	# Required for figure

# Create a figure
fig = figure("Curves", figsize = (4.5, 3), dpi = 72)

# Show the figure
plt.show()

#===============================================================================
# Define Fit class

# Import modules
import numpy as np
from scipy.optimize import curve_fit

# Start definition
class Fit:

	# Constructor
	def __init__(self):
		self.x0 = 0.0
		self.k = -10.0
		self.power = 1
		self.x = range(-100, 101)
		self.y = []
		self.y2 = []
		
	# Fit x, y to func with initial parameters in p
	def fit(self, x, y, p):
		# Fit curve
		popt, pcov = curve_fit(self.func, x, y, p0 = p)
		
		# Generate the fit curve
		self.x0 = popt[0]
		self.k = popt[1]
		self.y = self.func(self.x, self.x0, self.k)
		
		# Generate first power Boltzmann curve
		power = self.power
		self.power = 1
		self.y2 = self.func(self.x, self.x0, self.k)
		self.power = power
	
	# Target function
	def func(self, x, x0, k):
		return (1 / (1 + np.exp((x - x0) / k)))**self.power
		
# Instantiation
fit = Fit()

#===============================================================================
# Define Boltzmann class to hold the target curve
class Boltzmann:
	# Constructor
	def __init__(self, x0 = 0.0, k = -10.0):
		self.x0 = x0
		self.k = k
		self.x = range(-100, 101)
		self.y = []
		
	# Set x and y coordinates
	def set(self):
		# self.y = [self.func(i, self.x0, self.k) for i in self.x]
		self.y = [self.func(i, self.x0, self.k) for i in self.x]

	# Boltzmann function
	def func(self, x, x0, k):
		return 1.0 / (1.0 + np.exp((x - x0) / k))
		
# Instantiation
bm = Boltzmann()

#===============================================================================
# Import tkinter
from tkinter import *

#===============================================================================
# Define the ControlPanel class
class ControlPanel:
	# Constructor
	# master is the parent widget, which is the root widget here.
	def __init__(self, master):
		# Create a frame
		frameMain = Frame(master, width = 100, height = 100, padx = 5, pady = 5)
		frameMain.grid()
		rowNumber = 0
		
		#===================
		# Target Curve
		rowNumber += 1
		# Create a label
		Label(frameMain, text = "Target Curve").grid(row = rowNumber, 
														column = 1,
														columnspan = 2)

		#===================
		# Vhalf
		rowNumber += 1
		# Create a label
		Label(frameMain, text = "Vhalf").grid(row = rowNumber, column = 1)

		# Create a vhalf entry
		self.etyVhalf = Entry(frameMain)
		self.etyVhalf.insert(0, "0")
		self.etyVhalf.grid(row = rowNumber, column = 2)

		#===================
		# k
		rowNumber += 1
		# Create a label
		Label(frameMain, text = "k").grid(row = rowNumber, column = 1)

		# Create a k entry
		self.etyK = Entry(frameMain)
		self.etyK.insert(0, "-10")
		self.etyK.grid(row = rowNumber, column = 2)

		#===================
		# Boltzmann Curve
		rowNumber += 1
		# Create a label
		Label(frameMain, text = "Fit Curve: Boltzmann to the X power").grid(
			row = rowNumber, 
			column = 1,
			columnspan = 2)

		#=======================================================================
		# Power
		rowNumber += 2
		# Create a label
		Label(frameMain, text = "Power (X: 1~4)").grid(
			row = rowNumber, 
			column = 1)

		# Create a power entry
		self.etyPower = Entry(frameMain)
		self.etyPower.insert(0, "1")
		self.etyPower.grid(row = rowNumber, column = 2)

		#===================
		# Vhalf
		rowNumber += 1
		# Create a label
		Label(frameMain, text = "Vhalf").grid(row = rowNumber, column = 1)

		# Create a vhalf entry
		self.etyVhalf2 = Entry(frameMain)
		self.etyVhalf2.grid(row = rowNumber, column = 2)

		#===================
		# k
		rowNumber += 1
		# Create a label
		Label(frameMain, text = "k").grid(row = rowNumber, column = 1)

		# Create a k entry
		self.etyK2 = Entry(frameMain)
		self.etyK2.grid(row = rowNumber, column = 2)

		#===================
		# Plot
		rowNumber += 1
		# Create a plot button
		btnPlot = Button(frameMain, 
							text = "Plot",
							command = self.cbPlot,
							width = 5)
		btnPlot.grid(row = rowNumber, column = 1)

		#===================
		# Quit
		rowNumber += 1
		# Create a "Quit" button
		btnQuit = Button(frameMain, 
							text = "Quit",
							command = frameMain.quit,
							width = 5)
		btnQuit.grid(row = rowNumber, column = 1)

	# Methods
	def cbPlot(self):
		fig.clear()
		
		# x0
		x0 = float(self.etyVhalf.get())
		bm.x0 =  x0
		
		# k
		k = float(self.etyK.get())
		if(abs(k) < 1):
			if(k > 0):
				k = 1
			else:
				k = -1
			self.etyK.delete(0, END)
			self.etyK.insert(0, str(k))
		bm.k = k
		
		# Power
		power = int(self.etyPower.get())
		if(power < 1 or power > 4):
			power = 1
			self.etyPower.delete(0, END)
			self.etyPower.insert(0, str(power))
			print("Power is set to 1.")
			
		fit.power = power
		
		# Set x and y
		bm.set()
		
		# Fit
		fit.fit(bm.x, bm.y, [bm.x0, bm.k])
		
		# Plot
		plot(bm.x, bm.y, "b-", linewidth = 1)
		plot(fit.x, fit.y, "r--", linewidth = 2)
		plot(fit.x, fit.y2, "g:", linewidth = 2)
		axis([-100, 100, -0.1, 1.1])
		legend(["Target", "Fit", "Boltzmann"], loc = "best", frameon = False, 
				labelspacing = 0)
		
		# Update GUI
		self.etyVhalf2.delete(0, END)
		self.etyVhalf2.insert(0, str(fit.x0))
		self.etyK2.delete(0, END)
		self.etyK2.insert(0, str(fit.k))
		
		# Print information
		print("")
		print("=== Result ===")
		print("Power = ", fit.power)
		print("Vhalf = ", fit.x0)
		print("k = ", fit.k)
		print("")

		
#===============================================================================
# Create the root widget
rootWidget = Tk()
rootWidget.title("Curve Fitting")
rootWidget.geometry("+500+10")

#===============================================================================
# Instantiate App class
controlPanel = ControlPanel(rootWidget)

#===============================================================================
# Enter the event loop
rootWidget.mainloop()

#===============================================================================
