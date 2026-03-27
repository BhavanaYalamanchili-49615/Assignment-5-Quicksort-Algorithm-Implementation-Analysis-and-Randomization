## Assignments 5: Quicksort Algorithm
### Overview
There were deterministic and randomized versions of quicksort algorithm. Theoretical concepts and empirical testing have been used to carry out performance analysis. Findings showed effectiveness and performance at various input levels.
### Files Included
deterministicquicksort.py  
randomizedquicksort.py  
empiricalanalysis.py  
report.docx  
### Deterministic Quicksort
Partition function chose the final element as the pivot and sorted the values depending on the comparison. The division of array recursively gave sorted output.
### Randomized Quicksort
Random pivot was used to minimize the possibility of unbalanced partition. There was maintenance in performance regardless of the type of input.
### Empirical Analysis
Different input sizes and distributions were used in which the execution time was determined including random, sorted and reverse sorted arrays. Deterministic and randomized methods were compared in terms of results.
### Results Summary
Deterministic quicksort was an efficient algorithm when used on random data. Randomized quicksort demonstrated constant performance in all cases. There was a gradual increase in the execution time as the input size increased.
### How to Run
1. Open PyCharm  
2. Open project folder  
3. Open each file  
4. Run files using run button
### Conclusion
Quicksort was a good sorting algorithm with average O(n log n) complexity. Randomization led to the enhancement of stability and minimization of worst case probability.
