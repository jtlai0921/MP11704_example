from matplotlib.path import Path
from matplotlib.patches import PathPatch
import matplotlib.pyplot as plt


fig, ax = plt.subplots()

#定義繪圖指令與控制點坐標
#其中MOVETO表示將繪製起點移動到指定坐標
#CURVE4表示使用4個控制點繪製3次貝茲曲線
#CURVE3表示使用3個控制點繪製2次貝茲曲線
#LINETO表示從目前位置繪製直線到指定位置
#CLOSEPOLY表示從目前位置繪製直線到指定位置，並閉合多邊形
path_data = [
    (Path.MOVETO, (1.58, -2.57)),
    (Path.CURVE4, (0.35, -1.1)),
    (Path.CURVE4, (-1.75, 2.0)),
    (Path.CURVE4, (0.375, 2.0)),
    (Path.LINETO, (0.85, 1.15)),
    (Path.CURVE4, (2.2, 3.2)),
    (Path.CURVE4, (3, 0.05)),
    (Path.CURVE4, (2.0, -0.5)),
    (Path.CURVE3, (3.5, -1.8)),
    (Path.CURVE3, (2, -2)),
    (Path.CLOSEPOLY, (1.58, -2.57)),
    ]
codes, verts = zip(*path_data)
path = Path(verts, codes)
#按照指令和坐標進行繪圖
patch = PathPatch(path, facecolor='r', alpha=0.9)
ax.add_patch(patch)

# 繪製控制多邊形和連接點
x, y = zip(*path.vertices)
line, = ax.plot(x, y, 'go-')

#顯示網格
ax.grid()
#設定坐標軸刻度大小一致，可以更真實地顯示圖形
ax.axis('equal')
plt.show()
