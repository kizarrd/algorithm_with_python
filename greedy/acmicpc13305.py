# 매번 현재 위치보다 기름값이 낮은 곳까지, 혹은 마지막 도시까지만 이동해야함. 

import sys
input = sys.stdin.readline

n = int(input())
distanceList = [int(d) for d in input().split()]
priceList = [int(p) for p in input().split()]
totalCost = 0
currentCityIndex = 0

for i in range(n):
    if priceList[currentCityIndex] > priceList[i] or i == n-1:
        for j in range(currentCityIndex, i):
            totalCost += priceList[currentCityIndex]*distanceList[j]
        currentCityIndex = i
    
print(totalCost)