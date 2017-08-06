#import statements
from tkinter import *
from tkinter import ttk
import webbrowser


Bank = 0
L = []
L1 = []
L2 = []
L3 = []
L4 = []
L5 = []

def beginProgram():
    #write program to files and Tkinter review display
    import datetime
    import os.path
    global boot
    global L
    global L1
    global L2
    global L3
    global L4
    global L5
    global bankWeb
    global total
    i = 0


    ttk.Label(mainframe, text='Category').grid(column=1, row=1, sticky=W)
    ttk.Label(mainframe, text='Bank    ').grid(column=2, row=1, sticky=W)
    ttk.Label(mainframe, text='Cash    ').grid(column=3, row=1, sticky=W)
    ttk.Label(mainframe, text='Needed  ').grid(column=4, row=1, sticky=W)
    ttk.Label(mainframe, text='Total   ').grid(column=5, row=1, sticky=W)
    ttk.Label(mainframe, text='Status  ').grid(column=6, row=1, sticky=W)


    

    
    
    now = datetime.datetime.now()
    file = open(fileName, "w")
    file2 = open(fileName1, 'w')
    print(now.strftime("%a %b-%d-%Y %H:%M:%S"), '\n')
    file.write(str(now.strftime("%a %b-%d-%Y %H:%M:%S")) + '\n')
    file.write('\n')
    print('{:15} {:15} {:15} {:15} {:15} {:15}'.format('Category', 'Bank', 'Cash', 'Needed', 'Total', 'Status',), '\n')
    file.write('{:15} {:15} {:15} {:15} {:15} {:15}'.format('Category', 'Bank', 'Cash', 'Needed', 'Total', 'Status') + '\n')
    file.write('\n')
    for L, L1, L2, L3, L4, L5 in zip(L, L1, L2, L3, L4, L5):
        if L3 == L4:
            print('{:15} {:15} {:15} {:15} {:15} {:15}'.format(L, '$' + str(L1), '$' + str(L2), '$' + str(L3), '$' + str(L4), 'complete'))
            List = ttk.Label(mainframe, text=L).grid(column=1, row=2+i, sticky=W)
            List1 = ttk.Label(mainframe, text=L1).grid(column=2, row=2+i, stick=W)
            List2 = ttk.Label(mainframe, text=L2).grid(column=3, row=2+i, sticky=W)
            List3 = ttk.Label(mainframe, text=L3).grid(column=4, row=2+i, sticky=W)
            List4 = ttk.Label(mainframe, text=L4).grid(column=5, row=2+i, sticky=W)
            List5 = ttk.Label(mainframe, text='complete').grid(column=6, row=2+i, sticky=W)
            file.write('{:15} {:15} {:15} {:15} {:15} {:15}'.format(str(L), '$' + str(L1), '$' + str(L2), '$' + str(L3), '$' + str(L4), 'complete' + '\n'))
            file.write('\n')
            file2.write(str(L) + ',' + str(L1) + ',' + str(L2) + ',' + str(L3) + ',' + str(L4) + '\n')
        else:
            print('{:15} {:15} {:15} {:15} {:15} {:15}'.format(L, '$' + str(L1), '$' + str(L2), '$' + str(L3), '$' + str(L4), 'You need $' + str(L5) +
                  ' to reach your goal.'))
            List = ttk.Label(mainframe, text=L).grid(column=1, row=2+i, sticky=W)
            List1 = ttk.Label(mainframe, text=L1).grid(column=2, row=2+i, stick=W)
            List2 = ttk.Label(mainframe, text=L2).grid(column=3, row=2+i, sticky=W)
            List3 = ttk.Label(mainframe, text=L3).grid(column=4, row=2+i, sticky=W)
            List4 = ttk.Label(mainframe, text=L4).grid(column=5, row=2+i, sticky=W)
            List5 = ttk.Label(mainframe, text='You need $' + str(L5) + ' to reach your goal.').grid(column=6, row=2+i, sticky=W)
            file.write('{:15} {:15} {:15} {:15} {:15} {:15}'.format(str(L), '$' + str(L1), '$' + str(L2), '$' + str(L3), '$' + str(L4), 'You need $' + str(L5) +
                  ' to reach your goal.' + '\n'))
            file.write('\n')
            file2.write(str(L) + ',' + str(L1) + ',' + str(L2) + ',' + str(L3) + ',' + str(L4) + '\n')
        i += 1
    file2.write(bankWeb)
    if float(total) > float(Bank):
        print('You are $' + str(Bank2[1:]) + ' Overbudget.')
        file.write('You are $' + str(Bank2[1:]) + ' Overbudget.' + '\n')
        ttk.Label(mainframe, text='You are $' + str(Bank2[1:]) + ' Overbudget.').grid(column=1, row=i+2, sticky=W)
    elif float(total) < float(Bank):
        print('You have $' + str(Bank2) + ' Underbudget.')
        file.write('You have $' + str(Bank2) + ' Underbudget.' + '\n')
        ttk.Label(mainframe, text='You have $' + str(Bank2) + ' Underbudget.').grid(column=1, row=i+2, sticky=W)
    elif float(total) == float(Bank):
        print('You have all funds accounted for in bank.')
        file.write('You have all funds accounted for in bank.' + '\n')
        ttk.Label(mainframe, text='You have all funds accounted for in bank').grid(column=1, row=i+2, sticky=W)
    else:
        print()
    file.close()
    file2.close()
    ttk.Button(mainframe, text='Exit', command=Exit).grid(column=1, row=i+3, sticky=W)

    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)
    
    root.bind('<Return>', Exit)
    return

def callback(event):
    #open website for users bank
    global bankWeb
    webbrowser.open_new(bankWeb)

def definitions():
    global L1
    global L2
    global L3
    global L4
    global L5
    i = 0
    j = 0
#Begin L4 definitions
#Defines total cash and bank amount for each category.
    for item in L4:
        L4[i] = float(L1[i]) + float(L2[i])
        i += 1



#Begin L5 definitions
#Defines how close the user is to reaching desired goal.
    for item in L5:
        L5[j] = float(L3[j]) - L4[j]
        j += 1

    return

def Exit(*args):
    #closes the program
    root.destroy()

def formatLists():
#Begin Formating
#formats lists to round to 2 places
    i = 0
    j = 0
    k = 0
    l = 0
    m = 0
    for item in L:
        L1[i] = "{:.2f}".format(float(L1[i]))
        i += 1

    for item in L2:
        L2[j] = "{:.2f}".format(float(L2[j]))
        j += 1
        
    for item in L3:
        L3[k] = "{:.2f}".format(float(L3[k]))
        k += 1

    for item in L4: 
        L4[l] = "{:.2f}".format(float(L4[l]))
        l += 1

    for item in L5:
        L5[m] = "{:.2f}".format(float(L5[m]))
        m += 1
    print()
    global Bank2
    global Bank
    if L[-1] == 'Totals':
        Bank2 = float(Bank) - float(L1[-1])
        print(Bank)
        print(Bank2)
        print(total)
        Bank2 = "{:.2f}".format(float(Bank2))
    else:
        Bank2 = float(Bank)
        print(Bank)
        print(Bank2)
        print(total)
        Bank2 = "{:.2f}".format(float(Bank2))
    return
    
def inputLink():
    #opens GUI for user to enter the bank website
    #to create a link
    global top4
    top4 = Toplevel()
    top4.title('Budget')
    top4.resizable(0,0)
    
    subframe4 = ttk.Frame(top4, padding='3 3 12 12')
    subframe4.grid(column=0, row=0, sticky=(N, W, E, S))
    subframe4.columnconfigure(0, weight=1)
    subframe4.rowconfigure(0, weight=1)

    global bankWeb

    bankWeb = StringVar()

    ttk.Label(subframe4, text='Input Url:').grid(column=1, row=1, sticky=W)
    bankweb_entry = ttk.Entry(subframe4, width=25, textvariable=bankWeb)
    bankweb_entry.grid(column=2, row=1, sticky=(W, E))

    ttk.Button(subframe4, text='Input', command=inputLink2).grid(column=1, row=2, sticky=W)

    for child in subframe4.winfo_children():
        child.grid_configure(padx=5, pady=5)
    bankweb_entry.focus()
    top4.bind('<Return>', inputLink2)
    top4.mainloop()

def inputLink2(*args):
    #creates the link for a website
    global top4
    top4.destroy()
    global bankWeb
    bankWeb = str(bankWeb.get())
    if bankWeb == '':
        bankWeb = 'You do not have a link set up'
    else:
        print()

    return

def rest():
    beginProgram()

def runextra():
    definitions()
    
    formatLists()
    return

def totals():
    #adds all categories and puts them in a category called totals.
    global L1
    global L2
    global L3
    global L4
    global L5
    global total
#Define totals
    i = 0
    j = 0
    k = 0
    l = 0
    m = 0
    for item in L1:
        L1[i] = float(L1[i])
        i += 1
    for item in L2:
        L2[j] = float(L2[j])
        j += 1
    for item in L3:
        L3[k] = float(L3[k])
        k += 1
    for item in L4:
        L4[l] = float(L4[l])
        l += 1
    for item in L5:
        L5[m] = float(L5[m])
        m += 1
        
    i -= 1
    if L[i] != 'Totals':
        print(L[i])
        L.append('Totals')
        total = sum(L1)
        print(total)
        L1.append(total)
        total1 = sum(L2)
        print(total1)
        L2.append(total1)
        total2 = sum(L3)
        print(total2)
        L3.append(total2)
        total3 = sum(L4)
        print(total3)
        L4.append(total3)
        total4 = sum(L5)
        print(total4)
        L5.append(total4)
        print(L1[-1])
    else:
        total = sum(L1[:-1])
        print(total)
        L1[i] = total
        total1 = sum(L2[:-1])
        print(total1)
        L2[i] = total1
        total2 = sum(L3[:-1])
        print(total2)
        L3[i] = total2
        total3 = sum(L4[:-1])
        print(total3)
        L4[i] = total3
        total4 = sum(L5[:-1])
        print(total4)
        L5[i] = total4
    total = "{:.2f}".format(float(total))
    print()
    #rest()
    return

class New:
#sets up a new users budget
    def __init__(self, *args):
        #creates file path to store information
        global fileName
        global fileName1
        for widget in mainframe.winfo_children():
            widget.destroy()
        import datetime
        import os.path
        fileNow = datetime.datetime.now()
        savePath = 'C:/Users/Michael/Documents/GitHub/Budget/Saves/'
        savePath1 = 'C:/Users/Michael/Documents/GitHub/Budget/Computer Files/'
        fileName = str(fileName.get())
        completeName = os.path.join(savePath, fileName + ', ' + fileNow.strftime('%B-%Y') + '.txt')
        completeName2 = os.path.join(savePath1, fileName + '1.txt')
        fileName = completeName
        fileName1 = completeName2
        self.inputVars()

    
    def inputVars(self):
        #creates a GUI for user to input categories for budget and
        #set up a link for access to the banks website
        self.en = StringVar()
        self.en_entry = ttk.Entry(mainframe, width=15, textvariable=self.en)
        self.en_entry.grid(column=1, row=2, sticky=(W, E))

        self.l1 = StringVar()
        self.l1_entry = ttk.Entry(mainframe, width=15, textvariable=self.l1)
        self.l1_entry.grid(column=1, row=3, sticky=(W, E))

        self.l2 = StringVar()
        self.l2_entry = ttk.Entry(mainframe, width=15, textvariable=self.l2)
        self.l2_entry.grid(column=1, row=4, sticky=(W, E))

        self.l3 = StringVar()
        self.l3_entry = ttk.Entry(mainframe, width=15, textvariable=self.l3)
        self.l3_entry.grid(column=1, row=5, sticky=(W, E))


        ttk.Label(mainframe, text='Enter category and funds you would like to add then press input.').grid(column=1, row=1, sticky=W)
        ttk.Label(mainframe, text='Category').grid(column=2, row=2, sticky=E)
        ttk.Label(mainframe, text='Bank').grid(column=2, row=3, sticky=W)
        ttk.Label(mainframe, text='Cash').grid(column=2, row=4, sticky=W)
        ttk.Label(mainframe, text='Needed').grid(column=2, row=5, sticky=W)
        self.notify = ttk.Label(mainframe, text='Waiting on user...')
        self.notify.grid(column=1, row=7, sticky=W)
        

        ttk.Button(mainframe, text='Input', command=self.Input).grid(column=1, row=6, sticky=E)
        ttk.Button(mainframe, text='Done', command=self.Done).grid(column=1, row=9, sticky=E)
        ttk.Button(mainframe, text='Bank Link', command=inputLink).grid(column=1, row=8, sticky=E)
        self.en_entry.focus()
        root.bind('<Return>', self.Input)

    def Input(self, *args):
        #inputs users information into the correct lists
        self.category = str(self.en.get())
        self.list1 = str(self.l1.get())
        self.list2 = str(self.l2.get())
        self.list3 = str(self.l3.get())
        if self.category == '':
            print('')
        elif self.list1 == '':
            print('')
        elif self.list2 == '':
            print('')
        elif self.list3 == '':
            print('')
        else:
            L.insert(-1, self.category)
            list1 = float(self.l1.get())
            L1.insert(-1, self.list1)
            list2 = float(self.l2.get())
            L2.insert(-1, self.list2)
            list3 = float(self.l3.get())
            L3.append(self.list3)
            L4.append(0)
            L5.append(0)
        if L[-1] != 'Totals':
            L.append('Totals')
            L1.append(0)
            L2.append(0)
            L3.append(0)
            L4.append(0)
            L5.append(0)
        else:
            print()

        self.en_entry.delete(0, END)
        self.l1_entry.delete(0, END)
        self.l2_entry.delete(0, END)
        self.l3_entry.delete(0, END)
        self.notify.config(text='Success')
        root.after(1500, self.waiting)

    def waiting(self, *args):
        #creates a label to allow the user to know when
        #the categories have been added to the program
        self.notify.config(text='Waiting on User...')
        return

    def waiting1(self, *args):
        #creates a second label for same purpose
        self.notify1.config(text='Waiting on User...')
        return

    def Done(self, *args):
        #begins class for user to make changes to budget
        for widget in mainframe.winfo_children():
            widget.destroy()
        inputCalculations()

    
class Continue:
#class for user who is making changes to previous budget
    def __init__(self, *args):
        #reads file user has typed in and inputs variables
        global fileName
        global fileName1
        global bankWeb
        for widget in mainframe.winfo_children():
            widget.destroy()
        import datetime
        import os.path

        fileName = str(fileName.get())
        fileNow = datetime.datetime.now()
        savePath = 'C:/Users/Michael/Documents/GitHub/Budget/Saves/'
        savePath1 = 'C:/Users/Michael/Documents/GitHub/Budget/Computer Files/'
        completeName = os.path.join(savePath, fileName + ', ' + fileNow.strftime('%B-%Y') + '.txt')
        completeName2 = os.path.join(savePath1, fileName + '1.txt')
        fileName = completeName
        fileName1 = completeName2

        with open(fileName1, 'r') as file:
            for line in file:
                try:
                    L.append(line.split(',')[0])
                    L1.append(line.split(',')[1])
                    L2.append(line.split(',')[2])
                    L3.append(line.split(',')[3])
                    L4.append(line.split(',')[4].strip('\n'))
                    L5.append(0)
                except IndexError:
                    pass
            bankWeb = L[-1]
            del L[-1]
            self.inputVars()
            
    def inputVars(self):
        #creates GUI for user to input new categories, input bank link, and delete unwanted categories
        self.en = StringVar()
        self.en_entry = ttk.Entry(mainframe, width=10, textvariable=self.en)
        self.en_entry.grid(column=1, row=3, sticky=(W, E))

        self.l1 = StringVar()
        self.l1_entry = ttk.Entry(mainframe, width=7, textvariable=self.l1)
        self.l1_entry.grid(column=1, row=4, sticky=(W, E))

        self.l2 = StringVar()
        self.l2_entry = ttk.Entry(mainframe, width=7, textvariable=self.l2)
        self.l2_entry.grid(column=1, row=5, sticky=(W, E))

        self.l3 = StringVar()
        self.l3_entry = ttk.Entry(mainframe, width=7, textvariable=self.l3)
        self.l3_entry.grid(column=1, row=6, sticky=(W, E))

        self.cat = StringVar()


        ttk.Label(mainframe, text='Enter Category and amount to add').grid(column=1, row=1, sticky=W)
        ttk.Label(mainframe, text='Press input when finished').grid(column=1, row=2, sticky=W)
        ttk.Label(mainframe, text='Category').grid(column=2, row=3, sticky=E)
        ttk.Label(mainframe, text='Bank').grid(column=2, row=4, sticky=(W, E))
        ttk.Label(mainframe, text='Cash').grid(column=2, row=5, sticky=W)
        ttk.Label(mainframe, text='Needed').grid(column=2, row=6, sticky=W)

        self.notify = ttk.Label(mainframe, text='Waiting for user...')
        self.notify.grid(column=1, row=8, sticky=W)
        self.cat_entry = ttk.Entry(mainframe, width=10, textvariable=self.cat)
        ttk.Button(mainframe, text='Input', command=self.Input).grid(column=1, row=9, sticky=W)
        ttk.Label(mainframe, text='Enter category and press Delete.').grid(column=1, row=10, sticky=W)
        ttk.Label(mainframe, text='Category').grid(column=2, row=11, sticky=W)
        self.cat_entry.grid(column=1, row=11, sticky=(W, E))
        self.notify1 = ttk.Label(mainframe, text='Waiting for user...')
        self.notify1.grid(column=1, row=12, sticky=W)
        ttk.Button(mainframe, text='Delete', command=self.Subtract).grid(column=1, row=13, sticky=W)
        ttk.Button(mainframe, text='Bank Link', command=inputLink).grid(column=1, row=14, sticky=W)
        ttk.Button(mainframe, text='Done', command=self.Done).grid(column=1, row=15, sticky=W)
        self.en_entry.focus()
        root.bind('<Return>', self.Done)

    def Input(self):
        #same as method in the New class
        category = str(self.en.get())
        list1 = str(self.l1.get())
        list2 = str(self.l2.get())
        list3 = str(self.l3.get())
        if category == '':
            print('')
        elif list1 == '':
            print('')
        elif list2 == '':
            print('')
        elif list3 == '':
            print('')
        else:
            L.insert(-1, category)
            list1 = float(self.l1.get())
            L1.insert(-1, list1)
            list2 = float(self.l2.get())
            L2.insert(-1, list2)
            list3 = float(self.l3.get())
            L3.insert(-1, list3)
            L4.append(0)
            L5.append(0)

        if L[-1] != 'Totals':
            L.append('Totals')
            L1.append(0)
            L2.append(0)
            L3.append(0)
            L4.append(0)
            L5.append(0)
        else:
            print()

        self.en_entry.delete(0, END)
        self.l1_entry.delete(0, END)
        self.l2_entry.delete(0, END)
        self.l3_entry.delete(0, END)
        self.notify.config(text='Done')
        root.after(1500, self.waiting)

        return

    def Subtract(self):
        #deletes category and funds that the user suggested
        i = 0
        category = str(self.cat.get())
        print(category)
        if category == '':
            print('')
        else:
            for item in L:
                if category == L[i]:
                    L.pop(i)
                    L1.pop(i)
                    L2.pop(i)
                    L3.pop(i)
                    L4.pop(i)
                    L5.pop(i)
                else:
                    print('')
                i += 1
        self.cat_entry.delete(0, END)
        self.notify1.config(text='Done')
        self.cat = StringVar()
        root.after(1500, self.waiting1)

        return
    def waiting(self, *args):
        #same as method in New class
        self.notify.config(text='Waiting on User...')
        return
    def waiting1(self, *args):
        #same as method in New class
        self.notify1.config(text='Waiting on User...')
        return

    def Done(self, *args):
        #same as method in New class
        for widget in mainframe.winfo_children():
            widget.destroy()
        inputCalculations()

class inputCalculations():
    #creates a GUI for user to modify the budget
    def __init__(self, *args):
        i = 0
        j = 0
        k = 0
        l = 0
        m = 0

        global bankWeb

    

        self.selection = StringVar()

        self.List1 = []
        self.List2 = []
        self.List3 = []
        self.List4 = []

        self.Earned2 = ttk.Label(mainframe, text='Check: 0.00', font='Times 14 bold')
        self.Earned2.grid(column=1, row=1, sticky=W)
        ttk.Button(mainframe, text='Input Check', command=self.earned).grid(column=1, row=2, sticky=W)
        self.Bank3 = ttk.Label(mainframe, text='Bank: 0.00', font='Times 12 bold')
        self.Bank3.grid(column=1, row=3, sticky=W)
        ttk.Button(mainframe, text='Input Bank', command=self.bank).grid(column=1, row=4, sticky=W)
        ttk.Label(mainframe, text='Category', font='Times 10 bold').grid(column=1, row=5, sticky=W)
        ttk.Label(mainframe, text='Bank    ', font='Times 10 bold').grid(column=2, row=5, sticky=W)
        ttk.Label(mainframe, text='Cash    ', font='Times 10 bold').grid(column=3, row=5, sticky=W)
        ttk.Label(mainframe, text='Needed  ', font='Times 10 bold').grid(column=4, row=5, sticky=W)
        ttk.Label(mainframe, text='Total   ', font='Times 10 bold').grid(column=5, row=5, sticky=W)
    
        for item in L[:-1]:
            self.List = Radiobutton(mainframe, text=L[i], variable=self.selection, value=L[i], command=self.Select, indicatoron=0, background='Snow', anchor=W).grid(column=1, row=6+i, sticky=(W, E))
            i += 1
        for item in L1:
            self.List1.append(ttk.Label(mainframe, text=L1[j]))
            self.List1[j].grid(column=2, row=6+j, stick=W)
            j += 1
        for item in L2:
            self.List2.append(ttk.Label(mainframe, text=L2[k]))
            self.List2[k].grid(column=3, row=6+k, sticky=W)
            k +=1
        for item in L3:
            self.List3.append(ttk.Label(mainframe, text=L3[l]))
            self.List3[l].grid(column=4, row=6+l, sticky=W)
            l += 1
        for item in L4:
            self.List4.append(ttk.Label(mainframe, text=L4[m]))
            self.List4[m].grid(column=5, row=6+m, sticky=W)
            m += 1

        print(L)
        ttk.Label(mainframe, text=L[-1]).grid(column=1, row=i+6, sticky=W)

        ttk.Button(mainframe, text='Done', command=self.closeCalculate).grid(column=1, row=i+7, sticky=W)
        try:
            if bankWeb == 'You do not have a link set up':
                link = ttk.Label(mainframe, text=bankWeb, foreground='blue')
                link.grid(column=1, row=i+8, sticky=W)
            else:
                link = ttk.Label(mainframe, text=bankWeb, foreground='blue', cursor='hand2')
                link.grid(column=1, row=i+8, sticky=W)
                link.bind('<Button-1>', callback)
        except NameError:
            bankWeb = 'You do not have a link set up'
            link = ttk.Label(mainframe, text=bankWeb, foreground='blue')
            link.grid(column=1, row=i+8, sticky=W)
            pass
    

    
        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        root.bind('<Return>', self.closeCalculate)

    def earned(self):
        #allows user to input amount added to bank
        global top1
        top1 = Toplevel()
        top1.title('Budget')
        top1.resizable(0,0)

        subframe1 = ttk.Frame(top1, padding='3 3 12 12')
        subframe1.grid(column=0, row=0, sticky=(N, W, E, S))
        subframe1.columnconfigure(0, weight=1)
        subframe1.rowconfigure(0, weight=1)

        self.Earned1 = StringVar()

        ttk.Label(subframe1, text='Enter amount you have earned.').grid(column=1, row=1, sticky=W)
        self.Earned_entry = ttk.Entry(subframe1, width=15, textvariable=self.Earned1)
        self.Earned_entry.grid(column=2, row=1, sticky=(W, E))
        ttk.Button(subframe1, text='Input', command=self.inputearned).grid(column=1, row=2, sticky=W)

        for child in subframe1.winfo_children():
            child.grid_configure(padx=5, pady=5)
        self.Earned_entry.focus()
        top1.bind('<Return>', self.inputearned)
        top1.mainloop()

    def inputearned(self, *args):
        #calculates inputed amount for program use
        top1.destroy()
        try:
            self.Earned = float(self.Earned1.get())
            print('Earned', self.Earned)
            self.Earned = "{:.2f}".format(float(self.Earned))
            self.Earned2.config(text='Check: ' + str(self.Earned))
        except (ValueError, AttributeError):
            pass

    def bank(self):
        #allows the user to input amount of money in the bank
        global top3
        top3 = Toplevel()
        top3.title('Budget')
        top3.resizable(0,0)

        subframe3 = ttk.Frame(top3, padding='3 3 12 12')
        subframe3.grid(column=0, row=0, sticky=(N, W, E, S))
        subframe3.columnconfigure(0, weight=1)
        subframe3.rowconfigure(0, weight=1)

        self.Bank1 = StringVar()
        ttk.Label(subframe3, text='Enter amount in the Bank.').grid(column=1, row=1, sticky=W)
        self.Bank_entry = ttk.Entry(subframe3, width=7, textvariable=self.Bank1)
        self.Bank_entry.grid(column=2, row=1, sticky=(W, E))
        ttk.Button(subframe3, text='Input', command=self.inputbank).grid(column=1, row=2, sticky=W)
        for child in subframe3.winfo_children():
            child.grid_configure(padx=5, pady=5)
        self.Bank_entry.focus()
        top3.bind('<Return>', self.inputbank)
        top3.mainloop()

    def inputbank(self, *args):
        #calculates the amount entered for program use
        top3.destroy()
        try:
            self.Bank = float(self.Bank1.get())
            self.Bank = "{:.2f}".format(float(self.Bank))
            self.Bank3.config(text='Bank: ' + str(self.Bank))
            print(self.Bank)
            Bank = self.Bank
        except (ValueError, AttributeError):
            pass

    def Select(self, *args):
        #creates a GUI for user to make changes to selected category
        global top

        self.select = str(self.selection.get())

        self.calculate1 = StringVar()
        self.calculate2 = StringVar()
        self.calculate3 = StringVar()
        self.calculate4 = StringVar()
        self.user_Input = self.select
        self.user_Input2 = self.select
        self.user_Input3 = self.select
        self.user_Input4 = self.select
        

        top = Toplevel()
        top.title('Budget')
        top.resizable(0,0)

        subframe = ttk.Frame(top, padding='3 3 12 12')
        subframe.grid(column=0, row=0, sticky=(N, W, E, S))
        subframe.columnconfigure(0, weight=1)
        subframe.rowconfigure(0, weight=1)
        
        ttk.Button(subframe, text='Change Needed', command=self.needed).grid(column=1, row=3, sticky=W)
        ttk.Label(subframe, text='How much would you like to add to Bank?').grid(column=1, row=4, sticky=W)
        ttk.Label(subframe, text='How much would you like to add to Cash?').grid(column=1, row=5, sticky=W)
        ttk.Label(subframe, text='How much would you like to subtract from Bank?').grid(column=1, row=6, sticky=W)
        ttk.Label(subframe, text='How much would you like to subtract from Cash?').grid(column=1, row=7, sticky=W)

        self.calculate3_entry = ttk.Entry(subframe, width=7, textvariable=self.calculate3)
        self.calculate3_entry.grid(column=2, row=4, sticky=(W, E))
        self.calculate4_entry = ttk.Entry(subframe, width=7, textvariable=self.calculate4)
        self.calculate4_entry.grid(column=2, row=5, sticky=(W, E))
        self.calculate1_entry = ttk.Entry(subframe, width=7, textvariable=self.calculate1)
        self.calculate1_entry.grid(column=2, row=6, sticky=(W, E))
        self.calculate2_entry = ttk.Entry(subframe, width=7, textvariable=self.calculate2)
        self.calculate2_entry.grid(column=2, row=7, sticky=(W, E))

        ttk.Button(subframe, text="Input", command=self.CalculateUserInput).grid(column=2, row=8, sticky=W)
        ttk.Button(subframe, text='Done', command=self.closeCalculate1).grid(column=2, row=9, sticky=W)
    
        for child in subframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
        self.calculate3_entry.focus()
        top.bind('<Return>', self.CalculateUserInput)
        top.mainloop()

    def needed(self):
        #creates GUI for user to modify the amount needed
        #to reach goal of selected category
        global top2
        top2 = Toplevel()
        top2.title('Budget')
        top2.resizable(0,0)

        subframe2 = ttk.Frame(top2, padding='3 3 12 12')
        subframe2.grid(column=0, row=0, sticky=(N, W, E, S))
        subframe2.columnconfigure(0, weight=1)
        subframe2.rowconfigure(0, weight=1)

        self.need = StringVar()

        ttk.Label(subframe2, text='Enter new amount needed.').grid(column=1, row=1, sticky=W)
        self.need_entry = ttk.Entry(subframe2, width=7, textvariable=self.need)
        self.need_entry.grid(column=2, row=1, sticky=(W, E))

        ttk.Button(subframe2, text='Input', command=self.calculateNeed).grid(column=1, row=2, sticky=W)

        for child in subframe2.winfo_children():
            child.grid_configure(padx=5, pady=5)
        
        self.need_entry.focus()
        top2.bind('<Return>', self.calculateNeed)
        top2.mainloop()

    def calculateNeed(self, *args):
        #makes changes to the list where needed amounts are stored
        top2.destroy()
        i = 0
        self.need = float(self.need.get())
        for item in L:
            if self.select == L[i]:
                L3[i] = float(self.need)
                L3[i] = "{:.2f}".format(float(L3[i]))
                self.List3[i].config(text=L3[i])
                break
            else:
                print()
            i += 1
        return

    def closeCalculate(self, *args):
        #closes inputCalculations GUI and modifies the runs through functions
        #to store all the changes made
        for widget in mainframe.winfo_children():
            widget.destroy()

        definitions()
        totals()
        formatLists()
        rest()
        return

    def closeCalculate1(self):
        #closes GUI where changes to categories are being made
        global top
        top.destroy()
        return       
    
    def CalculateUserInput(self, *args):
        #prepares program to make implement changes made to the budget
        try:
            self.Bank = float(self.Bank.get())
            print('Bank', self.Bank)
        except (AttributeError, ValueError):
            self.Bank = 0
            self.Bank = float(self.Bank)
            print(self.Bank)
            pass

        try:
            self.userInput2 = self.select
            self.Calculate = float(self.calculate1.get())
            print('Calculate', self.Calculate)
            self.calculateInput2()
        except ValueError:
            pass

        try:
            self.userInput4 = self.select
            self.Calculate2 = float(self.calculate2.get())
            print('Calculate2', self.Calculate2)
            self.calculateCash2()
        except ValueError:
            pass

        try:
            self.userInput = self.select
            self.Calculate3 = float(self.calculate3.get())
            print('Calculate3', self.Calculate3)
            self.calculateInput()
        except ValueError:
            pass

        try:
            self.userInput3 = self.select
            self.Calculate4 = float(self.calculate4.get())
            print('Calculate4', self.Calculate4)
            self.calculateCash()
        except ValueError:
            pass
        self.Bank
        
        self.calculate1_entry.delete(0, END)
        self.calculate2_entry.delete(0, END)
        self.calculate3_entry.delete(0, END)
        self.calculate4_entry.delete(0, END)

    def calculateInput(self, *args):
        #calculates amount added to the bank
        i = 0
        j = 0
        for item in L:
            if self.userInput.upper() == L[i].upper():
                try:
                    self.Earned = float(self.Earned) - float(self.Calculate3)
                    self.Earned = "{:.2f}".format(float(self.Earned))
                    self.Earned2.config(text='Earned: ' + str(self.Earned))
                except (TypeError, AttributeError):
                    pass
                self.userInput = L1[i]
                L1[i] = float(self.userInput) + float(self.Calculate3)
                L1[i] = "{:.2f}".format(float(L1[i]))
                self.List1[i].config(text=L1[i])
            
                self.List4[i].config(text=L4[i])
                break
            else:
                print('')
            i += 1
        
        return

    def calculateInput2(self, *args):
        #calculates amount subtracted from bank
        i = 0
        for item in L:
            if self.userInput2 == L[i]: 
                self.userInput2 = L1[i]
                L1[i] = float(self.userInput2) - float(self.Calculate)
                L1[i] = "{:.2f}".format(float(L1[i]))
                self.List1[i].config(text=L1[i])
                runextra()
                self.List4[i].config(text=L4[i])
            
                break
            else:
                print('')
            i += 1
        return

    def calculateCash(self, *args):
        #calculates amount added to cash
        i = 0
        for item in L:
            if self.userInput3 == L[i]:
                try:
                    self.Earned = float(self.Earned) - float(self.Calculate4)
                    self.Earned = "{:.2f}".format(float(self.Earned))
                    self.Earned2.config(text='Earned: ' + str(self.Earned))
                except (TypeError, AttributeError):
                    pass
                self.userInput3 = L2[i]
                L2[i] = float(self.userInput3) + float(self.Calculate4)
                L2[i] = "{:.2f}".format(float(L2[i]))
                self.List2[i].config(text=L2[i])
                runextra()
                self.List4[i].config(text=L4[i])
                break
            else:
                print('')
            i += 1
        return

    def calculateCash2(self, *args):
        #subtracts amount added to cash
        i = 0
        for item in L:
            if self.userInput4 == L[i]:
                self.userInput4 = L2[i]
                L2[i] = float(self.userInput4) - float(self.Calculate2)
                L2[i] = "{:.2f}".format(float(L2[i]))
                self.List2[i].config(text=L2[i])
                runextra()
                self.List4[i].config(text=L4[i])
                break
            else:
                print('')
            i += 1
        return

#creates GUI mainframe where user can enter filename
#for existing budget or create a new file name for
#a new budget
root = Tk()
root.title('Budget')
root.resizable(0,0)
style = ttk.Style(root)
mainframe = ttk.Frame(root, padding='3 3 12 12')
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
style.configure(root, background='deep sky blue')

fileName = StringVar()

fileName_entry = ttk.Entry(mainframe, width=15, textvariable=fileName)
fileName_entry.grid(column=2, row=1, sticky=(W, E))
fileName_entry = fileName_entry

ttk.Label(mainframe, text='Enter Save Name.').grid(column=1, row=1, sticky=E) 
ttk.Button(mainframe, text='Continue', command=Continue).grid(column=1, row=4, sticky=W)
ttk.Button(mainframe, text='New', command=New).grid(column=1, row=3, sticky=W)
fileName_entry.focus()
root.bind('<Return>', Continue)
root.mainloop()
