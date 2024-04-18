def gradient_descent(m_cur, b_cur, points, L):
  m_gradient=0
  b_gradient=0
  n=len(points)
  for i in range(n):
    x = points.iloc[i].vendor
    y = points.iloc[i].score
    m_gradient += -(2/n) * x* (y- (m_cur * x + b_cur))
    b_gradient += -(2/n) * (y - (m_cur * x + b_cur))
  m = m_cur - m_gradient * L
  b = b_cur - b_gradient * L
  return m, b

m=0
b=0
L=0.0001
epochs=500

for i in range(epochs):
  if i%50==0:
    print(f"Epoch: {i}")
  m,b=gradient_descent(m,b,data,L)
print(m,b)


plt.scatter(data.vendor, data.score, color ="green")
plt.plot(list(range(0,20)), [m*x+b for x in range(0,20)], color="red")

plt.show()
