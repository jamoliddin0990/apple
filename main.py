# test=['hello', 'world']

# print(len(test))


# arr=[]

# arr.append('hello')

# arr.insert(0, 'world')

# arr.remove('world')

# arr.pop(0)

# arr.clear()


# arr=[]

# arr.append('pizza')
# arr.append('burger')
# arr.append('coffe')

# arr.insert(1, 'tea')
# arr.append('tea')
# arr.remove('burger')

# arr.remove('pizza')
# arr.insert(0, 'Pototo')
# arr.insert(2, 'Burger')
# arr.append('coffe')
# arr.remove('tea')
# arr.remove('coffe')

# arr.clear()

# arr.append('Coffe')
# arr.append('Coffe')
# arr.append('Coffe')




# print(arr)








# arr=['a', 'z', 'v', 'b']

# sort() sortorovka

# arr.sort()

# arr.reverse()
# .copy() obj kopiya qiladi


# print(arr)





# text='Hello world tashkent'
# text=text.split(' ')
# print(len(text))


# arr=['hello', 'world', 'tashkent']

# text=" : ".join(arr)

# print(text)

# arr=[]
# text=input('FIO kiriting: ')

# arr=text.split(' ')

# arr.reverse()

# print(arr)




# if 5>=5:
#     print('Haq')
# else:
#     print('Yoq')



    # fName=int(input('Yoshingiz nechida: '))

    # if fName <18:
    #     print('Diskoteka mumkin mas')
    # elif fName>70:
    #     print('kampirga bor')
    # else:
    #     print('marxamat')

# yangi dars eki grupa 

# while
# for 
# breack


# c=0
# while c<1000:
#     print(c)
#     c+=1
#     if c==50:
#         break

# print('finish')


# while True:
#     name=input('What is your name: ')
#     if name.lower()=="quit" or name.lower()=="q":
#         break
#     print("Salom")


# for i in []:
#     print(i)
    

# familiya=['petrov', 'popova', 'ikromova', 'omonov']

# for i in familiya:
#     if i[-1]=='a':
#         print('salom xonim: '+i)
#     else:
#         print('salom janob: '+i)

# familiya=['petrov', 'popova', 'ikromova', 'omonov']
# arr=[]

# for i in familiya:
#     arr.append(i.title())

# print(arr)

# engi dars eski grupa 2

# len()

# sum jamlash


# def kofe():
#     print('Trubkani kotarish')
#     print('raqami terish')
#     print('kofe etish')
#     print('trubkani qoish')


# def salom(x):
#     print()
#     print()


# def plus(x, y):
#     print(x+y)

# plus(2, 3)


# def minus(x, y):
#     return x-y

# z=minus(6, 6)

# print(z)

# def test(y, x):
#     x*x
#     return y

# z=test(2, 2)
# print(z)



# def uzunlik(x):
#     c=0
#     for i in x:
#         c+=1
#     return c

# z=uzunlik('Ubaydullo')
# print(z)



# def test(x):
#     return x

# def qoshish(x):
#     c=0
#     for i in x:
#         c+=i
#     return c
# z=qoshish([5, 5, 5])
# print(z)


# def qoshish(*args):
#     c=0
#     for i in args:
#         c+=i
#     return c

# z=qoshish(2, 3, 4, 7, 8)
# print(z)



# c=0

# def test():
#     global c
#     c=10

# print(c)


# x=lambda y,z: y+z
# print(x(5, 10))



# def test(y, z):
#     return y+z
# x=test(5, 10)
# print(x)


# fName='salom'
# lName='world'

# print("{} {}".format(fName, lName))

# print(f"{fName} {lName}")

# dict - dictonary - slovar




# bar={
#     "title": "Jamoliddin", 
#     "married": True,
#     "age": 27
# }

# print(bar["age"])



# for i in bar:
#     print(bar[i])


# for x, y in bar.items():
#     print(x, y)

# countries = {
#         {
#              "country": "Uzbekistan",
#              "detail": {
#              "capital": "Tashkent",
#              "populations": "33000000"
#         },
#         {
#              "country": "Kyrgyzstan",
#              "detail": {
#              "capital": "Bishkek",
#              "populations": "6500000"
#         },
#         {
#              "country": "Kazakhstan",
#              "detail": 
#              "capital": "Nursultan",
#              "populations": "18000000"
#         },
#     {
#             "country": "Tadjikistan",
#              "detail": {
#         "capital": "Dushanbe",
#         "populations": "5000000"
#     }
# }
# Bishkek is the capital of Kyrgyzstan and populations with a population of 6500000
# Nursultan is the capital of Kazakhstan and populations with a population of 18000000
# Tashkent is the capital of Uzbekistan and populations with a population of 33000000
# Dushanbe is the capital of Tajikistan and populations with a population of 5000000



# NameError, o'zgaruvchan to'pilmagan
# ZeroDivisionError  agar raqamdi 0 ga bo'lsez
# IndexError, agar spiskada index to'pilmasa
# KeyError, agar siz yoq kalitdi chaqirmoqchi bo'lsez
# KeyboardInterrupt, ishlab turgan skriptdi avariyna tohtatish
# IndentationError, probellarda hato qilish
# TypeError, str bilan int di plusuyem
# SyntaxError, siz koddi hato yozganizda
# AttributeError, siz obyektdi yoq metodini chaqirmoqchi bo'lsez
# ImportError, yoq bibleotekani chaqirmoqchi bo'sez
# ValueError, matndi raqam qilmoqchi bo'lganizda

# try: except:


# try:
#     print('1')
#     print(test)
#     print('2')
# except:
#     print('error')

# print('finish')


# son=input('Bir: ')
# age=input('Hrf: ')

# try:
#      print(int(son)+int(age))
# except:
#      print(son + age)


# print("finish")

# try:
#      print('1')
# except:
#      print('2')
# else:
#      print('3')
# finally:
#      print('4')


# import string

# print(dir(string))

# for i in dir(string):
#      print(i)

# print(string.printable)

# print(string.ascii_letters)

# from math import nan
# import random

# for i in dir(random):
#      print(i)


# def cod(x):
#     random.randint(True, 9000),
# x=random.randint(True, 9000)
# print(x)



# open (file name, mode)
# 'r'-oqish 'w'-  'a'
# 

# file=open('test.txt', 'r',encoding='utf-8')

# .read() matn qaytaradin
# .readlines()

# result=file.read()
# file.close()
# print(result)

# \n yangi qator
# \t bitta tab
# ]s bita spase 1probel
# \ bu universal

# print('apple\npear')


# try:
#     file=open('test.txt', 'r',encoding='utf-8')
#     result=file.read()
#     c=0
#     for i in result:
#         if i.lower()=="":
#             c==i
#             c+=1
#     print(c)
# except:
#     print('Xato')
# finally:
#     file.close()



# try:
#     file=open('test.txt', 'r',encoding='utf-8')
#     result=file.read()
#     c=0
#     for i in result.split(" "):
#         if i.lower() == "ipsum":
#             c+=1
#     print(c)
# except:
#     print('Xato')
# finally:
#     file.close()



# try:
#     file=open('file.txt', 'a', encoding='utf-8')
#     file.write('world\n')
# except:
#     print('Xato')
# finally:
#     file.close()


# with open('file.txt', 'a', encoding='utf-8') as file:
#     file.write('hello\n')

# with open('file.txt', 'r', encoding='utf-8') as file:
#     result=file.read()


# while True:
#     age=input('Ismiz nima: ')
#     with open('file.txt', 'a', encoding='utf-8') as file:
#         file.write (age + '\n')
#     if age=='a':
#         break

# print('Finish')


# while True:
#     with open('test.txt', 'r', encoding='utf-8') as file:
#         result=file.read ('hello')
#     c=0
#     for i in result:
#         c==i
#         c+=1
# print('Finish')


# eski gryupa yangi dars 






# with open('test.txt', 'r', encoding='utf-8') as file:
#     text=file.read()
# result=itrans(text, to_lang="uz")
# with open('result.txt', 'w', encoding='utf-8') as file:
#     text=file.write(result)

# print(result)

# from itranslate import itranslate as itrans
# from sys import argv

# result=itrans(argv[1], to_lang="uz")

# print(result)



# try:
#     with open('test.txt', 'r', encoding='utf-8') as file:
#         result=file.read()

#     variant=itrans(result, to_lang="uz",)

#     with open('result.txt', 'w', encoding='utf-8') as file:
#         file.write(variant)

#         # 

#     with open('test.txt', 'r', encoding='utf-8') as file:
#         text=file.read()
#     var=itrans(text, to_lang="ru",)
#     with open('text.txt', 'w', encoding='utf-8') as file:
#         file.write(var)
# except:
#     print('hato')



# from bs4 import BeautifulSoup as BS

# import requests 

# drug=input('Dorini kiriting: ')

# html = requests.get('https://pharmaclick.uz/ru/catalog/?q='+drug).text

# soup=BS(html, 'html.parser')

# for i in soup('.catalog_item main_wra'):
#     print(i.get_text().replace('\n', ''))



# povtoreniye esli grupa 




