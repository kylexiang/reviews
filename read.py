data = []
count = 0;
with open ("read(data)","r") as file:
	for line in file:
		data.append(line);
		count += 1;
		if count % 1000 == 0:
			print(len(data));
for i in data:
	print(i,"\n--------------------------------");