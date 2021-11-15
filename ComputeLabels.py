import itertools
import numpy as np
import math


def equivalentCycles(c1,c2):
  c1 = ''.join(c1)+''.join(c1)
  c2 = ''.join(c2)
  return c2 in c1


def getCyclicPermutations(P,k):
  permutations = itertools.permutations(P,k)
  cycles = []
  for permutation in permutations:
    new = True
    for cycle in cycles:
      if equivalentCycles(cycle,permutation):
        new = False
    if new:
      cycles.append(permutation)
  return cycles


def getCyclicPermutations2(n,points = None,start = 'A'):
  if not points:
    points = "BCDEFGHIJKLMNOP"[:n-1]
  permutations = itertools.permutations(points,len(points))
  cycles = [(start,) + permutation for permutation in permutations]
  return cycles


def windingNumber(L,cycle):
  cycle = list(cycle)
  cycle.append(cycle[0])
  winding = 0
  cycle_index = 0
  L_index = L.index({cycle[cycle_index],cycle[cycle_index+1]})
  index = (L_index+1) % len(L)
  while cycle_index < len(cycle)-1:
    if {cycle[cycle_index],cycle[cycle_index+1]} == L[index]:
      cycle_index += 1
    if index == L_index:
      winding += 1
    index = (index+1) % len(L)
  return winding

def makeMoves(L0,moves):
  L = L0.copy()
  for move in moves:
    index0 = L.index(set(move[0]))
    index1 = L.index(set(move[1]))
    L[index0] = set(move[1])
    L[index1] = set(move[0])
  return L

def descents(cycle, map):
  s = 0
  for i in range(1,len(cycle)-1):
    if map[int(cycle[i])] > map[int(cycle[i+1])]:
      s = s + 1
  return s


def getMap(n):
  map = np.zeros(n+1, dtype=int)
  k = n
  for i in range(n):
    map[i+1] = k % n
    k = k + int(n/2)
  return map

def perm(a, L, k=0):
  global contador_global, myCount, partition
  if k == len(a):
    cycle = ['A']
    for letter in a:
      cycle.append(P[letter])
    cycle = tuple(cycle)
    myCount[windingNumber(L,cycle)] += 1
    contador_global = contador_global + 1
    if contador_global % partition == 0:
      print(contador_global/partition, ":", cycle, windingNumber(L1,cycle))
  else:
    for i in range(k, len(a)):
      a[k], a[i] = a[i] ,a[k]
      perm(a, L, k+1)
      a[k], a[i] = a[i], a[k]


def permuteLine(L, A, B):
  for i in range(len(L)):
    s = ''.join(L[i])
    s = s.replace(A, '.')
    s = s.replace(B, A)
    s = s.replace('.', B)
    L[i] = set(s)
  return L

def linesEquivalent(L1, L2):
  global P
  if L1 == L2:
    return True
  lines_different = True
  i = 0
  while i < len(P) and lines_different:
    j = 0
    while j < len(P) and lines_different:
      if L1 == permuteLine(L2.copy(), P[i], P[j]):
        lines_different = False
      j = j + 1
    i = i + 1
  return not lines_different


def getLabelSet(L):
  n = len(set("".join(["".join(line) for line in L])))
  P = "ABCDEFGHIJKLMNOP"
  Gamma = dict()
  for k in range(4,n+1):
    Gamma[k] = dict()
    my_combinations = itertools.combinations(P[:n], k)
    for a in set(my_combinations):
      points = "".join(a)
      cycles = getCyclicPermutations2(k, points=points[1:], start=points[0])
      s = ""
      sum = [0]
      count = [0]
      myCount = [0]*k
      for cycle in cycles:
        myCount[windingNumber(L,cycle)] += 1
      if str(myCount[1:k]) in Gamma[k]:
        Gamma[k][str(myCount[1:k])] += 1
      else:
        Gamma[k][str(myCount[1:k])] = 1
    print(Gamma[k])

L = [{'C','A'},{'D','F'},{'B','C'},{'D','A'},{'E','F'},{'A','E'},{'B','D'},{'A','F'},{'B','E'},{'C','D'},{'C','E'},{'B','F'},{'C','F'},{'D','E'},{'B','A'}]

getLabelSet(L)