from PIL import Image

import pytesseract

import caer

import cv2

import os, sys, inspect #For dynamic filepaths

import numpy as np;	


cam = cv2.VideoCapture(0)


while True:

    check, frame = cam.read()
    


    img = cv2.resize(frame,(320,240))

    imgNew = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_empty = np.zeros((img.shape[0], img.shape[1]))
    img2 = cv2.normalize(imgNew, img_empty, 0, 255, cv2.NORM_MINMAX)
    img3 = cv2.GaussianBlur(imgNew, (5, 5), 2)
    img35 = cv2.adaptiveThreshold(img3, 60, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 0.5)
    img4 = cv2.threshold(img3, 175, 255, cv2.THRESH_BINARY)[1]
    img5 = cv2.Canny(img4, 100, 175)
    img6 = cv2.bilateralFilter(img3, 11,17, 17)
    contours, hierachies = cv2.findContours(img35, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    params = cv2.SimpleBlobDetector_Params()
    detector = cv2.SimpleBlobDetector_create(params)
    keypoints = detector.detect(img3)
    # Draw detected blobs as red circles.
    # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures
    # the size of the circle corresponds to the size of blob
 
    im_with_keypoints = cv2.drawKeypoints(img6, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    contours = sorted(contours, key =cv2.contourArea, reverse = True)[:30]
    screenContours = []
    overlay_contours = img35.copy()

    for c in contours:
        perimeter = cv2.arcLength(c, True)
        approx=cv2.approxPolyDP(c, 0.01*perimeter, True)
        if len(approx) == 4:
            screenContours.append(approx)

    cv2.drawContours(overlay_contours, screenContours, -1, (0,0, 255), 3) 

    cropped = img
    if len(screenContours) > 0:
        x,y,w,h = cv2.boundingRect(screenContours[0]) 
        cropped=img[y:y+h,x:x+w]




    # Output

    #cv2.imshow("Original", img)
   # cv2.imshow("Grey", imgNew)
    #cv2.imshow("Normalized", img2)
    #cv2.imshow("Blurred", img3)
   # cv2.imshow("adaptive Threshold", img35)
    #cv2.imshow("Threshold", img4)
    #cv2.imshow("Edges", img5)
    #cv2.imshow("bilateral", img6)
    #cv2.imshow("Blobs", im_with_keypoints)
    cv2.imshow("Contours", overlay_contours)
    cv2.imshow("Cropped", cropped)

    text = pytesseract.image_to_string(cropped)
    print(text)

    

    key = cv2.waitKey(1)

    if key == 27: # exit on ESC

        break

cam.release()

cv2.destroyAllWindows()
