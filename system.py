# -*- coding:utf-8 -*-

import re


# show system menu
def menu():
    pass


# main function
def main():
    ctrl = True
    while ctrl:
        menu()
        option = input("请选择：")
        option_str = re.sub("[^0-9]", "", option)      # replace all the non-digits to empty, only remains number
        



if __name__ == '__main__':
    main()
