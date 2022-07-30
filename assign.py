import re
list=[]
l=True
while l==True:
        print("Dashboard")
        print("Please press 1 to Sign up.")
        print("Please press 2 Login.")
        print("Please press 3 to Exit.")
        option=input("Enter your options [1/2/3]:")
        if(option!='1' and option!='2' and option!='3'):
                print("Enter Valid option.")
        elif(option=='1'):
                print("----------------------")
                print("Signup")
                print("----------------------")
                name=input("Enter your name:")
                password=input("Enter your password:")
                temp=1
                while temp:
                    if not re.search('[a-z]',password):
                        print("Password must contain number, alphabet and special characters")
                        break
                    elif not re.search('[@$#]',password):
                        print("Password must contain number, alphabet and special characters")
                        break
                    elif not re.search('[0-9]',password):
                        print("Password must contain number, alphabet and special characters")
                        break
                    else:
                        temp=0
                if temp==1:
                        continue
                password1=input("Confirm your password:")
                if(password==password1):
                        ph=input("Enter phone number:")
                        z=int(ph)
                        rev=0
                        x=0
                        while(x!=len(ph)):
                                rev=(rev*10)+z%10
                                z=z//10
                                x=x+1
                        if((len(ph)<=9) or (rev%10)!=0):
                                print("Invalid Ph number. Must contain 10 digits and starts with 0")
                        else:        
                                dob=input("Enter date of birth in format:DD/MM/YYYY:")
                                pattern='^\d{2}\/\d{2}\/\d{4}$'
                                if not (re.match(pattern,dob)):
                                        print("Invalid Date format")
                                        continue
                                list.append(name)
                                list.append(password)
                                list.append(ph)
                                list.append(dob)
                                print("You have sucessfully registered.")
                               

                else:
                        print("Password doesn't match.")
        elif(option=='2'):
                count=3
                counter=True
                while counter==True:
                        print("------------")
                        print("Login")
                        print("------------")
                        name1=input("Enter name:")
                        password1=input("Enter password")
                        count=count-1
                        
                        if count!=0:
                                a=list[0]
                                b=list[1]
                                c=list[2]
                                d=list[3]                              
                                if(a==name1 and b==password1):
                                                count=3
                                                print("You have sucessfully Signed In")
                                                print("Welcome,"+name)
                                                print("---------------------------------------------")
                                                print("Please press 1 for resetting your password.")
                                                print("Please press 2 for sign out.")
                                                ch=input("Press your option[1/2]:")
                                                if(ch!='1' and ch!='2'):
                                                        print("Invalid option")
                                                elif(ch=='1'):
                                                        p=input("Please enter your number:")
                                                        pas=input("Please enter your password:")
                                                        if(pas==b and p==c):
                                                        
                                                                db=open("user.txt","a")
                                                                newpass=input("Enter new password:")
                                                                newpas=newpass
                                                                temp=1
                                                                while temp:
                                                                    if not re.search('[a-z]',newpas):
                                                                        print("Password must contain number, alphabet and special characters")
                                                                        break
                                                                    elif not re.search('[@$#]',newpas):
                                                                        print("Password must contain number, alphabet and special characters")
                                                                        break
                                                                    elif not re.search('[0-9]',newpas):
                                                                        print("Password must contain number, alphabet and special characters")
                                                                        break
                                                                    else:
                                                                        temp=0
                                                                if temp==1:
                                                                        continue
                                                                list[1]=newpass
                                                                print("Password has been sucessfully reset")
                                                                
                                                                counter=False
                                                                break

                                                                
                                                        if(pas!=b or p!=c):
                                                                print("Password or Mobile doesn't match")
                                                                continue

                                                else:
                                                        print("Thank for using our application")
                                                        counter=False


                                
                                else:                                              

                                        print("Invalid Name or Password.")
                                                
                        else:
                                rc=True
                                while rc:
                                        print("______________________________________________________________")
                                        print("You have used maximum attempts of login")
                                        print("Please confirm following details to reset your password")
                                        p=input("Please confirm your mobile number")
                                        dob1=input("Please confirm you Date of Birth dd/mm/yyyy:")
                                        
                                        if(c==p and d==dob1):
                                                         db = open("user.txt","a")
                                                         newpas=input("Enter new password:")
                                                         password2=newpas
                                                         temp=1
                                                         while temp:
                                                             if not re.search('[a-z]',password2):
                                                                 print("Password must contain number, alphabet and special characters")
                                                                 break
                                                             elif not re.search('[@$#]',password2):
                                                                 print("Password must contain number, alphabet and special characters")
                                                                 break
                                                             elif not re.search('[0-9]',password2):
                                                                 print("Password must contain number, alphabet and special characters")
                                                                 break
                                                             else:
                                                                 temp=0
                                                                 
                                                         if temp==1:
                                                             continue
                                                         
                                                         
                                                         list[1]=newpas
                                                        
                                                         print("You have sucessfully resetted your password")
                                                         rc=False
                                                         break

                                        if(c!=p or d!=dob1):
                                                        print("Phone number or Date of Birth did not match")
                                                        continue



        else:
                print("Thank you for Using our application.")
                l=False
                break

