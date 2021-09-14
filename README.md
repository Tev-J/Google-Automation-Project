
# Google's Automation Course Project 

#### Problem Statement:
   
I work for an online fruits store, and I need to develop a system that will update the catalog information with data provided by my suppliers. The suppliers sent the data as large images with an associated description of the products in two files (.TIF for the image and .txt for the description). The images need to be converted to smaller jpeg images and the text needs to be turned into an HTML file that shows the image and the product description. The contents of the HTML file need to be uploaded to a web service that is already running using Django. I also need to gather the name and weight of all fruits from the .txt files and use a Python request to upload it to my Django server.

#### This project includes scripts to:

- [Edit image specifications using Pillow](changeImage.py) 
- [Upload edited images to webserver catalogue using POST requests](supplier_image_upload.py)
- [Process image descriptions to accompany respective image files in the catalogue.](run.py)
- [Notify the supplier, via email, with a PDF report that indicates the total weight of fruit (in lbs) that were uploaded.](report_email.py) 
- [In parallel of the automation running, check the health of the system and send an email if something goes wrong.](health_check.py) 



