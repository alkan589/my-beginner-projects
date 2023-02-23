##here is passed names
liste=["jon doe","foo","baz"]

def str_conv(str_:str)->str:
    result=""
    for i in range(str_.__len__()):
        c=chr(ord(str_[i])+1)
        result+=c
    return result
    
new_list=list(map(str_conv,liste))
def dict_zip():
    dict={}
    for i in range(len(liste)):
        d={liste[i]:new_list[i]}
        dict.update(d)
    return dict
print(dict_zip())
