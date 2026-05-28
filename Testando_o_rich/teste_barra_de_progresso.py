from rich.progress import track
import time

for i in track(range(2000), description="Iniciando..."):
    time.sleep(0.001)
