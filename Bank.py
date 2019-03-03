import mysql.connector as con
db=con.connect(host="localhost",user="root",password="root",database="mydb")
cur=db.cursor()
st=1
while(st==1):
    print"Press 1 to register"
    print"Press 2 to login:"
    ip=input("Enter yor choice:")
    if(ip==1):
        user_id=raw_input("Enter the user id of the customer:")
        user_name=raw_input("Enter the name of the customer:")
        user_acc=raw_input("Enter the account number of the customer:")
        user_add=raw_input("Enter the address of the customer:")
        user_pass=raw_input("Enter the password of the user:")
        q="insert into bank(userid, Name, accontno, address, password, balance) values(%s,%s,%s,%s,%s,%s)"
        v=[user_id,user_name,user_acc,user_add,user_pass,0]
        cur.execute(q,v)
        db.commit()
    if(ip==2):
        user_acc=raw_input("Enter the account number of the user:")
        usp="select accontno from bank"
        cur.execute(usp)
        d=cur.fetchall()
        
        for i in range(len(d)):
            if(user_acc==d[i][0]):
                acc=user_acc
        if(acc==user_acc):
           passw=raw_input("Enter the password of the user")
           pass_w="select password from bank"
           cur.execute(pass_w)
           d=cur.fetchall()
           pa=d[0][0]
           if(pa==passw):
               print"Login successfull"
               print"press 1 to add money in the account:"
               print"Press 2 to tranfer money from the account:"
               print"Press 3 to print the passbook:"
               print"Press 4 to exit :)"
               log=input("Enter your choice:")
               if(log==1):
                   mon=input("Enter the amount of money you want to add:")
                   fet_mo="select balance from bank where accontno="+user_acc+""
                   cur.execute(fet_mo)
                   fetc_mo=cur.fetchone()
                   amt=int(fetc_mo[0])+mon
                   amt=str(amt)
                   print amt
                   quee="update bank set balance='"+amt+"' where accontno="+user_acc+""
                   cur.execute(quee)
                   db.commit()
               if(log==3):
                   que="select balance from bank where accontno="+user_acc+""
                   cur.execute(que)
                   que_bal=cur.fetchone()
                   db.commit()
                   print "The balance is",que_bal[0]
               if(log==4):
                   break
        else:
           print"wrong username"
    st=input("Press 1 to continue:")
print"Thanks"
    
