data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取成功，總共有', len(data), '筆資料')

# print(data[0])

sum_len = 0
for d in data:
	sum_len += len(d)
print('平均長度是', sum_len/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')
# print(new[0])

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆留言有good')
# print(good[0])


# good = [1 for d in data if 'good' in d]
# output = [(number - 1) for number in reference if number % 2 == 0]
#              運算            變數       清單              篩選條件
# print(good)



wc = {} # word count
for d in data:
	words = d.split() #預設空白
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1

for word in wc:
	if wc[word] > 1000000:
		print('[', word, '],的出現次數非常高，總共出現', wc[word], '次')

print('總共分類了', len(wc), '個字')

while True:
	word = input('請問你想查什麼字： ')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為：', wc[word])
	else:
		print('這個字沒有出現過喔～')

print('感謝使用此查詢系統')








