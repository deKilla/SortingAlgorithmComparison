from Algorithms import *

import sys
import random
import timeit
import time

from scipy import stats
import numpy as np

import matplotlib as mpl
mpl.use('agg')
import matplotlib.pyplot as plt


# Auslesen der words.txt
words = []

text_file = open("words.txt", "r")
lines = text_file.readlines()
for line in lines:
    words.append(line[:-2])
text_file.close()


# Erhöhen des Rekursionslimits
sys.setrecursionlimit(10000)

# Paremeter für die Durchführung
items = 10000  # wieviele Items sollen in der Liste sein
runs = 1  # Durchschnitt wievieler Durchläufe soll ausgelesen werden (1 = jeder Durchlauf wird ausgelesen)
repeat = 1000  # Wiederholungen

# Wörter durchmischen
random.shuffle(words)

# Array für reguläre Sortierung
arr = words[:items]

# Array für umgekehrte Liste
#arr = list(reversed(words))[:items]

# Array für few uniques
#randomwords = random.sample(words, 10)
#arr = [randomwords[i//1000] for i in range(len(randomwords)*1000)]
#random.shuffle(arr)


#print(arr[:20])


print('sorting {} items over {} runs, repeating {} times'.format(items, runs, repeat))

# ----------------------------------------------------------- #
# bubblesort und insertionsort sind viel zu lahm -> O(n^2)    #
# ----------------------------------------------------------- #
#bubbletest = timeit.Timer(lambda: bubble_sort(list(arr)))
#print("Average time for bubble_sort: {} seconds".format(bubbletest.repeat(repeat=repeat, number=runs)))

#insertiontest = timeit.Timer(lambda: insertion_sort(list(arr)))
#print("Average time for insertion_sort: {} seconds".format(insertiontest.repeat(repeat=repeat, number=runs)))
# ----------------------------------------------------------- #


# Durchführung der Tests + Ausgabe einiger Logging Informationen
mergetest = timeit.Timer(lambda: merge_sort(list(arr)))
mergeresult = mergetest.repeat(repeat=repeat, number=runs)

print("MERGESORT:")
print("Maximum duration was {} seconds and minimum duration was {}".format(max(mergeresult), min(mergeresult)))
print("Shapiro-Wilk-Test for normality: {}".format(stats.shapiro(mergeresult)))
print("\n")

heaptest = timeit.Timer(lambda: heap_sort(list(arr)))
heapresult = heaptest.repeat(repeat=repeat, number=runs)

print("HEAPSORT:")
print("Maximum duration was {} seconds and minimum duration was {}".format(max(heapresult), min(heapresult)))
print("Shapiro-Wilk-Test for normality: {}".format(stats.shapiro(heapresult)))
print("\n")

timtest = timeit.Timer(lambda: sorted(list(arr)))
timresult = timtest.repeat(repeat=repeat, number=runs)

print("TIMSORT")
print("Maximum duration was {} seconds and minimum duration was {}".format(max(timresult), min(timresult)))
print("Shapiro-Wilk-Test for normality: {}".format(stats.shapiro(timresult)))
print("\n")

quicktest = timeit.Timer(lambda: quick_sort(list(arr)))
quickresult = quicktest.repeat(repeat=repeat, number=runs)

print("QUICKSORT:")
print("Maximum duration was {} seconds and minimum duration was {}".format(max(quickresult), min(quickresult)))
print("Shapiro-Wilk-Test for normality: {}".format(stats.shapiro(quickresult)))
print("\n")


# Erfassen statistischer Daten
stats = [
    [np.amin(mergeresult), np.amin(heapresult), np.amin(timresult), np.amin(quickresult)],
    [np.amax(mergeresult), np.amax(heapresult), np.amax(timresult), np.amax(quickresult)],
    [np.median(mergeresult), np.median(heapresult), np.median(timresult), np.median(quickresult)],
    [np.average(mergeresult), np.average(heapresult), np.average(timresult), np.average(quickresult)],
    [np.std(mergeresult), np.std(heapresult), np.std(timresult), np.std(quickresult)],
    [np.var(mergeresult), np.var(heapresult), np.var(timresult), np.var(quickresult)],
]

# Definition der Zeilen/Spalten für das CSV
types = ["Minimum","Maximum","Median","arithmetischer Durchschnitt","Standardabweichung","Varianz"]
algos = ["Mergesort","Heapsort","Timsort","Quicksort"]

# Generieren eines CSV mit den statistischen Daten
summary = open("results/summary_{}.csv".format(int(time.time())),"w+")
i = 0
summary.write(" , ")
for algo in algos:
    summary.write(algo + ", ")
summary.write("\n")
for values in stats:
    summary.write(types[i] + ", ")
    for value in values:
        summary.write("{}, ".format(value))
    summary.write("\n")
    i = i+1
summary.close()

# Erstellen des Plots - wie das geht ... => https://matplotlib.org/
fig = plt.figure(1, figsize=(10,8))
violin = fig.add_subplot(111)
box = fig.add_subplot(111)
violin.violinplot([mergeresult, heapresult, timresult, quickresult], showmeans=False, showmedians=False, showextrema=False)
box.boxplot([mergeresult, heapresult, timresult, quickresult], showfliers=False)
plt.ylabel("execution time in seconds")
violin.xaxis.set_ticklabels(["Mergesort","Heapsort","Timsort","Quicksort"])

# Plot speichern oder
fig.savefig('results/graph_{}.png'.format(int(time.time())), bbox_inches='tight')
# Plot anzeigen - nur eines davon geht (entweder speichern ODER anzeigen)
# wenn man anzeigen will muss man die Line 12 oben auskommentieren
#fig.show()

# Messzeiten speichern
mergelog = open("results/log_merge_{}_{}_{}".format(items, repeat, int(time.time())),"w+")
for result in mergeresult:
    mergelog.write("{}, ".format(result))
mergelog.close()
heaplog = open("results/log_heap_{}_{}_{}".format(items, repeat, int(time.time())),"w+")
for result in heapresult:
    heaplog.write("{}, ".format(result))
heaplog.close()
timlog = open("results/log_tim_{}_{}_{}".format(items, repeat, int(time.time())),"w+")
for result in timresult:
    timlog.write("{}, ".format(result))
timlog.close()
quicklog = open("results/log_quick_{}_{}_{}".format(items, repeat, int(time.time())),"w+")
for result in quickresult:
    quicklog.write("{}, ".format(result))
quicklog.close()
