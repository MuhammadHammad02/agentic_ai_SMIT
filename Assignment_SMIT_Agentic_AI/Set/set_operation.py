'''
Create two sets: A = {1, 2, 3, 4} B = {3, 4, 5, 6}

Print their:

Union (all unique elements from both sets)
Intersection (elements common to both sets)
Difference (elements in A but not in B)
'''

if __name__ == "__main__":
    A = {1, 2, 3, 4}
    B = {3, 4, 5, 6}

    # Union
    union_set = A.union(B)
    print("Union of A and B:")
    print(union_set)

    # Intersection
    intersection_set = A.intersection(B)
    print("\nIntersection of A and B:")
    print(intersection_set)

    # Difference
    difference_set = A.difference(B)
    print("\nDifference of A and B (A - B):")
    print(difference_set)


    