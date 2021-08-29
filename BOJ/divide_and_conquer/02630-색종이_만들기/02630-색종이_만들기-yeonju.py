import sys

n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)] 

num = [] 

def div(x, y, n) :
  color = arr[x][y]
  for i in range(x, x+n) :
    for j in range(y, y+n) :
      if color != arr[i][j] :
        div(x, y, n//2)
        div(x, y+n//2, n//2)
        div(x+n//2, y, n//2)
        div(x+n//2, y+n//2, n//2)
        return
  if color == 0 :
    num.append(0)
  else :
    num.append(1)


div(0,0,n)
print(num.count(0)) # 흰색
print(num.count(1)) # 파란색





# n = int(input()) # 한 변의 길이 n

# arr = [list(map(int, input().split())) for _ in range(n)]
# white = 0
# blue = 0
# num = []

# def div(x, y, n):
#     global white, blue
#     color = arr[x][y]
#     for i in range(x, x+n):
#         for j in range(y, y+n):
#             if color != arr[x][y]:
#                 div(x, y, n//2)
#                 div(x, y+n//2, n//2)
#                 div(x+n//2, y, n//2)
#                 div(x+n//2, y+n//2, n//2)
#                 return 

#     if color == 0:
#         white+= 1
#     else:
#         blue += 1

# div(0,0,n)

# print(white) # 흰색 
# print(blue) # 파란색

# [row, column][row, column+ n//2]
# [row+ n//2][row + n//2 , coluumn + n//2]
# git commit -m "Solve boj 02630 색종이 만들기 (yeonju)"

