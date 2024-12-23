import matplotlib.pyplot as plt
import json

data = json.load(open("result.json", "r"))

print(data.keys())
fig, ax = plt.subplots(1, 2, figsize=(8, 4), layout="tight")
# fig.suptitle('Experiment 1 (mask all image by mask)', fontsize=20)
fig.supxlabel("Количество классов", fontsize=15)

ax[0].scatter(data["num_classes"], data["acc"])
# ax[0].set_xlabel("Количество классов")
ax[0].set_title("Точность", fontsize=20)
ax[0].set_ylim([0, 1.1])

ax[1].scatter(data["num_classes"], data["epochs"])
# ax[1].set_xlabel("Количество классов", fontsize=15)
ax[1].set_title("Эпох затрачено", fontsize=20)
plt.show()
