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
a = 0;
for i in data:
	a += len(i);
print("资料总长度为",a);
print("资料平均长度为",(a / len(data)));
