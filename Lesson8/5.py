f = open("file.txt", "a+")
data = f.read()
newdata  = data +" also Hello from Anel"
f.write(newdata)
f.close()