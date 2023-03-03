#calculator
from tkinter import *

window = Tk()
window.title("Calculator")

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)
    
def btn_clear():
    global expression
    expression = ""
    input_text.set("")

def btn_equal():
    global expression
    total = str(eval(expression))
 
    input_text.set(total)
 
    expression = ""
    expression = ""

expression = ""
input_text = StringVar()

input_frame = Frame(window, bd = 0, highlightbackground = "black", highlightcolor = "black")
input_frame.pack(side = TOP)

input_field = Entry(input_frame, font = ('arial', 10, 'bold'), textvariable = input_text, width = 50, bg = '#eee', bd = 0)
input_field.pack(ipady = 10)

btns_frame = Frame(window, bg = 'grey')
btns_frame.pack()


clear = Button(btns_frame, text = "C", fg = 'red', bg = 'black', command = btn_clear).grid(row=4,column=1)
bt9 = Button(btns_frame, text = "9", fg = 'red', bg = 'black', command = lambda:btn_click(9), height=1, width=7).grid(row=1, column=2)
bt8 = Button(btns_frame, text = "8", fg = 'red', bg = 'black', command = lambda:btn_click(8), height=1, width=7).grid(row=1, column=1)
bt7 = Button(btns_frame, text = "7", fg = 'red', bg = 'black', command = lambda:btn_click(7), height=1, width=7).grid(row=1, column=0)
bt6 = Button(btns_frame, text = "6", fg = 'red', bg = 'black', command = lambda:btn_click(6), height=1, width=7).grid(row=2, column=2)
bt5 = Button(btns_frame, text = "5", fg = 'red', bg = 'black', command = lambda:btn_click(5), height=1, width=7).grid(row=2, column=1)
bt4 = Button(btns_frame, text = "4", fg = 'red', bg = 'black', command = lambda:btn_click(4), height=1, width=7).grid(row=2, column=0)
bt3 = Button(btns_frame, text = "3", fg = 'red', bg = 'black', command = lambda:btn_click(3), height=1, width=7).grid(row=3, column=2)
bt2 = Button(btns_frame, text = "2", fg = 'red', bg = 'black', command = lambda:btn_click(2), height=1, width=7).grid(row=3, column=1)
bt1 = Button(btns_frame, text = "1", fg = 'red', bg = 'black', command = lambda:btn_click(1), height=1, width=7).grid(row=3, column=0)
bt0 = Button(btns_frame, text = '0', fg = 'red', bg = 'black', command = lambda:btn_click(0), height=1, width=7).grid(row=4, column=0)
bte = Button(btns_frame, text = "=", fg = 'red', bg = 'black', command = lambda:btn_equal(), height=1, width=7).grid(row=4, column=2)
btadd = Button(btns_frame, text = '+', fg = 'red', bg = 'black', command = lambda:btn_click('+'), height=1, width=7).grid(row=1, column=3)
btsub = Button(btns_frame, text = '-', fg = 'red', bg = 'black', command = lambda:btn_click('-'), height=1, width=7).grid(row=2, column=3)
btmul = Button(btns_frame, text = '*', fg = 'red', bg = 'black', command = lambda:btn_click('*'), height=1, width=7).grid(row=3, column=3)
btdiv = Button(btns_frame, text = '/', fg = 'red', bg = 'black', command = lambda:btn_click('/'), height=1, width=7).grid(row=4, column=3)
btdec = Button(btns_frame, text = '.', fg = 'red', bg = 'black', command = lambda:btn_click('.'), height=1, width=7).grid(row=5, column=0)
