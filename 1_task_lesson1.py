duration = int(input())
if duration // 86400 > 0:
	print(duration // 86400, "дн ", end = '')
	duration = duration - 86400*(duration // 86400)
if duration // 3600 > 0:
	print(duration // 3600, "час ", end = '')
	duration = duration - 3600*(duration // 3600)
if duration // 60 > 0:
	print(duration // 60, "мин ", end = '')
	duration = duration - 60*(duration // 60)
if duration // 1 > 0:
	print(duration // 1, "cек ", end = '')
	duration = duration - 1*(duration // 1)
print(1)
print(123334 // 10)
