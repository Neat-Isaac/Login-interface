import tkinter as tk
import tkinter.messagebox as box
ID = None
PASSWORD = None
class MyError(Exception):
    def __init__(self,msg):
        self.msg = msg
        
def snare(file,id2,ps2):
    global ID,PASSWORD
    file.write(str(id2.get("0.0","end")) + "\n")
    file.write(str(ps2.get("0.0","end")) + "\n")
    box.showinfo("Info","login was successful")
    file.close()
    ID = int(id2.get("0.0","end"))
    PASSWORD = int(ps2.get("0.0","end"))
    
def kick(id1,data,password):
    global ID,PASSWORD
    if int(id1.get("0.0","end")) in data.keys():
        for i,j in data.items():
            if int(id1.get("0.0","end")) == i:
                if int(password.get("0.0","end")) == j:
                    box.showinfo("Info","Welcome," + str(id1.get("0.0","end")))
                    ID = int(id1.get("0.0","end"))
                    PASSWORD = int(password.get("0.0","end"))
                else:
                    box.showerror("Error","Wrong password")
    else:
        a = box.askyesno("Choose","You enter a wrong ID.Do you want to logon?")
        if a:
            file = open("data.neat","a")
            f = tk.Tk()
            f.title("logon")
            f.geometry("250x100")
            id2 = tk.Text(f,width = 20,height = 1)
            id2.pack()
            ps2 = tk.Text(f,width = 20,height = 1)
            ps2.pack()
            ba = tk.Label(f,text = "ID")
            bb = tk.Label(f,text = "Password")
            bc = tk.Button(f,text = "logon",command = lambda :snare(file,id2,ps2))
            ba.place(x = 5,y = 5)
            bb.place(x = 5,y = 30)
            id2.place(x = 70,y = 5)
            ps2.place(x = 70,y = 30)
            bc.place(x = 100,y = 60)
        else:
            box.showinfo("Ok","Ok")
def login():
    file = open("data.neat","r")
    lst = file.readlines()
    lst2 = []
    for i in range(len(lst) - 1):
        if lst[i]  != '\n':
            lst2.append(int(lst[i]))
    data = dict(zip(lst2[::2],lst2[1::2]))
    file.close()
    form = tk.Tk()
    form.title("login")
    form.geometry("250x100")
    a = tk.Label(form,text = "ID")
    ide = tk.Text(form,width = 20,height = 1)
    ide.pack()
    b = tk.Label(form,text = "Password")
    b.pack()
    password = tk.Text(form,width = 20,height = 1)
    c = tk.Button(form,text = "login",command = lambda :kick(ide,data,password))
    d = tk.Button(form,text = "exit",command = exit)
    a.place(x = 5,y = 5)
    b.place(x = 5,y = 30)
    ide.place(x = 70,y = 5)
    password.place(x = 70,y = 30)
    c.place(x = 50,y = 60)
    d.place(x = 150,y = 60)
    form.mainloop()
