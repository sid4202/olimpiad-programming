n = int(input())
n_bin = bin(n)[2::]

answer = ''

for c in n_bin:
    if c == '1':
        answer += 'SX'
    elif c == '0':
        answer += 'S'

print(answer[2::])