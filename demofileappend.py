f=open("demofile.txt" , "a")
f.write("This is for demo.")
f.close()

f=open("demofile.txt" , "r")
print(f.read())