from tkinter import *

root = Tk()

root.wm_title("BMI Calculator")

def Choice():
	# Metric
	if var.get() == 1:
		weightlabel.config(text = "Enter your weight in kilograms")
		heightlabel.config(text = "Enter your height in meters")
	# Imperial
	elif var.get() == 2:
		weightlabel.config(text = "Enter your weight in pounds")
		heightlabel.config(text = "Enter your height in inches")
	else:
		weightlabel.config(text = "Error")
		heightlabel.config(text = "Error")

def Calc():
	# Metric
	if var.get() == 1:
		return float(weightvar.get()) / float(heightvar.get()) ** 2
	elif var.get() == 2:
		return (float(weightvar.get()) * 703) / float(heightvar.get()) ** 2
	else:
		return "Error"

def Scale(bmi):
	if bmi < 18.5:
		return "Underweight"
	elif bmi < 24.9 and bmi > 18.5:
		return "Normal"
	elif bmi < 29.9 and bmi > 25.0:
		return "Overweight"
	elif bmi > 30:
		return "Obese"
	else:
		return "Error"

def PrintAns():
	anslabel.config(text = Calc())
	scalelabel.config(text = Scale(Calc()))

# Create canvas
HEIGHT = 700
WIDTH = 800

canvas = Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

# Create the frames
f1 = Frame(root, bg = "#0099ff", bd = 5)
f1.place(relx = 0.07, rely = 0.07, relwidth = 0.25, relheight = 0.6)

f2 = Frame(root, bg = "#0099ff", bd = 5)
f2.place(relx = 0.4, rely = 0.07, relwidth = 0.525, relheight = 0.6)

f3 = Frame(root, bg = "#0099ff", bd = 5)
f3.place(relx = 0.07, rely = 0.74, relwidth = 0.86, relheight = 0.19)

# Create items inside of frame one
syslabel = Label(f1, text = "System of measurement:", bg = "#0099ff", font = 80)
syslabel.place(relx = 0.025, rely = 0.05)

var = IntVar()
syschoice = Radiobutton(f1, text = "Metric", variable = var, value = 1, bg = "#0099ff", font = 80, activebackground = "#0099ff", command = Choice)
syschoice.place(relx = 0, rely = 0.2, relwidth = 1, relheight = 0.25)

syschoice = Radiobutton(f1, text = "Imperial", variable = var, value = 2, bg = "#0099ff", font = 80, activebackground = "#0099ff", command = Choice)
syschoice.place(relx = 0, rely = 0.55, relwidth = 1, relheight = 0.25)

# Create stuff inside of frame two
heightvar = StringVar()
weightvar = StringVar()

weightlabel = Label(f2, font = 80, bg = "#0099ff")
weightlabel.place(relx = 0.25, rely = 0.05)

weightentry = Entry(f2, font = 80, bg = "grey", textvariable = weightvar)
weightentry.place(relx = 0.25, rely = 0.125)


heightlabel = Label(f2, font = 80, bg = "#0099ff")
heightlabel.place(relx = 0.25, rely = 0.35)

heightentry = Entry(f2, font = 80, bg = "grey", textvariable = heightvar)
heightentry.place(relx = 0.25, rely = 0.425)


dimenbutton = Button(f2, text = "Submit", font = 80, bg = "grey", command = PrintAns)
dimenbutton.place(relx = 0.375, rely = 0.7)

# Create stuff inside of frame three
anslabel = Label(f3, font = 80, bg = "#0099ff")
anslabel.place(relx = 0.4, rely = 0.3)

scalelabel = Label(f3, font = 80, bg = "#0099ff")
scalelabel.place(relx = 0.43, rely = 0.6)

root.mainloop()
