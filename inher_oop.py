# class parent:
#     a=10
#     b=20
#     def fun(self):
#         print("hello")
# class drive:
#     c=24
#     d=45
#     def dis(self):
#         print("queen")
# base=parent()
# print(base.a,base.b)
# base.fun()
# print(base.c,base.d)
# base.dis()

# class parent:
#     a=10
#     b=20
#     def fun(self):
#         print("hello")
# class drive(parent):
#     c=24
#     d=45
#     def dis(self):
#         print("queen")
# base=drive()
# print(base.a,base.b)
# base.fun()
# print(base.c,base.d)
# base.dis()

# class gra_para:
#     def gra_dis(self):
#         print("grand ma")
# class para(gra_para):
#     def paran(self):
#         print("parent")
# class chil(para):
#     def chi(self):
#         print('child')
# a=chil()
# a.gra_dis()
# a.paran()
# a.chi()

# hiretical
# class gra_para:
#     def gra_dis(self):
#         print("grand ma")
# class para(gra_para):
#     def paran(self):
#         print("parent")
# class chil(gra_para):
#     def chi(self):
#         print('child')
# a=chil()
# a.gra_dis()
# a.chi()
# b=para()
# b.gra_dis()
# b.paran()

class fath:
    def father(self):
        print("father")
class mon:
    def month(self):
        print('monter')
class chil(fath,mon):
    def chi(self):
        print("child")
a=chil()
a.father()
a.month()
a.chi()