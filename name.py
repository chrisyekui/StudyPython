names = ['yekui','tester','yezi']
for name in names:
	print(name)

sum =0
for x in range(5):
	sum =sum + x
print(sum)

# -*- coding: utf-8 -*-
L = ['Bart', 'Lisa', 'Adam']
for l in L:
	print ('hello,',l,'!')


n=0
while n<len(L):

	print('hello,%s !'%L[n])

	n = n+1

m = 0
while m < 10:
    m = m + 1
    if m % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(m)



p = 0
while p>=0:
	print(p)
	p=p+1


n1 = 255
n2 = 1000

n3=hex(n1)
n4=hex(n2)
print(n3,n4)




