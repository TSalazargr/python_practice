with open("/usercode/files/books.txt") as f:
  print(f.read())

with open("example.txt", "w") as file:
    file.write("Hello World!")
