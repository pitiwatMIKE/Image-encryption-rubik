import os
import tkinter as tk
from tkinter import *
from tkinter import ttk, filedialog, messagebox
from time import time
from algorithm import encrypt, decrypt

def openfile():
    #clear path old
    pathFileIn.delete(0, END)
    pathFileOut.delete(0, END)
    size.config(text='')
    timeSpent.config(text='')

    #open path new
    pathfile = tk.filedialog.askopenfilename()
    pathFileIn.insert("",str(pathfile))

    #size file
    file_stats = os.stat(pathfile)
    size.config(text='{:.2f}KB'.format(file_stats.st_size / 1024))

def openExplorer():
    pahtfile = pathFileOut.get()
    pahtfile = pahtfile.split('/')
    pahtfile.remove(pahtfile[-1])
    pahtfile = '/'.join(map(str,pahtfile))
    print(pahtfile)
    os.system("start "+str(pahtfile))

def openImage():
    if(pathFileOut.get() == ''):
        return
    pahtfile = pathFileOut.get()
    os.system("start " + str(pahtfile))

def encryption():
    #clear path old
    pathFileOut.delete(0, END)
    # get path image
    pathIn = pathFileIn.get();

    # start time
    t1 = time()

    #algorithm rubik's cube encrypt
    pathOut = encrypt.encryptionImage(pathIn)

    # end time
    t2 = time()
    tResult = t2 - t1
    timeSpent.config(text='{:.6f} second'.format(tResult))

    pathFileOut.insert("", str(pathOut))
    messagebox.showinfo("Encryption", "Success!!!")

def decryption():
    # clear path old
    pathFileOut.delete(0, END)
    # get path image
    pathIn = pathFileIn.get();

    # start time
    t1 = time()

    # algorithm rubik's cube decrypt
    pathOut = decrypt.decryptionImage(pathIn)

    # end time
    t2 = time()
    tResult = t2 - t1
    timeSpent.config(text='{:.6f} second'.format(tResult))

    pathFileOut.insert("", str(pathOut))
    messagebox.showinfo("Decryption", "Success!!!")

# GUI
mainfrm = Tk()
mainfrm.title("Encryption-Image")
mainfrm.iconbitmap('icon/key.ico')

lalFrm = ttk.LabelFrame(mainfrm, text="Encryption---Decryption")
lalFrm.pack(padx=10, pady=10)

btnOpenFile = ttk.Button(lalFrm, text="Openfile", command=openfile).grid(column=0, row=1, padx=5, pady=5, sticky="e")
btnOpenExplorer = ttk.Button(lalFrm, text="Path-Ouput", command=openExplorer).grid(column=0, row=2, padx=5, pady=5, sticky='e')
# lalpathOut = ttk.Label(lalFrm, text="Path-Ouput").grid(column=0, row=2, padx=5, pady=5, sticky='e')

pathFileIn = ttk.Entry(lalFrm, width=50)
pathFileOut = ttk.Entry(lalFrm, width=50)
pathFileIn.grid(column=1, columnspan=3, row=1, padx=5)
pathFileOut.grid(column=1, columnspan=3, row=2, padx=5)

btnEncryp = ttk.Button(lalFrm, text="Encryption", command=encryption).grid(column=1, row=3, padx=5, pady=5, sticky='w')
btnDecryp = ttk.Button(lalFrm, text="Decryption", command=decryption).grid(column=2, row=3, padx=5, pady=5, sticky='w')
btnPlay = ttk.Button(lalFrm, text="Open Image", command=openImage).grid(column=3, row=3, padx=5, pady=5, sticky='w')

lblSize = ttk.Label(lalFrm, text="Size :").grid(column=0, row=4, pady=4, sticky="e")
size = ttk.Label(lalFrm)
size.grid(column=1, row=4, pady=4, sticky='w')

lblTime = ttk.Label(lalFrm, text="Time Spent :").grid(column=0, row=5, pady=4, sticky="e")
timeSpent = ttk.Label(lalFrm)
timeSpent.grid(column=1, row=5, pady=4, sticky='w')

mainfrm.mainloop()