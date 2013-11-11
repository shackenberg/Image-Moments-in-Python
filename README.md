Image Moments in Python
=======================
This script implements a function that calculates image moments similar to OpenCV for any image passed as a numpy array.

The code is not written to be efficient, but easy to read and easy to understand moments. See the code for further comments.

There are several synonymous names for the moments:
- raw or spatial moments (the basis) is equal to the mean of the image
- central moments (depending on the raw moments) is equal to the variance of the image
- central standardized or normalized or scale invariant moments (based on the central moments) is equal to the skewness of the image

You can compare the results with:

    import cv2
    from scipy.misc import imread
    image = imread('myimage.png',flatten=1)
    cv2.moments(image)
    
For some reason, some of the central and normlized differ to OpenCV. Please let me know, if you find the error. 
One have to check how OpenCV does the calculations in modules/imgproc/src/moments.cpp

Further reading:
- https://en.wikipedia.org/wiki/Image_moment
- https://en.wikipedia.org/wiki/Central_moment
- https://en.wikipedia.org/wiki/Moment_(mathematics)
- https://en.wikipedia.org/wiki/Standardized_moment
- http://docs.opencv.org/modules/imgproc/doc/structural_analysis_and_shape_descriptors.html#moments
