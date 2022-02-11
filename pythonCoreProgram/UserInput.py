import re
userName = input('Enter your UserName: ')
string = " Hello " +userName+ ", How are you?" 
newUserName = input("enter new UserName:")
newString = string.replace(userName,newUserName)
Match = re.match('[A-Z]{1}[a-z]{2,}$',newUserName)
if Match:
    print(newString)
else:
    print('Invalid UserName')

