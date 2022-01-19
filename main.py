# son1 = 1
# while son1<=5:
#      print(son1,end=' ')
#      son1 = son1+1
# print('Kritilgan sonni kvadratga oshiruvchi dastur
# ')
# savol = 'Istalgan sonni kiriting'
# savol +='(To`xtatish uchun "exit" deb yozing): '
# qiymat = ''
# while qiymat !='exit':
#     qiymat = input(savol)
#     if qiymat !='exit':
#         print(float(qiymat)**2)
# print('Kritilgan sonni kvadratga oshiruvchi dastur')
# savol = 'Istalgan sonni kiriting'
# savol +='(To`xtatish uchun "exit" deb yozing): '
# qiymat = ''
# while qiymat !='exit':
#     qiymat = input(savol)
#     if qiymat !='exit':
#         print(float(qiymat)**2)
# print("Yoqritgan Kitobingiz nomini kiriting")
# kitob ="Istalgan kitob \n"
# kitob +="Dasturni to`xtatish uchun 'sotp'ni kiriting: "
# Qiymat = ''
# while Qiymat != 'stop':
#     Qiymat = input(kitob)
#     if Qiymat != 'stop':
#         print(Qiymat)
# print("Istalgan Kitobingiz nomini kiriting")
# kitob = 'Kitob nomini kiriting>>>'
# kitob += "(Dasturni to`xtatish uchun 'exit','quit' ni kiriting):"
# qiymat = True
# while qiymat:
#     qiymat = str(input(kitob))
#     if qiymat == 'exit' or qiymat == 'quit':
#         qiymat = False
#     else:
#         qiymat =int(qiymat)
#         if qiymat<=7:
#             print("Assalomu Alaykum sizga muzayga kirish narxi 2000 so`m")
#         elif (qiymat>7 and qiymat<18):
#             print("Assalomu Alaykum sizga muzayga kirish narxi 3000 so`m")
#         elif (qiymat>18 and qiymat<65):
#             print("Assalomu Alaykum sizga muzayga kirish narxi 10000 so`m")
#         elif (qiymat>65):
#             print("Assalomu Alaykum sizga muzayga kirish narxi 10000 so`m")
#         else:qiymat == False
#
# savol = 'kiritilgan sonni ildizini qaytaruvchi dastur .\n'
# savol += 'musbat son kiriting '
# savol +="(Dasturni to`xtatish uchun 'exit' deb yozing '): "
# while True:
#     qiymat = input(savol)
#     if qiymat<'0':
#         continue
#     elif str(qiymat)=='exit':
#         break
#     else:
#         ildiz = float(int(qiymat)**0.5)
#         print(f"{qiymat} - ni ildizi {ildiz}")
# ismlar = []
# print("Yaqin do`slarimizni  ro`yxatini tuzamiz.")
# n = 1
# while True:
#     savol = f"{n} do`stingizni ismini kiriting: "
#     ism = input(savol)
#     ismlar.append(ism)
#     javob = input(f"Yana ism qo`shasizmi ? (xa/yo`q)")
#     if javob =='xa':
#         n+=1
#     else:
#         break
# print("Ro`yxat tuzildi .")
# for ims in ismlar:
#     print(ims)
# print("Do`slaringiz yoshini saqlaymiz.")
# doslar = {
#
# }
# ishoralar = True
#
# while True:
#     ism = input('Do`stingiz ismini kiriting: ')
#     yosh = input(f"{ism.title()}ni Yoshini kiriting: ")
#     doslar[ism]=int(yosh)
#     javob = input("Yana qo`shasizmi?(ha/Yo`q):")
#     if javob == "Yo`q":
#         ishoralar = False
#         break
# for key,valu in doslar.items():
#     print(key , valu)
# cars = ['nexia','lacetti','nexia','toyota','malibu','nexia','tiko']
# while 'nexia' in cars:
#     cars.remove('nexia')
# print(cars)
# talabalar = ['hasan','husan','olim','nodira','shakarxon']
# baxolar = {}
# while talabalar:
#     talaba = talabalar.pop()
#     boho = input(f"{talaba.title()}ning baxosini kiriting: ")
#     print(f"{talaba.title()} Baxolandi")
#     baxolar[talaba] = boho
# print("Talabalar kundaligi")
# for key,qiymat in baxolar.items():
#     print(f"{key} bohosi {qiymat}")
# print(" e-bozorga xush kelibsiz ")
# son = float(input('juft son kiriting :'))
# if int(son)%2==0:
#     print("raxmat")
# else:print('xatolig')
# yosh = int(input("yoshingiz nechida ?"))
# if (yosh>4) and (yosh>60):
#     narx = 0
# elif yosh<18:
#     narx = 1000
# else:
#     narx = 20000
# print(f"chipa narxi {narx}")
# yosh = int(input("yoshingizni kiriting: "))
# try:
#     yosh = int(yosh)
#     print('')
# except ValueError:
#     print(yosh)
# else:
# #     print('siz adashdiz')
# def salom_ber():
#     """Salom Beruvchi funksiya"""
#     print("Assalomu Alaykum !")
#
# def tugulgan_yilni_xisoblash(Hozirgi_yil,yosh):
#     """foydalanuvchi tug`ilgan yilini xioblovchi funksiya"""
#     print(f"{Hozirgi_yil-yosh} siz shu yilda tug`ulgansiz")
# tugulgan_yilni_xisoblash(Hozirgi_yil=2022,yosh=90)
# def xningNchidarjasi(x,n):
#     """x ni n chi darajasini aniqlovchi funksiya"""
#     print(f"{x**n }- x ning n chi darajasi")
# xningNchidarjasi(x=2,n=1)
# def bolinish(n):
#     for i in range(2,10+1):
#
#         if n % i == 0:
#             print(f"2-dan 10-gacha bo`lgan sonlar ichida siz kiritgan songa qoldiqsiz bo`linadigan solar {i} ")
# bolinish(n=4)
# def avto_info(make,model,rangi,korobka,yili,narxi=None):
#     avto={
#         'kampaniya':make,
#         'model':model,
#         'rangi':rangi,
#         'karobka':korobka,
#         'yil':yili,
#         'narxi':narxi
#     }
#     return avto
#
# avto1=avto_info('Gm','Malibu','Qora','Avtomat',2018,20000)
#
# avto2=avto_info('Gm','Nexi','Oq','Mexanik',2013,5000)
#
# avtolar = [avto1,avto2]
# print("online bozordagi mavjud mashinalar:")
#
# for avto in avtolar:
#     if avto['narxi']:
#         print(f"{avto['rangi']}{avto['model']}.Narxi:{avto['narxi']}")
#     else:
#         print(f"{avto['rangi']}{avto['model']}.Narxi:Noma`lum")


# def oraiq(min,max,qadam):
#     sonlar=[]
#     while min<max:
#         sonlar.append(min)
#         min +=qadam
#     return sonlar
# print(oraiq(1,21,2))
# def avto_info(make,model,rangi,korobka,yili,narxi=None):
#     avto={
#         'kampaniya':make,
#         'model':model,
#         'rangi':rangi,
#         'karobka':korobka,
#         'yil':yili,
#         'narxi':narxi
#     }
#     return avto
# print("Saytimizdagi avtolar ro`yxatini shakllantiramiz,")
# avtolar = []
# while True:
#     print("\nQuyidagi ma`lumotlarni kiriting" , end=' ')
#     kompaniya=input('Ishlab chiqaruvchi: ')
#     model = input('Modeli: ')
#     rangi = input('Rangi: ')
#     korobka = input('Korobka: ')
#     yili = input('Yili: ')
#     narxi = input('Narxi: ')
#     avtolar.append(avto_info(make=kompaniya,model=model,rangi=rangi,korobka=korobka,yili=yili,narxi=narxi))
#     javob = input("Yana qo`shmoqchimisiz (yes/no)")
#     if javob=='no':
#         break
#     else:
#         continue
# def registratsiya(ism,familya,yil,manzil,email,tel,kasbi,malumoti):
#     register ={
#         'ism':ism,
#         'fam':familya,
#         'yil':yil,
#         'manzil':manzil,
#         'email':email,
#         'tel':tel,
#         'kasbi':kasbi,
#         'malumoti':malumoti
#     }
#     return register
# print("Assalomu Alaykum  Iltimos ro`yxatdan o`ting")
# register = []
# while True:
#     print("\nQuyidagi Malumotlarni to`ldirihingizni So`raymiz")
#     ism = input('Ismni kiriting: ')
#     fam = input('Famni kiriting: ')
#     yil = input('Qachon tug`ulgansiz: ')
#     manzil =input('Manzilni kiritin: ')
#     email = input('Elektron manzilni kirting: ')
#     tel = input('Telefon raqam: ')
#     kasbi = input('Kasbingiz nima?:')
#     malumot = input('Malumotingiz qanday?:')
#     javob = input('Malumotlar to`g`ri yozilgan bo`lsa (yuborish/bekorqilish): ')
#     register.append(registratsiya(ism,fam,yil,manzil,email,tel,kasbi,malumot))
#     for  shaxs in register:
#         if shaxs['tel']:
#             shaxs['tel']=tel
#         else:
#             shaxs['tel'] = 'Noma`lum'
#         print(f"{shaxs['ism']}\n{shaxs['fam']}\n{shaxs['yil']}\n{shaxs['manzil']}\n{shaxs['email']}\n{shaxs['tel']}\n{shaxs['kasbi']}\n{shaxs['malumoti']}")
#     if javob =='yuborish':
#         continue
#     else:
#
#         break
# son =[]
# def nush(a,b,c):
#     son.append(a)
#     son.append(b)
#     son.append(c)
#     print(max(son))
#     return son
# nush(5,8,9)
