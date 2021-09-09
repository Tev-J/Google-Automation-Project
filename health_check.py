#!/usr/bin/env python3
import psutil, socket
import emails

def cpu_check():
    """ Sends alert if CPU usage surpasses 80% """
    cpu_usage = psutil.cpu_percent(interval=5, percpu=False)
    if cpu_usage > 80:
        subject = "Error - CPU usage is over 80%"
        message = email.generate_error_report(subject)
        emails.send(message)
        

def disk_check():
    """ Sends alert if disk space is lower than 20%% """
    disk_usage = psutil.disk_usage("/").percent # 
    if disk_usage > 80:
        subject = "Error - Available disk space is less than 20%"
        message = email.generate_error_report(subject)
        emails.send(message)
        

def mem_check():
    """ Sends alert if available memory is less than 500MB """
    mem_available = psutil.virtual_memory().available
    minimum = 500 * 1024 * 1024  # 500MB
    if mem_available < minimum:
        subject = "Error - Available memory is less than 500MB"
        message = email.generate_error_report(subject)
        emails.send(message)
        

def ip_check():
    """ Sends alert if localhost cannot be resolved to 127.0.0.1 """
    ip_address = socket.gethostbyname("localhost")
    if ip_address != "127.0.0.1":
        subject = "Error - localhost cannot be resolved to 127.0.0.1"
        message = email.generate_error_report(subject)
        emails.send(message)
        

   
if __name__ == "__main__":
    cpu_check()
    disk_check()
    mem_check()
    ip_check()
