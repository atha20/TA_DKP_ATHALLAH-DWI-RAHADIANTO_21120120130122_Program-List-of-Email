from tkinter import *
from tkinter import messagebox


objects = []
screen = Tk()
screen.withdraw()
screen.title('List of Email')

class main_screen(object):

    attempts = 0

    def __init__(self, master):
        top = self.top = Toplevel(master)
        top.title('Input Password')
        top.geometry("250x100")
        top.resizable(width=False, height=False)
        self.l = Label(top, text=" Keyword: ", font=('Times New Roman', 14, 'bold'), justify=CENTER)
        self.l.pack()
        self.e = Entry(top, show='*', width=30)
        self.e.pack(pady=7)
        self.b = Button(top, text='Submit', command=self.verify, font=('Times New Roman', 14))
        self.b.pack()

    def verify(self):
        self.value = self.e.get()
        access = 'a'

        if self.value == access:
            self.top.destroy()
            screen.deiconify()

        else:
            self.attempts += 1
            if self.attempts == 5:
               screen.quit()
            self.e .delete(0, 'end')
            messagebox.showerror('Incorrect Password', 'Incorrect password, attempts remaining: ' + str(5 - self.attempts))


class object_add:

    def __init__(self, master, n, p, e):
        self.password = p
        self.name = n
        self.email = e
        self.screen = master

    def write(self):
        f = open('emails.txt', "a")
        n = self.name
        e = self.email
        p = self.password

        n_write = n + " "
        e_write = e + " "
        p_write = p + " "

        f.write(n_write + ',' + e_write + ',' + p_write + ', \n')
        f.close()


class object_display:

    def __init__(self, master, n, e, p, i):
        self.password = p
        self.name = n
        self.email = e
        self.screen = master
        self.i = i

        self.label_name = Label(self.screen, text=n, font=('Times New Roman', 14))
        self.label_email = Label(self.screen, text=e, font=('Times New Roman', 14))
        self.label_pass = Label(self.screen, text=p, font=('Times New Roman', 14))

    def display(self):
        self.label_name.grid(row=7 + self.i, sticky=W)
        self.label_email.grid(row=7 + self.i, column=1, sticky=W)
        self.label_pass.grid(row=7 + self.i, column=2, sticky=W)
        
    def delete(self):
        answer = messagebox.askquestion('Delete Confirmation', 'Are you sure you want to delete all entry?')

        if answer == 'yes':
            for i in objects:
                i.destroy()

            f = open('emails.txt', 'r')
            lines = f.readlines()
            f.close()

            f = open('emails.txt', 'w')
            count = 0

            f.close()
            readfile()

    def destroy(self):
        self.label_name.destroy()
        self.label_email.destroy()
        self.label_pass.destroy()


def to_add():
    m = email.get()
    p = password.get()
    n = name.get()
    e = object_add(screen, n, p, m)
    
    if m == '':
        messagebox.showerror('Error', 'Need to be added')
    
    elif p == '':
        messagebox.showerror('Error', 'Need to be added')

    elif n == '':
        messagebox.showerror('Error', 'Need to be added')

    else :
        e.write()
        name.delete(0, 'end')
        email.delete(0, 'end')
        password.delete(0, 'end')
        messagebox.showinfo('Added Object', 'Successfully Added \n' + 'Name: ' + n + '\nEmail: ' + m + '\nPassword: ' + p)
        readfile()

def to_delete():
    d = object_display(screen, 'n', 'e', 'p', 'i')
    d.delete()
    readfile()

def readfile():
    f = open('emails.txt', "r")
    count = 0

    for line in f:
        objectList = line.split(',')
        e = object_display(screen, objectList[0], objectList[1], objectList[2], count)
        objects.append(e)
        e.display()
        count += 1
    f.close()


m = main_screen(screen)

title_label = Label(screen, text='Add Email', font=('Times New Roman', 16, 'bold'))
name_label = Label(screen, text='Name:', font=('Times New Roman', 14))
email_label = Label(screen, text='Email:', font=('Times New Roman', 14))
pass_label = Label(screen, text='Password:', font=('Times New Roman', 14))
name = Entry(screen, font=('Times New Roman', 14))
email = Entry(screen, font=('Times New Roman', 14))
password = Entry(screen, show='*', font=('Times New Roman', 14))
submit = Button(screen, text='Add', command=to_add, width=7, font=('Times New Roman', 14))
delete = Button(screen, text='Delete', fg='red', command=to_delete, width=7, font=('Times New Roman', 14))

title_label.grid(columnspan=3, row=0)
name_label.grid(row=1, sticky=E, padx=3)
email_label.grid(row=2, sticky=E, padx=3)
pass_label.grid(row=3, sticky=E, padx=3)

name.grid(columnspan=3, row=1, column=1, padx=2, pady=2, sticky=W)
email.grid(columnspan=3, row=2, column=1, padx=2, pady=2, sticky=W)
password.grid(columnspan=3, row=3, column=1, padx=2, pady=2, sticky=W)

submit.grid(columnspan=3, pady=4)
delete.grid(columnspan=3, pady=4)

name_label2 = Label(screen, text='Name:', font=('Times New Roman', 14))
email_label2 = Label(screen, text='Email:', font=('Times New Roman', 14))
pass_label2 = Label(screen, text='Password:', font=('Times New Roman', 14))

name_label2.grid(row=6, sticky=W)
email_label2.grid(row=6, column=1, sticky=W)
pass_label2.grid(row=6, column=2, sticky=W)

readfile()

screen.mainloop()

