products = []
while True:
	name = input('請輸入商品名稱：') 
	if name.title() == 'Q':
		break
	price = input('請輸入商品價格：')
	price = int(price)
	date = input('請輸入日期：')
	
	products.append([name, price, date])
print(products)

for p in products:
	print(p[0], '的價格是', p[1], '購買日期為:', p[2])

with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ', ' + str(p[1]) + ', ' + p[2] + '\n')