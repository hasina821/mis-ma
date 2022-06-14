from tkinter import * 

root = Tk()
root.title("Simple calculator")

e=Entry(root,width=35,borderwidth=5,fg='black',bg="white")
e.grid(column=0,row=0,columnspan=3,padx=10,pady=10)

def Btn_Clicked(number):
     current = e.get()
     e.delete(0,END)
     e.insert(0,str(current) + str(number))
def Btn_del_cliked():
     e.delete(0,END)
def Btn_plus_clicked():
     first_number = e.get()
     global f_num
     f_num=int(first_number)
     e.delete(0,END)
def Btn_egal_clicked():
     second_number = e.get()
     e.delete(0,END)
     e.insert(0,int(second_number)+f_num)
     

btn_1=Button(root,borderwidth=5,text="1",fg='black',bg="white",padx=40,pady=20,command=lambda:Btn_Clicked(1))

btn_2=Button(root,borderwidth=5,text="2",fg='black',bg="white",padx=40,pady=20,command=lambda:Btn_Clicked(2))

btn_3=Button(root,borderwidth=5,text="3",fg='black',bg="white",padx=40,pady=20,command=lambda:Btn_Clicked(3))


btn_4=Button(root,borderwidth=5,text="4",fg='black',bg="white",padx=40,pady=20,command=lambda:Btn_Clicked(4))
btn_5=Button(root,borderwidth=5,text="5",fg='black',bg="white",padx=40,pady=20,command=lambda:Btn_Clicked(5))
btn_6=Button(root,borderwidth=5,text="6",fg='black',bg="white",padx=40,pady=20,command=lambda:Btn_Clicked(6))


btn_7=Button(root,borderwidth=5,text="7",fg='black',bg="white",padx=40,pady=20,command=lambda:Btn_Clicked(7))

btn_8=Button(root,borderwidth=5,text="8",fg='black',bg="white",padx=40,pady=20,command=lambda:Btn_Clicked(8))

btn_9=Button(root,borderwidth=5,text="9",fg='black',bg="white",padx=40,pady=20,command=lambda:Btn_Clicked(9))



btn_zero=Button(root,borderwidth=5,text="0",fg='black',bg="white",padx=40,pady=20,command=lambda:Btn_Clicked(0))

btn_effacer=Button(root,borderwidth=5,text="del",fg='black',bg="white",padx=89,pady=20,command=Btn_del_cliked)

btn_plus=Button(root,borderwidth=5,text="+",fg='black',bg="white",padx=39,pady=20,command=Btn_plus_clicked)

btn_egale=Button(root,borderwidth=5,text="=",fg='black',bg="white",padx=92,pady=20,command=Btn_egal_clicked)

btn_1.grid(column=0,row=3)
btn_2.grid(column=1,row=3)
btn_3.grid(column=2,row=3)
btn_4.grid(column=0,row=2)
btn_5.grid(column=1,row=2)
btn_6.grid(column=2,row=2)
btn_7.grid(column=0,row=1)
btn_8.grid(column=1,row=1)
btn_9.grid(column=2,row=1)
btn_zero.grid(column=0,row=4)
btn_effacer.grid(column=1,row=4,columnspan=2)
btn_plus.grid(column=0,row=5)
btn_egale.grid(column=1,row=5,columnspan=2)


root.mainloop()