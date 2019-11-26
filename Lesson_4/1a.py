'''

20191123 Sikorskiy Yuriy
cs.yury.v@pm.me

'''


import json
import matplotlib.pyplot as plt

with open("res_file.json", "r") as fl:
    list_content = json.load(fl)

print(list_content)
x_keys = list(list_content['lg1'].keys())

x_keys_int = sorted(map(int, x_keys))
y_lg1_func_call = []
y_lg2_func_call = []
y_lg3_func_call = []
for i in x_keys_int:
    y_lg1_func_call.append(list_content['lg1'][str(i)]['func_call'])
    y_lg2_func_call.append(list_content['lg2'][str(i)]['in_time'])
    y_lg3_func_call.append(list_content['lg3'][str(i)]['in_time'])

fig_lg1 = plt.figure(figsize=plt.figaspect(0.75))
ax_lg1 = fig_lg1.add_subplot(221)

ax_lg1.plot(x_keys_int, y_lg1_func_call, color='lightblue', linewidth=3)
ax_lg1.scatter(x_keys_int, y_lg1_func_call, color='darkgreen', marker='^')

ax_lg2 = fig_lg1.add_subplot(222)

ax_lg2.plot(x_keys_int, y_lg2_func_call, color='lightcoral', linewidth=3)
ax_lg2.scatter(x_keys_int, y_lg2_func_call, color='darkblue', marker='^')

ax_lg3 = fig_lg1.add_subplot(223)
ax_lg3.plot(x_keys_int, y_lg3_func_call, color='lightblue', linewidth=3)
ax_lg3.scatter(x_keys_int, y_lg3_func_call, color='darkgreen', marker='*')

plt.savefig('lg123.png')
plt.show()

# x = map(list_content['lg1'].keys()
