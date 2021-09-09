#!/usr/bin/env python3

from datetime import datetime
import os
import reports
import emails

def report_details():
    """ reads .txt files for report details"""
    texts_folder = "" # left empty for testing
    update_post = []

    for file in sorted(os.listdir(texts_folder)):
        if file.endswith(".txt"):
            file_path = texts_folder + file
            with open(file_path, "r") as f: 
                lines = [x.rstrip() for x in f.readlines()]
                update = f"name: {lines[0]}<br/>weight: {lines[1]}<br/><br/>"
                update_post.append(update)

    return update_post
        

if __name__ == "__main__":
    #Generates Report
    date = datetime.now().date().strftime("%B %d, %Y")
    paragraph = "".join(report_details())
    title = "Processed Update on {} ".format(date)
    attachment = #"/Users/tev/Documents/Automation_Project/just_testing.pdf"
    reports.generate_report(attachment, title, paragraph)
    
    #Generates Email
    sender = "" #left empty
    receiver = "" #left empty
    subject = "Upload Completed - Online Fruit Store"
    body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'
    message = emails.generate_email(sender, receiver, subject, body, attachment)
    emails.send(message)


