# qorg BTFO once again
# <~qorg> lilibyte: want a programming challenge?
#         rewrite tac(1)
print(*[line.strip() for line in __import__('sys').stdin.readlines()[::-1]], sep="\n")
