import re
import re
from datetime import date
import datetime
global incr
global list1, list2, list3, list4
lista=[]
def checkout(pp,s):
        if s=='Self Pickup':
                print(f'The payable amount is {pp}.')
                print("-------------------------------------------------------------")
                po=input("Do you wish to proceed with the order [y/n]:")
                if po=='y' or po=='Y':
                        inc='A00'+str(incr)
                        list2.append(inc)
                        today=date.today()
                        dt=today.strftime("%d/%m/%Y")
                        list2.append(dt)
                        list2.append(s)
                        list2.append(pp)
                        list4.append(inc)
                        list4.append(dt)
                        list4.append(s)
                        list4.append(pp)
                        while True:
                                dt=input("Please enter the Date of Pick up (DD/MM/YYYY):")
                                pattern='^\d{2}\/\d{2}\/\d{4}$'
                                if not re.match(pattern,dt):
                                                print("****Invalid Date****")
                                                continue
                                tm=input("Plese enter the time of Pick up [24-hr Format] (HH:MM):")
                                pat='^\d{2}\:\d{2}$'
                                if not re.match(pat,tm):
                                        print("****Invalid Time****")
                                        continue
                                break
                        no=input("Please enter Name of Person:")
                        print("-------------------------------------------------------------")
                        print(f"Your order Id is {inc}")
                        print("Thank You for entering details. Your Booking is confirmed.")
                        print("-------------------------------------------------------------")
        else:
                print(f'The payble amount is {pp}. There will be additional delivery charges')
                print("----------------------------------------------------------------------")
                while True:
                        dt=input("Please enter the Date of Delivery (DD/MM/YYYY):")
                        pattern='^\d{2}\/\d{2}\/\d{4}$'
                        if not re.match(pattern,dt):
                                        print("****Invalid Date****")
                                        continue
                        tm=input("Plese enter the time of Delivery [24-hr Format] (HH:MM):")
                        pat='^\d{2}\:\d{2}$'
                        if not re.match(pat,tm):
                                print("****Invalid Time****")
                                continue
                        break
                dist=input("Enter distance from the resturant in KM:")
                if dist>'0' and dist<='2':
                        dc=5
                elif dist>'2'and dist<='5':
                        dc=10
                elif dist>'10':
                        dc=18
                else:
                        print("-----------------------------------------------------------------------------------------")
                        print("No delivery provided if distance is more than 10 KM. Please proceed with pick up option")
                        pick='Self Pickup'
                        order(pick)
                        return
                        
                pp=pp+dc
                print("-------------------------------------------------------------")
                print(f'The payable amount is {pp} including delivery charge {dc}')
                print("-------------------------------------------------------------")
                po=input("Do you wish to proceed with the order [y/n]:")
                if po=='y' or po=='Y':
                        inc='A00'+str(incr)
                        list3.append(inc)
                        today=date.today()
                        dt=today.strftime("%d/%m/%Y")
                        list3.append(dt)
                        list3.append(s)
                        list3.append(pp)
                        list4.append(inc)
                        list4.append(dt)
                        list4.append(s)
                        list4.append(pp)
                        print(f"Your order Id is {inc}")
                        print("Thank You for your order. Your Order is confirmed.")
                        
                        print("-------------------------------------------------------------")
                
                
                
        
def drinks(pay,s): 
        pp=pay
        print("Enter 1 for coffee       Aud 2")
        print("Enter 2 for colddrink    Aud 4")
        print("Enter 3 for shake        Aud 6")
        print("Enter 4 for checkout")
        l=True
        while l:
                o=input("Enter the ID of Drinks you would like to order: ")
                if o=='1':
                        pp=pp+2
                elif o=='2':
                        pp=pp+4
                elif o=='3':
                        pp=pp+6
                elif o=='4':
                                tax=0.10*pp
                                pp=tax+pp
                                print("-------------------------------------------------------------")
                                print(f'The total payable amount is {pp} with service charge {tax}')
                                po=input("Do you wish to proceed with the order [y/n]:")
                                if po=='y' or po=='Y':
                                        inc='A00'+str(incr)
                                        list1.append(inc)
                                        today=date.today()
                                        dt=today.strftime("%d/%m/%Y")
                                        list1.append(dt)
                                        list1.append("Dine In")
                                        list1.append(pp)
                                        list4.append(inc)
                                        list4.append(dt)
                                        list4.append(s)
                                        list4.append(pp)
                                        while True:
                                                dt=input("Please enter the Date of Booking (DD/MM/YYYY):")
                                                pattern='^\d{2}\/\d{2}\/\d{4}$'
                                                if not re.match(pattern,dt):
                                                                print("****Invalid Date****")
                                                                continue
                                                tm=input("Plese enter the time of Booking [24-hr Format] (HH:MM):")
                                                pat='^\d{2}\:\d{2}$'
                                                if not re.match(pat,tm):
                                                        print("****Invalid Time****")
                                                        continue
                                                break
                                        no=input("Please enter Number of People:")
                                        print(f"Your order Id is {inc}")
                                        print("Thank You for entering details. Your Booking is confirmed.")
                                        print("-------------------------------------------------------------")


                                l=False
                                break
                else:
                        print("Invalid Option")
        
def order(s):
        l=True
        pay=0
        while l:
                ord=input("Enter the ID of item you would like to order: ")
                if ord=='1':
                        pay=pay+2
                        
                elif ord=='2':
                        pay=pay+4
                        
                elif ord=='3':
                        pay=pay+6
                        
                elif ord=='4':
                        pay=pay+8
                        
                elif ord=='5':
                        pay=pay+10
                        
                elif ord=='6':
                        pay=pay+20
                        
                elif ord=='7':
                        if s=='Dine In':
                                drinks(pay,s)
                                l=False
                                break;
                        else:
                                checkout(pay,s)
                                break
                        
                else:
                        print("Invalid item ID")
list1=[]
list2=[]
list3=[]
list4=[]
incr=0
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
                                py=2022
                                db=int(dob[-4:])
                                age=py-db
                                if age<18:
                                    print("Age below 18")
                                    continue
                                address=input("Enter Address:") 
                                lista.append(name)
                                lista.append(password)
                                lista.append(ph)
                                lista.append(dob)
                                lista.append(address)
                                print(lista)
                                print("You have sucessfully registered.")
                               

                else:
                        print("Password doesn't match.")
        elif(option=='2'):
                counter=True
                while counter==True:
                        print("------------")
                        print("Login")
                        print("------------")
                        name1=input("Enter name:")
                        password1=input("Enter password:")
                        a=lista[0]
                        b=lista[1]
                        c=lista[2]
                        d=lista[3]
                        e=lista[4]                              
                        if(a==name1 and b==password1):
                                print("welcome, "+a+"!!")
                                while True:
                                        print("-------------------------------------------------------------")
                                        print("Please enter 2.1 to start Ordering")
                                        print("Please enter 2.2 to print statistics")
                                        print("Please enter 2.3 for logout")
                                        choice=input("Enter your option:")
                                        print("-------------------------------------------------------------")
                                        if choice=='2.1':
                                                incr=incr+1
                                                print("Press 1 for Dine in")
                                                print("Press 2 for Order Online")
                                                print("Press 3 to go to Previous Page")
                                                select=input("Enter your option:[1/2/3]:")
                                                print("-------------------------------------------------------------")
                                                if (select!='1' and select!='2' and select!='2'):
                                                        print("Invalid Option.")
                                                        continue
                                                elif select=='1':
                                                        print("-------------------------------------------------------------")
                                                        print("{:<5} {:<15} {:<10}".format('ID','Name','Price'))
                                                        print("{:<5} {:<15} {:<10}".format('1','Noodles','AUD 2'))
                                                        print("{:<5} {:<15} {:<10}".format('2','Sandwich','AUD 4'))
                                                        print("{:<5} {:<15} {:<10}".format('3','Dumpling','AUD 6'))
                                                        print("{:<5} {:<15} {:<10}".format('4','Muffins','AUD 8'))
                                                        print("{:<5} {:<15} {:<10}".format('5','Pasta','AUD 10'))
                                                        print("{:<5} {:<15} {:<10}".format('6','Pizza','AUD 20 '))
                                                        print("{:<5} {:<15}".format('7','Drinks'))
                                                        print("-------------------------------------------------------------")
                                                        typ1='Dine In'
                                                        order(typ1)
                                                        continue
                                                elif select=='2':
                                                        print("Press 1 for Self Pickup")
                                                        print("Press 2 for Home Delivery")
                                                        print("Press 3 to go to previous Menu")
                                                        s=input("Enter your choice[1/2/3]:")              
                                                        if s=='1':
                                                                print("-------------------------------------------------------------")
                                                                print("{:<5} {:<15} {:<10}".format('ID','Name','Price'))
                                                                print("{:<5} {:<15} {:<10}".format('1','Noodles','AUD 2'))
                                                                print("{:<5} {:<15} {:<10}".format('2','Sandwich','AUD 4'))
                                                                print("{:<5} {:<15} {:<10}".format('3','Dumpling','AUD 6'))
                                                                print("{:<5} {:<15} {:<10}".format('4','Muffins','AUD 8'))
                                                                print("{:<5} {:<15} {:<10}".format('5','Pasta','AUD 10'))
                                                                print("{:<5} {:<15} {:<10}".format('6','Pizza','AUD 20 '))
                                                                print("-------------------------------------------------------------")
                                                                print("{:<5} {:<15}".format('7','checkout'))
                                                                typ2='Self Pickup'
                                                                order(typ2)
                                                                continue
                                                        elif s=='2':
                                                                if lista[4]=='':
                                                                        print("You need to enter address for Delivery option.")
                                                                        add=input("Enter address:")
                                                                        lista[4]=add
                                                                print("-------------------------------------------------------------")
                                                                print("{:<5} {:<15} {:<10}".format('ID','Name','Price'))
                                                                print("{:<5} {:<15} {:<10}".format('1','Noodles','AUD 2'))
                                                                print("{:<5} {:<15} {:<10}".format('2','Sandwich','AUD 4'))
                                                                print("{:<5} {:<15} {:<10}".format('3','Dumpling','AUD 6'))
                                                                print("{:<5} {:<15} {:<10}".format('4','Muffins','AUD 8'))
                                                                print("{:<5} {:<15} {:<10}".format('5','Pasta','AUD 10'))
                                                                print("{:<5} {:<15} {:<10}".format('6','Pizza','AUD 20 '))
                                                                print("{:<5} {:<15}".format('7','checkout'))
                                                                print("-------------------------------------------------------------")
                                                                typ3='Delivery'
                                                                order(typ3)
                                                                continue
                                                        else:
                                                                break
                                                        
                                                else:
                                                        break
                                        elif choice=='2.2':
                                                while True:
                                                        print("1-All Dine in Orders.")
                                                        print("2-All Pick up Orders")
                                                        print("3-All Deliveries")
                                                        print("4-All Orders")
                                                        print("5-Total amount spent on All Orders")
                                                        print("6-Go to previous menu")
                                                        orderss=input("Please Enter the option to print the statistics:")
                                                        if orderss=='1':
                                                                print("-------------------------------------------------------------------")
                                                                start=0
                                                                end=(len(list1))
                                                                print("{:<8} {:<15} {:<10} {:<10}".format('ID','Date','Type','Price[Aud]'))
                                                                while start<end:
                                                                        print("{:<8} {:<15} {:<10} {:<10}".format(list1[start],list1[start+1],list1[start+2],list1[start+3]))
                                                                        start=start+4
                                                                print("-------------------------------------------------------------------")
                                                                continue
                                                        elif orderss=='2':
                                                                start=0
                                                                end=(len(list2))
                                                                print("--------------------------------------------------------------------")
                                                                print("{:<8} {:<15} {:<15} {:<10}".format('ID','Date','Type','Price[Aud]'))
                                                                while start<end:
                                                                        print("{:<8} {:<15} {:<15} {:<10}".format(list2[start],list2[start+1],list2[start+2],list2[start+3]))
                                                                        start=start+4

                                                                print("--------------------------------------------------------------------")
                                                                continue
                                                        elif orderss=='3':
                                                                start=0
                                                                end=(len(list3))
                                                                print("--------------------------------------------------------------------")
                                                                print("{:<8} {:<15} {:<15} {:<10}".format('ID','Date','Type','Price[Aud]'))
                                                                while start<end:
                                                                        print("{:<8} {:<15} {:<15} {:<10}".format(list3[start],list3[start+1],list3[start+2],list3[start+3]))
                                                                        start=start+4
                                                                print("--------------------------------------------------------------------")
                                                                continue
                                                        elif orderss=='4':
                                                                end=(len(list4))-1
                                                                print(list4,end)
                                                                print("--------------------------------------------------------------------")
                                                                print("{:<8} {:<15} {:<10} {:<15}".format('ID','Date','Type','Price[Aud]'))
                                                                while end>-1:
                                                                        print("{:<8} {:<15} {:<15} {:<10}".format(list4[end-3],list4[end-2],list4[end-1],list4[end]))
                                                                        end=end-4
                                                                print("--------------------------------------------------------------------")
                                                                continue
                                                        elif orderss=='5':
                                                                start=0
                                                                end=(len(list4))
                                                                totalp=0
                                                                while start<end:
                                                                        totalp=totalp+list4[start+3]
                                                                        start=start+4
                                                                print("--------------------------------------------------------------------")      
                                                                print(f"Total amount spent on all orders: {totalp}")
                                                                print("--------------------------------------------------------------------")
                                                                continue
                                                        elif orderss=='6':
                                                                break
                                                                
                                                        else:
                                                                print("Invalid option")
                                                                continue
                                                        
                                        elif choice=='2.3':
                                                break

                                        else:
                                                print("Invalid Option")
                                
                        else:                                              

                            print("Invalid Name or Password.")
                                        
        else:
                print("Thank you for Using our application.")
                l=False
                break

