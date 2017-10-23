import sqlite3 as lite
import sys
import os
import time
import ctypes

from tkinter import *
from tkinter import messagebox

con = lite.connect('PublicEncoder.db')
print("Enter Key")
print("If you don't want the usb folder opening go to settings and dissable the autorun/autoplay for usb drives")

def find():
    #note for loop and list merge the list A-Z + "\\0@123@0.txt""
    #this is to find the usb file
    global document, t
    for i in ["A:","B:","C:","D:","E:","F:","G:","H:","I:","J:","K:","L:","M:","N:","O:","P:","Q:","R:","S:","T:","U:","V:","W:","X:","Y:","Z:"]:
        try:
            document = open(i+"\\GuestKey.txt")
            t = document.readlines()
            find = True
            return find
        except:
            find = False


def email2():
    import os
    import smtplib
    from email import encoders
    from email.mime.base import MIMEBase
    from email.mime.multipart import MIMEMultipart
    print("warning this only is for gmail accounts!")
    s = input("Do you wish to email a file? y/n: ").lower()

    if s == "y":
        COMMASPACE = ', '
        print("warning this only is for gmail accounts!")
        #---
        sender = input("Sender: ")
        gmail_password = input("Password: ")
        recipients = [input("Recipient: ")]
        
        # Create the enclosing (outer) message
        outer = MIMEMultipart()
        outer['Subject'] = input("Subject: ")
        outer['To'] = COMMASPACE.join(recipients)
        outer['From'] = sender
        outer.preamble = 'You will not see this in a MIME-aware mail reader.\n'

        # List of attachments
        data()
        attachments = [input("attach:")]

        # Add the attachments to the message
        for file in attachments:
            try:
                with open(file, 'rb') as fp:
                    msg = MIMEBase('application', "octet-stream")
                    msg.set_payload(fp.read())
                encoders.encode_base64(msg)
                msg.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file))
                outer.attach(msg)
            except:
                print("Unable to open one of the attachments. Error: ", sys.exc_info()[0])
                raise

        composed = outer.as_string()


        # Send the email
        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as s:
                s.ehlo()
                s.starttls()
                s.ehlo()
                s.login(sender, gmail_password)
                s.sendmail(sender, recipients, composed)
                s.close()
            print("Email sent!")
        except:
            print("Unable to send the email. Error: ", sys.exc_info()[0])
            raise
        os.system('cls')
    else: os.system('cls')
    
#this sends emails but I wanted Files to be sent only
##def email():
##    import smtplib
##    from email.mime.text import MIMEText
##    from email.mime.application import MIMEApplication
##    from email.mime.multipart import MIMEMultipart
##    from smtplib import SMTP
##    import smtplib
##    import sys
##    
##    fromaddr = ''
##    toaddrs  = ''
##    msg = 'Why,Oh why!'
##    username = fromaddr
##    password = ''
##    server = smtplib.SMTP('smtp.gmail.com:587')
##    server.ehlo()
##    server.starttls()
##    server.login(username,password)
##    server.sendmail(fromaddr, toaddrs, msg)
##    server.quit()


#displays the data in the database relating to files encrypted with this program
def data():
    cursor = con.execute("SELECT * from Files")
    for row in cursor:
       print ("File = ", row[0])
       print ("State = ", row[1])
       print ("Key = ", row[2], "\n")
       #print ("Email = ", row[3])



    ##NC=input("New File?:")
    ##if NC=="yes":
    ##    firstname = input('Enter File name: ')
    ##    lastname = input('Enter last name: ')
    ##    phone = input('Enter phone number: ')
    ##    email = input('Enter Email address: ')
    ##    Add=input("Add?:")
    ##    if Add=="yes":
    ##        cur = con.cursor()
    ##        cur.execute("INSERT INTO Files VALUES (?, ?, ?, ?);", (firstname, lastname, phone, email))
    ##        con.commit()

    #con.close()



#encrypt
word = ""

def code(i,c,g):
    global word
    if i == c:
        #print(g)
        word = word + g

def encodeKey(i):
    code(i,"a","(")
    code(i,"b",")")
    code(i,"c","!")
    code(i,"d","@")
    code(i,"e","#")
    code(i,"f","$")
    code(i,"g","%")
    code(i,"h","^")
    code(i,"i","&")
    code(i,"j","*")
    code(i,"k","8")
    code(i,"l","7")
    code(i,"m","6")
    code(i,"n","5")
    code(i,"o","4")
    code(i,"p","3")
    code(i,"q","2")
    code(i,"r","1")
    code(i,"s","0")
    code(i,"t","9")
    code(i,"u"," ")
    code(i,"v","|")
    code(i,"w","\\")
    code(i,"x","-")
    code(i,"y","=")
    code(i,"z","+")

    code(i,"A","<")
    code(i,"B",">")
    code(i,"C","'")
    code(i,"D",'"')
    code(i,"E","[")
    code(i,"F","]")
    code(i,"G",".")
    code(i,"H",";")
    code(i,"I","_")
    code(i,"J",",")
    code(i,"K","/")
    code(i,"L","?")
    code(i,"M",":")
    code(i,"N","`")
    code(i,"O","{")
    code(i,"P","}")
    code(i,"Q","~")
    code(i,"R","a")
    code(i,"S","b")
    code(i,"T","c")
    code(i,"U","d")
    code(i,"V","e")
    code(i,"W","f")
    code(i,"X","g")
    code(i,"Y","h")
    code(i,"Z","i")



    code(i,"0","j")
    code(i,"1","k")
    code(i,"2","l")
    code(i,"3","m")
    code(i,"4","n")
    code(i,"5","o")
    code(i,"6","p")
    code(i,"7","q")
    code(i,"8","r")
    code(i,"9","s")

    code(i,"(","t")
    code(i,"*","u")
    code(i,"&","v")
    code(i,"^","w")
    code(i,"%","x")
    code(i,"$","y")
    code(i,"#","z")
    code(i,"@","A")
    code(i,"!","B")
    code(i,")","C")


    code(i," ","D")
    #code(i," ","Ǟ") didn't work
    code(i,"\\","E")
    code(i,"-","F")
    code(i,"=","G")
    code(i,"+","H")
    code(i,"<","I")
    code(i,">","J")
    code(i,"'","K")
    code(i,'"',"L")
    code(i,"[",'M')
    code(i,"]","N")
    code(i,".","O")
    code(i,";","P")
    code(i,"_","Q")
    code(i,",","R")
    code(i,"/","S")
    code(i,"?","T")
    code(i,":","U")
    code(i,"`","V")
    code(i,"{","W")
    code(i,"}","X")
    code(i,"~","Y")
    code(i,"|","Z")

def decodeKey(i):
    code(i,"(","a")
    code(i,")","b")
    code(i,"!","c")
    code(i,"@","d")
    code(i,"#","e")
    code(i,"$","f")
    code(i,"%","g")
    code(i,"^","h")
    code(i,"&","i")
    code(i,"*","j")
    code(i,"8","k")
    code(i,"7","l")
    code(i,"6","m")
    code(i,"5","n")
    code(i,"4","o")
    code(i,"3","p")
    code(i,"2","q")
    code(i,"1","r")
    code(i,"0","s")
    code(i,"9","t")
    code(i," ","u")
    code(i,"|","v")
    code(i,"\\","w")
    code(i,"-","x")
    code(i,"=","y")
    code(i,"+","z")

    code(i,"<","A")
    code(i,">","B")
    code(i,"'","C")
    code(i,'"',"D")
    code(i,"[","E")
    code(i,"]","F")
    code(i,".","G")
    code(i,";","H")
    code(i,"_","I")
    code(i,",","J")
    code(i,"/","K")
    code(i,"?","L")
    code(i,":","M")
    code(i,"`","N")
    code(i,"{","O")
    code(i,"}","P")
    code(i,"~","Q")
    code(i,"a","R")
    code(i,"b","S")
    code(i,"c","T")
    code(i,"d","U")
    code(i,"e","V")
    code(i,"f","W")
    code(i,"g","X")
    code(i,"h","Y")
    code(i,"i","Z")



    code(i,"j","0")
    code(i,"k","1")
    code(i,"l","2")
    code(i,"m","3")
    code(i,"n","4")
    code(i,"o","5")
    code(i,"p","6")
    code(i,"q","7")
    code(i,"r","8")
    code(i,"s","9")

    code(i,"t","(")
    code(i,"u","*")
    code(i,"v","&")
    code(i,"w","^")
    code(i,"x","%")
    code(i,"y","$")
    code(i,"z","#")
    code(i,"A","@")
    code(i,"B","!")
    code(i,"C",")")


    code(i,"D"," ")
    #code(i," ","Ǟ") didn't work
    code(i,"E","\\")
    code(i,"F","-")
    code(i,"G","=")
    code(i,"H","+")
    code(i,"I","<")
    code(i,"J",">")
    code(i,"K","'")
    code(i,"L",'"')
    code(i,"M",'[')
    code(i,"N","]")
    code(i,"O",".")
    code(i,"P",";")
    code(i,"Q","_")
    code(i,"R",",")
    code(i,"S","/")
    code(i,"T","?")
    code(i,"U",":")
    code(i,"V","`")
    code(i,"W","{")
    code(i,"X","}")
    code(i,"Y","~")
    code(i,"Z","|")


def encodeFile(x):
    global word
    global Key
    global CKey

    CKey = str(Key)
    
    fullword = ""

    while True:
        if x == None:
            file = input("File:")
        else:
            file = x

        state = "encoded"
        
        cur = con.cursor()
        cur.execute("Delete from Files where File = '"+file+"'")
        con.commit()
        
        cur.execute("INSERT INTO Files VALUES ( ?, ?, ?);", (file, state, CKey))
        con.commit()



        
        print("Please wait until Done is displayed")
        while Key > 0:
            Key = Key - 1
            try:
                document = open(file,"U")
            except:
                break
            t = document.readlines()
            
            for i in t:
                #print(i.strip())
                for i in i:
                    #print(i.strip())
                    #i = i.lower()
                    encodeKey(i)

                #print(word)

                if fullword == "":
                    fullword = fullword + word
                else:
                    fullword = fullword +"\n"+ word

            #overide the file name and clear and add text that has been encoded.
                if Key == 1:
                    document = open(file, "w")
                    document.write(fullword +"\n"+"\n"+ CKey)
                else:
                    document = open(file, "w")
                    document.write(fullword)

                word = ""
            fullword = ""
        if Key == 0:
            print("Done")
            document.close()

        try:
            #time.sleep(3)
            os.system('cls')
        except:
            print()
        break



def decodeFile(x):
    global word
    global Key
    fullword = ""
    

    while True:
        if x == None:
            file = input("File:")
        else:
            file = x

        #try:
            #os.system("start"+file)
        #except:
            #os.system("open "+file)

        Key = 1
        #print("Take the last line of characters and decode them to get the key")

        try:
            document = open(file)
        except:
            break
        t = document.readlines()
        for i in t:
            #print(i.strip())
            CodedKey = i.strip()
            #print(CodedKey)
            #for i in i.strip():

        Key = decode(CodedKey)
        RKey = Key

        try:
            cur = con.cursor()
            cur.execute("Delete from Files where File = '"+file+"'")
            con.commit()
        except:
            print()

        state = "decoded"
        
        cur.execute("INSERT INTO Files VALUES ( ?, ?, ?);", (file, state, 0))
        con.commit()


        print("Please wait until Done is displayed")
        #print("When the file opens don't forget to remove the last line of text and save")
        
        while Key > 0:
            Key = Key - 1
            try:
                document = open(file)
            except:
                break
            t = document.readlines()
            for i in t:
                #print(i.strip())
                for i in i:
                    #i = i.lower()
                    
                    decodeKey(i)


                #print(word)

                if fullword == "":
                    fullword = fullword + word
                elif word == str(RKey) and Key == (RKey - 1):
                    fullword = fullword
                else:
                    fullword = fullword +"\n"+ word

            #overide the file name and clear and add text that has been encoded.
                document = open(file, "w")
                #http://stackoverflow.com/questions/1877999/delete-final-line-in-file-with-python
                #fullword = fullword.split()
                
                document.write(fullword)
                document.close()
                word = ""
            fullword = ""

            
            
        print("first - Done")
        
        #import os, sys
##        try:
##            readFile = open(file)
##
##            lines = file.readlines()
##            lines = lines[:-1]
##
##            readFile.close()
##            w = open(file,'w')
##
##            w.write([item for item in lines])
###lines
##            w.close()
##
##            print("second - Done")
##        except:
##            print("Fail")

        import subprocess
        programName = "notepad.exe"
        #fileName = "file.txt"
        subprocess.Popen([programName, file])

        #try:
            #os.system("start"+file)
        #except:
            #os.system("open "+file)
        try:
            #time.sleep(3)
            os.system('cls')
        except:
            print()
        break

def encode():
    global word
    global Key
    while True:
        t= input("Insert Message:")

        while Key > 0:
            Key = Key - 1

            for i in t:
                #print(i)
                encodeKey(i)
            
            
            if Key == 0:
                print(word)
            t = word
            word = ""
        
        break

def decode(CodedKey):
    global word
    global Key
    while True:
        try:
            t = CodedKey
        except:
            t= input("Decode Message:")
        if CodedKey == None:
            t= input("Decode Message:")
            
        #t=t.lower()
        while Key > 0:
            Key = Key - 1
            for i in t:
                #print(i)
                
                decodeKey(i)

            
            
            if Key == 0:
                print(word)
            t = word
            word = ""

        try:
            return int(t)
        except:
            break


def Activate():
    global word
    global Key
    global CKey
    #print()
    #print("         <<<     >>>")
    #print("          <<< 0 >>>")
    #print("           <<000>>")
    #print("            00000")
    #print("           <<000>>")
    #print("          <<< 0 >>>")
    #print("         <<<     >>>")
    print("Data:")
    data()
    if find() == None: ED = None
    ED = input("GUI / Email file/ Encode / Decode / Encode File / Decode File / Compatible or Com / Close / Open File / Open Text File or OTF / Remove Record(RR) / Press enter to refresh:").lower()
    if find() == None: ED = None

    if ED == None or ED == "email file" or ED == "gui" or ED == "decode file" or ED == "" or ED == "acis" or ED == "compatible" or ED == "com" or ED == "close" or ED == "open file" or ED == "otf" or ED == "open text file" or ED == "rr":
        print()
    else:
        try:
            Key = int(input("Key (recomended K <= 20):"))

        except:
            print()
            #continue

    if ED == "encode":
        encode()
        input("Press Enter:")
    elif ED == "decode":
        decode(None)
        input("Press Enter:")
    elif ED == "encode file":
        encodeFile(None)
    elif ED == "decode file":
        decodeFile(None)
    elif ED == "email file":
        email2()
    elif ED == "close":
        #break
        exit()
    elif ED == "compatible" or ED == "com":
        print("--The Encryptor only encrypts characters that are located on the basic keyboard. If you wish to encrypt a file ensure that only these basic characters are used.--")
        print("")
        print("This Encryptor has been tested successfull against: \n> cs \n> js \n> txt \n> html \n> py \n> url","\n", "\n","It has failed against:\n> jpg \n> docx \n> zip \n> pdf")
        try:
            #time.sleep(3)
            input("Press Enter:")
            os.system('cls')
        except:
            print()
    elif ED == "otf" or ED == "open text file":
        import subprocess
        t = input("file location: ")
        programName = "notepad.exe"
        #fileName = "file.txt"
        subprocess.Popen([programName, t])
    elif ED == "open file":
        t = input("file location: ")
        try:
            os.system("start"+t)
        except:
            os.system("open "+t)
        try:
            time.sleep(3)
            os.system('cls')
        except:
            print()
    elif ED == "gui":
        GUI()
    elif ED == "rr":
        t = input("File:")
        cur = con.cursor()
        cur.execute("Delete from Files where File = '"+t+"'")
        con.commit()
        try:
            time.sleep(3)
            os.system('cls')
        except:
            print()
        
    else:
        print()
        #continue

def GUI():
    #simple GUI
    import tkinter

    #create the Window
    frame = Tk()

    #modify root window
    frame.title("File Encrypt: ")
    frame.geometry('300x150')
    #frame = Frame(root, width=400, height=100)
    #frame.grid()

    

    

    

    #label
    label = Label(frame, text = "File Encrypt: ")
    label.grid()

    def helloCallBack():
        label = Label(frame, text = "hello")
        label.grid()
        
    def btnMasterDecode():
        if find() == True:
            os.system('cls')
            cursor = con.execute("SELECT * from Files")
            for row in cursor:
               if row[1] == "encoded":
                   #btn3 = Label(frame, text = row[0], command = decodeFile(row[0]))
                   #btn3.grid()
                   print(row[0])
                   decodeFile(row[0])
            #msg = messagebox.showinfo( "Done", "When the files open don't forget to remove the last line of text and save them")
        else: frame.destroy()
        
    def btnDecode():
        if find() == True:
            check = 0
            os.system('cls')
            cursor = con.execute("SELECT * from Files")
            for row in cursor:
               if row[1] == "encoded":
                   #label = Label(frame, text = row[0])
                   #label.grid()
                   print(row[0])
                   check = 1

            if check == 1:
                decodeFile(None)
                #msg = messagebox.showinfo("Done", "When the file opens don't forget to remove the last line of text and save")
                a = input("Continue decoding? y/n: ").lower()

                if a == "y":
                    btnDecode()
                else:
                    os.system('cls')
        else: frame.destroy() #root.destroy()
    def btnMasterEncode():
        if find() == True:
            os.system('cls')
            cursor = con.execute("SELECT * from Files")
            for row in cursor:
               if row[1] == "decoded":
                   #btn3 = Label(frame, text = row[0], command = decodeFile(row[0]))
                   #btn3.grid()
                   global Key
                   print(row[0])
                   Key = int(input("key: "))
                   encodeFile(row[0])
            msg = messagebox.showinfo( "Done", "Done")

        
        else: frame.destroy()
        
    def btnEncode():
        global Key
        if find() == True:
            os.system('cls')

            check = 0
            cursor = con.execute("SELECT * from Files")
            for row in cursor:
               if row[1] == "decoded":
                   #label = Label(frame, text = row[0])
                   #label.grid()
                   print(row[0])
                   check = 1

            if check == 0:
                print("no data")
                a = input("new file? y/n: ").lower()
                if a == "y":
                    check = 1

            if check == 1: 
                try:
                    Key = int(input("Key (recomended K <= 20):"))

                except:
                    print()
                
                encodeFile(None)
                
                a = input("Continue encoding? y/n: ").lower()

                if a == "y":
                    btnEncode()
                else:
                    os.system('cls')

            
        else: frame.destroy()
    def btnActivate():
        if find() == True:
            os.system('cls')
            Activate()
            os.system('cls')
        else: frame.destroy()
    def btndata():
        if find() == True:
            os.system('cls')
            print("Data:")
            data()
        else: frame.destroy()
        
    def OTF():
        import subprocess
        if find() == True:
            os.system('cls')
            data()
            t = input("file location: ")
            programName = "notepad.exe"
            #fileName = "file.txt"
            subprocess.Popen([programName, t])
        else: frame.destroy()
    #button
    if find() == True:

        btn1 = Button(frame, text = "Master Decode", command = btnMasterDecode)
        btn1.grid(row=1, column=2, columnspan=23)
        #btn1.grid()

        btn2 = Button(frame, text = "Decode", command = btnDecode)
        btn2.grid(row=1, column=25, columnspan=23)
        #btn2.grid()

        btn3 = Button(frame, text = "Master Encode", command = btnMasterEncode)
        btn3.grid(row=2, column=2, columnspan=23)
        #btn3.grid()

        btn4 = Button(frame, text = "Encode", command = btnEncode)
        btn4.grid(row=2, column=25, columnspan=23)
        #btn4.grid()

        btn5 = Button(frame, text = "Text Commands", command = btnActivate)
        btn5.grid(row=4, column=10, columnspan=30)

        btn6 = Button(frame, text = "Data", command = btndata)
        btn6.grid(row=3, column=2, columnspan=10)

        btn7 = Button(frame, text = "Email File", command = email2)
        btn7.grid(row=3, column=25, columnspan=30)

        btn8 = Button(frame, text = "OTF", command = OTF)
        btn8.grid(row=3, column=14, columnspan=10)

        

    else: frame.destroy()

    

    #Centers Text
    #frame.pack()

    #kick off event loop
    mainloop()




check = 1
USBCheck = 1

while True:
    if find() == None and USBCheck == 1:
        os.system('cls')
        print("Insert USB Key")
        USBCheck = 0
    if find() == None:
        check = 1
        
    if check == 1:
        if find() == True:
            print("File:",find())
            #time.sleep(3)
            os.system('cls')

            count = 0
            for i in t:
                if count == 0:
                    ID = str(i.strip())
                if count == 1:
                    Name = str(i.strip())
                count = count + 1
            #print(ID, Name)

            cursor = con.execute("SELECT * from People")
            for row in cursor:
               DID = row[0]
               DName = row[1]
               if ID == str(DID):
                   if Name == str(DName):
                       #check = 1
                       while find() == True:
                           print("welcome:",DName)
                           print("If you don't want the usb folder opening go to settings and dissable the autorun/autoplay for usb drives")
                           #print("Remove cylindar")
                           #Activate()
                           GUI()
                           os.system('cls')
                       check = 0
                       USBCheck = 1
        else: continue








    
