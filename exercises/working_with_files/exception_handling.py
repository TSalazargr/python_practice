myStuff = []
try:
  f = open("Stuff.mine","r")
  myStuff = f.read()
  f.close()
# Try to find a file called 'Stuff.mine' and open it
except Exception:
  print("Unable to open")

for row in myStuff:
  print(row)

# In this case, the file can't be opened as read because it hasn't been created yet. To do so, do the following:


f = open("Stuff.mine","a") # If a file doesn't exist, "a" or append mode will create it
file.write("This has been written to a file")  # Appends this to the end of the file
f.close()

myStuff = []
try:
  f = open("Stuff.mine","r")
  myStuff = f.read()
  f.close()
# Try to find a file called 'Stuff.mine' and open it
except Exception:
  print("Unable to open")

for row in myStuff:
  print(row)
