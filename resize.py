from PIL import Image

# Open the image
img = Image.open("C:\\Users\\Supriya\\Downloads\\Portfoliowebsite_template\\images\\passportcv.jpg")

# Resize the image
resized_img = img.resize((1000, 1194))

# Save the resized image
resized_img.save("C:\\Users\\Supriya\\Downloads\\Portfoliowebsite_template\\images\\piuimgcv.jpg")
