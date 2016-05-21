import os

for dirpath, dirnames, filenames in os.walk("~/a-lv-notes"):
  #whatever you want to do with these folders
  if "/data/modules/" in dirpath:
    print(dirpath, dirnames, filenames)