




def print_emp_directory(directory,searchkey,ident):
  for key,val in directory.items():
    if searchkey == key:
      if not val[2]:
        print "%s %d %s %s" %("  "*ident,key, val[0],val[1])
        return
      else:
        print "%s %d %s %s" %("  "*ident,key, val[0],val[1])
        print "%s %s" %("  "*ident,"|")
        print "%s %s" %("  "*ident,"-"*ident)
        for sub_key in val[2]:
          print_emp_directory(directory,sub_key,ident+2)    




emp_directory={1:["prakash","CEO",[2,3,4]],2:["babu","CTO",[5,6,7]],3:["gopu","SVP",[8,9]],4:["ramu","SVPI",[10,11]],5:["name5","T5",[]],6:["nam6","T6",[]],7:["name7","T7",[]],8:["name8","T8",[]],9:["name9","T9",[]],10:["name10","T10",[]],11:["name11","T11",[]]}
print_emp_directory(emp_directory,1,2)
