class test():
    a = 'hhh'
    def run(self):
        print('GFRIENDaa')
t = test()
print(getattr(t,'a'))
print(getattr(t,'b',1))
print(getattr(t,'b','not found'))
#print(getattr(t,'b'))

