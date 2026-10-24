## Image-Handling-and-Pixel-Transformations-Using-OpenCV


**Name:**  SADHANA S
**Register Number:**  212224230234
**Experiment:** Image Handling and Pixel Transformations Using OpenCV

---

## AIM

To perform image handling and pixel transformations using Python and OpenCV, including reading and displaying images, drawing shapes, adding text, color space conversion, pixel manipulation, image resizing, cropping, flipping, and saving the modified image.

## SOFTWARE REQUIRED

- Python
- OpenCV
- Matplotlib
- Jupyter Notebook
- Anaconda (optional)

## INSTALLATION

Install the required libraries using the following command:

```bash
pip install opencv-contrib-python-headless matplotlib
```

## ALGORITHM

### Step 1: Read and Display an Image

1. Import OpenCV and Matplotlib libraries.
2. Read an image from the local directory using `cv2.imread()`.
3. Convert the image from BGR to RGB.
4. Display the original image using Matplotlib.

### Step 2: Draw Shapes and Add Text

1. Draw a line from the top-left to the bottom-right of the image.
2. Draw a circle at the center of the image.
3. Draw a rectangle around the image.
4. Add the text "OpenCV Drawing" at the top-left corner.

### Step 3: Color Space Conversion

1. Convert the RGB image to HSV and display it.
2. Convert the RGB image to grayscale and display it.
3. Convert the RGB image to YCrCb and display it.
4. Convert the HSV image back to RGB and display it.

### Step 4: Pixel Manipulation

1. Access and print the pixel value at coordinates `(100, 100)`.
2. Change the pixel at coordinates `(200, 200)` to white.
3. Modify a 300 × 300 region of the image to white.
4. Display the modified image.

### Step 5: Image Resizing

1. Read the original image.
2. Resize the image to half its original width and height.
3. Display the resized image.

### Step 6: Image Cropping

1. Read the original image.
2. Extract a 300 × 300 region of interest starting at `(50, 50)`.
3. Display the cropped image.

### Step 7: Image Flipping

1. Flip the original image horizontally.
2. Flip the original image vertically.
3. Display both flipped images.

### Step 8: Save the Final Modified Image

1. Save the modified image in the local directory using `cv2.imwrite()`.
2. Verify that the image has been saved successfully.

---

## PROGRAM

### Step 1: Read and Display an Image

```
import cv2
import matplotlib.pyplot as plt

# Read the image using OpenCV
img = cv2.imread(r"C:\Users\admin\Downloads\me2.jpeg", cv2.IMREAD_COLOR)

# Convert BGR (OpenCV's default) to RGB (Matplotlib's expected color order)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Display the image using Matplotlib
plt.imshow(img_rgb, cmap='viridis')  
plt.title("Original Image")
plt.axis('off')  
plt.show()
```

### Step 2: Draw Shapes and Add Text

#### 2.1 Draw a Line

```
# Load the image
image = cv2.imread(r"C:\Users\admin\Downloads\me2.jpeg") 

# Convert BGR to RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(img_rgb.shape)

# Draw a line from top-left to bottom-right
line_img = cv2.line(img_rgb, (0, 0), (768, 600), (255, 0, 0), 2) 

# Display the image
plt.imshow(line_img, cmap='viridis')  
plt.title("Image with Line")
plt.axis('off')  
plt.show()
```

#### 2.2 Draw a Circle

```
# Load the image
image = cv2.imread(r"C:\Users\admin\Downloads\me2.jpeg") 

# Convert BGR to RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(img_rgb.shape)

# Draw a circle
circle_img = cv2.circle(img_rgb, (400, 300), 150, (255, 0, 0), 10) 

# Display the image
plt.imshow(circle_img, cmap='viridis')  
plt.title("Image with Circle")
plt.axis('off')  
plt.show()
```

#### 2.3 Draw a Rectangle

```
# Load the image
image = cv2.imread(r"C:\Users\admin\Downloads\me2.jpeg") 

# Convert BGR to RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(img.shape)

# Draw a rectangle around the Whole image
rectangle_img = cv2.rectangle(img_rgb, (0, 0), (768, 600), (0, 0, 255), 10)  

# Display the image
plt.imshow(rectangle_img, cmap='viridis')  
plt.title("Image with Rectangle")
plt.axis('off')  
plt.show()
```

#### 2.4 Add Text to the Image

```
# Load the image
image = cv2.imread(r"C:\Users\admin\Downloads\me2.jpeg") 

# Convert BGR to RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Add text to the image
text_img = cv2.putText(img_rgb, "Sadhana S", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 10)  

# Display the image
plt.imshow(text_img, cmap='viridis')  
plt.title("Image with Text")
plt.axis('off')  
plt.show()
```

### Step 3: Color Space Conversion

```
# Load the image
image = cv2.imread(r"C:\Users\admin\Downloads\me2.jpeg") 

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Original RGB Image
plt.imshow(image_rgb)
plt.title("Original RGB Image")
plt.axis("off")
plt.show()

# Convert RGB to HSV
image_hsv = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2HSV)

# HSV Image
plt.imshow(image_hsv)
plt.title("HSV Image")
plt.axis("off")
plt.show()

# Convert RGB to GRAY
image_gray = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2GRAY)

# Grayscale Image
plt.imshow(image_gray, cmap='gray')
plt.title("Grayscale Image")
plt.axis("off")
plt.show()

# Convert RGB to YCrCb
image_ycrcb = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2YCrCb)

# YCrCb Image
plt.imshow(image_ycrcb)
plt.title("YCrCb Image")
plt.axis("off")
plt.show()

# Convert HSV back to RGB
image_hsv_to_rgb = cv2.cvtColor(image_hsv, cv2.COLOR_HSV2RGB)

plt.imshow(image_hsv_to_rgb)
plt.title("HSV to RGB Image")
plt.axis("off")
plt.show()

```

### Step 4: Pixel Manipulation

```
# Modify a block of pixels (300x300) to white, starting from (200, 200)
image[200:500, 200:500] = [255, 255, 255]  

# Convert BGR to RGB for displaying with Matplotlib
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Display the modified image
plt.imshow(image_rgb)
plt.title("Image with 300x300 White Block")
plt.axis("off")
plt.show()
```

### Step 5: Image Resizing

```
image = cv2.imread(r"C:\Users\admin\Downloads\me2.jpeg") 
print(image.shape)

# Resize the image to half its size
resized_image = cv2.resize(image, (768 // 2, 600 // 2))  

# Convert BGR to RGB for displaying with Matplotlib
resized_image_rgb = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)

print(resized_image_rgb.shape)

# Display the resized image
plt.imshow(resized_image_rgb)
plt.title("Resized Image (Half Size)")
plt.axis("off")
plt.show()
```

### Step 6: Image Cropping

```
# Load the image
image = cv2.imread(r"C:\Users\admin\Downloads\me2.jpeg")

print(image.shape)

# Crop a 300x300 region starting from (50, 50)
roi = image[50:350, 50:350]  

# Convert BGR to RGB for displaying with Matplotlib
roi_rgb = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)

# Display the cropped region (ROI)
plt.imshow(roi_rgb)
plt.title("Cropped Region of Interest (ROI)")
plt.axis("off")
plt.show()
```

### Step 7: Image Flipping

```
# Load the image
image = cv2.imread(r"C:\Users\admin\Downloads\me2.jpeg")

# Flip the image horizontally (left-right)
flipped_horizontally = cv2.flip(image, 1)
flipped_horizontally_rgb = cv2.cvtColor(flipped_horizontally, cv2.COLOR_BGR2RGB)

# Horizontal flip
plt.imshow(flipped_horizontally_rgb)
plt.title("Flipped Horizontally")
plt.axis("off")
plt.show()

# Flip the image vertically (up-down)
flipped_vertically = cv2.flip(image, 0)
flipped_vertically_rgb = cv2.cvtColor(flipped_vertically, cv2.COLOR_BGR2RGB)

# Vertical flip
plt.imshow(flipped_vertically_rgb)
plt.title("Flipped Vertically")
plt.axis("off")
plt.show()
```

---

## OUTPUT

#The following outputs are obtained:

#1. Original image displayed using OpenCV and Matplotlib.


<img width="888" height="477" alt="image" src="https://github.com/user-attachments/assets/1a0b37dd-f1ae-451c-846a-26781d19e955" />




#2. Image with a line drawn from the top-left to the bottom-right.

<img width="1175" height="527" alt="image" src="https://github.com/user-attachments/assets/78e39e5f-2408-4472-80be-dbb38f18c29f" />



#3. Image with a circle at the center.


<img width="948" height="524" alt="image" src="https://github.com/user-attachments/assets/7d647185-39d6-47ec-9cf5-5983f35eb831" />



#4. Image with a rectangle around its boundary.


<img width="996" height="521" alt="image" src="https://github.com/user-attachments/assets/309216b6-6d00-4a2d-b903-529c9509c44e" />



#5. Image with the text "Sadhana S".


<img width="950" height="476" alt="image" src="https://github.com/user-attachments/assets/2cf4495a-26c1-45a0-a11e-afcc816937c1" />



#6. HSV, grayscale, and YCrCb color space conversions.


<img width="940" height="414" alt="image" src="https://github.com/user-attachments/assets/39f5efb5-e1c9-4fa3-bc8c-81818a42502c" />


<img width="903" height="416" alt="image" src="https://github.com/user-attachments/assets/973e28c9-c199-4d19-aa53-bc64e907b2d8" />


<img width="952" height="430" alt="image" src="https://github.com/user-attachments/assets/be7d68a7-fcde-471f-9625-1f933f507b51" />



#7. Image converted from HSV back to RGB.


<img width="977" height="422" alt="image" src="https://github.com/user-attachments/assets/6cf4e828-7a75-4680-8f1f-ef994557855e" />



#8. Pixel value displayed and a white region added to the image.


<img width="971" height="481" alt="image" src="https://github.com/user-attachments/assets/bd35f1f3-7939-451f-9422-01e53c3a9d57" />



#9. Image resized to half its original dimensions.


<img width="903" height="594" alt="image" src="https://github.com/user-attachments/assets/7a3f0177-84df-4bc5-aac3-334911b70e4d" />



#10. Cropped region of interest displayed.


<img width="815" height="568" alt="image" src="https://github.com/user-attachments/assets/fe39a2f1-cae3-4092-a5a8-5dd361d74814" />



#11. Horizontally flipped image displayed.


<img width="974" height="474" alt="image" src="https://github.com/user-attachments/assets/0e9c5ab4-4dd1-4b6e-b25b-f918e4376400" />



#12. Vertically flipped image displayed.


<img width="956" height="494" alt="image" src="https://github.com/user-attachments/assets/9451e66d-87f7-43b3-87cf-822d973a8888" />



## RESULT

Thus, image handling and pixel transformations were performed using Python, OpenCV, and Matplotlib. The experiment demonstrated image reading, shape drawing, text insertion, color space conversion, pixel manipulation, image resizing, cropping, flipping, and saving.

---
