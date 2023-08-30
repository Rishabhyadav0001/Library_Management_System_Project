import mysql.connector as a
x=a.connect(host="localhost",user="root",passwd="rishabh")
c=x.cursor()
c.execute("create database if not exists library")
c.execute("use library")
c.execute("create table if not exists library_master(cardno char(10) primary key,name_of_person varchar(30),phone_no char(10),address varchar(30),dob date)")
c.execute("create table if not exists books(book_name varchar(30),book_no varchar(5) primary key,genre varchar(10),authors_name varchar(15),language varchar(15))")
c.execute("create table if not exists library_transaction(cardno char(10),foreign key(cardno) references library_master(cardno),book_name varchar(20),date_of_lend date,date_of_return date);") 
c.execute("create table if not exists buy_new_books(orderno varchar(6) primary key,name_of_book varchar(20),del_date date,price char(4))")
x.commit()
while True:
   print"**************1=create a new account***************"
   print"***************2=see the account info***************"
   print"***************3=update card holder info***************"
   print"***************4=delete the account***************"
   print"***************5=add new book***************"
   print"***************6=see books***************"
   print"***************7=update book details***************"
   print"***************8=delete book***************"
   print"***************9=lend a book***************"
   print"***************10=update return date***************"
   print"***************11=display lending history***************"
   print"***************12=order a new book***************"
   print"***************13=update order details***************"
   print"***************14=display ordering history***************"
   print"***************15=EXIT***************"
   ch=int(raw_input("enter your choice:-"))
   if ch==1:
        print"if you want go back press  1"
        print" "
        print"if you want continue press  2"
        print" "
        a=int(raw_input("enter your choice:"))
        if a==1:
            continue
        if a==2:
            print"FILL ALL PERSONAL DETAILS OF ACCOUNT HOLDER"
            cardno=str(raw_input("enter your preferrable card no:"))
            name_of_person=str(raw_input("Enter name (limit 30 characters):"))
            phone_no=str(raw_input("Enter phone no:"))
            address=str(raw_input("Enter the address (max 30 words):"))
            dob=str(raw_input("Enter the date of birth(yyyy-mm-dd):"))
            c.execute("insert into library_master values('"+cardno+"','"+name_of_person+"','"+phone_no+"','"+address+"','"+dob+"')")
            x.commit()
            print"ACCOUNT IS SUCCESSFULLY CREATED!!!"
   elif ch==2:
      cardno=str(raw_input("Enter card no:"))
      c.execute("select  *  from library_master where cardno='"+cardno+"'")
      for i in c:
         print i
   elif ch==3:
        print"press 1 to update name:"
        print" "
        print"press 2 to update phone no:"
        print" "
        print"press 3 to update address:"
        print" "
        print"press 4 to update date of birth:"
        print" "
        d=int(raw_input("Enter your choice:"))
        if d==1:
            c.execute("select * from library_master")
            for i in c:
                print i
            cardno=str(raw_input("Enter card no:"))
            name_of_person=str(raw_input("Enter new name:"))
            c.execute("update library_master set name_of_person='"+name_of_person+"' where cardno='"+cardno+"'")
            x.commit()
            print("*Name has been updated*")
            c.execute("select * from library_master")
            for i in c:
                print i
        elif d==2:
            c.execute("select * from library_master")
            for i in c:
                print i
            cardno=str(raw_input("Enter card no:"))
            phone_no=str(raw_input("Enter new phone no:"))
            c.execute("update library_master set phone_no='"+phone_no+"' where cardno='"+cardno+"'")
            x.commit()
            print"*Number has been updated*"
            c.execute("select * from library_master")
            for i in c:
                print i
        elif d==3:
            c.execute("select * from library_master")
            for i in c:
                print i
            cardno=str(raw_input("Enter card no:"))
            address=str(raw_input("Enter new address:"))
            c.execute("update library_master set address='"+address+"' where cardno='"+cardno+"'")
            x.commit()
            print"*Address has been updated*"
            c.execute("select * from library_master")
            for i in c:
                print i
        elif d==4:
         c.execute("select * from library_master")
         for i in c:
             print i
         cardno=str(raw_input("Enter card no:"))
         dob=str(raw_input("Enter new date of birth(yyyy-mm-dd):"))
         c.execute("update library_master set dob='"+dob+"' where cardno='"+cardno+"'")
         x.commit()
         print"*Date of birth has been updated*"
         c.execute("select * from library_master")
         for i in c:
             print i
   elif ch==4:
        c.execute("select * from library_master")
        for i in c:
                print i
        cardno=str(raw_input("Enter card no:"))
        c.execute("delete from library_master where cardno='"+cardno+"'")
        x.commit()
        print"*Removed succesfully*"
        c.execute("select * from library_master")
        for i in c:
                print i
   elif ch==5:
        print"FILL ALL BOOK DETAILS "
        book_name=str(raw_input("enter book  name:"))
        book_no=str(raw_input("Enter no (limit 5 characters):"))
        genre=str(raw_input("Enter genre:"))
        authors_name=str(raw_input("Enter the authors name (max 15 words):"))
        language=str(raw_input("Enter the language of book:"))
        c.execute("insert into books values('"+book_name+"','"+book_no+"','"+genre+"','"+authors_name+"','"+language+"')")
        x.commit()
        print"*Book added  succesfully*"
        for i in c:
            print i
   elif ch==6:
        c.execute("select * from books")
        for i in c:
                print i
   elif ch==7:
        print"press 1 to update Book name"
        print" "
        print"press 2 to update genre"
        print" "
        print"press 3 to update Author Name"
        print" "
        print"press 4 to update Language"
        print" "
        d=int(raw_input("Enter your choice:"))
        if d==1:
            c.execute("select * from books")
            for i in c:
                print i
            book_no=str(raw_input("Enter bookno:"))
            name_of_book=str(raw_input("Enter new name:"))
            c.execute("update books set book_name='"+name_of_book+"' where book_no='"+book_no+"'")
            x.commit()
            print"*Name has been updated*"
            c.execute("select * from books")
            for i in c:
                print i
        elif d==2:
            c.execute("select * from books")
            for i in c:
                print i
            book_no=str(raw_input("book no.:"))
            genre=str(raw_input("Enter new genre:"))
            c.execute("update books set genre='"+genre+"' where book_no='"+book_no+"'")
            x.commit()
            print"*Genre has been updated*"
            c.execute("select * from books")
            for i in c:
                print i
        elif d==3:
            c.execute("select * from books")
            for i in c:
                print i
            book_no=str(raw_input("Enter book no:"))
            author=str(raw_input("Enter new authors name:"))
            c.execute("update books set authors_name='"+author+"' where book_no='"+book_no+"'")
            x.commit()
            print"*Authors name has been updated*"
            c.execute("select * from books")
            for i in c:
                print i
        elif d==4:
            c.execute("select * from books")
            for i in c:
                print i
            book_no=str(raw_input("Enter boom no:"))
            language=str(raw_input("Enter new language:"))
            c.execute("update books set language='"+language+"' where book_no='"+book_no+"'")
            x.commit()
            print"*Language has been updated*"
            c.execute("select * from books")
            for i in c:
                print i
   elif ch==8:
        c.execute("select * from books")
        for i in c:
            print i
        book_no=str(raw_input("Enter book no:"))
        c.execute("delete from books where book_no='"+book_no+"'")
        x.commit()
        print"*Removed succesfully*"
        c.execute("select * from books")
        for i in c:
            print i
   elif ch==9:
        print"if you want go back press 1"
        print" "
        print"if you want continue press 2"
        print" "
        a=int(raw_input("enter your choice:"))
        if a==1:
            continue
        if a==2:
            cardno=str(raw_input("Enter card no:"))
            book_name=str(raw_input("Enter the name of the book:"))
            date_of_lend=str(raw_input("Enter date of lending(yyyy-mm-dd)"))
            date_of_return=str(raw_input("enter date of return(yyyy-mm-dd):"))    
            c.execute("insert into library_transaction values('"+cardno+"','"+book_name+"','"+date_of_lend+"','"+date_of_return+"')")
            x.commit()
   elif ch==10:
        print"if you want go back press 1"
        print" "
        print"if you want continue press 2"
        print" "
        a=int(raw_input("enter your choice:"))
        if a==1:
            continue
        if a==2:
            cardno=str(raw_input("Enter card no:"))
            date_of_return=str(raw_input("Enter date of returning(yyyy-mm-dd):"))
            c.execute("update library_transaction set date_of_return='"+date_of_return+"' where cardno='"+cardno+"'")
            x.commit()
   elif ch==11:
      cardno=str(raw_input("Enter card no:"))
      c.execute("select  *  from library_transaction where cardno='"+cardno+"'")
      for i in c:
       print i
   elif ch==12:
        orderno=str(raw_input("Enter the order no:"))
        name_of_book=str(raw_input("Enter the name of the book:"))
        del_date=str(raw_input("enter the expected delivery date of books(yyyy-mm-dd):"))
        price=str(raw_input("Enter the price of the book"))
        c.execute("insert into buy_new_books values('"+orderno+"','"+name_of_book+"','"+del_date+"','"+price+"')")
        x.commit()
   elif ch==13:
        print"press 1 to update name of book"
        print" "
        print"press 2 to update delivery date"
        print" "
        print"press 3 to update price"
        print" "
        d=int(raw_input("Enter your choice:"))
        if d==1:
            c.execute("select * from buy_new_books")
            for i in c:
                print i
            orderno=str(raw_input("Enter order no:"))
            name_of_book=str(raw_input("Enter new name:"))
            c.execute("update buy_new_books set name_of_book='"+name_of_book+"' where orderno='"+orderno+"'")
            x.commit()
            print"*Name has been updated*"
            c.execute("select * from buy_new_books")
            for i in c:
                print i
        elif d==2:
            c.execute("select * from buy_new_books")
            for i in c:
                print i
            orderno=str(raw_input("Enter order no:"))
            del_date=str(raw_input("Enter new delivery date(yyyy-mm-dd):"))
            c.execute("update buy_new_books set del_date='"+del_date+"' where orderno='"+orderno+"'")
            x.commit()
            print"*Delivery date has been updated*"
            c.execute("select * from buy_new_books")
            for i in c:
                print i
        elif d==3:
            c.execute("select * from buy_new_books")
            for i in c:
                print i
            orderno=str(raw_input("Enter order no:"))
            price=str(raw_input("Enter new price:"))
            c.execute("update buy_new_books set price='"+price+"' where orderno='"+orderno+"'")
            x.commit()
            print"*Price has been updated*"
            c.execute("select * from buy_new_books")
            for i in c:
                print i
   elif ch==14:
        orderno=str(raw_input("Enter order number:"))
        c.execute("select * from buy_new_books where orderno='"+orderno+"'")
        for i in c:
            print i      
   else:
       break 
 


               
