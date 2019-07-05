data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))

print('There are total', len(data), 'of reviews')

sum_len =0
for d in data: # name every review as d
	sum_len = sum_len + len(d)
print('The average length of 1 million reviews is', sum_len/len(data))


