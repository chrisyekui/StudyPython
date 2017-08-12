# -*- coding: utf-8 -*-

height = float(input('请输入身高'))
weight = float(input('请输入体重'))

bim = weight/(height*height)

if bim>=32:
	print('严重肥胖')
elif bim>=28 and bim<32:
	print('肥胖')
elif bim>=25 and bim<28:
	print('过重')
elif bim>=18.5 and bim<25:
	print('正常')
else:
	print('过轻')