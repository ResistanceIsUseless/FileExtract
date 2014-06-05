import glob,os,zipfile,shutil,rarfile

dir = "/home/action/files"
dest = "/tmp"
#dir = "C:\\Users\\user\\Downloads\\"
#extractiondir = "C:\\Users\\user\\temp\\moved"

rarfiles = glob.iglob(dir + "*.rar")

for rfn in rarfiles:
    source = os.path.abspath(os.path.realpath(rfn))
    print("Extracting File", source)
    z = rarfile.RarFile(source)
    z.extractall()
    currentdir = os.getcwd()
    glob.glob(currentdir + ".r??")
    print("Cleaning up..")
    shutil.move(source,dest)

#except StopIteration:python
    #print("No more files found")

else:
    print("No Files to extract")
