# f=open("city.txt",'r')
# f1=open("delhi.txt",'w')
# f2=open("simla.txt",'w')
# f3=open("other.txt",'w')
# p=f.read()
# data=p.split("/n")
# i=0
# while i <len(data):
#     if  "delhi" in data[i]:
#         f1.write(data[i])
#         f1.write("\n")
#         print(f1)
#     elif "simla" in data[i]:
#         f2.write(data[i])
#         f2.write("\n")
#         print(f2)
#     else:
#         f3.write(data[i])
#         print(f3)
#     i=i+1

# # print(data)
# for i in data:
#     if  "delhi" in data[i]:
#         f1.write(data[i])
#         print(f1)
# # for i in data:
# #     if  "delhi" in data[i] :
# #         f1.write(i)
# #     elif  "simla" in data[i]:
# #         f2.write(i)
# #     # elif data[i] == "other":
# #     else:
# #         f3.write(i)










# my_file = open("city.text")
# file_data = my_file.read()
# print (file_data)
# my_file.close()

f=open("city.txt","r")
file1=open("delhi.txt","w")
file2=open("simla.txt","w")
file3=open("other.txt","w")
file=f.read()
file_data=file.split("\n")
print(file_data)
i=0
while i<len(file_data):
    if "delhi" in file_data[i]:
        file1.write(file_data[i])
        file1.write("\n")
        print(file1)
      
    elif "shimla" in file_data[i]:
        file2.write(file_data[i])
        file2.write("\n")
    else:
        file3.write(file_data[i])
        file3.write("\n")
    i+=1
    