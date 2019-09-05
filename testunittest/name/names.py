# -*- coding: utf-8 -*-
# Author  : 李俊阳
# @Time    : 2019/9/3 21:18

from name.name_function import get_formatted_name

print("enter 'q'at any time to quit")
while 1 == 1:
    first = input("\n请输入第一个名字：")
    if first == 'q':
        break
    last = input("\n请输入第二个名字:")
    if first == 'q':
        break
    formatted_name = get_formatted_name(first, last)
    print('\t全名叫叫做'+formatted_name)
