"""
str="this is a lot of text. It goes on and on."
justify(str, 18)

--- output ---
this  is  a lot of
text.  It  goes on
and on.


justify(str, 10)

this  is a
lot     of
text.   It
goes    on
and on.

' ' * 5 == '     '
"""
def justify_line(line, columns):
    num_words = len(line.split())
    new_line=None
    count = columns
    for word in line.split()
        if (count > 0) and (num_words > 0)
            if len(new_line) == 1:
                new_line = new_line + word
                count = count - len(word)
                num_words = num_words - 1
            elif len(new_line) == (num_words-1): 
               new_line = new_line + ' '*(coulmns - (len(newline) + len(word))) + word
            else:
                space = columns - (len(new_line) + sum(len(left_over_words)))
                equal_space = space/num_words
                new_line = new_line + (' ' * equal_space) + word
                count = count - len(word)
                num_words = num_words - 1
    return new_line          
                
       
def justify(str, columns):
    str_list = str.split()
    
    ['this', 'is', .....]
    new_str=None
    for word in str_list: //this  is a
        if len(new_str + ' ' + word) < columns:  10< 10
            new_str = new_str + ' ' + word ' This is a'
        elif len(new_str) == columns
           print justify_line(new_str,columns)
        
        
        
