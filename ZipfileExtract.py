import glob,os,zipfile,shutil

dir = "/home/action/"
dest = "/tmp"
#dir = "C:\\Users\\user\\Downloads\\"
#extractiondir = "C:\\Users\\user\\temp\\moved"

zipfiles = glob.iglob(dir + "*.zip")

for zfn in zipfiles:
    source = os.path.abspath(os.path.realpath(zfn))
    print("Extracting File", source)
    z = zipfile.ZipFile(source)
    z.extractall(dest)
    print("Cleaning up..")
    shutil.move(source,dest)

#except StopIteration:
    #print("No more files found")

else:
    print("No Files to extract")
