from sys import argv

if len(argv) < 4 or len(argv) > 4:
    print('Try: python args_demo [USER] [TASK] [BENEFIT]')
    exit()
user = argv[0]

task = argv[1]

benefit = argv[3]

print(f'As a {user} I want to {task} so that {benefit}')

