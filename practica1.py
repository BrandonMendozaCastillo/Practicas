import os
import random
import subprocess
from datetime import datetime, timedelta

# --- CONFIGURACIÓN ---
inicio = input("📅 Ingresa la fecha de inicio (YYYY-MM-DD): ")
fin = input("📅 Ingresa la fecha final (YYYY-MM-DD): ")

fecha_inicio = datetime.strptime(inicio, "%Y-%m-%d")
fecha_fin = datetime.strptime(fin, "%Y-%m-%d")

# Número de commits por día
min_commits = 3
max_commits = 4

fecha_actual = fecha_inicio

while fecha_actual <= fecha_fin:
    num_commits = random.randint(min_commits, max_commits)
    for i in range(num_commits):
        with open("actividad.txt", "a", encoding="utf-8") as f:
            f.write(f"Commit del {fecha_actual.strftime('%Y-%m-%d %H:%M:%S')} #{i+1}\n")

        subprocess.run(["git", "add", "actividad.txt"])
        subprocess.run([
            "git", "commit", "-m", f"Commit automático {fecha_actual.strftime('%Y-%m-%d')} #{i+1}",
            "--date", fecha_actual.strftime("%Y-%m-%d %H:%M:%S")
        ])
    fecha_actual += timedelta(days=1)

print("🚀 Subiendo todos los commits al repositorio remoto...")
subprocess.run(["git", "push", "origin", "main"])

print("✅ Commits generados y subidos con éxito.")
