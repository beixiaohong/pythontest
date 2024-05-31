#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 例2：elif用法
# 格式化日期对象为字符串
formatted_date = date_obj.strftime("%d-%B-%Y")
print(formatted_date)

# 解析字符串为日期对象
parsed_date = datetime.strptime(formatted_date, "%d-%B-%Y")
print(parsed_date)