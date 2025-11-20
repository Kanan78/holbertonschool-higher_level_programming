def search_replace(my_list, search, replace):
    for i,v in enumerate(my_list):
        if v == search:
            new_list.append(replace)
        else:
            new_list.append(v)
    return 
