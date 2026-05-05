# import json
# from multiprocessing.util import info
# from operator import index
# import random
# import string
# from pathlib import Path


# class Bank:
#     database = 'data.json'
#     info=[]
                
#     try:
#        if Path(database).exists():
#            with open(database, 'r') as fs:
#                info = json.loads(fs.read())
#        else:
#            print("no such file exists")
#     except Exception as e:
#         print(f"Error: {e}")
        
        
#     @classmethod
#     def __update(cls):
#         with open(Bank.database, 'w') as fs:
#            fs.write(json.dumps(Bank.info))
           
#     @classmethod
#     def __accountgenerate(cls):
#         alpha = random.choices(string.ascii_letters, k=3)
#         num = random.choices(string.digits, k=3)
#         spchar= random.choices("!@#$%&*^", k=1)
#         id = alpha + num + spchar 
#         random.shuffle(id)
#         return ''.join(id)
       
#     def create_account(self):
#         info = {
#             "name": input("Enter your name: "),
#             "age": int(input("Enter your age: ")),  
#             "email": input("Enter your email: "),
#             "pin":int(input("Enter your pin: ")),
#             "accountNo": Bank.__accountgenerate(),
#             "balance": 0
             
#         }
#         if info["age"] < 18 or len(str(info["pin"])) != 4:
#             print("sorry you are not eligible to create an account")
#         else:
#             print("account created successfully")
#             for i in info:
#                 print(f"{i}: {info[i]}")
#             print("please remember your account number and pin for future use")
#             Bank.info.append(info)
#             Bank.__update()
                
#     def depositmoney(self):
#         accountNo = input("Enter your account number: ")
#         pin = int(input("Enter your pin: "))
#         userdata= [i for i in Bank.info if i["accountNo"] == accountNo and i["pin"] == pin]
#         if userdata == False:
#             print("invalid account number or pin")
#         else:
#             amount = int(input("Enter the amount you want to deposit: "))    
#             if amount > 10000 or amount < 0:
#                 print("sorry you cannot deposit this amount")
#             else:
#                 userdata[0]["balance"] += amount
#                 Bank.__update()
#                 print("money deposited successfully")
                
#     def withdrawmoney(self):
#         accountNo = input("Enter your account number: ")
#         pin = int(input("Enter your pin: "))
#         userdata= [i for i in Bank.info if i["accountNo"] == accountNo and i["pin"] == pin]
#         if userdata == False:
#             print("invalid account number or pin")
#         else:
#             amount = int(input("Enter the amount you want to withdraw: "))    
#             if userdata[0]['balance'] < amount:
#                 print("sorry you dont have sufficient balance to withdraw this amount")
#             else:
#                 userdata[0]["balance"] -= amount
#                 Bank.__update()
#                 print("money withdrawn successfully") 
                  
#     def showdetails(self):
#         accountNo = input("Enter your account number: ")
#         pin = int(input("Enter your pin: "))
#         userdata= [i for i in Bank.info if i["accountNo"] == accountNo and i["pin"] == pin]
#         print("your account details are: ")
#         for i in userdata[0]:
#             print(f"{i}: {userdata[0][i]}") 
            
#     def updatedetails(self):
#         accountNo = input("Enter your account number: ")
#         pin = int(input("Enter your pin: "))  
#         userdata= [i for i in Bank.info if i["accountNo"] == accountNo and i["pin"] == pin]
#         if userdata == False:
#             print("no such account exists")
#         else:
#             print("you can not update your age , account number and balance")
#             print("fill the details you want to update")
#             newdata = {
#                 "name": input("Enter your name: "),
#                 "email": input("Enter your email: "),
#                 "pin":int(input("Enter your pin: "))
#             }
#             if newdata['name'] == "":
#                 newdata['name'] = userdata[0]['name']
#             if newdata['email'] == "":
#                 newdata['email'] = userdata[0]['email']
#             if newdata['pin'] == "":
#                 newdata['pin'] = userdata[0]['pin']
                
#         newdata['age'] = userdata[0]['age']
        
#         newdata['accountNo'] = userdata[0]['accountNo']
#         newdata['balance'] = userdata[0]['balance']
        
#         if type(newdata['pin']) == str:
#            newdata['pin'] = int(newdata['pin'])
#         for i in newdata:
#          if newdata[i] == userdata[0][i]:
#               continue  
#         else:
#               userdata[0][i] = newdata[i]
#         Bank.__update()
#         print("details updated successfully")
        
        
#     def deleteaccount(self):
#         accountNo = input("Enter your account number: ")
#         pin = int(input("Enter your pin: "))
#         userdata= [i for i in Bank.info if i["accountNo"] == accountNo and i["pin"] == pin]
#         if userdata == False:
#             print("no such data exists")
#         else:
#            check = input("are you sure you want to delete your account? (y/n): ")   
#            if check == 'n'  or check == 'N':
#                print("account deletion cancelled")
#            else:
#             index = Bank.data.index(userdata[0]) 
#             Bank.data.pop(index) 
#             print("account deleted successfully")
#             Bank.__update()
   
                   
   
    
# user = Bank()
# print("press 1 for creating an account")
# print("press 2 for depositing money into your account")
# print("press 3 for withdrawing money from your account")
# print("press 4 for details")
# print("press 5 for updating your details")
# print("press 6 for deleting your account")

# check = int(input("Enter your choice: "))

# if check == 1:
#     user.create_account()
# if check ==2:
#     user.depositmoney()
# if check == 3:
#     user.withdrawmoney()
# if check == 4:
#     user.showdetails()
# if check == 5:
#     user.updatedetails()
# if check == 6:
#     user.deleteaccount()