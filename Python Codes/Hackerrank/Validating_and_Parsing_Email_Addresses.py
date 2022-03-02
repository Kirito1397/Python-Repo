import re

def email_validate(the_email): 
    filter= re.compile(r'<[a-z][a-zA-Z0-9\-\.\_]+@[a-zA-Z]+\.[a-zA-Z]{1,3}>')
    if filter.findall(the_email) != None:
        return filter.findall(the_email)
    else:
        return False

no_of_mails = int(input())
email_list = []
for e in range(no_of_mails):
    name,email = input().split()
    print(email)
    print(email_validate(email))
    if email in email_validate(email) :
        # print(email_validate(email))
        email_list.append((name,email))
print(email_list)
for x,y in email_list:
    print(x,y)

# DEXTER <dexter@hotmail.com>
# VIRUS <virus!@variable.:p>


# ALTERNATE :
# ==============

# import re

# N = int(input())

# for i in range(N):
#     name, email = input().split()
#     pattern="<[a-z][a-zA-Z0-9\-\.\_]+@[a-zA-Z]+\.[a-zA-Z]{1,3}>"
#     if bool(re.match(pattern, email)):
#         print(name,email)