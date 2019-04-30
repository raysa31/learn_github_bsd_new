#  Materi 03 - LOOP 

# Solve It 1!
# angka = 0
# while (angka <=10):
#     print ("Nomer Urut " + str(angka))
#     angka += 1

# for item in range (0,11,1):
#     print("Nomer Urut " + str(item))

# Solve It 2!
# angka = 0
# while (angka <=20):
#     print ("Nomer Urut " + str(angka))
#     angka += 2

# for item in range (0,21,2):
#     print("Nomer Urut " + str(item))

# Solve It 3!
# angka = 1
# while (angka <=19):
#     print ("Nomer Urut " + str(angka))
#     angka += 2

# for item in range (1,21,2):
#     print("Nomer Urut " + str(item))

# Example Loop Drawing bikin kotak
# cara bikin kotak 1
# z=' '
# for item in range(5):
#     z += '*  *  *  *  * '
#     z += '\n '
# print(z)

# # cara bikin kotak 2
# z=' * ' * 5
# for item in range(5):
#     print(z)

# cara bikin kotak 3
# z=' '
# for baris in range(5):
#     for kolom in range(5):
#         z += ' * '
#     z += ' \n '
# print (z)

# Example Loop Drawing 2
# z=' '
# for item in range(0,5):
#     z += ' * '
#     z += '*\n ' 
#     print (z)
# # arti dari \n artinya enter

# Example Loop Drawing 3
# cek triangle kiri
# num=int(input("enter the number of rows : "))
# for i in range(1, num+1):
#   for j in range(1, i+1):
#     print(' * ',end=' ')
#   print()

# ----------------------------------------
# HOMEWORK LOOP - SOLVE IT

# Solve it1! triangle right

# num= int(input('insert number : '))

# for x in range(num,0,-1):
#     z = ''
#     for y in range (0,x):
#         z += '*   ' 
#     print (z)

# Solve it2! triangle up down (rys)
# num=int(input("enter the number of rows : "))
# for x in range(num):
#     for y in range(num-x):
#         print('*',end='   ')
#     print()
# for x in range(1, num):
#     for y in range(x+1):
#         print('*',end='   ')
#     print()

# python 3 function:
#   By default there is a newline character appended to the item being printed (end='\n'), and end='' is used to make it printed on the same line.
#   And print() prints an empty newline, which is necessary to keep on printing on the next line.


# Solve it2! triangle up down
# z = ''

# for x in range(5):
#     for y in range (5-x):
#         z += ' * '
#     z += '\n'

# for x in range (1,5):
#     for y in range(x+1):
#         z += ' * '
#     if x != 4:
#         z += '\n'
# print (z)

# Solve it2! triangle up down versi mas indra
# z = ' * '

# for item in range (9):
#     if item < 5:
#         num = 5 - item
#         print (z * num)
#     else:
#         num = item - 3
#         print (z * num)
        
# Solve it3! pyramid up (pak wendy)
# z = '   '
# x = ' * '

# for line in range(10):
#     spasi = z * (9 - line)
#     bintang = (x * 2 * line) + x
#     print (spasi + bintang)

# z = ' - '
# x = ' * '

# Solve it3! pyramid up (mas indra)
# lines = 10
# line = 0
# z = ' * '
# dec_spasi = 1
# mul_bintang = 1

# while line < lines:
#     spasi = '   ' * (10 - dec_spasi)
#     bintang = z * mul_bintang

#     print(line, spasi + bintang)

#     # update
#     line += 1
#     dec_spasi += 1
#     mul_bintang += 2

# Solve it3! pyramid up (raysa) - dont have space between stars
# num=int(input('insert number : '))
# for pyramid in range(0,num):
#     for baris_spasi in range(0,num-1-pyramid):
#         print(' ', end='   ')
#     for baris_bintang in range(0, 2*pyramid + 1):
#         print('*', end='   ')
#     print ('\n')    

# Solve it3! pyramid up (raysa) - print all stars with space
# num=int(input('insert number : '))
# for pyramid in range(0,num):
#     for baris_spasi in range(0,num-1-pyramid):
#         print(' ', end=' ')
#     for baris_bintang in range(0, pyramid + 1):
#         print('*  ', end=' ')
#     print ('\n')    

# python 3 function:
#   By default there is a newline character appended to the item being printed (end='\n'), and end='' is used to make it printed on the same line.
#   And print() prints an empty newline, which is necessary to keep on printing on the next line.


# Solve it4! Inverted Pyramid (Raysa)
# num=int(input('insert inverted pyramid rows : '))

# for pyramid in reversed(range(0, num)):                #tambahankan fungsi reversed untuk membali
#     for baris_spasi in range(0, num-pyramid-1):
#         print('   ', end=' ')
#     for baris_bintang in range(0, 2*pyramid +1):
#         print(' * ', end=' ')
#     print('\n') 

# Solve it4! Inverted Pyramid (Raysa2)
# num= int(input('insert inverted pyramid rows : '))

# bintang = ' * '
# spasi = ' - '

# for pyramid in range(num, -1,-1):   
#     baris_bintang = bintang + (bintang*2*pyramid) 
#     baris_spasi = spasi * (num-pyramid)
#     print (baris_spasi + baris_bintang)

# Solve it4! Inverted Pyramid (Raysa3)
# num= int(input('insert inverted pyramid rows : '))

# bintang = ' * '
# spasi = ' - '

# for pyramid in range(0, num):   
#     baris_bintang = num*2 - (2*pyramid) - 1
#     baris_spasi = pyramid
#     print (spasi*baris_spasi + bintang*baris_bintang)

# Solve it5! Hourglass Pattern (Raysa)
num = int(input('insert how many rows : '))

for pyramid in (range(0, num)):                        #Pyramid 
    for baris_spasi in range(0, num-pyramid-1):
        print('   ', end=' ')
    for baris_bintang in range(0, 2*pyramid +1):
        print(' * ', end=' ')
    print('\n') 

while pyramid in reversed(range(0, num)):                #reversed pyramid
    for baris_spasi in range(0, num-pyramid-1):
        print('   ', end=' ')
    for baris_bintang in range(0, 2*pyramid +1):
        print(' * ', end=' ')
    print('\n') 

# python 3 function:
#   By default there is a newline character appended to the item being printed (end='\n'), and end='' is used to make it printed on the same line.
#   And print() prints an empty newline, which is necessary to keep on printing on the next line.

# Solve it5! Hourglass Pattern (Raysa1)
num= int(input('insert inverted pyramid rows : '))

bintang = ' * '
spasi = ' - '

for pyramid in range(0, num):                                   #reversed pyramid
    baris_bintang = num*2 - (2*pyramid) - 1
    baris_spasi = pyramid
    print (spasi*baris_spasi + bintang*baris_bintang)

for pyramid in reversed(range(0, num)):                               # pyramid
    baris_bintang = num*2 - (2*pyramid) - 1
    baris_spasi = pyramid
    print (spasi*baris_spasi + bintang*baris_bintang)