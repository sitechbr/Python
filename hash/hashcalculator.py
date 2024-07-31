import argparse
import os
import hashlib
import csv

def filesInDir(dir):
  files = []
  for dirpath, _, filenames in os.walk(args.dirname):
    for filename in filenames:
      files.append(os.path.join(dirpath, filename))
  return files

def fileHash(file):
  path,filename = os.path.split(file)
  with open(file, "rb") as f:
    md5Hash = hashlib.file_digest(f, "md5").hexdigest()
    sha1Hash = hashlib.file_digest(f, "sha1").hexdigest()
    sha256Hash = hashlib.file_digest(f, "sha256").hexdigest()
  return filename,md5Hash,sha1Hash,sha256Hash

def filesHashDict(files):
  dictlist = []
  for file in files:
    fh = fileHash(file)
    hashDict = {}
    hashDict = dict(filename = fh[0], md5Hash = fh[1], sha1Hash = fh[2], sha256Hash = fh[3])
    print(hashDict)
    dictlist.append(hashDict)
  return dictlist


def dict2CSV(dictlist):
  with open('names.csv', 'w', newline='') as csvfile:
    fieldnames = ["filename","md5Hash","sha1Hash","sha256Hash"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for obj in dictlist:
      writer.writerow(obj)



if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='FileHash Calculation')
  parser.add_argument('-d', dest="dirname", type=str, help='выбор директории для рекурсивного подсчека',default=os.getcwd())
  parser.add_argument('-f', dest="filename", type=str, help='выбор файла', default="")
  args = parser.parse_args()
  if (args.filename == ""):
    files = filesInDir(args.dirname)
    dict2CSV(filesHashDict(files))
  else: 
    print("FileName: %s\n md5: %s\n sha1:  %s\n sha256: %s \n" % fileHash(args.filename))




  
