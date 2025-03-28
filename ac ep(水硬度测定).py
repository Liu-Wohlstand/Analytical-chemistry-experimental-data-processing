import numpy as np

m_Ca = 0.3710  # 请输入碳酸钙质量，单位以“克”计，保留四位小数

V_EDTA = np.array([18.40,18.30,18.30])  # 请输入三次标定消耗EDTA的体积，单位以“毫升”计，以逗号隔开

V_H2O = np.array([100.00, 100.00, 100.00])  # 请输入三次所测定水的体积，单位以“毫升”计，以逗号隔开

V_edta_origin = np.array([0.00, 0.00, 0.00])  # 请输入三次edta使用初体积，单位以“毫升”计，以逗号隔开

V_edta_terminal = np.array([14.10,14.15,14.15])  # 请输入三次edta使用末体积，单位以“毫升”计，以逗号隔开

c_Ca = (m_Ca / 100.09) / 0.25

C_edta = c_Ca * 25 * 0.001 / (V_EDTA * 0.001)

print('CaCO3标准溶液浓度为：{}mol/L'.format(c_Ca))
for i in range(3):
    print('第{}组EDTA浓度为{}mol/L'.format(i + 1, C_edta[i]))
average_C_edta = np.mean(C_edta)
print()
print('EDTA平均浓度为：{}mol/L'.format(average_C_edta))

delta_V_edta = V_edta_terminal - V_edta_origin
# print(delta_V_edta)
M_CaO = 56.077  # 氧化钙相对分子质量
hardness = np.zeros_like(V_H2O)
for i in range(3):
    hardness[i] = (average_C_edta * (delta_V_edta[i]) * M_CaO / 1000) / (V_H2O[i]) * 10 ** 5
# for element in hardness:
# print(hardness)
for i in range(3):
    print('第{}组水的硬度为{}'.format(i + 1, hardness[i]))
print()

average_hardness = np.average(hardness)
print('三组水硬度平均值为:', average_hardness)
print()
divation = np.zeros_like(V_H2O)
for i in range(3):
    divation[i] = hardness[i] - average_hardness

absdivation = np.abs(divation)

mean_deviation = np.average(absdivation)
'''
for element in divation:
    print('divation is={:.2f}'.format(element))
print(divation)
print(absdivation)
print(mean_deviation)
'''
Relative_mean_deviation = mean_deviation / average_hardness * 100
print('相对平均偏差为:{}%'.format(Relative_mean_deviation))
