# 历史上的今天

import ybc_data as d
import ybc_ui as u


mouth = u.picker('选择月份',list(range(1,13))) # 选月份
if mouth in [1,3,5,7,8,10,12]:
    day = u.picker('选择日期',list(range(1,32)))
elif mouth == 2:
    day = u.picker('选择日期',list(range(1,30)))
elif mouth in [4,6,9,11]:
    day = u.picker('选择日期',list(range(1,31)))

text = d.history(mouth,day)
lst = text.split('\n')
for i in lst:
    u.message(i)
