# --- ARCHIVO AÑADIDO POR MODIFICACIÓN ---
# Archivo: TrainingMonitor.py
# Descripción: Clase para monitorizar parámetros durante el entrenamiento/render.
# --------------------------------------------------

import time

class TrainingMonitor:
    def __init__(self, log_file):
        self.log_file = log_file
        self.start_time = None

    def start(self):
        self.start_time = time.time()

    def log_iteration(self, iteration, psnr, loss, iterations_per_second):
        if self.start_time is None:
            raise ValueError("Start time not initialized. Call start() before logging iterations.")
        
        current_time = time.time()
        elapsed_time = current_time - self.start_time

        with open(self.log_file, 'a') as f:
            f.write(f"Iteration: {iteration} of 200000, PSNR: {psnr:.8f}, Loss: {loss:.8f}, Elapsed Time: {elapsed_time:.3f} seconds, Iterations per second: {iterations_per_second:.5f} it/s\n")
            
    def log_iteration_render(self, elapsed_time):

        with open(self.log_file, 'a') as f:
            f.write(f"Elapsed Time for Rendering an image: {elapsed_time:.3f} seconds/s\n")