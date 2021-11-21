from tkinter import *
root=Tk()
root.title("CALCUALTOR!")
root.geometry("490x200")
root.config(bg="light blue")

operator=""
text_input=StringVar()

text_display=Entry(root,font=("arial",20,"bold"),textvariable=text_input,bd=4,insertwidth=4,justify="right").grid(columnspan=4)

def click(numbers):
  global operator
  operator+=str(numbers)
  text_input.set(operator)

def clear():
  global operator
  operator=""
  text_input.set("")

def equals():
  global operator
  sumup=str(eval(operator))
  text_input.set(sumup)
  operator=""

b1=Button(root,padx=4,pady=4,bd=8,fg="black",font=("arial",20,"bold"),bg="cadet blue",text="1",command=lambda:click(1)).grid(row=3,column=0)

b2=Button(root,padx=4,pady=4,bd=8,fg="black",font=("arial",20,"bold"),bg="cadet blue",text="2",command=lambda:click(2)).grid(row=3,column=1)

b3=Button(root,padx=4,pady=4,bd=8,fg="black",font=("arial",20,"bold"),bg="cadet blue",text="3",command=lambda:click(3)).grid(row=3,column=2)

b4=Button(root,padx=4,pady=4,bd=8,fg="black",font=("arial",20,"bold"),bg="cadet blue",text="4",command=lambda:click(4)).grid(row=2,column=0)

b5=Button(root,padx=4,pady=4,bd=8,fg="black",font=("arial",20,"bold"),bg="cadet blue",text="5",command=lambda:click(5)).grid(row=2,column=1)

b6=Button(root,padx=4,pady=4,bd=8,fg="black",font=("arial",20,"bold"),bg="cadet blue",text="6",command=lambda:click(6)).grid(row=2,column=2)

b7=Button(root,padx=4,pady=4,bd=8,fg="black",font=("arial",20,"bold"),bg="cadet blue",text="7",command=lambda:click(7)).grid(row=1,column=0)

b8=Button(root,padx=4,pady=4,bd=8,fg="black",font=("arial",20,"bold"),bg="cadet blue",text="8",command=lambda:click(8)).grid(row=1,column=1)

b9=Button(root,padx=4,pady=4,bd=8,fg="black",font=("arial",20,"bold"),bg="cadet blue",text="9",command=lambda:click(9)).grid(row=1,column=2)

b0=Button(root,padx=4,pady=4,bd=8,fg="black",font=("arial",20,"bold"),bg="cadet blue",text="0",command=lambda:click(0)).grid(row=1,column=3)

b10=Button(root,padx=4,pady=4,bd=8,fg="black",font=("arial",20,"bold"),bg="cadet blue",text="+",command=lambda:click("+")).grid(row=1,column=4)

b11=Button(root,padx=4,pady=4,bd=8,fg="black",font=("arial",20,"bold"),bg="cadet blue",text="-",command=lambda:click("-")).grid(row=2,column=4)

b12=Button(root,padx=4,pady=4,bd=8,fg="black",font=("arial",20,"bold"),bg="cadet blue",text="*",command=lambda:click("")).grid(row=3,column=4)

b13=Button(root,padx=4,pady=4,bd=8,fg="black",font=("arial",20,"bold"),bg="cadet blue",text="/",command=lambda:click("/")).grid(row=2,column=3)

b14=Button(root,padx=4,pady=4,bd=8,fg="black",font=("arial",20,"bold"),bg="cadet blue",text="%",command=lambda:click("%")).grid(row=3,column=3)

b15=Button(root,padx=4,pady=4,bd=8,fg="black",font=("arial",20,"bold"),bg="cadet blue",text="CL",command=lambda:clear()).grid()

b16=Button(root,padx=4,pady=4,bd=8,fg="black",font=("arial",20,"bold"),bg="cadet blue",text="=",command=lambda:equals()).grid(row=2,column=5)

root.mainloop()
