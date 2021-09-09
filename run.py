#!/usr/bin/env python3
import os 
import requests

def json_upload(texts_folder, image_files, url):
    """ Parses .txt file descriptions into json POST requests """
    for count,txt in enumerate(sorted(os.listdir(texts_folder))):
      if txt.endswith(".txt"):
        txt_path = texts_folder + txt
        with open(txt_path, "r") as f:
                lines = [x.strip() for x in f.readlines()]
                fruit = {}
                fruit["name"] = lines[0]
                e1 = lines[1].split()
                fruit["weight"] = int(e1[0])
                fruit["description"] = lines[2]
                fruit["image_name"] = image_files[count-1] #.txt matches JPEG

                #posts json payload to provided url
                r = requests.post(url, json=fruit)
                #print(r.status_code)
                #print(fruit)

if __name__ == "__main__":
    texts_folder = "" #left empty for testing
    image_files = [x for x in os.listdir("") if x.endswith("jpeg")] #left empty
    url = #'https://httpbin.org/post'

    json_upload(texts_folder, image_files, url)
        
    
    
