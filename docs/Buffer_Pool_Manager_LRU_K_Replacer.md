# Buffer Pool Manager LRU-K Replacement Algorithm Specification

## 1. Formulation
Tracks the timestamp of the last K references to each page frame (default K=2):
- Backward K-Distance: D_K(p) = t_current - t_K(p)
- Frames with fewer than K historical references receive infinite backward distance, ensuring sequential scans do not pollute hot cached pages.
