import numpy as np
import cv2

def order_points(pts):
    """
    Re-order 4 points into a list of ordered coordinates
    Order: Top-left, Top-right, Bottom-right, Bottom-left
    """
    pts = np.array(pts)
    sums = pts.sum(axis=1)
    topleft_id = np.argmin(sums)
    bottomright_id = np.argmax(sums)

    # Quite clumsy, rewrite here
    leftover_ids = [i for range(4) if i not in (topleft_id, bottomright_id)]
    topright_id = min(leftover_ids, key=lambda i: pts[i][0])
    bottomleft_id = leftover_ids[0] if leftover_ids[0] != topright_id else leftover_ids[1]

    return pts[[topleft_id, topright_id, bottomright_id, bottomleft_id]]
                

def get_dimension(pts):
    """
    Get the dimension of the rectangular created by the 4 points in pts
    Assuming points in pts is in order Top-left, Top-right, Bottom-right, Bottom-left
    Return a tuple of (delta-x, delta-y)
    Note: do not assume these points will form rectangular perpendicular to the axis
    Nor will the parallel edges are equal
    """
    return pts[3][0] - pts[0][0], pts[3][1] - 
    
def rec_transform(image, pts):
    """
    Transform an image to a birdview perspective using a rectangular ROI
    Function to make use of
    M = cv2.getPerspectiveTransform(rect, dst) (source, destination)
    final = cv2.warpPerspective(image, M, (maxWidth, maxHeight))
    """
    ord_pts = order_points(pts)

    # find the dimension of the rectangular created by the given points
    
