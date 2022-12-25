#8-dars ro'yhatlar bilan ishlash 01.12.2022
#lists
#sort
#.sort()  alifbo bo'yicha tartiblaydi
#.sort(reverse=True) teskari alibo bo'yicha tartiblaydi
#.sorted() alohida tartiblaydi
#.reverse()  oxiridan boshlab yozib chiqadi
#len() uzunlik
#range(0,10)=range(10) qadam ham bersak bo'ladi (0,10,2)
#list(range())
#kesish [0:n] [:n] [0:]
#a=b[:]

# davlatlar=['USA','Russia','China','Turkey','Uzbekistan']
# print(len(davlatlar))
# a=sorted(davlatlar)
# print(a)
# # davlatlar.sort()
# print(davlatlar)
# print(sorted(davlatlar,reverse=True))
# print(davlatlar)
# davlatlar.reverse()
# print(davlatlar)
# a=list(range(120,1201,2))
# # print(a)
# print(sum(a))
# print(max(a)-min(a))
# print(len(a))
# b=a[0:20]
# c=a[270:290]
# d=a[521:541]
# print(b)
# print(c)
# print(d)
#nonushta = []
# taomlar=['moshxo\'rda','osh','tuxum','non','choy']
# nonushta = taomlar[:]
# nonushta = nonushta[2:]
# nonushta.append("coffee")
# print(taomlar)
# print(nonushta)
# """nonushta=taomlar[2:4]
# print(nonushta1)
# nonushta=nonushta.append('coffe')
# print(nonushta)"""
# nonushta=tuple(nonushta)
# nonushta[0]='qora choy'

#9-dars for
#09.12.2022 
# #SESSIYA YAQIN,O'QI DANGASA!!!

# universitet=['samandar','javlon','abdurahmon','muslimbek','bunyod']
# for kursdoshlar in universitet:
#    print(f"{kursdoshlar} LAG ga qo'llab yuboring,ism sharifni yozib  \nkatta rahmat!")
# print('kod 5 marta takrorlandi')

# a=range(11,100,2)
# for sonlarning_kubi in a:
#     print(f"{sonlarning_kubi} ning kubi {sonlarning_kubi**2} ga teng")
  
# 10.12.2022
# kinolar=[]
# print('5 ta eng sevimli filmingizni kiriting')
# for n in range(1,6):
#      kinolar.append(input(f"{n}-kinongizni nomini kiriting:\n" ))
    
     
# print(kinolar)     

# print('Bugun necha kishi bilan suhbatlashdingiz?')
# odamlar=[]
# a=int(input())
# for suhbatlar in range(1,a+1):
#   odamlar.append(input(f"{suhbatlar}-odamning ismini kiriting: "))
# print(odamlar)

#muslimbek's idea
# people = int(input("How many people did you meet today?"))
# array = []
# for i in range(1, people+1):
#     name = input(f"{i}-odamning ismi: ")
#     array.append(name)
# print(array)  


# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#    if car=='gm' :
#     print(car.upper())
#    else: 
#     print(car.title())

# name=input('Write your login:>>>')
# if name=='admin':
#     print('Hush kelibsiz admin,foydalanuvchilarning ro\'yhatini ko\'rishni istaysizmi?')
# else:
#     print(f"Xush kelibsiz,{name} ")

# a=int(input("Write some number>>>"))
# b=int(input("Write number again>>>"))
# if a==b:
#     print('Bu sonlar teng!')
# else:
#     print("bu sonlar teng emas!!")Q

# a=float(input('Biror son kiriting:>>>'))
# if a<0:
#     print('Manfiy son!')
# elif a>0:
#     print("Musbat son!")                        
# elif a==0:  #agar else ishlatsak a==0 kerak emas
#     print("Bu son 0 ga teng!")

# from math import sqrt
# a=int(input("Son kiriting:>>>"))
# if a>=0 :
#     print(f"Bu sonning kvadrat ildizi,{str(sqrt(a))} ga teng")
# else:
#     print("Bu haqiqiy son emas")

# 22.12.2022

# a=int(input('juft son kiriting:\n'))
# if a%2==0:
#     print('rahmat!')
# else:
#     print('Bu son juft emas!')


# 24.12.2022 2:20 uyqu yo'q 

# a=int(input('Yoshingiz nechida?:\n>>> '))
# if a<4 or a>60 :
#     price="bepul"
# elif a<18:
#     price='10000 so\'m'
# elif a>=18:
#     price='20000 so\'m'
# print(f"Sizga kirish {price}")

# a=float(input('Birinchi sonni kiriting:>>> '))
# b=float(input('Ikkinchi sonni kiriting:>>> '))
# if a==b:
#     print(f"Bu sonlar teng ya\'ni,{a}={b}") #1-marta a va b ni {str(a)} qilib yozgandim))
# elif a-b>0:
#     print(f"birinchi son ikkinchisidan katta ya\'ni {a}>{b}")
# elif a-b<0:
#     print(f"ikkinchi son birinchi sondan katta ya\'ni, {a}<{b} ")
# else: 
#     print('bu sonlarni taqqoslab bo\'lmaydi')


# mahsulotlar=['sut','non','kartoshka','yog`','piyoz','rollton','banan','limon','go\'sht','baliq','qaymoq']

# a=input('Savatga birinchi mahsulotni qo\'shing: ')
# b=input('Savatga ikkinchi mahsulotni qo\'shing: ')
# c=input('Savatga uchinchi mahsulotni qo\'shing: ')
# d=input('Savatga to\'rtinchi mahsulotni qo\'shing: ')
# e=input('Savatga beshinchi mahsulotni qo\'shing: ')
# f=input('Savatga oltinchi mahsulotni qo\'shing: ')
# royhat=[a,b,c,d,e,f]
# if a in mahsulotlar:
#     print(f"Do\'konimizda {str(a)} bor ")
# if b in mahsulotlar:
#     print(f"Do\'konimizda {str(b)} bor ")
# if c in mahsulotlar:
#     print(f"Do\'konimizda {str(c)} bor ")
# if d in mahsulotlar:
#     print(f"Do\'konimizda {str(d)} bor ")
# if e in mahsulotlar:
#     print(f"Do\'konimizda {str(e)} bor ")
# if f in mahsulotlar:
#     print(f"Do\'konimizda {str(f)} bor ")
# for i in royhat:
#     if i not in mahsulotlar:
#         print(f"{i} do\'konimizda yo\'q")

# mahsulotlar=['sut','non','kartoshka','yog`','piyoz','rollton','banan','limon','go\'sht','baliq','qaymoq']

# bor_mahsulotlar=[]
# yoq_mahsulotlar=[]
# a=input('Savatga birinchi mahsulotni qo\'shing: ')
# b=input('Savatga ikkinchi mahsulotni qo\'shing: ')
# c=input('Savatga uchinchi mahsulotni qo\'shing: ')
# d=input('Savatga to\'rtinchi mahsulotni qo\'shing: ')
# e=input('Savatga beshinchi mahsulotni qo\'shing: ')
# f=input('Savatga oltinchi mahsulotni qo\'shing: ')
# royhat=[a,b,c,d,e,f]
# if a in mahsulotlar:
#     bor_mahsulotlar.append(a)
# if b in mahsulotlar:
#     bor_mahsulotlar.append(a)
# if c in mahsulotlar:
#     bor_mahsulotlar.append(a)
# if d in mahsulotlar:
#     bor_mahsulotlar.append(a)
# if e in mahsulotlar:
#     bor_mahsulotlar.append(a)
# if f in mahsulotlar:
#     bor_mahsulotlar.append(a)
# for i in royhat:
#     if i not in mahsulotlar:
#         yoq_mahsulotlar.append(i)
# if yoq_mahsulotlar:
#             print(f"Do\'konimizda quyidagi mahsulotlar yoq:\n {str(yoq_mahsulotlar)} ")
# else: print('Siz so\'ragan barcha mahsulot bizda bor')
# pastda qisqaroq yechim qilganman

# 3:25 uyqu keldi uxlash kerak
# yuqoridagi masalaga Javlonbekdan idea

# mahsulotlar=['sut','non','kartoshka','yog`','piyoz','rollton','banan','limon','go\'sht','baliq','qaymoq']
# savat = []

# for i in range(6):
#     savat.append(input("Mahsulot kiriting: "))

# for i in savat:
#     if i in mahsulotlar:
#         print(f"Dokonimizda {i} bor")
#     else:
#         print(f"Dokonimizda {i} yoq")



# 25.12.2022 9:17

# users=['abdulaziz','xamza17','laziz','abdulaziz2212','qorakul2019']
# a=input('Yangi login tanlang: ').lower()
# if a in users:
#     print('Login band,boshqa login tanlang!:')
# else: print(f"Xush kelibsiz! {a.lower()}! ")

a=int(input('Son kiriting:  '))
for i in range(2,11):
    if a%i==0:
        print(f"{a} soni {i} ga bo\'linadi ")

#if not (a%i): #bilan ham ishlasa bolarkan

# 154-qatordagi masalani qisqaroq usuli:

# mahsulotlar=['sut','non','kartoshka','yog`','piyoz','rollton','banan','limon','go\'sht','baliq','qaymoq']
# savat=[]
# for i in range(1,6):
#     savat.append(input(f"{i} chi mahsullotni tanlang: "))
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f"{mahsulot} dokonimizda bor")
#     else:print(f"{mahsulot} dokonimzda yoq")


# mahsulotlar=['sut','non','kartoshka','yog`','piyoz','rollton','banan','limon','go\'sht','baliq','qaymoq']

# bor_mahsulotlar=[]
# yoq_mahsulotlar=[]
# royhat=[]
# for a in range(1,7):
#     royhat.append(input(f"Savatga {a} chi mahsulotni qo\'shing: "))
# for savat in royhat:
#     if savat in mahsulotlar:
#         bor_mahsulotlar.append(savat)
#     else: 
#         yoq_mahsulotlar.append(savat)
# if yoq_mahsulotlar:
#             print(f"Do\'konimizda quyidagi mahsulotlar yoq:\n {str(yoq_mahsulotlar)} ")
# else: print('Siz so\'ragan barcha mahsulot bizda bor')


# BUNAQA QILSA HAM BOLARKAN OXIRINI:
## if yoq_mahsulotlar:
##      print(f"Do\'konimizda quyidagi mahsulotlar yoq: ")
##     for savat in yoq_mahsulotlar:
##         print(savat)
## else: print('Bizda barcha mahsulotlar bor')


# 12-dars xatolar bilan ishlash


















