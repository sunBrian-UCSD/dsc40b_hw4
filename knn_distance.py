import random

def knn_distance(arr, q, k):
    dist_points = [(abs(point - q), point) for point in arr]
    
    kth_dist, kth_point = quickselect(dist_points, k - 1) 
    
    return (kth_dist, kth_point)


def quickselect(items, k):
    if len(items) == 1:
        return items[0]
    
    pivot = random.choice(items)
    
    less = [item for item in items if item[0] < pivot[0]]
    equal = [item for item in items if item[0] == pivot[0]]
    greater = [item for item in items if item[0] > pivot[0]]
    
    if k < len(less):
        return quickselect(less, k)
    elif k < len(less) + len(equal):
        return equal[0] 
    else:
        return quickselect(greater, k - len(less) - len(equal))