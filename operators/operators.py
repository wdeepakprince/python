print("OPERATORS")
print("---------")


print("\n")
print("Arithmetic Operators")
print("--------------------")
a=int(input("Provide a number for Arithmetic Operations (a): "))
b=int(input("Provide another number for Arithmetic Operations (b): "))
print("\n")
print(a,"+",b," = ",a+b)
print(a,"-",b," = ",a-b)
print(a,"*",b," = ",a*b)
print(a,"/",b," = ",a/b)
print(a,"%",b," = ",a%b)
print(a,"//",b," = ",a//b)
print(a,"**",b," = ",a**b)



print("\n")
print("Assignment Operators")
print("--------------------")
c=int(input("Provide a number for Assignment Operations (c): "))
cc=c
d=int(input("Provide another number for Assignment Operations (d): "))
dd=d

print("\n")
c=cc
d=dd
print("Before c=d :: c is : ",c, " and d is : ",d)
c=d
print("After c=d :: c is : ",c, " and d is : ",d)

print("\n")
c=cc
d=dd
print("Before c+=d :: c is : ",c, " and d is : ",d)
c+=d
print("After c+=d :: c is : ",c, " and d is : ",d)

print("\n")
c=cc
d=dd
print("Before c-=d :: c is : ",c, " and d is : ",d)
c-=d
print("After c-=d :: c is : ",c, " and d is : ",d)

print("\n")
c=cc
d=dd
print("Before c*=d :: c is : ",c, " and d is : ",d)
c*=d
print("After c*=d :: c is : ",c, " and d is : ",d)

print("\n")
c=cc
d=dd
print("Before c/=d :: c is : ",c, " and d is : ",d)
c/=d
print("After c/=d :: c is : ",c, " and d is : ",d)

print("\n")
c=cc
d=dd
print("Before c%=d :: c is : ",c, " and d is : ",d)
c%=d
print("After c%=d :: c is : ",c, " and d is : ",d)

print("\n")
c=cc
d=dd
print("Before c//=d :: c is : ",c, " and d is : ",d)
c//=d
print("After c//=d :: c is : ",c, " and d is : ",d)

print("\n")
c=cc
d=dd
print("Before c**=d :: c is : ",c, " and d is : ",d)
c**=d
print("After c**=d :: c is : ",c, " and d is : ",d)


print("\n")
print("Comparison Operators")
print("--------------------")
e=int(input("Provide a number for Comparison Operations (e): "))
f=int(input("Provide another number for Comparison Operations (f): "))
print("\n")
print("e(",e,")==f(",f,") : ",e==f)
print("e(",e,")!=f(",f,") : ",e!=f)
print("e(",e,")<f(",f,") : ",e<f)
print("e(",e,")>f(",f,") : ",e>f)
print("e(",e,")>=f(",f,") : ",e>=f)
print("e(",e,")<=f(",f,") : ",e<=f)


print("\n")
print("Logical Operators")
print("--------------------")
g=int(input("Provide a number for Logical Operations (g): "))
gg=g
h=int(input("Provide another number for Logical Operations (h): "))
hh=h
print("\n")
i = (g>0) and (g>h)
print("g > 0 AND g > h : ", i) 
i = (g>0) or (g>h)
print("g > 0 OR g > h : ", i)
print("NOT (g > 0 OR g > h) : ", not(i))


print("\n")
print("Special Operators")
print("--------------------")
j=input("Provide a text for Special Operations (j): ")
jj=j
k=input("Provide another text for Special Operations (k): ")
kk=k
print("\n")
member = jj in kk
print("j(",jj,") is a Member in k(",kk,") : ", member)
member = jj not in kk
print("j(",jj,") is not a Member in k(",kk,") : ", member)

print("\n")
identity = jj is kk
print("j(",jj,") is Identity in k(",kk,") : ", identity)
identity = jj is not kk
print("j(",jj,") is not Identity in k(",kk,") : ", member)


print("\n")
print("Bitwise Operators")
print("--------------------")
l=int(input("Provide a number for Bitwise Operations (l): "))
ll=l
m=int(input("Provide another number for Bitwise Operations (m): "))
mm=m
print("\n")

n=l&m
print("l(",l,") & m(",m,") is : ",n)

n=l|m
print("l(",l,") | m(",m,") is : ",n)

n=l^m
print("l(",l,") ^ m(",m,") is : ",n)

n=~l
print("l(",l,") ~ l is : ",n)

n=l>>m
print("l(",l,") >> m(",m,") is : ",n)

n=l<<m
print("l(",l,") << m(",m,") is : ",n)
