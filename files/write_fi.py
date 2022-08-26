# f=open("swati.text",'w')
# f.write("hello")

f=open("swati.text",'r')
f1=open("abc",'w')
for i in f:
    f1.write(i)

# my_file2 = open("abc", "w")
# my_file2.write("Abhishek - Gurgaon")
# my_file2.write("Ranveer - Delhi")
# my_file2.close()

# with open("abc", 'a') as f:
#    f.write(" This is a good course.\n")
#    f.write("Enjoy learning.")

# f=open("abc", 'w')
# f.write(" This is a good course.\n")
# f.write("Enjoy learning.")
