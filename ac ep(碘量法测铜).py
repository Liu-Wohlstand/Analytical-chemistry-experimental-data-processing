import numpy as np

m_CuSO4 = np.array([0.1593,0.1516,0.1534])  # 硫酸铜质量
v_Na2S203 = np.array([15.85,14.93,15.08])  # 硫代硫酸钠消耗体积
c_Na2S203 = 0.05  # 硫代硫酸钠浓度
M_Cu= 63.546
zlhl_Cu = c_Na2S203 * v_Na2S203 * 0.001 * M_Cu / m_CuSO4 * 100
mean_zlhl_Cu = np.mean(zlhl_Cu)


# -------------------------------------------------以下切勿改动-----------------------------------------------------------
def Relative_mean_deviation(i, mean):
    divation = np.zeros_like(i)
    for j in range(3):
        divation[j] = i[j] - mean

    absdivation = np.abs(divation)

    mean_deviation = np.average(absdivation)
    Relative_mean_deviation = mean_deviation / mean * 100
    return Relative_mean_deviation


Relative_mean_deviation = Relative_mean_deviation(zlhl_Cu, mean_zlhl_Cu)
for i in range(3):
    print(f'第{i+1}组硫酸铜铜含量为：{zlhl_Cu[i]}%')
print(f'平均值为：{mean_zlhl_Cu}%')
print(f'相对平均偏差为：{Relative_mean_deviation}%')
