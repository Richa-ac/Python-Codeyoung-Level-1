from tkinter import *
root=Tk()
root.configure(bg='light green')
root.geometry('400x250')
root.title('Compound Intrest Calculator')
def clear_all():
    principle_field.delete(0,END)
    rate_field.delete(0,END)
    time_field.delete(0,END)
    compound_field.delete(0,END)

def calculate_ci():
    principle=int(principle_field.get())
    rate=int(rate_field.get())
    time=int(time_field.get())
    CI= principle* (pow((1+rate/100),time))
    compound_field.insert(10,CI)

label1=Label(root,text='Principle Amount',fg='black',bg='red')
label2=Label(root,text='Rate',fg='black',bg='red')
label3=Label(root,text='Time',fg='black',bg='red')
label4=Label(root,text='Compound Intrest',fg='black',bg='red')

label1.grid(row=1,column=0)
label2.grid(row=2,column=0)
label3.grid(row=3,column=0)
label4.grid(row=5,column=0)

principle_field=Entry(root,fg='white',bg='black')
rate_field=Entry(root,fg='white',bg='black')
time_field=Entry(root,fg='white',bg='black')
compound_field=Entry(root,fg='white',bg='black')

principle_field.grid(row = 1, column = 1) 
rate_field.grid(row = 2, column = 1) 
time_field.grid(row = 3, column = 1 )
compound_field.grid(row = 5, column = 1)

button1=Button(root,text='Submit',bg='red',fg='black',command=calculate_ci)
button2 = Button(root, text = "Clear", bg = "red", fg = "black", command = clear_all)

button1.grid(row = 4, column = 1,)
button2.grid(row = 6, column = 1,)
root.mainloop()
 
               



