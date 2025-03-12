from itertools import combinations
def indexer(arr : list[str]):
    indexed_map = dict()
    for i,val in enumerate(arr):
        indexed_map[val] = i 
    
    return indexed_map


