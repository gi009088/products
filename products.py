#載入模組查看檔案是否存在
import os
products = []

if os.path.isfile('products.csv'):
	print('檔案存在~')

	#讀取檔案
	with open('products.csv','r', encoding = 'utf-8') as f:
		for line in f:
			if '商品,價格,日期' in line:
				continue	#挑過本回合
			name, price, date = line.strip().split(',')  #先去掉"\n"再使用逗點分割
			products.append([name, price, date])	#將讀取的檔案放到主要清單中
else:
	print('首次執行程式')

#讓使用者輸入
while True:
	name = input('請輸入商品名稱：') 
	if name.title() == 'Q':
		break
	price = input('請輸入商品價格：')
	price = int(price)
	date = input('請輸入日期：')
	products.append([name, price, date])
print(products)

#列印購買紀錄
for p in products:
	print(p[0], '的價格是', p[1], '購買日期為:', p[2])

#儲存檔案
with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品,價格,日期\n')
	for p in products:
		f.write(p[0] + ', ' + str(p[1]) + ', ' + p[2] + '\n')
print('檔案建置完成~!')

