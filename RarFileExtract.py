import glob,os,zipfile,shutil,rarfile

dir = "/volume1/video/Movies/*/*/*"
dest = "/volume1/video/extracted/"
#dir = "C:\\Users\\user\\Downloads\\"
#extractiondir = "C:\\Users\\user\\temp\\moved"

rarfiles = glob.iglob(dir + "*.rar")

for rfn in rarfiles:
    path_with_file = os.path.abspath(os.path.realpath(rfn))
    print("Extracting File", path_with_file)
    rar = rarfile.RarFile(path_with_file)
    cwd = os.path.dirname(path_with_file)
    rar.extractall(cwd)
    print("Cleaning up..")
    #all_rars = glob.glob(cwd + "*.r??")
    shutil.move(cwd,dest)

#except StopIteration:python
    #print("No more files found")

else:
    print("No Files to extract")

