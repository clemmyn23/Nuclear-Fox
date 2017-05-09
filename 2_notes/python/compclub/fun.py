username = "bob"
password = "awesome123"

userLogin = raw_input("What is your username?: ")

while (userLogin != username):
	print ("Incorrect username")
	userLogin = raw_input("What is your username?: ")

userPass = raw_input("Enter correct password for " + username + ": ")

tries = 0
while (userPass != password and tries <= 3):
	print ("Incorrect password")
	userPass = raw_input("Enter correct password for " + username + ": ")
	tries += 1			# make sure you increment this

if tries == 3:
	print ("Welcome back " + username)
else:
	print("go away you hacker!!!")
