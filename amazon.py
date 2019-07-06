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

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('There are total', len(new), 'of reviews that contain 100 words or less')

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('There are total', len(good), 'of reviews that contain a word ''good'' ')



