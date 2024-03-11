# main.py
from PIL import Image, ImageDraw, ImageFont
import os

# Function to create posters
def create_posters(template_folder, image_folder, captions, output_folder):
    # Load templates
    templates = [Image.open(os.path.join(template_folder, template_file)) for template_file in os.listdir(template_folder)]
    
    # Load images
    images = [Image.open(os.path.join(image_folder, image_file)) for image_file in os.listdir(image_folder)]
    
    # Iterate over templates
    for template in templates:
        for image in images:
            for caption in captions:
                # Create a copy of the template
                poster = template.copy()
                
                # Paste image onto template
                poster.paste(image, (x_position, y_position))  # Adjust position based on your template
                
                # Add caption to template
                draw = ImageDraw.Draw(poster)
                font = ImageFont.load_default()
                draw.text((caption_x_position, caption_y_position), caption, fill="black", font=font)  # Adjust position based on your template
                
                # Save poster
                poster.save(os.path.join(output_folder, f"poster_{template_index}_{image_index}_{caption_index}.jpg"))
