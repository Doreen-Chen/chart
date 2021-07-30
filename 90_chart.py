# 90. 製作圖表 - (使用第三方套件流程示範)
#   https://matplotlib.org/


# as : import 套件.模組, 將模組直接命名'plt'
import matplotlib.pyplot as plt


### line figure
plt.plot([1, 2, 3, 4])  # 沒有命名plt : matplotlib.pyplot.plot([1, 2, 3, 4])
plt.ylabel('some numbers')  # Y軸標籤
#plt.show()  # 開啟秀圖工具 (python.exe ?)  # 按關閉後才繼續以下程式


### circle figure
# 傳入第1個清單是X軸,第2個是Y軸 ; ro是  line style string (default format string is 'b-', which is a solid blue line)
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')  # ro 可改 r- 測試效果
# 清單[X軸範圍, Y軸範圍]
plt.axis([0, 6, 0, 20])
#plt.show()


### figure 3
import numpy as np
mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 50, density=1, facecolor='g', alpha=0.75)

plt.xlabel('Smarts')  # X軸標示
plt.ylabel('Probability')  # Y軸標示 (機率)
plt.title('Histogram of IQ')  # 標題
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')  # 圖示註解文字
plt.axis([40, 160, 0, 0.03])  # X軸及Y軸範圍
plt.grid(True)  # 顯示格線
#plt.show()
plt.savefig('matplotlib_figure_3.png')  # 不在螢幕顯示,存成檔案


