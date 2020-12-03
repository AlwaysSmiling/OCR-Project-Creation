import cv2 as cv



def run(crop_dat):
    image = cv.imread('srcraw.png')
    (h,w) = image.shape[:2]
    pivot = (w//2, h//2)
    M = cv.getRotationMatrix2D(pivot, crop_dat['rotate'], 1)
    if w>h:
        rotated = cv.warpAffine(image, M, (w, w))
    else:
        rotated = cv.warpAffine(image, M, (h, h))
    
    #x = int(crop_dat['x'])


    cropped = rotated[int(crop_dat['y']):int(crop_dat['y']+crop_dat['height']), int(crop_dat['x']):int(crop_dat['x']+crop_dat['width'])]
    
    cv.imwrite('source.png',cropped)
    return
