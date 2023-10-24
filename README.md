# Money-Counter-using-Computer-Vision 💸

![Project Screenshot](https://github.com/saikumaradapa/Money-Counter-using-Computer-Vision/assets/96902883/9581590d-3b37-4895-ada9-a56bcbabd26e)

Ever faced the tedious task of counting numerous coins manually? Fret no more! With the `Coin Counter` project, you can easily count the number of different denominations and get the total value, all using your camera 🎥.

## Project Overview 📖:

This project uses computer vision and image processing to detect coins, differentiate between their denominations, and calculate their total value. It's a useful utility for anyone dealing with a large number of coins regularly or for educational purposes.

## Features 🌟:

- **Real-time Coin Detection**: Instantly detect and differentiate between coins.
  
- **Multi-denomination Support**: Supports various denominations for comprehensive counting.

- **Total Value Calculation**: Get the total monetary value of all detected coins.

- **Visual Feedback**: See the detected coins and their values in a real-time video feed.

- **Stability in Counting**: Ensures accurate coin counting even with a large number of coins, avoiding frequent fluctuation in the count.

## How It Works ⚙️:
- **Image Pre-processing**: The captured video frame undergoes Gaussian blur and edge detection to identify potential coins.

- **Contour Detection**: The pre-processed image is used to detect contours. Based on the area of these contours, the denominations of the coins are identified.

- **Value Calculation**: The number of each denomination is multiplied by its value to get the total money value.

## Tech Stack 🛠️:
- **Python**: Primary programming language.
- **OpenCV**: For image processing and computer vision tasks.
- **cvzone**: An additional utility for easier contour handling and image stacking.

## Installation 💻:

1. Clone this repository:
   ```bash
   git clone https://github.com/saikumaradapa/Money-Counter-using-Computer-Vision

## Project Demo Video 🎥:


https://github.com/saikumaradapa/Money-Counter-using-Computer-Vision/assets/96902883/5b11d3f8-e051-47de-89f5-695389ff42d1




