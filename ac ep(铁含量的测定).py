import numpy as np

m_Fe = np.array([0.0872,0.0908,0.0896])  # 请输入铁试样质量，单位以克计，以逗号隔开
v_K2Cr2O7 = np.array([18.9,20.39,19.91])  # 请输入所消耗重铬酸钾体积，单位以毫升计，以逗号隔开
m_K2Cr2O7 = 0.74  # 请输入配置重铬酸钾时所用重铬酸钾质量
v_H2O = 0.25  # 请输入配置重铬酸钾溶液时所用水的体积，单位以升计
c_K2Cr2O7 = 0.01001
n_Fe = (c_K2Cr2O7 * v_K2Cr2O7 * 0.001) * 6  # 铁元素摩尔量
zlhl_Fe = ((c_K2Cr2O7 * v_K2Cr2O7 * 0.001) * 55.85 /  m_Fe) * 100 * 6  # 铁元素对于铁试样的质量分数
mean_zlhlFe = np.mean(zlhl_Fe)
divation = np.zeros_like(m_Fe)
print(n_Fe)

for i in range(3):
    divation[i] = zlhl_Fe[i] - mean_zlhlFe

absdivation = np.abs(divation)

mean_deviation = np.average(absdivation)
Relative_mean_deviation = mean_deviation / mean_zlhlFe * 100
for i in range(3):
    print(f'第{i + 1}组铁的含量为：{zlhl_Fe[i]}%')
print(f'铁的平均含量为{mean_zlhlFe}%')
print(f'重铬酸钾的浓度为{c_K2Cr2O7}mol/L')
print('相对平均偏差为:{}%'.format(Relative_mean_deviation))
