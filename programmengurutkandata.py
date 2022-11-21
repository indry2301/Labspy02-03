print("program mengurutkan data")
a = int(input("masukkan bilangan ke 1: "))
b = int(input("masukkan bilangan ke 2: "))
c = int(input("masukkan bilangan ke 3: "))

if a<b and a<c:
  if b<c:
    print(a,b,c)
  else:
    print(a,c,b)
elif b<a and b<c:
  if a<c:
    print(b,a,c)
  else:
    print(b,c,a)

else:
  if a<b:
    print(c,a,b)
  else:
    print(c,a,b)

print(" ")