#!/usr/bin/env python3
from PIL import Image
import os, sys

def process_images(folder):
    """Resize, reformat, and replaces images in the provided image folder"""
    for f in sorted(os.listdir(folder)):
        if f.endswith(".tiff"):
            infile = os.path.join(folder,f) 
            im = Image.open(infile)    
            im_a = im.convert('RGB')
            im_b = im_a.resize((600,400))
            f_path, f_ext = os.path.splitext(infile) 
            outfile = f"{f_path}.jpeg"
            os.rename(infile, outfile)
            im_b.save(outfile, "JPEG")
       
if __name__ == "__main__":    
    images_folder = "" #left empty
    
    try:
        process_images(images_folder)   
    except FileNotFoundError:
        print("ERROR: Enter complete path of the images.")




