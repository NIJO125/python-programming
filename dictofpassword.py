users={'Nijo':'nkppp','Sam':'cppp'}
while True:
  p=input("Enter q to exit or 1 to continue:")
  if p.lower() =='q':
    break
  username=input("Enter your Username:")
  if username in users:
    print("This user name already exits")
  else:
    pass_1=input("Enter your password:")
    pass_2=input("Confirm your password:")
    if pass_1==pass_2:
      users[username]=pass_1
print(users)
