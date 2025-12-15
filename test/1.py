import matplotlib.pyplot as plt  # 导入matplotlib库中的pyplot子库并取名为plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为黑体
plt.rcParams['axes.unicode_minus'] = False   # 解决保存图像是负号'-'显示为方块的问题
# 收集情绪数据
name = input()  # 变量name获取名字输入
mood_score = input()  # 变量mood_score获取心情打分输入
energy_level = input()  # 变量energy_level获取能量值输入
# 转换数据类型，将mood_score和energy_level的数据类型转为浮点型
mood = float(mood_score)  # 变量mood为转换后的mood_score
energy = float(energy_level)  # 变量energy为转换后的energy_level
# 计算综合情绪温度
emotion_temp = (mood + energy) / 2 * 10
# 绘制温度计
plt.figure(figsize=(3, 8))  # 画布尺寸
plt.bar(0, emotion_temp, width=0.1, color='red')  # 柱状图样式
plt.axhline(y=emotion_temp, color='blue', linestyle='--')  # 标记线样式
plt.ylim(0, 100)  # 设置y轴范围0~100
plt.grid(True, axis='y')  # 网格线仅显示y轴网格线
plt.title(f'{name}的情绪温度: {emotion_temp:.1f}°C', fontsize=16)  # 标题样式
plt.axis('off')  # 隐藏全部坐标轴
# 展示神奇效果
plt.savefig('src1/temp/pic.png')  # 图片保存（注意：先保存）
plt.show()  # 显示图片（后显示）
plt.close()