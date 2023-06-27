def fac(f):
  res=1
  while f>=1:
    res=res*f
    f=f-1
  return(res)

f=int(input("num : "))
print(fac(f))
