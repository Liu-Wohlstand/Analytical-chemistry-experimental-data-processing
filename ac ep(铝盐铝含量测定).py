import numpy as np

m_Al = 0.6019  # 请输入铝盐试样质量，单位以克计，以逗号隔开
v_Zn = np.array([15.51, 15.52, 15.52])  # 请输入所消耗锌溶液体积，单位以毫升计，以逗号隔开
M_Al = 26.981539  # 铝相对分子质量
c_Zn = 0.0200
n_Al = (c_Zn * v_Zn * 0.001)  # 铝元素摩尔量
zlhl_Al = ((c_Zn * (25 - v_Zn) * 0.001) * M_Al / m_Al) * 100 * 10  # 铝元素对于铝试样的质量分数

mean_zlhlAl = np.mean(zlhl_Al)
divation = np.zeros_like(v_Zn)

for i in range(3):
    divation[i] = zlhl_Al[i] - mean_zlhlAl

absdivation = np.abs(divation)

mean_deviation = np.average(absdivation)

Relative_mean_deviation = mean_deviation / mean_zlhlAl * 100
for i in range(3):
    print(f'第{i + 1}组铝的含量为：{zlhl_Al[i]}%')
print(f'铝的平均含量为{mean_zlhlAl}%')

print('相对平均偏差为:{}%'.format(Relative_mean_deviation))
