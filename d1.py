#!/usr/bin/env python
# coding: utf-8

# ## EXP.NO:01-Image Handling and Pixel Transformations Using OpenCV
# ## NAME: Sadhana S
# ## Reg.No:212224230234

# In[1]:


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


# In[2]:


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


# In[3]:


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


# In[4]:


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


# In[5]:


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


# In[6]:


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


# In[7]:


# Modify a block of pixels (300x300) to white, starting from (200, 200)
image[200:500, 200:500] = [255, 255, 255]  

# Convert BGR to RGB for displaying with Matplotlib
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Display the modified image
plt.imshow(image_rgb)
plt.title("Image with 300x300 White Block")
plt.axis("off")
plt.show()


# In[8]:


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


# In[9]:


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


# In[10]:


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


# In[ ]:




