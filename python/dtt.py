from datetime import datetime

simdi = datetime.now()

simdii21 = datetime.strftime(simdi, '%Y')
simdii22 = datetime.strftime(simdi, '%X')
simdii23 = datetime.strftime(simdi, '%d')
simdii24 = datetime.strftime(simdi, '%A')
simdii25 = datetime.strftime(simdi, '%B')
tam = datetime.strftime(simdi, '%Y %B %A')

print(f'{simdi.year} {simdi.month} {simdi.day}')
print(f'{simdi.second} {simdi.minute} {simdi.hour}')
print(f'{datetime.ctime(simdi)}')


print(f'{simdii21} {simdii22} {simdii23} {simdii24} {simdii25}')
print(f'{tam}')

# İSTEDİĞİM BİR TARİH
birthday = datetime(1983, 5, 9, 12, 30, 10)
result = datetime.timestamp(birthday)
result = datetime.fromtimestamp(result)

print(result)

