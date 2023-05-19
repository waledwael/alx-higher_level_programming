#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def e_r(elm):
        return (elm if elm != search else replace)
    return list(map(e_r, my_list))
