from PIL import Image

# Open the two input images
image1 = Image.open("/home/kalin/Desktop/Dics/diplom_masters.jpg")
image2 = Image.open("/home/kalin/Desktop/Dics/diplom_masters_2.jpg")

# Get the dimensions of the first image
width1, height1 = image1.size

# Get the dimensions of the second image
width2, height2 = image2.size

# Create a new blank image with the combined width and maximum height
merged_width = width1 + width2
merged_height = max(height1, height2)
merged_image = Image.new("RGB", (merged_width, merged_height))

# Paste the first image on the left side of the merged image
merged_image.paste(image1, (0, 0))

# Paste the second image on the right side of the merged image
merged_image.paste(image2, (width1, 0))

# Save the merged image
merged_image.save("merged_diplom.jpg")
