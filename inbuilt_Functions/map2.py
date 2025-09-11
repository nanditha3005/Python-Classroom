# create new list-enames ,collect all usernames with uppercase and store into new list

unames=["sonia","rahul","priyanka","ramya"]
new_users=[]
for uname in unames:
    new_users.append(uname.upper())

print(unames)
print(new_users)

#-----------
def change_case(name):
    return name.upper()
new_users=list(map(change_case,unames))

print(unames)
print(new_users)


#-------
new_users=list(map(lambda uname:uname.upper(),unames ))
print(unames)
print(new_users)