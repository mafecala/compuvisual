import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.metrics import confusion_matrix

# === Cargar datos guardados ===
data = np.load("resultados/metricas_entrenamiento.npz")
train_losses = data["train_losses"]
val_losses = data["val_losses"]
all_preds = data["all_preds"]
all_labels = data["all_labels"]

# === Curvas de pérdida ===
plt.figure(figsize=(8, 5))
plt.plot(train_losses, label="Pérdida Entrenamiento")
plt.plot(val_losses, label="Pérdida Validación")
plt.xlabel("Épocas")
plt.ylabel("Pérdida")
plt.title("Curvas de Pérdida - Entrenamiento vs Validación")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("resultados/loss_curve.png")
plt.show()

# === Matriz de confusión ===
cm = confusion_matrix(all_labels, all_preds)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel("Predicción")
plt.ylabel("Etiqueta Real")
plt.title("Matriz de Confusión")
plt.tight_layout()
plt.savefig("resultados/confusion_matrix.png")
plt.show()

# === Comparación sin vs. con Fine-Tuning ===
acc_simple = data["acc_simple"].item()
acc_finetune = data["acc_finetune"].item()

plt.figure(figsize=(6, 4))
plt.bar(["Sin Fine-Tuning", "Con Fine-Tuning"], [acc_simple, acc_finetune], color=["gray", "green"])
plt.ylim(0, 1)
plt.ylabel("Precisión")
plt.title("Comparación: Sin vs. Con Fine-Tuning")
plt.tight_layout()
plt.savefig("resultados/comparacion_finetuning.png")
plt.show()
