import time
import sys,os

rootPath = "D:\\ifhu.github.io\\p\\"

title = sys.argv[1]

path_date =  (time.strftime("%Y%m%d\\", time.localtime()))

file_dir = rootPath + path_date  + title 
file_is_exists = os.path.exists(file_dir)

if not file_is_exists:
    os.makedirs(file_dir)
    f = open(file_dir + "\\index.md","w")
    f.write("# " + title)
    f.close
