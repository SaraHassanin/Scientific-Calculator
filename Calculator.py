from tkinter import *
import math
def push(value):
    act=entrybox.get()
    ans=' '
    try:
        if value=='x²':
            ans=eval(act)**2
        elif value=='x³':
            ans=eval(act)**3
        elif value=='xʸ':
            entrybox.insert(END,'**')
            return
        elif value=='deg':
            ans=math.degrees(eval(act))
        elif value=='rad':
            ans=math.radians(eval(act))
        elif value =='AC':
            act=act[0:len(act)-1]
            entrybox.delete(0,END)
            entrybox.insert(0,act)
        elif value=='Del':
            entrybox.delete(0,END)
        elif value=='e':
            ans=math.e
        elif value=='+':
            entrybox.insert(END,'+')
            return
        elif value=='sin':
            ans=math.sin(math.radians(eval(act)))
        elif value=="(":
            entrybox.insert(END,'(')
            return
        elif value==")":
            entrybox.insert(END,')')
            return
        elif value=='√':
            ans=math.sqrt(eval(act))
        elif value=='-':
            entrybox.insert(END,'-')
            return
        elif value=='cos':
            ans=math.cos(math.radians(eval(act)))
        elif value=='*':
            entrybox.insert(END,'*')
            return
        elif value=='tan':
            ans=math.tan(math.radians(eval(act)))
        elif value=='/':
            entrybox.insert(END,'/')
            return
        elif value=='log':
            ans=math.log(eval(act))
        elif value=='%':
            entrybox.insert(END,'%')
            return
        elif value=='ln':
            ans=math.log2(eval(act))
        elif value=='=':
            ans=eval(act)
        elif value=='•':
            entrybox.insert(END,'.')
            return
        elif value=='¶':
            ans=math.pi
        elif value=='X!':
            ans=math.factorial(eval(act))
        else:
            entrybox.insert(END,value)
            return
        if value!="AC":
             entrybox.delete(0,END)
        entrybox.insert(0,ans)
    except SyntaxError:
        entrybox.insert(END,'Error')
window=Tk()
window.title("calculator")
window.config(bg='black')
screen_width=window.winfo_screenwidth()
screen_hight=window.winfo_screenheight()
middel_width=screen_width//2 - 400//2
middel_hight=screen_hight//2 - 300
window.geometry(f"390x470+{middel_width}+{middel_hight}")


entrybox=Entry(window,justify=LEFT,font=('Agency FB',20,'bold')
               ,width=30,bg='black',fg='white',bd=15,relief=SUNKEN)
entrybox.grid(row=0,column=0,columnspan=5)
entrybox.focus()
buttontext=['x²','x³','xʸ','rad','deg',
            'Del','AC','e','+','sin',
            '(',')','√','-','cos',
            '7','8','9','*','tan',
            '6','5','4','/','log',
            '1','2','3','%','ln',
            '=','0','•','¶','X!']
var=0
num=['0','1','2','3','4','5','6','7','8','9']
colv=0
rowv=1
for var in buttontext:
    if var in num:
        bu = Button(window,bg="white",fg='darkred' ,text=var, bd=5, width=3, height=1, font=('arial', 15, 'bold'),
                    relief=SUNKEN, activebackground='green',command=lambda bu=var: push(bu))
        bu.grid(row=rowv, column=colv, pady=5)
        colv += 1
    else:
        bu=Button(window,text=var,bg='cyan',fg='darkred',bd=5,width=3,height=1,font=('arial',15,'bold'),
                 relief=SUNKEN,activebackground='green',command=lambda bu=var:push(bu))
        bu.grid(row=rowv,column=colv,pady=5)
        colv+=1
    if colv>4:
        rowv+=1
        colv=0
window.mainloop()