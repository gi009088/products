#讀取檔案
def read_file(filename):
	products = []
	with open(filename,'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue	#挑過本回合
			name, price = line.strip().split(',')  #先去掉"\n"再用逗點分割使
			products.append([name, price])	#將讀取的檔案放到主要清單中
	return products

#讓使用者輸入
def user_input(products):
	while True:
		name = input('請輸入商品名稱：') 
		if name.title() == 'Q':
			break
		price = input('請輸入商品價格：')
		price = int(price)
		products.append([name, price])
	print(products)
	return products

#列印購買紀錄
def print_products(products):
	for p in products:
		print(p[0], '的價格是', p[1])

#儲存檔案
def save_file(new_filename, products):
	with open(new_filename, 'w', encoding = 'utf-8') as f:
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')
	print('檔案建置完成~!')

def main():
	#載入模組查看檔案是否存在
	filename = input('請輸入欲載入的檔案名稱：')+'.csv'
	import os
	if os.path.isfile(filename):
		print('檔案存在~')
		products = read_file(filename)
	else:
		products = []
		print('檔案不存在~')

	products = user_input(products)
	print_products(products)
	new_filename = input('請輸入欲儲存的檔案名稱：') + '.csv'
	save_file(new_filename, products)

main()

