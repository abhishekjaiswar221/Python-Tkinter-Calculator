# import everything from tkinter module
from tkinter import *
from math import *


# globally declare the expression variable
expression = ""


# Function to update expression
# in the text entry box
def press(num):
	# point out the global expression variable
	global expression
	# concatenation of string
	expression = expression + str(num)
	# update the expression by using set method
	equation.set(expression)



# Function to evaluate the final expression
def equalpress():
	# Try and except statement is used
	# for handling the errors like zero
	# division error etc.
	# Put that code inside the try block
	# which may generate the error
	try:
		global expression
		# eval function evaluate the expression
		# and str function convert the result
		# into string
		total = str(eval(expression))
		equation.set(total)
		# initialize the expression variable
		# by empty string
		expression = ""
	# if error is generate then handle
	# by the except block
	except:
		equation.set(" error ")
		expression = ""


def squareroot():
	global expression
	sqrt = math.sqrt()
	equation.set("expression")
	expression = ""



# Function to delete the last entered
# number in the textbox
def backspace():
        global expression
        value = equation.get()
        if value:
                equation.set(value[:-1])
                expression = expression[:-1]
       

# Function to clear the contents
# of text entry box
def clear():
	global expression
	expression = ""
	equation.set("")


# Main code
if __name__ == "__main__":
	# create a GUI window
	gui = Tk()
	# set the background colour of GUI window
	gui.configure(background="ghostwhite")
	# set the title of GUI window
	gui.title("Calculator")
	# Set an icon for the calculator 
	gui.iconbitmap(r"C:\Users\abhis\OneDrive\Desktop\Abhishek D Jaiswar\Project\Own Projects\Python\Tkinter Calculator\favicon.ico")
	# set the configuration of GUI window
	gui.geometry("376x271")
	# StringVar() is the variable class
	# we create an instance of this class
	equation = StringVar()
	# create the text entry box for
	# showing the expression .
	expression_field = Entry(gui, font =('Times New Roman', 16, 'bold'), textvariable=equation, bd=5, insertwidth = 4, justify = 'left')
	# grid method is used for placing
	# the widgets at respective positions
	# in table like structure .
	expression_field.grid(columnspan=4, ipadx=70)
	# create a Buttons and place at a particular
	# when user press the button, the command or
	# function affiliated to that button is executed .

	
	#==========================================================================================
	#Row2
	#Use different name of  buttons than name of user defined button functions
	button1 = Button(gui, text=' 0 ', fg='black', bg='gray95', height=2, width=12,
                         command = gui.bind('0', lambda e:press(0)))
	button1.grid(row=2, column=0)

	decimal= Button(gui, text='.', fg='black', bg='gray95', height=2, width=12,
					command=gui.bind('.', lambda e:press('.')))
	decimal.grid(row=2, column=1)

	equal = Button(gui, text=' = ', fg='black', bg='gray95', height=2, width=12,
				command=gui.bind('=', lambda e:equalpress()))
	equal.grid(row=2, column=2)

	plus = Button(gui, text=' + ', fg='black', bg='gray95', height=2, width=12,
				command=gui.bind('+', lambda e:press('+')))
	plus.grid(row=2, column=3)

	#==========================================================================================
	#Row3

	button4 = Button(gui, text=' 7 ', fg='black', bg='gray95',  height=2, width=12,
					command=gui.bind('7', lambda e :press(7)))
	button4.grid(row=3, column=0)
	
	button3 = Button(gui, text=' 8 ', fg='black', bg='gray95', height=2, width=12,
					command = gui.bind('8', lambda e:press(8)))
	button3.grid(row=3, column=1)

	button2 = Button(gui, text=' 9 ', fg='black', bg='gray95', height=2, width=12,
					command = gui.bind('9', lambda e:press(9)))
	button2.grid(row=3, column=2)

	minus = Button(gui, text=' - ', fg='black', bg='gray95', height=2, width=12,
				command=gui.bind('-', lambda e:press('-')))
	minus.grid(row=3, column=3)

	#===========================================================================================
	#Row4
	button7 = Button(gui, text=' 4 ', fg='black', bg='gray95', height=2, width=12,
					command=gui.bind('4', lambda e:press(4)))
	button7.grid(row=4, column=0)
	
	button6 = Button(gui, text=' 5 ', fg='black', bg='gray95', height=2, width=12,
					command=gui.bind('5', lambda e:press(5)))
	button6.grid(row=4, column=1)
	
	button5 = Button(gui, text=' 6 ', fg='black', bg='gray95', height=2, width=12,
					command=gui.bind('6', lambda e:press(6)))
	button5.grid(row=4, column=2)

	multiply = Button(gui, text=' * ', fg='black', bg='gray95', height=2, width=12,
					command=gui.bind('*', lambda e:press('*')))
	multiply.grid(row=4, column=3)

	#============================================================================================
	#Row5

	button10 = Button(gui, text=' 1 ', fg='black', bg='gray95', height=2, width=12,
					command=gui.bind('1', lambda e :press(1)))
	button10.grid(row=5, column=0)

	button9 = Button(gui, text=' 2 ', fg='black', bg='gray95', height=2, width=12,
					command=gui.bind('2', lambda e:press(2)))
	button9.grid(row=5, column=1)

	button8 = Button(gui, text=' 3', fg='black', bg='gray95', height=2, width=12,
					command=gui.bind('3', lambda e:press(3)))
	button8.grid(row=5, column=2)
	
	divide = Button(gui, text=' / ', fg='black', bg='gray95', height=2, width=12,
					command=gui.bind('/', lambda e: press('/')))
	divide.grid(row=5, column=3)
	
	#==============================================================================================
	#Row6
	backspacebutton = Button(gui, text = 'Backspace', fg='black', bg='gray95', height=2, width=12,
                                 command=gui.bind('b', lambda e:backspace()))
	backspacebutton.grid(row=6, column=0)

	clearbutton = Button(gui, text='Clear', fg='black', bg='gray95', height=2, width=12,
                             command=gui.bind('c', lambda e:clear()))
	clearbutton.grid(row=6, column=1)

	brackets = Button(gui, text='√x', fg='black', bg='gray95', height=2, width=12,
                          command=gui.bind('s', lambda e:squareroot()))
	brackets.grid(row=6, column=2)

	modulo = Button(gui, text=' % ', fg='black', bg='gray95', height=2, width=12,
					command=gui.bind('%', lambda e:press('%')))
	modulo.grid(row=6, column=3)
        #================================================================================================
	
	# start the GUI
	gui.mainloop()
