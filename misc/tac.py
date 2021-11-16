# qorg BTFO once again
# <~qorg> lilibyte: want a programming challenge?
#         rewrite tac(1)
print(*[line.strip() for line in __import__('fileinput').input()][::-1], sep="\n")
