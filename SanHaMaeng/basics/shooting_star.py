from pip._vendor.colorama import Fore, Style

print(Fore.YELLOW, end='')
print(' ' * 8 + '*')

print(Fore.GREEN, end='')
for x in range(1, 8):
    print(' ' * (9 - x) + '* ' * x)

for x in range(4, 10):
    print(' ' * (9 - x) + '* ' * x)

print(Fore.LIGHTBLACK_EX, end='')
for _ in range(3):
    print(' ' * 6 + '* ' * 3)

print(Style.RESET_ALL)
