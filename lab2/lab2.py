import matplotlib.pyplot as plt

with open('DS4.txt', 'r') as file:
    data = [tuple(map(int, line.strip().split())) for line in file]

fig, ax = plt.subplots(figsize=(960/80, 540/80))
x, y = zip(*data)
ax.scatter(y, x)
ax.axis('off')
fig.savefig('resultDS4.png')
plt.show()
