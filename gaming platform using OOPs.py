#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class PUBG:
    def installation(self):
        print('installing.....')
        return ('pubg successfully installed')
class Create_Account:
    def __init__(self, username, password):
        self.username=username
        self.password=password
    
    def log(self):
        user=input('enter username')
        pas=input('enter password')
        if user==self.username and pas==self.password:
            logt=str(input('login through mobile_num or facebook or google: '))
        
            if logt=='mobile_num':
                mob=int(input('enter your mobile number: '))
                if mob>9999999999 or mob<999999999:
                    print('invalid')
                else:
                    print('login successful')
            elif logt=='facebook':
                user_id=input('enter user_id :')
                password=input('enter password: ')
                print('login successful')
            elif logt=='google':
                print('choose mail id')
                print('a)abs@gmail.com')
                print('b)xyz@gmail.com')
                choose=str(input('choose a or b:'))
                if choose==a or b:
                    print('login successfully')
                else:
                    print('invalid input')
            else:
                print('invalid input')
        else:
            print('username or password incorrect')
class gender:
    def select_gender(self):
        p=input('select gender M)male F)female: ')
        if p=='M':
            return ('male')
        elif p=='F':
            return ('female')
        else:
            return ('invalid input')
            
class training:
    def Rules(self):
        print('T...R...A...I...N...I...N...G')
        print('1)There are three ranks A)silver B)gold C)platinum')
        print('2)For increasing your rank you have to kill other player')
        print('3)For killing other player you have to select weapon first and there are two wepon in game A)AKM B)M24')
        print('4)AKM is a machine gun so if you want to kill other player using AKM you have to write k for three times and in case of M24 you have to write k for only one time')
        print('5)After killing 10 players your rank will increase by one level ')
    def start_game(self):
        st=input('enter start for starting game')
        if st=='start':
            w=input('select weapon A)AKM B)M24')
            Akills=0
            Mkills=0
            if w=='A':
                for i in range(10):
                    A=input('')
                    if A=='kkk':
                        Akills+=1
                    else:
                        print('you lose game')
                        break
                if Akills==10:
                    print('winner winner chiken dinner')
                    print('silver')
                    w=input('select weapon A)AKM B)M24')
                    Akills=0
                    Mkills=0
                    if w=='A':
                        for i in range(10):
                            A=input('')
                            if A=='kkk':
                                Akills+=1
                            else:
                                print('you lose game')
                                break
                        if Akills==10:
                            print('winner winner chiken dinner')
                            print('gold')
                        else:
                            print('you lose the game and your rank is silver...try next time')
                    elif w=="B":
                        for i in range(10):
                            A=input('')
                            if A=='k':
                                Mkills+=1
                            else:
                                print('you lose game')
                                break 
                        if Mkills==10:
                            print('winner winner chiken dinner')
                            print('gold')
                        
                        else:
                            print('you lose the game and your rank is silver..try next time')
                    else:
                        print('weapon not found')
            elif w=="B":
                for i in range(10):
                    A=input('')
                    if A=='k':
                        Mkills+=1
                    else:
                        print('you lose game')
                        break
                if Mkills==10:
                    print('winner winner chiken dinner')
                    print('silver')
                    w=input('select weapon A)AKM B)M24')
                    Akills=0
                    Mkills=0
                    if w=='A':
                        for i in range(10):
                            A=input('')
                            if A=='kkk':
                                Akills+=1
                            else:
                                print('you lose game')
                                break
                        if Akills==10:
                            print('winner winner chiken dinner')
                            print('gold')
                        else:
                            print('you lose the game and your rank is silver')
                    elif w=="B":
                        for i in range(10):
                            A=input('')
                            if A=='k':
                                Mkills+=1
                            else:
                                print('you lose game')
                                break
                        if Mkills==10:
                            print('winner winner chiken dinner')
                            print('gold')
                        else:
                            print('you lose the game and your rank is silver')       
                    else:
                        print('weapon not available')
            else:
                print('weapon is not available')
                
a=PUBG()
print(a.installation())
b=Create_Account('ashish','pass@123')
print(b.username)
print(b.password)
print(b)
print(b.log())
c=gender()
print(c.select_gender())
d=training()
print(d.Rules())
print(d.start_game())


# In[ ]:





# In[ ]:





# In[ ]:




