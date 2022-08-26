# def red():
#     f=open("efg.text",'r')
#     while True:
#         s=f.readline()
#         if s=="":
#             break
#         else:
#             print(s)
# red()

# def red():
#     f=open("efg.text",'r')
#     lines=f.readline()
#     print(lines)
# red()

def red():
    f=open("efg.text",'r')
    lines=f.readline()
    for i in lines:
        if i[0]=='L':
            print(i)
red()
