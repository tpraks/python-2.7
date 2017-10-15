import re


def find_and_replace_control_chars(line,mydelimiter):
  return re.sub(r'[\x00-\x1F]+', mydelimiter, line)

def generate_delimited_file(in_file,delimiter):
  out_file = open("delimited_file.txt", "w")
  f = open(in_file,"r")
  for line in f:
    new_line=find_and_replace_control_chars(line,delimiter)
    out_file.write(new_line+"\n")

def apps_with_max_rating(delimited_file,delimiter,max_rating):
  out_file = open("results.txt", "w")
  f = open(delimited_file,"r")
  for line in f:
    if not line.startswith("#"):
      if int(line.rsplit(delimiter,2)[1]) <= max_rating:
        out_file.write(line)
  
      

def main():
  print("This script reads  input file name, app max rating level and delimiter")
  print("And generates delimited_file.txt and also spits out results.txt with all app ids of rating 1 to MAX")
  in_file = raw_input("Input File Name \(default: free_application_popularity_per_genre\):")
  max_rating = raw_input("Enter MAX Rating level (default 100) :")
  my_delimiter  = raw_input("Enter Delimiter (default ,(comma) :")
  if in_file == "":
    in_file = "free_application_popularity_per_genre"
  if max_rating == "":
    max_rating = 100
  if my_delimiter == "":
    my_delimiter = ","
  generate_delimited_file(in_file,my_delimiter)
  apps_with_max_rating("delimited_file.txt",my_delimiter,100)
  
if __name__ == '__main__':
  main()
