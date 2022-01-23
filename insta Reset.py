import requests
import random
from tkinter import *
from tkinter import messagebox
import string
import uuid
win = Tk()
win.iconbitmap(r'1212.ico')
img = win.iconbitmap(r'1212.ico')
def send():
    params = {
        'email': e3.get()
    }
    email = params['email']
    head = {
        "user-agent": f"Instagram 150.0.0.0.000 Android (29/10; 300dpi; 720x1440; {''.join(random.choices(string.ascii_lowercase + string.digits, k=16))}/{''.join(random.choices(string.ascii_lowercase + string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase + string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase + string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase + string.digits, k=16))}; en_GB;)"}
    data = {
        "_csrftoken": "".join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=32)),
        "user_email": email,
        "guid": uuid.uuid4(),
        "device_id": uuid.uuid4()
    }
    req = requests.post("https://i.instagram.com/api/v1/accounts/send_password_reset/", headers=head, data=data,)
    if 'Please wait a few minutes before you try again.' in req.text:
        messagebox.showerror("D7", "Error Send rest [Try Again Later]")
    elif 'obfuscated_email' in req.text:
        messagebox.showinfo("D7", "Done Send Rest")
    else:
        messagebox.showerror("D7", "Unknown Error")
if __name__ == '__main__':
    rest = Label(win, text="Email",bg="#666666", fg="#00ccff")
    e3 = Entry(win,  bg="#666666",fg="#00ccff")
    b1 = Button(win, text='Reset',bg="#666666", fg="#00ccff", command=send)
    rest1 = Label(win, text="By @3fuq.old",bg="#666666", fg="#00ccff")
    win.title('D7')
    win.geometry("190x90")
    win.configure(background="#666666")
    rest.pack(fill=X,pady=0)
    e3.pack(fill=X,pady=0)
    b1.pack(fill=X,pady=0)
    rest1.pack(fill=X,pady=0)
    win.mainloop()