import socket
from ftplib import FTP

def check_ftp_connection():
    f=FTP('p30download.com')
    f.login()
    print(f)

def exception_handles_ftp():
    try:
        f=FTP('p30download.com')
        f.login()
    except socket.gaierror:
        print("error in connecting to p30download.com")
    except Exception as e:
        print(e)
        # print(e.__class__)
check_ftp_connection()
# exception_handles_ftp()
