f=open("demofile.txt" , "w")
f.write("I have deleted content.")
f.close()

f=open("demofile.txt" , "r")
print(f.read())