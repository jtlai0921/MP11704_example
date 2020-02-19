def demo(*para):
    avg = sum(para) / len(para)		#平均值
    g = [i for i in para if i>avg]		#列表推導式
    return (avg,)+tuple(g)

print(demo(1, 2, 3, 4))
