import re


def find_and_replace_control_chars(line,mydelimiter):
  return re.sub(r'[\x00-\x1F]+', mydelimiter, line)

def generate_delimited_appdetail_file(in_file,my_delimiter,my_date):
  out_file = open("appdetail_delimited_file.txt", "w")
  f = open(in_file,"r")
  for line in f:
    if ( not line.startswith("#") ) and (line.startswith(my_date)):
      new_line=find_and_replace_control_chars(line,my_delimiter)
      out_file.write(new_line+"\n")
  out_file.close()
  in_file.close()


def generate_delimited_file(in_file,delimiter):
  out_file = open("delimited_file.txt", "w")
  f = open(in_file,"r")
  for line in f:
    new_line=find_and_replace_control_chars(line,delimiter)
    out_file.write(new_line+"\n")
  out_file.close()
  in_file.close()

def apps_with_max_rating(delimited_file,delimiter,max_rating):
  out_file = open("results.txt", "w")
  f = open(delimited_file,"r")
  for line in f:
    if not line.startswith("#"):
      if int(line.rsplit(delimiter,2)[1]) <= max_rating:
        out_file.write(line)
  out_file.close()
  delimited_file.close()

def retrieve_app_name(app_ids_file):
  out_file = open("app_names.list", "r")
  f = open(app_ids_file,"r")
  for line in f:
    if not line.startswith("#"):
      if int(line.rsplit(delimiter,2)[1]) <= max_rating:
        out_file.write(line)
  app_ids_file.close()
  out_file.close()
  
def merge_appname_and_popularity(app_info,popularity_info,merge_file):
  app_info_file = open(app_info, "r")  
  popularity_info_file = open(popularity_info, "r")  
  merged_filehandle = open(merge_file, "w")
  tmp_filehandle = open("tmp_file", "w")
  my_dictionary = {}
  delimiter = "#"

  # Create a dictionary of app_id and app_name

  for line in app_info_file:
    app_name = line.rsplit(delimiter,3)[1]
    app_id = line.rsplit(delimiter,5)[1]
    if not app_id in my_dictionary:
      my_dictionary[app_id] = app_name
  for k, v in my_dictionary.items():
    tmp_filehandle.write(k + " -- " + v + "\n")

  for line in popularity_info_file:
    app_id = line.rsplit(delimiter,3)[1]
    #if app_id in my_dictionary.keys():
    if app_id in my_dictionary:
      updated_line=line.rstrip()+my_dictionary[app_id]
      merged_filehandle.write(updated_line + "\n")
    else:
      print("App id : %s not found" % app_id) 
  app_info_file.close()      
  popularity_info_file.close()      
  merged_filehandle.close()      
  tmp_filehandle.close()

def main():
  print("This script reads  input file name, app max rating level and delimiter")
  print("And generates delimited_file.txt and also spits out results.txt with all app ids of rating 1 to MAX")
  in_file = raw_input("Input File Name \n ( Enter 1 or 2 or 3) \n (default: 1 - free_application_popularity_per_genre): \n ( 2 - application_detail ): \n ( 3 - Merge files ): \n ")
  max_rating = raw_input("Enter MAX Rating level (default 100) :")
  my_delimiter  = raw_input("Enter Delimiter (default ,(comma) :")
  my_date = "1506502800513"
  if (in_file == "") or (in_file == "1") :
    in_file = "free_application_popularity_per_genre"
  elif (in_file == 2): 
    in_file = "application_detail"
  else: 
    in_file = "merged_file.txt"
  if max_rating == "":
    max_rating = 100
  if my_delimiter == "":
    my_delimiter = "#"
  if ( in_file == "application_detail" ):
    generate_delimited_appdetail_file(in_file,my_delimiter,my_date)
  elif ( in_file == "merged_file.txt" ):
    app_info = "appdetail_delimited_file.txt"
    popularity_info = "results.txt"
    merge_file = in_file
    merge_appname_and_popularity(app_info,popularity_info,merge_file)
  else:
    generate_delimited_file(in_file,my_delimiter)
    apps_with_max_rating("delimited_file.txt",my_delimiter,100)
    retrieve_app_name(results.txt)
  
  
if __name__ == '__main__':
  main()
