# def cunt():
#     f=open("efg.text",'r')
#     c=0
#     s=f.read()
#     word=s.split()
#     print(word)
#     for i in word:
#         if len(i)>=5:
#             c=c+1
#             print(i)
#     print(c)
# cunt()
f=open("efg.text",'r')
c=0
s=f.read()
word=s.split()
print(word)
m=0
for i in word:
    if len(i)>m:
        m=len(i)
        c=i
print(c,m)
# f=open("efg.text",'r')


# for i in f.readlines():
#     print(i)