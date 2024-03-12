from PIL import Image, ImageDraw, ImageFont
import os
import random
script_dir = os.path.dirname(os.path.abspath(__file__))
template_folder = os.path.join(script_dir, "templates")
image_folder = os.path.join(script_dir, "images")
captions = ["Live music", "mysic is life", "fell the beat","Protect your passion for music with our tailored insurance plans, ensuring your instruments and equipment are always in tune with your needs."]  # List of captions
output_folder =os.path.join(script_dir, "outputfolder")
text_folder =os.path.join(script_dir, "textimage")
font_path = os.path.join(script_dir, "fonts")
#create_posters(template_folder, image_folder, captions, output_folder)
def convert_to_oval(source_image):
    # Open the source image
    img = source_image
    img = img.convert("RGBA")

    # Create a mask in the shape of an oval
    mask = Image.new("L", img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, img.width, img.height), fill=255)

    # Apply the mask to the source image
    oval_image = Image.composite(img, Image.new("RGBA", img.size, (255, 255, 255, 0)), mask)

    return oval_image
def create_fancy_text_image(text,text1, font_path1, font_size, output_path):
    # Load the font
    font_files = [f for f in os.listdir(font_path1) if f.endswith('.ttf')]

    # Select a random font file
    selected_font_file = random.choice(font_files)
    font_path = os.path.join(font_path1, selected_font_file)
    print(font_path)
    font = ImageFont.truetype(font_path, font_size)

    # Calculate text size
    draw = ImageDraw.Draw(Image.new('RGBA', (1, 1), (255, 255, 255, 0)))

    # Calculate text size
    ascent, descent = font.getmetrics()
    r = font.getmetrics()
    print(r)

    text_width = font.getmask(text1).getbbox()[2]
    text_height = font.getmask(text1).getbbox()[3] + descent+ ascent
    # print(font.font.getsize(text))
    # # text_width=0
    # # text_height=0
    # # for c in text:
    # #     text_width += font.getsize(c)[0]
    # # text_height = font.getsize(c)[1]
    # (text_width, text_height) = draw.textsize(text, font=font)
    #text_width, text_height = font.getsize(text)[0],font.getsize(text)[1]

    # Resize the image based on text size
    image = Image.new('RGBA', (text_width, text_height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)

    # Draw the text on the image
    draw.text((0, 0), text1, fill='white', font=font)

    # Save the image
    d=os.path.join(text_folder, f"{text}.png")
    image.save(d)
    return(d)
# Function to create posters
def create_posters(template_folder, image_folder, captions, output_folder):
    # Define positions for image and text insertion based on templates
    template_positions = {
        'template1.jpg': {'image': (5, 265), 'text': (344, 38),'imgdim':(577,376),'textdim':(245,212),'textlen':20},
        'template2.jpg': {'image': (200, 200), 'text': (100, 100),'imgdim':(239,207),'textdim':(239,207)}
        # Add more templates with their respective positions
    }
    
    # Load templates
    templates = [Image.open(os.path.join(template_folder, template_file)) for template_file in os.listdir(template_folder)]
    
    # Load images
    images = [Image.open(os.path.join(image_folder, image_file)) for image_file in os.listdir(image_folder)]
    
    # Iterate over templates
    for template in templates:
        template_filename = os.path.basename(template.filename)
        print(template_filename)
        template_info = template_positions.get(template_filename, {'image': (0, 0), 'text': (0, 0)})  # Default positions if template not found
        
        image_position = template_info['image']
        text_position = template_info['text']
        img_dim=template_info['imgdim']
        text_dim=template_info['textdim']
        text_len=template_info['textlen']
        
        for image in images:
            for caption in captions:
                
                if len(caption)<=text_len:
                    caption1=caption
                    textsize=80                    
                    (textimagelink)=create_fancy_text_image(caption,caption1,font_path, textsize, text_folder)
                    textimage=Image.open(textimagelink)
                    oval_image = convert_to_oval(image)
                    image1=oval_image.resize(img_dim)
                    
                    paste_mask1 = image1.split()[3]
                    
                    # Create a copy of the template
                    poster = template.copy()
                    
                    # Paste image onto template
                    poster.paste(image1, image_position,mask=paste_mask1)
                    
                    textimage=textimage.resize(text_dim)
                    paste_mask = textimage.split()[3]
                    poster.paste(textimage, text_position,mask=paste_mask)
                    # Add caption to template
                    # draw = ImageDraw.Draw(poster)
                    # font = ImageFont.load_default()
                    # draw.text(text_position, caption, fill="black", font=font)
                    c=os.path.join(output_folder, f"poster_{template_filename}_{os.path.basename(image.filename)}_{caption}.jpg")
                    # print(image.filename)
                    print(c)
                    # Save poster
                    poster.save(c)


create_posters(template_folder, image_folder, captions, output_folder)