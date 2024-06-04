import matplotlib.pyplot as plt


def save_graph(path, x1, y1, x2, y2):
	plt.plot(x1, y1, label='math_log', linewidth=5, color="b")
	plt.plot(x2, y2, label='taylor_log', linewidth=2, color="r")
	plt.axis('equal')
	plt.legend()
	plt.grid()
	plt.savefig(path)
	plt.clf()