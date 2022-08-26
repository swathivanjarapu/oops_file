# class hun:
#     def __init__(self):
#         print("construct")
#     def run(self):
#         print("running")
#     def walk(self):
#         print("walking")
# a=hun()






class hun:
    def __init__(self,c,w):
        self.color=c
        self.weight=w
       
    def run(self):
        print("running")
    def walk(self):
        print("walking")
a=hun('white',5)
print(a.color,a.weight)
a.run()
a.walk()

    