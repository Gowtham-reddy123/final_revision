try:
    filename =input("\nEnter the file name : ")
    file=open(filename,'r')
    content=file.read()
    print("\nFile Content : \n  ",content)
    file.close()
except FileNotFoundError:
    print("\nYou are trying to open a file which doesnot exists")
finally:
    print("\nThe file is closed")