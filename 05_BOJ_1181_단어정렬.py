# 05_BOJ_1181_단어정렬.py
import heapq

heap = []

for _ in range(13):
    String = input()
    heapq.heappush(heap,String)
# print(heap)
result = []
for s in heap:
    if s not in result:
        heapq.heappush(result, s)
# print(result)

result.sort()
# print(result)
result.sort(key=len)
# print(result)
print(*result, sep='\n')


# 5회차_장하늬 — 오늘 오후 5:14
# ㅋㅋ 저는 heap으로 안풀고 sort로만 푸는 도박을 했습니다.
N = int(input())
lst = []
for _ in range(N):
    word = input()
    if word not in lst: # 중복 방지
        lst.append(word)

lst.sort(key= lambda x : (len(x), x))

print(*lst, sep = '\n') 