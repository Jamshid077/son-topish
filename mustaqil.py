          # for misol-1
# k,n=map(int,input().split())
# for i in range(n):
#    print(k)
         # for misol-2
# a,b=map(int,input().split())
# for i in range(a,b+1):
#    print(i)
        # for misol-4
#a =int(input())
#for i in range(1,11):
#    print(i*a)
        #
#n,k=map(int,input().split())
#c=0

#for i in range(1,n+1):
#    c+=i**k
#print(c)
      # while misol-1
#a,b=map(int,input().split())
#i=0
#while a-b>0:
#   if b < 0:
 #      continue
 #  i+=1

#n=int(input())
#sonlar={0:"nol",1:'bir',2:'ikki',
#        3:'uch',4:'tort',5:'besh'
#        ,6:'olti',7:'yetti',8:'sakkiz',
#        9:'toqqiz',10:'on'
#        }
#if n%10!=0:
#    print(sonlar[10]+sonlar[n % 10])
# Kabisa yoki Kabisa bolmagan yilni kunini hisoblovchi dastur
# n=int(input())
# if n%4==0:
#     if n%100==0:
#         if n%400==0:
#             print('Bu  kabisa yili unda-', 366, 'kun bor')
#         else:
#             print('Bu Kabisa yili emas unda-',365,'kun bor')

#SON TOPISH OYINI

# import random
# def son_topaman(x):
#     tasodifiy=random.randint(1,x)
#     print(f"Salom, Men  {1} dan {x} gacha bolgan sonlardan oyladim!Topinchi???")
#     c=0
#     while True:
#         c+=1
#         son=int(input('>>>'))
#         if tasodifiy< son:
#             print(' Xato.Men oylagan son bundan kichikroq')
#         elif tasodifiy >son:
#             print('Xato.Men oylagan son bundan kattaroq')
#         else:
#             break
#     print(f"Tabriklayman siz {c} urinish bn topdingiz")
# son_topaman(10)
#
# savol=str(input('Men topishimni hohlaysizmi(Ha/Yoq)>>>'))
# if savol=='Ha':
#     def son_topadi(y):
#         s = random.randint(1, y)
#         d = 0
#         print(f"Siz {1} dan {y} gacha bolgan sonlardan oylang men topib beraman!")
#         while True:
#             d += 1
#             son1 = input(
#                 f"Siz oylagan son {s}shumi shu bolsa (T) Kichikroq bolsa (-) Kattaroq bolsa (+)>>>")
#             if son1== "-":
#                 s-=1
#             elif son1== "+":
#                 s+=1
#             else:
#                 break
#         print(f"Men {d} urinish bn topdim!")
#
#     son_topadi(10)


# SOZ TOPISH OYINI



















