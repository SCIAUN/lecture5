import sys
import zipfile
def extractFile(zfile,password):
    password=password.encode()
    try:
        zfile.extractall(pwd=password)
        return password
    except:
        return
def getPasswords():
    f=open('passwords','r')
    passwords=f.read()
    passwords=passwords.split('\n')
    return passwords
def main():
    zfile=zipfile.ZipFile('bash_scripting.zip')
    passwords=getPasswords()
    for pwd in passwords:
        guess=extractFile(zfile,pwd)
        if guess:
            print("password of the file is : {0}".format(guess))
            sys.exit(0)

main()