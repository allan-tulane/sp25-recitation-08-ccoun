# CMPS 2200 Recitation 08

## Answers

**Name:** Charlie Coun
**Name:** Vincent Camacho


Place all written answers from `recitation-08.md` here for easier grading.



- **1b)** Each edge can cause at most one heap push, and each vertex is popped at most once for a given (dist, edges). Each heap pop or push takes O(log|V|) work, so combining all this we get a total work of O((|E|+|V|)log|V|). For span, the heap pops must be sequential since you must process the best (dist, edges) before considering its neighbors. At each pop there is O(log|V|) span for the heap and then you sequentially iterate over the neighbors, so the total span would be O(|V|log|V|+|E|).



- **2b)**

