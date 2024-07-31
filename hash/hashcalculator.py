import argparse
import os
import hashlib
import csv

def list_dir(dir):
  files = []
  for dirpath, _, filenames in os.walk(args.dirname):
    for filename in filenames:
      files.append(os.path.join(dirpath, filename))
  return files

def file_hash(file):
  path,filename = os.path.split(file)
  with open(file, "rb") as f:
    md5_hash = hashlib.file_digest(f, "md5").hexdigest()
    sha1_hash = hashlib.file_digest(f, "sha1").hexdigest()
    sha256_hash = hashlib.file_digest(f, "sha256").hexdigest()
  return {"filename": filename, "md5": md5_hash, "sha1": sha1_hash, "sha256": sha256_hash}

def get_hash_of_files(files):
  dictlist = []
  for file in files:
    hash_dict = file_hash(file)
    dictlist.append(hash_dict)
  return dictlist


def dict_2_csv(dictlist,filename):
  with open(filename, 'w', newline='') as csvfile:
    fieldnames = ["filename","md5","sha1","sha256"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for obj in dictlist:
      writer.writerow(obj)



if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='FileHash Calculation')
  parser.add_argument('-d', dest="dirname", type=str, help='выбор директории для рекурсивного подсчета',default=os.getcwd())
  parser.add_argument('-o', dest="outputfile", type=str, help='файл с результами в формате csv',default="hashes.csv")
  parser.add_argument('-f', dest="filename", type=str, help='выбор файла', default="")
  args = parser.parse_args()
  if (args.filename == ""):
    files = list_dir(args.dirname)
    dict_2_csv(get_hash_of_files(files),args.outputfile)
  else: 
    print("FileName: %s\n md5: %s\n sha1:  %s\n sha256: %s \n" % file_hash(args.filename))
