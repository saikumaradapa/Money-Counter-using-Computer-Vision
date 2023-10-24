import cvzone
import cv2
import numpy as np
from cvzone.ColorModule import ColorFinder

# Preset values for the coin areas
areaOfOne = 7100
areaOfTwo = 8450
areaOfFive = 6450

# Placeholder image for the results
imgResult = np.zeros((480, 640, 3), np.uint8)

# Initialize camera capture
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Set the width
cap.set(4, 480)  # Set the height

threshold = 200

# Instantiate ColorFinder object
myColorFinder = ColorFinder(False)

# Define the color range in the HSV space
hsvVals = {'hmin': 0, 'smin': 0, 'vmin': 156, 'hmax': 42, 'smax': 255, 'vmax': 255}


# Function for image preprocessing
def preProcessing(img):
    # Apply Gaussian blur
    imgPre = cv2.GaussianBlur(img, (5, 5), 3)
    # Detect edges using Canny edge detector
    imgPre = cv2.Canny(imgPre, 225, 120)
    kernel = np.ones((3, 3), np.uint8)
    # Dilate the image to enhance the main features
    imgPre = cv2.dilate(imgPre, kernel, iterations=1)
    # Close small holes using morphology
    imgPre = cv2.morphologyEx(imgPre, cv2.MORPH_CLOSE, kernel)
    return imgPre


# Main loop to process video frames
while True:
    # Read a frame from the camera
    success, img = cap.read()
    # Process the frame
    imgPre = preProcessing(img)
    # Find contours on the processed image
    imgContours, conFound = cvzone.findContours(img, imgPre, minArea=20)

    # Variables to hold coin counts and total value
    totalMoney = 0
    nOnes, nTwos, nFives = 0, 0, 0

    # If contours are found
    if conFound:
        for count, contour in enumerate(conFound):
            # Calculate the perimeter of each contour
            peri = cv2.arcLength(contour['cnt'], True)
            # Approximate the contour
            approx = cv2.approxPolyDP(contour['cnt'], 0.02 * peri, True)

            # Process only those contours with more than 5 vertices (likely to be coins)
            if len(approx) > 5:
                area = contour['area']
                x, y, w, h = contour['bbox']

                # Extract the coin's region
                imgCrop = img[y:y + h, x:x + w]

                # Find the color of the coin
                imgColor, mask = myColorFinder.update(img, hsvVals)

                # Count the number of white pixels in the mask (indicating detected color)
                whitePixelCount = cv2.countNonZero(mask)
                print(whitePixelCount)

                # Check the area of the contour to classify the coin and update total money and coin counts
                if area <= areaOfFive + 250:
                    totalMoney += 5
                    nFives += 1
                elif areaOfFive + 250 <= area <= areaOfTwo - 200:
                    totalMoney += 1
                    nOnes += 1
                else:
                    totalMoney += 2
                    nTwos += 1

    # Display the results on the imgResult frame
    cvzone.putTextRect(imgResult, f'Rs.{totalMoney}', (200, 100), scale=5, offset=20, thickness=7, colorT=(255, 0, 0))
    cvzone.putTextRect(imgResult, f'1 X {nOnes} = {1 * nOnes}', (200, 250), scale=2, offset=20, thickness=5,
                       colorT=(0, 255, 0))
    cvzone.putTextRect(imgResult, f'2 X {nTwos} = {2 * nTwos}', (200, 330), scale=2, offset=20, thickness=5,
                       colorT=(0, 255, 0))
    cvzone.putTextRect(imgResult, f'5 X {nFives} = {5 * nFives}', (200, 410), scale=2, offset=20, thickness=5,
                       colorT=(0, 255, 0))

    # Stack and display the images
    stacked = cvzone.stackImages([img, imgPre, imgContours, imgResult], 2, 0.5)
    cv2.imshow("stacked image", stacked)

    # Quit loop on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
