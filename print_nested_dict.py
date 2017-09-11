def print_dict(dictionary, ident = '', braces=2):
    """ Recursively prints nested dictionaries."""

    for key, value in dictionary.iteritems():
        if isinstance(value, dict):
            print '%s%s%s%s' %(ident,braces*'[',key,braces*']') 
            print_dict(value, ident+'  ', braces+1)
        else:
            print ident+'%s = %s' %(key, value)

def find_in_dict(dictionary, search_key):
    """ Recursively finds a key nested dictionaries."""

    for key, value in dictionary.iteritems():
        if (key == search_key):
            print(key)
            print_dict(dictionary[key])
        if isinstance(value, dict):
            find_in_dict(value, search_key)
def myprint(d,depth):
  for k, v in d.iteritems():
    if isinstance(v, dict):
      depth+=4
      print "%s%s" %(depth*' ',k)
      myprint(v,depth)
    else:
      print "%s%s%s%s" %(depth*' ',k,"-->",v)

if __name__ == '__main__':

    example_dict = { 'EMP1': { 'EMP2' : 'norep',
                                'EMP3' : 'norep',
                                'EMP4' : { 'EMP6': 'norep' },
                                'EMP5' : { 'EMP7': { 'EMP9': 'norep',
                                                      'EMP10': 'norep',
                                                      'EMP11': 'norep'},
                                           'EMP8': 'norep'}
                              }
                   }

    print_dict(example_dict)
    print ("###################")
    find_in_dict(example_dict, "EMP5")
    print ("###################")
    myprint(example_dict,1)


