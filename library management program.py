import mysql.connector as a
con=a.connect(host="localhost",user="root",passwd="123456",database="l1")
def stu():
    def issueb():
        n=input("Enter Scholar number : ")
        r=input("Enter Name : ")
        q=input("Enter Class : ")
        w=input("Enter Section : ")
        d=input("Enter Issueing Book Data : ")
        co=input("Enter Book Code : ")
        a="insert into s_issue values(%s,%s,%s,%s,%s,%s)"
        data=(n,r,q,w,d,co)
        c=con.cursor()
        c.execute(a,data)
        con.commit()
        print(">------------------------------------------------------------------<")
        print("Book issued to : ",r,"--",n)
        bookup(co,-1)

    def submitb():
        n=input("Enter Scholar number : ")
        r=input("Enter Name : ")
        q=input("Enter Class : ")
        w=input("Enter Section : ")
        d=input("Enter Submiting Book Data : ")
        co=input("Enter Book Code : ")
        a="insert into s_submit values(%s,%s,%s,%s,%s,%s)"
        data=(n,r,q,w,d,co)
        c=con.cursor()
        c.execute(a,data)
        con.commit()
        print(">------------------------------------------------------------------<")
        print("Book Submitted from : ",r,"--",n)
        bookup(co,1)

    def bookup(co,u):
        
        a="select TOTAL from books where BCODE=%s"
        data=(co,)
        c=con.cursor()
        c.execute(a,data)
        myresult=c.fetchone()
        t=myresult[0]+u
        sql="update books set TOTAL = %s where BCODE = %s"
        d=(t,co)
        c.execute(sql,d)
        con.commit()
        main()

    def dispbook():
        
        a="select *from books"
        c=con.cursor()
        c.execute(a)
        myresult=c.fetchall()
        for i in myresult:
            
            print("Book Name : ",i[0])
            print("Book Code : ",i[1])
            print("Total : ",i[2])
            print(">------------------------<")
        main()

    def main():
        
        print('''
                                  Welcome!!!!!!
                    To STUDENT Nosegay Public School Library
        1. ISSUE BOOK
        2. SUBMIT BOOK
        3. DISPLAY BOOKS
        ''')
        cho=input("Enter Task No. : ")
        print(">--------------------------------------------------------------------<")           
        if cho=='1' :
            issueb()
        elif cho=='2' :
            
            submitb()
        elif cho=='3' :
            
            dispbook()
        else:
            print("wrong choice entered!!!!!!!!")
        main()
    
    main()

def pp():
    def addbook():
        bn=input("Enter BOOK NAME : ")
        c=input("Enter BOOK CODE : ")
        t=input("TOTAL BOOKS : ")
        s=input("Enter SUBJECT : ")
        data=(bn,c,t,s)
        sql='insert into books values(%s,%s,%s,%s)'
        c=con.cursor()
        c.execute(sql,data)
        con.commit()
        print(">-------------------------------------------------------------------<")
        print("Data ENTERED Successfully")
        main()

    def issueb():
        n=input("Enter Name : ")
        r=input("Enter Reg No : ")
        co=input("Enter Book Code : ")
        d=input("Enter Data in dd-mm-yyyy : ")
        a="insert into issue values(%s,%s,%s,%s)"
        data=(n,r,co,d)
        c=con.cursor()
        c.execute(a,data)
        con.commit()
        print(">------------------------------------------------------------------<")
        print("Book issued to : ",n)
        bookup(co,-1)

    def submitb():
        n=input("Enter Name : ")
        r=input("Reg No : ")
        co=input("Book Code : ")
        d=input("Enter Data in dd-mm-yyyy : ")
        a="insert into submit values(%s,%s,%s,%s)"
        data=(n,r,co,d)
        c=con.cursor()
        c.execute(a,data)
        con.commit()
        print(">------------------------------------------------------------------<")
        print("Book Submitted from : ",n)
        bookup(co,1)

    def bookup(co,u):
        a="select TOTAL from books where BCODE=%s"
        data=(co,)
        c=con.cursor()
        c.execute(a,data)
        myresult=c.fetchone()
        t=myresult[0]+u
        sql="update books set TOTAL = %s where BCODE = %s"
        d=(t,co)
        c.execute(sql,d)
        con.commit()
        main()

    def dbook():
        ac=input("Enter Book Code : ")
        a="delete from books where BCODE = %s"
        data=(ac,)
        c=con.cursor()
        c.execute(a,data)
        con.commit()
        main()

    def dispbook():
        a="select *from books"
        c=con.cursor()
        c.execute(a)
        myresult=c.fetchall()
        for i in myresult:
            print("Book Name : ",i[0])
            print("Book Code : ",i[1])
            print("Total : ",i[2])
            print("Subject : ",i[3])
            print(">------------------------<")
        main()
    def main():
        print('''
                                      LIBRARY MANAGER

        1.ADD BOOK
        2.ISSUE BOOK
        3.SUBMIT BOOK
        4.DELETE BOOK
        5.DISLAY BOOKS
        ''')
        choice=input("Enter Task No. : ")
        print(">-------------------------------------------------------------------<")
        if(choice=='1'):
            addbook()
        elif(choice=='2'):
            issueb()
        elif(choice=='3'):
            submitb()
        elif(choice=='4'):
            dbook()
        elif(choice=='5'):
            dispbook()
        else:
            print("wrong choice.......")
            main()

    def pswd():
        ps=input("Enter Password : ")
        if ps=="py123":
            main()
        else:
            print("wrong Password")
            pswd()
    pswd()
    
print('''         WELCOME TO NOSEGAY PUBLIC SCHOOL, SRI GANGANAGAR (Raj.)

                   >---------------------LIBRARY-----------------<

        PRESS 1                                                     PRESS 2
        STUDENT                                              ADMINISTRATOR OR TEAHER
''')
qq=input("ENTER WHO ARE YOU : ")
if qq=='1':
    stu()
elif qq=='2':
    pp()
    
