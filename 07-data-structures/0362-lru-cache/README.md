# 0362 — LRU Cache

With a capacity-2 LRU cache: put(1,1),put(2,2),get(1),put(3,3) evicts key 2; then get(1)=1 and get(2)=-1, printing `1 -1`. An OrderedDict with move_to_end and popitem(last=False) gives O(1) recency tracking idiomatically.

## Run

    python3 main.py
