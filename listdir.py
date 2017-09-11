import os                                       

def print_directory_contents(sPath):
    for sChild in os.listdir(sPath):                
        #print(sChild)
        #enter_key = raw_input("Enter to continue....")
        sChildPath = os.path.join(sPath,sChild)
        if os.path.isdir(sChildPath):
            print(sChildPath)
            print_directory_contents(sChildPath)
        #if os.path.isdir(sChildPath):
        #    print_directory_contents(sChildPath)
        #else:
        #    print(sChildPath)

dirname = raw_input("Enter dirname or path to list: ") 
print_directory_contents(dirname)


