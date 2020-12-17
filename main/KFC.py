import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
import cam
import cv2
import facerec3
import requests




store_name = "KFC"

class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack frames on top of each other, then the one we want visible will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, Scan, Setting):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Face Wallet KFC",fg="black", font=("controller.title_font", 50, "bold italic"))
#        label.config(font=)
        label.pack(side="top", fill="x", padx=50, pady=50)
        
        button1 = tk.Button(self, text="Scan",bg = '#DC143C', fg ='black',
                            command=lambda: controller.show_frame("Scan"))
        # button2 = tk.Button(self, text="Manual",
        #                     #command=lambda: topLevel(controller, "controller"))
        #                     #command=lambda: controller.show_frame("Controller"))
        #                     command=lambda: check_session(controller, "Controller"))
#         button3 = tk.Button(self, text="Register",
# #                            command=lambda: controller.show_frame("Register"))
#                             command=lambda: check_session(controller, "Register"))

        button1.config(font="System, 20")
        button1.pack(pady=10)
        # button2.config(font="System, 20")
        # button2.pack(pady=10)
        # button3.config(font="System, 20")
        # button3.pack(pady=10)

def topLevel(controller, frame):
    top=tk.Toplevel()
    top.title("Password")
    passwordentry = tk.Entry(top,show="*")
    passwordentry.pack()
    passwordentry.config(width="30")
    button2 = tk.Button(top, text="Submit",
                        command=lambda: check_password(top, controller,frame, passwordentry.get()))
    button2.config(font="System, 30")
    button2.pack()

def check_password(top, controller,frame, password):
    if password == '123456':
#    if requests.post('http://'+url+':5000/login', data={'password':password}).text == 'True':
        top.destroy()
        print('Password Correct')
        return controller.show_frame(frame)
    return False


def check_session(controller,frame):
    #if requests.get('http://'+url+':5000/login').text == 'True':
    #controller.show_frame(frame)

#    else:
    topLevel(controller,frame)

class Scan(tk.Frame):
    global store_name
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Scan", font=("controller.title_font", 50, "bold italic"))
        label.pack(side="top", fill="x", padx=50, pady=50)
        button = tk.Button(self, text="Scan",
                           command=lambda: facerec3.facerec(store_name))
        button2 = tk.Button(self, text="Back to Home",
                           command=lambda: controller.show_frame("StartPage"))
        button.config(font="System, 30")
        button.pack()
        button2.config(font="System, 30")
        button2.pack()

class Controller(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Manual Input", font=("controller.title_font", 50, "bold italic"))
        label.pack(side="top", fill="x", padx=50, pady=50)
        button = tk.Button(self, text="Open",
                           command= smartsafe)
        button1 = tk.Button(self, text="Close",
                           command= smartsafeClose)
        button2 = tk.Button(self, text="Back to Home",
                           command=lambda: controller.show_frame("StartPage"))
        button.config(font="System, 30")
        button.pack()
        button1.config(font="System, 30")
        button1.pack()
        button2.config(font="System, 30")
        button2.pack()

class Register(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Face Registering", font=("controller.title_font", 50, "bold italic"))
        label.grid(row=0,ipadx=50, ipady=50)

        registerentry = tk.Entry(self)
        registerentry.grid(row=2)
        registerentry.config(width="30")
        
        button = tk.Button(self, text="Submit",
                           command=lambda: check(registerentry))
        button.bind("<Button-1>",lambda:controller.show_frame("StartPage") )
        button1 = tk.Button(self, text="Logout",
                           command=lambda: (controller.show_frame("StartPage"), requests.get('http://'+url+':5000/logout')))
        button2 = tk.Button(self, text="Back to Home",
                           command=lambda: controller.show_frame("StartPage"))
        
        label1= tk.Label(self,text="Username")
        label1.config(font="System, 40")
        label1.grid(row=1)
        button.config(font="System, 30")
        button.grid(row=3)
        button1.config(font="System, 30")
        button1.grid(row=4)
        button2.config(font="System, 30")
        button2.grid(row=5)

        #tum username laew hai mun popup camera to take pic #milestone 2
def check(text):
    if text.get()=="":
        return
        #print ("error! 404!")
    else:
        cam.cam(text.get())
        text.delete(0,'end')
        done()
def done():
    done=tk.Toplevel()
    done.title("Success")
    label = tk.Label(done, text="Successful!", font=("controller.title_font", 50, "bold italic"))
    label.pack(side="top", fill="x", padx=50, pady=50)
    button = tk.Button(done, text="Close",
                           command=lambda: done.destroy() )
    button.config(font="System, 15")
    button.pack()
        
# if username have no entry can't take pic :(

class Setting(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Setting", fg="red", font=("controller.title_font", 50, "bold italic"))
        label.pack(side="top", fill="x", padx=50, pady=50)
        button = tk.Button(self, text="Back to Home",
                           command=lambda: controller.show_frame("StartPage"))
        button.config(font="System, 30")
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()