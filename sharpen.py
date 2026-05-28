from PIL import Image, ImageEnhance
import os

img_path = r"d:\Check\mhuy\tot-nghiep.png"
if os.path.exists(img_path):
    img = Image.open(img_path)
    # Convert to RGB if needed
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    # 1. Enhance Sharpness (2.0 = twice as sharp)
    enhancer_sharp = ImageEnhance.Sharpness(img)
    img = enhancer_sharp.enhance(2.0)
    
    # 2. Enhance Contrast (1.1 = 10% more contrast)
    enhancer_contrast = ImageEnhance.Contrast(img)
    img = enhancer_contrast.enhance(1.15)
    
    # 3. Enhance Color/Saturation (1.1)
    enhancer_color = ImageEnhance.Color(img)
    img = enhancer_color.enhance(1.1)
    
    # Save it back (overwrite or save as new)
    img.save(r"d:\Check\mhuy\tot-nghiep.png", quality=95)
    print("Sharpened and enhanced image saved successfully.")
else:
    print("Image not found.")
