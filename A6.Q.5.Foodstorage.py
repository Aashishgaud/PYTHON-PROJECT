#1.Create a Food Storage System which perform following Operation on it.
#using OOPS Concept (Class and Object )
'''Class Food has Following Properties (foodId, foodName, foodType(Veg/Non-Veg) ,foodPrice)
Add Food 
Update Food 
Delete Food 
Show Food List
Show Food by Id
Show Food by Name
Show Food by Type 
Sort Food List by Name
Sort Food List by Price'''
class Food:
    def __init__(self):
        self._d={'foodid':['1','2','3','4','5'],'foodname':['eggs','rice','roti','chicken','paneer'],'foodtype':['nonveg','veg','veg','nonveg','veg'],'foodprice':['60','80','10','150','120']}
    def __del__(self):
        pass
#
class FoodStorageSystem(Food):
    def __init__(self):
        super().__init__()
    def addfood(self):
        while (True):
            a=input('Enter food Id : ')
            b=input('Enter food Name : ')
            c=input('Enter food Type(Veg/Nonveg): ')
            d=input('Enter food Price : ')
            self._d['foodid'].append(a)
            self._d['foodname'].append(b)
            self._d['foodtype'].append(c)
            self._d['foodprice'].append(d)
            ans=input('Do you want to add more (Y/N) : ')
            if ans=='N' or ans=='n':
                break
    def updatefood(self):
        while (True):
            a=input('Enter Food id to update food : ')
            m=self._d['foodid'].index(a)
            b=input('Enter new food Name : ')
            c=input('Enter new food Type(Veg/Nonveg): ')
            d=input('Enter new food Price : ')
            for i in range(0,len(self._d['foodid'])):
                if i==m:
                    self._d['foodname'][i]=b
                    self._d['foodtype'][i]=c
                    self._d['foodprice'][i]=d
            ans=input('Do you want to make more changes (Y/N) : ')
            if ans=='N' or ans=='n':
                break
    def deletefood(self):
        a=input('Enter Food id to delete food : ')
        for i in range(0,len(self._d['foodid'])):
            m=self._d['foodid'].index(a)
            if i==m:
                del self._d['foodid'][i]
                del self._d['foodname'][i]
                del self._d['foodtype'][i]
                del self._d['foodprice'][i]
            ans=input('Do you want to make more changes (Y/N) : ')
            if ans=='N' or ans=='n':
                break
    def show1(self): #Show Food List
        for row in zip(*([key]+(value) for key,value in self._d.items())):
            print(*row,  '  ')
    def show2(self): # Show Food id
        a=input('Enter Food id : ')
        m=self._d['foodid'].index(a)
        for i in range(0,len(self._d['foodid'])):
            if i==m:
                print(self._d['foodname'][i])
                print(self._d['foodtype'][i])
                print(self._d['foodprice'][i])
    def show3(self): #Show Food name
        a=input('Enter Food name : ')
        m=self._d['foodname'].index(a)
        for i in range(0,len(self._d['foodname'])):
            if i==m:
                print(self._d['foodid'][i])
                print(self._d['foodtype'][i])
                print(self._d['foodprice'][i])
    def display(self) :
        print('Food Storage System List')
        print(self._d)
    
#
while(True):
    obj=FoodStorageSystem()
    obj.display()
    while(True):
        print('\n1.Add Food\n2.Update Food\n3.Delete Food\n4.Show Food List\n5.Show Food by Id\n6.Show Food by Name\n7.Show Food by Type\n8.Sort Food List by Name\n9.Sort Food List by Price\n10.Exit')
        op=int(input('Enter your choice : '))
        if op==1:
            obj.addfood()
            obj.display()
        elif op==2:
            obj.updatefood()
            obj.display()
        elif op==3:
            obj.deletefood()
            obj.display()
        elif op==4:
            obj.show1()
        elif op==5:
            obj.show2()
        elif op==6:
            obj.show3()
        else:
            break
    ans=input('Do you want to continue (Y/N) : ')
    if ans=='N' or ans=='n':
        break


            
            
