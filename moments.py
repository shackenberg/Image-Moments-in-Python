from numpy import mgrid, sum

def moments2e(image):
  """
  This function calculates the raw, centered and normalized moments
  for any image passed as a numpy array.

  Further reading:
  https://en.wikipedia.org/wiki/Image_moment
  https://en.wikipedia.org/wiki/Central_moment
  https://en.wikipedia.org/wiki/Moment_(mathematics)
  https://en.wikipedia.org/wiki/Standardized_moment
  http://opencv.willowgarage.com/documentation/cpp/structural_analysis_and_shape_descriptors.html#cv-moments
  
  compare with:
  import cv2
  cv2.moments(image)

  """
  assert len(image.shape) == 2 # only for grayscale images        
  x, y = mgrid[:image.shape[0],:image.shape[1]]
  moments = {}
  moments['mean_x'] = sum(x*image)/sum(image)
  moments['mean_y'] = sum(y*image)/sum(image)
          
  # raw or spatial moments
  moments['m00'] = sum(image)
  moments['m01'] = sum(x*image)
  moments['m10'] = sum(y*image)
  moments['m11'] = sum(y*x*image)
  moments['m02'] = sum(x**2*image)
  moments['m20'] = sum(y**2*image)
  moments['m12'] = sum(x*y**2*image)
  moments['m21'] = sum(x**2*y*image)
  moments['m03'] = sum(x**3*image)
  moments['m30'] = sum(y**3*image)
  
  # central moments
  # moments['mu01']= sum((y-moments['mean_y'])*image) # should be 0
  # moments['mu10']= sum((x-moments['mean_x'])*image) # should be 0
  moments['mu11'] = sum((x-moments['mean_x'])*(y-moments['mean_y'])*image)
  moments['mu02'] = sum((y-moments['mean_y'])**2*image) # variance
  moments['mu20'] = sum((x-moments['mean_x'])**2*image) # variance
  moments['mu12'] = sum((x-moments['mean_x'])*(y-moments['mean_y'])**2*image)
  moments['mu21'] = sum((x-moments['mean_x'])**2*(y-moments['mean_y'])*image) 
  moments['mu03'] = sum((y-moments['mean_y'])**3*image) 
  moments['mu30'] = sum((x-moments['mean_x'])**3*image) 

    
  # opencv versions
  #moments['mu02'] = sum(image*(x-m01/m00)**2)
  #moments['mu02'] = sum(image*(x-y)**2)

  # wiki variations
  #moments['mu02'] = m20 - mean_y*m10 
  #moments['mu20'] = m02 - mean_x*m01
        
  # central standardized or normalized or scale invariant moments
  moments['nu11'] = moments['mu11'] / sum(image)**(2/2+1)
  moments['nu12'] = moments['mu12'] / sum(image)**(3/2+1)
  moments['nu21'] = moments['mu21'] / sum(image)**(3/2+1)
  moments['nu20'] = moments['mu20'] / sum(image)**(2/2+1)
  moments['nu03'] = moments['mu03'] / sum(image)**(3/2+1) # skewness
  moments['nu30'] = moments['mu30'] / sum(image)**(3/2+1) # skewness
  return moments