#JAI SHREE RAM

print("\t\t\t\t----------------------")
print("\t\t\t\tRailway ticket counter")
print("\t\t\t\t----------------------\n\n")

def project():
    print("1. To BOOKING TICKET")
    
    
    option=input("Enter your choice =")
    while(option.isdigit()==True):
        if(option=="1"):
            book_ticket()
            break
        elif(option=="2"):

            cancle()
        elif(option=="3"):
            print("seat_enquiry()")
        else:
            print("\n\n************************PLEASE GIVE THE RIGHT INPUT************************")
            print("\n\tplease choose from the given option's\n\n")
            project()
    
    while(option.isdigit()!=True):
        print("\n\n************************PLEASE GIVE THE RIGHT INPUT************************")
        print("\n\tplease write the digit not variable\n\n")
        project()

# BOOKING TICKETS

def book_ticket():
    print("**************************************")
    print("You pressed 1 in the given option's\nWhich is of BOOKING TICKETS")
    print("**************************************\n\n")
    print("1. To Conferm It")
    print("2. To Select Another Option's")
    select=input("Enter your choice =")
    select2=int(select)
    while(select.isdigit()==True):
        if(select2==2)       :
            print("The OPTIOMS are\n")
            project()
        if(select2<1 or select2>2):
            print("\n\n************************PLEASE GIVE THE RIGHT INPUT************************")
            print("\n\tplease write the digit not variable\n\n")
            book_ticket()
        if(select2==1):           
            
#####################    PASSENGER First NAME    #####################################  
            print("\n______________________________________________________________")
            name=input("\n\nFirst name Of Passenger=")
            while(name.isalpha()==True):
                if(len(name)>2):
                    break
                else:
                    print("Please Give The correct Name")
                    name=input("First name Of Passenger=")
                    pass
            while(name.isalpha()!=True):
                print("\n\n************************PLEASE GIVE THE RIGHT INPUT************************")
                print("\n\tplease write the Character's not digit\n\n")
                name=input("First name Of Passenger=")
                if(len(name)>2):
                    break
                else:
                    print("Please Give The Full Name")
                    name=input("First name Of Passenger=")
                    
#####################    PASSENGER Second NAME    #####################################  
            print("\n______________________________________________________________")
            name2=input("\n\nSecond name Of Passenger=")
            while(name2.isalpha()==True):
                if(len(name2)>2):
                    break
                else:
                    print("Please Give The correct Name")
                    name2=input("Second name Of Passenger=")
                    pass
            while(name2.isalpha()!=True):
                print("\n\n************************PLEASE GIVE THE RIGHT INPUT************************")
                print("\n\tplease write the Character's not digit\n\n")
                name2=input("Second name Of Passenger=")
                if(len(name2)>2):
                    break
                else:
                    print("Please Give The correct Name")
                    name2=input("Second name Of Passenger=")
               
            
#####################    age    ################################################
            print("\n______________________________________________________________")
            age=input("\n\nAge of Passenger :")   
            while(age.isdigit()==True):
                age2=int(age)
                if(age2>0 and age2<=110):
                    break
                else:
                    print("\n\n************************PLEASE GIVE THE RIGHT INPUT************************")
                    print("\n\tPlease the Valid age")
                    age=input("Age of Passenger :")
                    pass
            while(age.isdigit()!=True):
                print("\n\n************************PLEASE GIVE THE RIGHT INPUT************************")
                print("\n\tplease write the Character's not digit\n\n")
                age=input("Age of Passenger :")   
                age2=int(age)
                if(age2>0 and age2<=110):
                    break
                else:
                    print("\n\n************************PLEASE GIVE THE RIGHT INPUT************************")
                    print("\n\tPlease the Valid age")
                    age=input("Age of Passenger :")
                    
            
 #####################    Gender    ############################################       

            print("\n______________________________________________________________")
            gender=input("\n\nGender of passenger Male/Female/Transgender (M/F/T) : ")       
            while(gender.isalpha()==True):
                if(gender=="M" or gender=="m" or gender=="Male" or gender=="male"):
                    break
                elif(gender=="F" or gender=="f" or gender=="Female" or gender=="female"):
                    break   
                elif(gender=="T" or gender=="t" or gender=="Transgender" or gender=="transgender"):
                    break
                else:
                    print("\n\n************************PLEASE GIVE THE RIGHT INPUT************************")
                    print("\n\tPlease the Valid Gender")
                    gender=input("Gender of passenger Male/Female/Transgender (M/F/T) : ")  
                    pass
            while(gender.isalpha()!=True):
                print("\n\n************************PLEASE GIVE THE RIGHT INPUT************************")
                print("\n\tplease write the degit not Character's\n\n")
                gender=input("Gender of passenger Male/Female/Transgender (M/F/T) : ")  
                if(gender=="M" or gender=="m" or gender=="Male" or gender=="male"):
                    break
                elif(gender=="F" or gender=="f" or gender=="Female" or gender=="female"):
                    break   
                elif(gender=="T" or gender=="t" or gender=="Transgender" or gender=="transgender"):
                    break
                else:
                    print("\n\n************************PLEASE GIVE THE RIGHT INPUT************************")
                    print("\n\tPlease the Valid Gender")
                    gender=input("Gender of passenger Male/Female/Transgender (M/F/T) : ")  

#####################    from    ###############################################     
            print("\n______________________________________________________________")
            from1=input("\n\nEnter the starting point : ")
            while(from1.isalpha()==True):
                if(len(from1)>1):
                    break
                else:
                    print("\n\n************************PLEASE GIVE THE RIGHT INPUT************************")
                    print("\n\tPlease the Valid Name of place")
                    from1=input("Enter the starting point : ")
                    pass
            while(from1.isalpha()!=True):
                print("\n\n************************PLEASE GIVE THE RIGHT INPUT************************")
                print("\n\tplease write the Character's not digit\n\n")
                from1=input("Enter the starting point : ")
                if(len(from1)>1):
                    break
                else:
                    print("\n\n************************PLEASE GIVE THE RIGHT INPUT************************")
                    print("\n\tPlease the Valid Name of place")
                    from1=input("Enter the starting point : ")
                    
                
#####################    to    #################################################      
            print("\n______________________________________________________________")        
            to=input("\n\nEnter the ending point : ")
            while(to.isalpha()==True):
                if(len(to)>1):
                    break
                else:
                    print("\n\n************************PLEASE GIVE THE RIGHT INPUT************************")
                    print("\n\tPlease the Valid Name of place")
                    to=input("Enter the ending point : ")
                    pass
            while(to.isalpha()!=True):
                print("\n\n************************PLEASE GIVE THE RIGHT INPUT************************")
                print("\n\tplease write the Character's not digit\n\n")
                to=input("Enter the ending point : ")
                if(len(to)>1):
                    break
                else:
                    print("\n\n************************PLEASE GIVE THE RIGHT INPUT************************")
                    print("\n\tPlease the Valid Name of place")
                    to=input("Enter the ending point : ")
                
#####################    distance    ###########################################
              
            print("\n______________________________________________________________")
            print("\n\nWhat is the distance between ",from1," to ",to)
            distance=input("write the total distance : ")
            while(distance.isdigit()==True):
                distance2=int(distance)
                if(distance2>=0 and distance2<=25000):
                    break
                else:
                    print("\n\n************************PLEASE GIVE THE RIGHT INPUT************************")
                    print("What is the distance between ",from1," to ",to)
                    distance=input("write the total distance : ")
                    pass
            while(distance.isdigit()!=True):
                print("What is the distance between ",from1," to ",to)
                distance=input("write the total distance : ")
                while(distance.isdigit()==True):
                    distance2=int(distance)
                if(distance2>=0 and distance2<=25000):
                    break
                else:
                    print("\n\n************************PLEASE GIVE THE RIGHT INPUT************************")
                    print("What is the distance between ",from1," to ",to)
                    distance=input("write the total distance : ")
                    
#####################    Journey amount    ###########################################
            print("\n______________________________________________________________")
            amount=input("\n\nWrite the Cabine (AC1 / AC2 / AC3 / SLEEPER(S) /GENERAL(G)) : ")
            distance1=float(distance)
            while(amount.isalnum()==True):
                if(amount=="ac1" or amount=="AC1"):
                    total=distance1*2.30
                    break
                elif(amount=="ac2" or amount=="AC2"):
                    total=distance1*2.15
                    break
                elif(amount=="ac3" or amount=="AC3"):
                    total=distance1*1.80
                    break
                elif(amount=="Sleeper" or amount=="sleeper" or amount=="s" or amount=="S" or amount=="SLEEPER"):
                    total=distance1*1.48
                    break
                elif(amount=="General" or amount=="general" or amount=="GENERAL" or amount=="g" or amount=="G"):
                    total=distance1*1.17
                    break
                else:
                    print("\n\n************************PLEASE GIVE THE RIGHT INPUT************************")
                    print("\n\tPlease write the valid Coach name")
                    amount=input("Write the Cabine (AC1 / AC2 / AC3 / SLEEPER(S) /GENERAL(G)) : ")
                    pass
            while(amount.isalnum()!=True):
                if(amount=="ac1" or amount=="AC1"):
                    total=distance1*2.30
                    break
                elif(amount=="ac2" or amount=="AC2"):
                    total=distance1*2.15
                    break
                elif(amount=="ac3" or amount=="AC3"):
                    total=distance1*1.80
                    break
                elif(amount=="Sleeper" or amount=="sleeper" or amount=="s" or amount=="S" or amount=="SLEEPER"):
                    total=distance1*1.48
                    break
                elif(amount=="General" or amount=="general" or amount=="GENERAL" or amount=="g" or amount=="G"):
                    total=distance1*1.17
                    break
                else:
                    print("\n\n************************PLEASE GIVE THE RIGHT INPUT************************")
                    print("\n\tPlease write the valid Coach name")
                    amount=input("Write the Cabine (AC1 / AC2 / AC3 / SLEEPER(S) /GENERAL(G)) : ")
                    
                    
                    
#__________________________________________OUTPUT_________________________________________________________
            
            print("\n\nName of Passenger      : ",name,name2)
            print("\nAge of Passenger         : ",age)
            if(gender=="M" or gender=="m" or gender=="Male" or gender=="male"):
                print("\nGender of Passenger    : Male")
            if(gender=="F" or gender=="f" or gender=="Female" or gender=="female"):
                print("\nGender of Passenger    : Female")
            if(gender=="T" or gender=="t" or gender=="Transgender" or gender=="transgender"):
                print("\nGender of Passenger    : Transgender")

            print("\nStarting journer point   : ",from1)
            print("\nDestination of journey   : ",to)
            print("\nTotal distance to travel : ",distance,"km")
        
            if(amount=="ac1" or amount=="AC1"):
                print("\nThe coach is             : AC1")
            if(amount=="ac2" or amount=="AC2"):
                print("\nThe coach is             : AC2")
            if(amount=="ac3" or amount=="AC3"):
                print("\nThe coach is             : AC3")
            if(amount=="Sleeper" or amount=="sleeper" or amount=="s" or amount=="S" or amount=="SLEEPER"):
                print("\nThe coach is             : SLEEPER")
            if(amount=="General" or amount=="general" or amount=="GENERAL" or amount=="g" or amount=="G"):
                print("\nThe coach is             : GENERAL")
            print("\nAmount to pay            : ",total)        
project()
