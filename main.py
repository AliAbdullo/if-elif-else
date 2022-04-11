#Juft ekanini tekshiruvchi dastur
juft = int(input('Juft son kiriting: '))
if juft%2==0:
  son = "Raxmat!"
else :
  son = "Bu son juft emas"
print(son)

#Chipta narxini yoshiga qarab belgilash
yosh = int(input("Yoshingiznikiriting: "))
if yosh<=4 or yosh>60:
  narx = 0
elif yosh<=18:
  narx = 10000 
else :
  narx = 20000 
print(f"Sizga kirish {narx} so\'m")

#Ikki sonni solishtirish
son1 = float(input("Birinchi sonni kiriting: "))
son2 = float(input('Ikkinchi sonni kiriting: '))
if son1>son2:
  katta = f"{son1}>{son2}"
elif son1<son2:
  katta = f"{son1}<{son2}"
else:
  katta = f"{son1}={son2}"
print(katta)

#maxsuklotlar sotib olish
maxsulotlar  = ['non','pecheney','xurmo','cola','fanta','suv','gul','pepsi']
savat = []
for n in range(5):
  savat.append(input(f"Savatga {n+1}-maxsulotni qo'shing: "))
  
bor_maxsulotlar=[]
mavjud_emas=[]
for maxsulot in savat:
  if maxsulot in maxsulotlar:
     bor_maxsulotlar.append(maxsulot)
  else:
    mavjud_emas.append(maxsulot)
 
if mavjud_emas:
  print(f"Do'konimizda quydagi maxsulotlar yo'q: ")
  for maxsulot in mavjud_emas:
    print(maxsulot)
else:
      print("Siz so'ragan maxsulotlarning barchsi bor!")

#Login kiritish
foydalanuvchilar = ['ali','abdulloh','abror','islom','sardor']
login = input('Yangi login kiriting: ')
if login.lower() in foydalanuvchilar:
    print("Login band, yangi login tanlang!")
else:
  print("Xush kelibsiz, foydalanuvchi!")
