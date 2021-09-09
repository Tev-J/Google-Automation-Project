#!/usr/bin/env python3
import requests
import os

def images_upload(source_folder, url):
    """uploads JPEG images from provided directory to website"""
    for x in sorted(os.listdir(source_folder)): 
        if x.endswith("jpeg"):   
            path = source_folder + x
            image = {'file': open(path,'rb')}
            r = requests.post(url, files=image)
            # print(r.status_code)
            
        

if __name__ == "__main__":
    url = # "https://httpbin.org/post" to test
    folder = "" # left empty to test
    images_upload(folder, url)