class phone_Contacts:                                                                                   
    
    def __init__(self,Firstname,Lastname,Phone_number,Email_ID,Groups,DOB):                             
        self.firstname=Firstname
        self.lastname=Lastname
        self.phonenumber=Phone_number
        self.emailid=Email_ID
        self.groups=Groups
        self.dob=DOB
        
        
    def open_phcontacts(self):
        print("Phone Contacts")
    
        
    def firstname_verification(self):
        if type(self.firstname) == str:
            if len(self.firstname) <= 15:                                                                                
                print("Firstnameame verified")
            else:
                raise ValueError("Firstnameame should contain lesser than or equal to 15 letters")
        else:
            raise TypeError("Firstname should contain letters only")
        
     def phonenumber_verification(self):
        if (len(self.phonenumber)==10):
            if type(self.phonenumber) == str:                                                                            
                print("Phone number verified")
            else:
                raise TypeError("Phone number should contain only integers ")
        else:
            raise ValueError("phone number should not be grater than or lesser than 10")
        
    def emailid_verification(self):
        if type(self.emailid) == str:                                                                               
            if len(self.emailid) <= 25:                                                                              
                print("Emailid verified")
            else:
                raise ValueError("Emailid should not contain more than 25 values")
        else:
            raise TypeError("Invalid emailid")    
        

    def groups_verification(self):
        if type(self.groups) == str:
            if len(self.groups) <= 10:                                                                              
                print("Groups verified")
            else:
                raise ValueError("Groups should contain lesser than or equal to 10 letters")
        else:
            raise TypeError("Groups should contain letters only")

    def dob_verification(self):
        if isinstance(self.dob,str):                                                                                
            if len(self.dob) <= 10:                                                                                 
                print("DOB verified")
            else:
                raise ValueError("DOB should contain lesser than or equal to 10 letters")
        else:
            raise TypeError("DOB should contain numbers and symbols only")   
   

v=input("enter the first name")
a=input("enter the last name")
s=input("enter the number")
u=input("enter the email id")
p=input("enter the family")
h=input("enter the dob")
Indhu=phone_Contacts(v,a,s,u,p,h)
Indhu.open_phcontacts()
Indhu.firstname_verification()
Indhu.phonenumber_verification()
Indhu.emailid_verification()
Indhu.groups_verification()
Indhu.dob_verification()



        
phone=[{"Firstname":"vasu","Phno":9854261725,"Email_id":"123@gmail.com","Groups":"Family","DOB":"08/04/2001"},                                  
       {"Firstname":"kumar","Phno":9987968725,"Email_id":"Email_id":"abc@gmail.com":"Friends","DOB":"03/05/2001"},
       {"Firstname":"nanbi","Phno":9854068725,"Email_id":"123@gmail.com","Groups":"Family","DOB":"08/04/2001"},                                  
       {"Firstname":"nanu","Phno":9987968725,"Email_id":"Email_id":"abc@gmail.com":"Friends","DOB":"03/05/2001"},
       {"Firstname":"barath","Phno":9854268725,"Email_id":"123@gmail.com","Groups":"Family","DOB":"08/04/2001"},                                  
       {"Firstname":"nani","Phno":9987768725,"Email_id":"Email_id":"abc@gmail.com":"Friends","DOB":"03/05/2001"},
       {"Firstname":"lila","Phno":9854228725,"Email_id":"123@gmail.com","Groups":"Family","DOB":"08/04/2001"},                                  
       {"Firstname":"ola","Phno":9987969725,"Email_id":"Email_id":"abc@gmail.com":"Friends","DOB":"03/05/2001"},
       {"Firstname":"Abu","Phno":9854262725,"Email_id":"123@gmail.com","Groups":"Family","DOB":"08/04/2001"},                                  
       {"Firstname":"bhii","Phno":9987988725,"Email_id":"Email_id":"abc@gmail.com":"Friends","DOB":"03/05/2001"},
       {"Firstname":"kila","Phno":9854298725,"Email_id":"123@gmail.com","Groups":"Family","DOB":"08/04/2001"},                                  
       {"Firstname":"anni","Phno":9987948725,"Email_id":"Email_id":"abc@gmail.com":"Friends","DOB":"03/05/2001"},
       {"Firstname":"hila","Phno":9854288725,"Email_id":"123@gmail.com","Groups":"Family","DOB":"08/04/2001"},                                  
       {"Firstname":"gool","Phno":9987978725,"Email_id":"Email_id":"abc@gmail.com":"Friends","DOB":"03/05/2001"},
       {"Firstname":"jela","Phno":9854238725,"Email_id":"123@gmail.com","Groups":"Family","DOB":"08/04/2001"},                                  
       {"Firstname":"hail","Phno":9987998725,"Email_id":"Email_id":"abc@gmail.com":"Friends","DOB":"03/05/2001"},
       {"Firstname":"farath","Phno":9853268725,"Email_id":"123@gmail.com","Groups":"Family","DOB":"08/04/2001"},                                 
       {"Firstname":"unni","Phno":9987998725,"Email_id":"Email_id":"abc@gmail.com":"Friends","DOB":"03/05/2001"},
       {"Firstname":"keli","Phno":9854208725,"Email_id":"123@gmail.com","Groups":"Family","DOB":"08/04/2001"},                                  
       {"Firstname":"fula","Phno":9987968725,"Email_id":"Email_id":"abc@gmail.com":"Friends","DOB":"03/05/2001"},
       {"Firstname":"vasu","Phno":9854298725,"Email_id":"123@gmail.com","Groups":"Family","DOB":"08/04/2001"},                                  
       {"Firstname":"yuou","Phno":9987908725,"Email_id":"Email_id":"abc@gmail.com":"Friends","DOB":"03/05/2001"},
       {"Firstname":"duha","Phno":9854238725,"Email_id":"123@gmail.com","Groups":"Family","DOB":"08/04/2001"},                                  
       {"Firstname":"thii","Phno":9987988725,"Email_id":"Email_id":"abc@gmail.com":"Friends","DOB":"03/05/2001"},
       {"Firstname":"frii","Phno":9854298725,"Email_id":"123@gmail.com","Groups":"Family","DOB":"08/04/2001"},                                  
       {"Firstname":"sela","Phno":9987938725,"Email_id":"Email_id":"abc@gmail.com":"Friends","DOB":"03/05/2001"},
       {"Firstname":"ratha","Phno":9854068725,"Email_id":"123@gmail.com","Groups":"Family","DOB":"08/04/2001"},                                  
       {"Firstname":"kila","Phno":9987958725,"Email_id":"Email_id":"abc@gmail.com":"Friends","DOB":"03/05/2001"},
       {"Firstname":"ruthaa","Phno":9850268725,"Email_id":"123@gmail.com","Groups":"Family","DOB":"08/04/2001"},                                  
       {"Firstname":"meha","Phno":9987988725,"Email_id":"Email_id":"abc@gmail.com":"Friends","DOB":"03/05/2001"},
       {"Firstname":"sree","Phno":9854228725,"Email_id":"123@gmail.com","Groups":"Family","DOB":"08/04/2001"},                                  
       {"Firstname":"saha","Phno":9987968725,"Email_id":"Email_id":"abc@gmail.com":"Friends","DOB":"03/05/2001"},
       {"Firstname":"vila","Phno":9854208725,"Email_id":"123@gmail.com","Groups":"Family","DOB":"08/04/2001"},                                  
       {"Firstname":"Anu","Phno":9987968725,"Email_id":"Email_id":"abc@gmail.com":"Friends","DOB":"03/05/2001"},
       {"Firstname":"Abi","Phno":9854264725,"Email_id":"123@gmail.com","Groups":"Family","DOB":"08/04/2001"},                                  
       {"Firstname":"pkki","Phno":9987908725,"Email_id":"Email_id":"abc@gmail.com":"Friends","DOB":"03/05/2001"},
       {"Firstname":"fila","Phno":9854288725,"Email_id":"123@gmail.com","Groups":"Family","DOB":"08/04/2001"},                                  
       {"Firstname":"cool","Phno":9987908725,"Email_id":"Email_id":"abc@gmail.com":"Friends","DOB":"03/05/2001"},
       {"Firstname":"vila","Phno":9854248725,"Email_id":"123@gmail.com","Groups":"Family","DOB":"08/04/2001"},                                  
       {"Firstname":"fila","Phno":9987988725,"Email_id":"Email_id":"abc@gmail.com":"Friends","DOB":"03/05/2001"},
       {"Firstname":"meja","Phno":9854238725,"Email_id":"123@gmail.com","Groups":"Family","DOB":"08/04/2001"},                                  
       {"Firstname":"yuoi","Phno":9987978725,"Email_id":"Email_id":"abc@gmail.com":"Friends","DOB":"03/05/2001"},
       {"Firstname":"dhii","Phno":9854238725,"Email_id":"123@gmail.com","Groups":"Family","DOB":"08/04/2001"},                                  
       {"Firstname":"kaal","Phno":9987908725,"Email_id":"Email_id":"abc@gmail.com":"Friends","DOB":"03/05/2001"},
       {"Firstname":"bhiii","Phno":9854768725,"Email_id":"123@gmail.com","Groups":"Family","DOB":"08/04/2001"},                                  
       {"Firstname":"lool","Phno":9987998725,"Email_id":"Email_id":"abc@gmail.com":"Friends","DOB":"03/05/2001"},
       {"Firstname":"shila","Phno":9854368725,"Email_id":"123@gmail.com","Groups":"Family","DOB":"08/04/2001"},                                  
       {"Firstname":"neena","Phno":9987068725,"Email_id":"Email_id":"abc@gmail.com":"Friends","DOB":"03/05/2001"}
       {"Firstname":"vasu","Phno":9854261725,"Email_id":"123@gmail.com","Groups":"Family","DOB":"08/04/2001"},                                  
       {"Firstname":"kumar","Phno":9987968725,"Email_id":"Email_id":"abc@gmail.com":"Friends","DOB":"03/05/2001"},
       {"Firstname":"nanbi","Phno":9854068725,"Email_id":"123@gmail.com","Groups":"Family","DOB":"08/04/2001"},                                  
       {"Firstname":"nanu","Phno":9987968725,"Email_id":"Email_id":"abc@gmail.com":"Friends","DOB":"03/05/2001"},
       {"Firstname":"barath","Phno":9854268725,"Email_id":"123@gmail.com","Groups":"Family","DOB":"08/04/2001"},                                  
       {"Firstname":"nani","Phno":9987768725,"Email_id":"Email_id":"abc@gmail.com":"Friends","DOB":"03/05/2001"},
       {"Firstname":"lila","Phno":9854228725,"Email_id":"123@gmail.com","Groups":"Family","DOB":"08/04/2001"},                                  
       {"Firstname":"ola","Phno":9987969725,"Email_id":"Email_id":"abc@gmail.com":"Friends","DOB":"03/05/2001"},
       {"Firstname":"Abu","Phno":9854262725,"Email_id":"123@gmail.com","Groups":"Family","DOB":"08/04/2001"},                                  
       {"Firstname":"bhii","Phno":9987988725,"Email_id":"Email_id":"abc@gmail.com":"Friends","DOB":"03/05/2001"},
       {"Firstname":"kila","Phno":9854298725,"Email_id":"123@gmail.com","Groups":"Family","DOB":"08/04/2001"},                                  
       {"Firstname":"anni","Phno":9987948725,"Email_id":"Email_id":"abc@gmail.com":"Friends","DOB":"03/05/2001"},
       {"Firstname":"hila","Phno":9854288725,"Email_id":"123@gmail.com","Groups":"Family","DOB":"08/04/2001"},                                  
       {"Firstname":"gool","Phno":9987978725,"Email_id":"Email_id":"abc@gmail.com":"Friends","DOB":"03/05/2001"},
       {"Firstname":"jela","Phno":9854238725,"Email_id":"123@gmail.com","Groups":"Family","DOB":"08/04/2001"},                                  
       {"Firstname":"hail","Phno":9987998725,"Email_id":"Email_id":"abc@gmail.com":"Friends","DOB":"03/05/2001"},
       {"Firstname":"farath","Phno":9853268725,"Email_id":"123@gmail.com","Groups":"Family","DOB":"08/04/2001"},                                 
       {"Firstname":"unni","Phno":9987998725,"Email_id":"Email_id":"abc@gmail.com":"Friends","DOB":"03/05/2001"},
       {"Firstname":"keli","Phno":9854208725,"Email_id":"123@gmail.com","Groups":"Family","DOB":"08/04/2001"},                                  
       {"Firstname":"fula","Phno":9987968725,"Email_id":"Email_id":"abc@gmail.com":"Friends","DOB":"03/05/2001"},
       {"Firstname":"vasu","Phno":9854298725,"Email_id":"123@gmail.com","Groups":"Family","DOB":"08/04/2001"},                                  
       {"Firstname":"yuou","Phno":9987908725,"Email_id":"Email_id":"abc@gmail.com":"Friends","DOB":"03/05/2001"},
       {"Firstname":"duha","Phno":9854238725,"Email_id":"123@gmail.com","Groups":"Family","DOB":"08/04/2001"},                                  
       {"Firstname":"thii","Phno":9987988725,"Email_id":"Email_id":"abc@gmail.com":"Friends","DOB":"03/05/2001"},
       {"Firstname":"frii","Phno":9854298725,"Email_id":"123@gmail.com","Groups":"Family","DOB":"08/04/2001"},                                  
       {"Firstname":"sela","Phno":9987938725,"Email_id":"Email_id":"abc@gmail.com":"Friends","DOB":"03/05/2001"},
       {"Firstname":"ratha","Phno":9854068725,"Email_id":"123@gmail.com","Groups":"Family","DOB":"08/04/2001"},                                  
       {"Firstname":"kila","Phno":9987958725,"Email_id":"Email_id":"abc@gmail.com":"Friends","DOB":"03/05/2001"},
       {"Firstname":"ruthaa","Phno":9850268725,"Email_id":"123@gmail.com","Groups":"Family","DOB":"08/04/2001"},                                  
       {"Firstname":"meha","Phno":9987988725,"Email_id":"Email_id":"abc@gmail.com":"Friends","DOB":"03/05/2001"},
       {"Firstname":"sree","Phno":9854228725,"Email_id":"123@gmail.com","Groups":"Family","DOB":"08/04/2001"},                                  
       {"Firstname":"saha","Phno":9987968725,"Email_id":"Email_id":"abc@gmail.com":"Friends","DOB":"03/05/2001"},
       {"Firstname":"vila","Phno":9854208725,"Email_id":"123@gmail.com","Groups":"Family","DOB":"08/04/2001"},                                  
       {"Firstname":"Anu","Phno":9987968725,"Email_id":"Email_id":"abc@gmail.com":"Friends","DOB":"03/05/2001"},
       {"Firstname":"Abi","Phno":9854264725,"Email_id":"123@gmail.com","Groups":"Family","DOB":"08/04/2001"},                                  
       {"Firstname":"pkki","Phno":9987908725,"Email_id":"Email_id":"abc@gmail.com":"Friends","DOB":"03/05/2001"},
       {"Firstname":"fila","Phno":9854288725,"Email_id":"123@gmail.com","Groups":"Family","DOB":"08/04/2001"},                                  
       {"Firstname":"cool","Phno":9987908725,"Email_id":"Email_id":"abc@gmail.com":"Friends","DOB":"03/05/2001"},
       {"Firstname":"vila","Phno":9854248725,"Email_id":"123@gmail.com","Groups":"Family","DOB":"08/04/2001"},                                  
       {"Firstname":"fila","Phno":9987988725,"Email_id":"Email_id":"abc@gmail.com":"Friends","DOB":"03/05/2001"},
       {"Firstname":"meja","Phno":9854238725,"Email_id":"123@gmail.com","Groups":"Family","DOB":"08/04/2001"},                                  
       {"Firstname":"yuoi","Phno":9987978725,"Email_id":"Email_id":"abc@gmail.com":"Friends","DOB":"03/05/2001"},
       {"Firstname":"dhii","Phno":9854238725,"Email_id":"123@gmail.com","Groups":"Family","DOB":"08/04/2001"},                                  
       {"Firstname":"kaal","Phno":9987908725,"Email_id":"Email_id":"abc@gmail.com":"Friends","DOB":"03/05/2001"},
       {"Firstname":"bhiii","Phno":9854768725,"Email_id":"123@gmail.com","Groups":"Family","DOB":"08/04/2001"},                                  
       {"Firstname":"lool","Phno":9987998725,"Email_id":"Email_id":"abc@gmail.com":"Friends","DOB":"03/05/2001"},
       {"Firstname":"shila","Phno":9854368725,"Email_id":"123@gmail.com","Groups":"Family","DOB":"08/04/2001"},                                  
       {"Firstname":"neena","Phno":9987068725,"Email_id":"Email_id":"abc@gmail.com":"Friends","DOB":"03/05/2001"}
       {"Firstname":"meha","Phno":9987988725,"Email_id":"Email_id":"abc@gmail.com":"Friends","DOB":"03/05/2001"},
       {"Firstname":"sree","Phno":9854298725,"Email_id":"123@gmail.com","Groups":"Family","DOB":"08/04/2001"},                                  
       {"Firstname":"saha","Phno":9987968725,"Email_id":"Email_id":"abc@gmail.com":"Friends","DOB":"03/05/2001"},
       {"Firstname":"vila","Phno":9854208725,"Email_id":"123@gmail.com","Groups":"Family","DOB":"08/04/2001"},                                  
       {"Firstname":"Anu","Phno":9987968725,"Email_id":"Email_id":"abc@gmail.com":"Friends","DOB":"03/05/2001"},
       {"Firstname":"Abi","Phno":9854264765,"Email_id":"123@gmail.com","Groups":"Family","DOB":"08/04/2001"},                                  
       {"Firstname":"pkki","Phno":9987908725,"Email_id":"Email_id":"abc@gmail.com":"Friends","DOB":"03/05/2001"},
       {"Firstname":"fila","Phno":9854288725,"Email_id":"123@gmail.com","Groups":"Family","DOB":"08/04/2001"},                                  
       {"Firstname":"cool","Phno":9987908725,"Email_id":"Email_id":"abc@gmail.com":"Friends","DOB":"03/05/2001"},
       {"Firstname":"vila","Phno":95454248725,"Email_id":"123@gmail.com","Groups":"Family","DOB":"08/04/2001"},                                  
       {"Firstname":"fila","Phno":9987988725,"Email_id":"Email_id":"abc@gmail.com":"Friends","DOB":"03/05/2001"},
       {"Firstname":"meja","Phno":9854238725,"Email_id":"123@gmail.com","Groups":"Family","DOB":"08/04/2001"},                                  
       {"Firstname":"yuoi","Phno":9987976725,"Email_id":"Email_id":"abc@gmail.com":"Friends","DOB":"03/05/2001"},
       {"Firstname":"dhii","Phno":9854238725,"Email_id":"123@gmail.com","Groups":"Family","DOB":"08/04/2001"}, ]
       


for i in phone:                                                                                                             
    for j,k in i.items():                                                                                                     
        print(f"{j}:{k}")
