"""
CSE101: Introduction to Programming
Assignment 3

Name        :Vaibhav Gupta
Roll-no     :2019341
"""



import math as m
import random



def dist(p1, p2):
    """
    Find the euclidean distance between two 2-D points

    Args:
        p1: (p1_x, p1_y)
        p2: (p2_x, p2_y)
    
    Returns:
        Euclidean distance between p1 and p2
    """
    return m.sqrt(m.pow(p1[0] - p2[0],2) + m.pow(p1[1] - p2[1],2))



def sort_points_by_X(points):
    """
    Sort a list of points by their X coordinate

    Args:
        points: List of points [(p1_x, p1_y), (p2_x, p2_y), ...]
    
    Returns:
        List of points sorted by X coordinate
    """
    return sorted(points,key=lambda x:x[0])



def sort_points_by_Y(points):
    """
    Sort a list of points by their Y coordinate

    Args:
        points: List of points [(p1_x, p1_y), (p2_x, p2_y), ...]
    
    Returns:
        List of points sorted by Y coordinate 
    """
    return sorted(points,key=lambda x:x[1])



def naive_closest_pair(plane):
    """
    Find the closest pair of points in the plane using the brute
    force approach

    Args:
        plane: List of points [(p1_x, p1_y), (p2_x, p2_y), ...]

    Returns:
        Distance between closest pair of points and closest pair 
        of points: [dist_bw_p1_p2, (p1_x, p1_y), (p2_x, p2_y)]
    """
    l=[]

    for i in range(len(plane)-1):
        for j in range(i+1,len(plane)):
            l.append([dist(plane[i],plane[j]),plane[i],plane[j]])

    a=sorted(l,key=lambda x:x[0])

    return a[0]



def closest_pair_in_strip(points, d):
    """
    Find the closest pair of points in the given strip with a 
    given upper bound. This function is called by 
    efficient_closest_pair_routine

    Args:
        points: List of points in the strip of interest.
        d: Minimum distance already found found by 
            efficient_closest_pair_routine

    Returns:
        Distance between closest pair of points and closest pair 
        of points: [dist_bw_p1_p2, (p1_x, p1_y), (p2_x, p2_y)] if
        distance between p1 and p2 is less than d. Otherwise
        return -1.
    """
    if len(points)>=2:

        s=[]
        p=sort_points_by_Y(points)

        for i in range(len(p)-1):
            for j in range(i+1,len(p)):
                s.append([dist(p[i],p[j]),p[i],p[j]])

        a = sorted(s, key=lambda x: x[0])

        if a[0][0]<d:
            return a[0]
        else:
            return -1
    else:
        return -1



def efficient_closest_pair_routine(points):
    """
    This routine calls itself recursivly to find the closest pair of
    points in the plane.

    Args:
    points: List of points sorted by X coordinate

    Returns:
    Distance between closest pair of points and closest pair
    of points: [dist_bw_p1_p2, (p1_x, p1_y), (p2_x, p2_y)]
    """
    n = len(points)

    if n<=3:
        return naive_closest_pair(points)

    mid=n//2

    s1 = points[:mid]
    s2 = points[mid:]

    d1=efficient_closest_pair_routine(s1)
    d2=efficient_closest_pair_routine(s2)

    d,k=min(d1[0],d2[0]),min(d1,d2)

    l = []
    l.append(s2[0])

    for i in range(len(s1)):
        if dist(s1[i], s2[0]) < d:
            l.append(s1[i])

    for j in range(1, len(s2)):
        if dist(s2[j], s2[0]) < d:
            l.append(s2[j])

    fd = closest_pair_in_strip(l,d)

    if fd == -1:
        return k
    else:
        return fd



def efficient_closest_pair(points):
    """
    Find the closest pair of points in the plane using the divide
    and conquer approach by calling efficient_closest_pair_routine.

    Args:
        plane: List of points [(p1_x, p1_y), (p2_x, p2_y), ...]

    Returns:
        Distance between closest pair of points and closest pair 
        of points: [dist_bw_p1_p2, (p1_x, p1_y), (p2_x, p2_y)]
    """
    pt=sort_points_by_X(points)
    return efficient_closest_pair_routine(pt)



def generate_plane(plane_size, num_pts):
    """
    Function to generate random points.

    Args:
        plane_size: Size of plane (X_max, Y_max)
        num_pts: Number of points to generate

    Returns:
        List of random points: [(p1_x, p1_y), (p2_x, p2_y), ...]
    """
    
    gen = random.sample(range(plane_size[0]*plane_size[1]), num_pts)
    random_points = [(i%plane_size[0] + 1, i//plane_size[1] + 1) for i in gen]

    return random_points



if __name__ == "__main__":  
    #number of points to generate
    num_pts = 10
    #size of plane for generation of points
    plane_size = (10, 10)
    plane = generate_plane(plane_size, num_pts)
    print(plane)
    print(naive_closest_pair(plane))
    print(efficient_closest_pair(plane))