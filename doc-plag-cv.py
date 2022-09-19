import cv2

original = cv2.imread("/Users/rahul.madan/Desktop/image2.png")
duplicate = cv2.imread("/Users/rahul.madan/Desktop/image1.jpeg")

# 1) Check if 2 images are equals
if original.shape == duplicate.shape:
    print("The images have same size and channels")
else:
    print("not same")

print(original.shape)