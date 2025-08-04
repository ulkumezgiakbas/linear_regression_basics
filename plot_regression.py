import matplotlib.pyplot as plt


plt.scatter(X, y, color='blue', label='Gerçek Veri')


x_line = np.linspace(min(X)[0], max(X)[0], 100).reshape(-1, 1)
y_line = model.predict(x_line)
plt.plot(x_line, y_line, color='red', label='Regresyon Doğrusu')


plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear Regression – Ezgi')
plt.legend()
plt.grid(True)


plt.show()

