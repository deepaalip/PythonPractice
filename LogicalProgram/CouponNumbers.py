import random
def coupon(random_num):
	num = '0123456789'
	coupon_no = ''
	for i in range(0, random_num):
		random_num = random.randint(0, len(num) - 1)
		coupon_no += num[random_num: random_num + 1]
	return coupon_no

print(coupon(6))