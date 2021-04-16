class student:
    id=0;#atrributes
    name=""#attributes
    address=''#attributes
    def getinfo(self):
        self.id=int(input('enter id'))
        self.name=input("enter name")
        self.address=input('enter address')
    def display(s):
        print('your id is',s.id)
        print('your name is',s.name)
        print('your address is',s.address)
s1=student();#object calling
s1.getinfo();#method calling
s1.display();#method calling
