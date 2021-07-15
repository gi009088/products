products = []
while True:
	name = input('請輸入商品名稱：') 

	if name.title() == 'Q':
		break

	price = input('請輸入商品價格：')
	date = input('請輸入日期：')
	#p = [name, price]
	#p.append(name)
	#p.append(price)
	products.append([name, price, date])
print(products)

for p in products:
	print(p[0], '的價格是', p[1], '購買日期為:', p[2])