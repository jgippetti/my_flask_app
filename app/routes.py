from flask import send_file
from app import my_app
import matplotlib
matplotlib.use('Agg')  # Use the Agg backend for rendering plots
import matplotlib.pyplot as plt
import numpy as np
import io

class MathArtGenerator:
    def __init__(self):
        self.fig, self.ax = plt.subplots(figsize=(10, 6))

    def generate_plot(self):
        x = np.linspace(0, 2 * np.pi, 1000)
        y = np.sin(x ** 2)

        self.ax.plot(x, y, label='y = sin(x^2)')
        self.ax.set_title('Math Art')
        self.ax.set_xlabel('x')
        self.ax.set_ylabel('y')
        self.ax.legend()

        img = io.BytesIO()
        self.fig.savefig(img, format='png')
        img.seek(0)
        plt.close(self.fig)
        return img

@my_app.route('/')
def index():
    generator = MathArtGenerator()
    img = generator.generate_plot()
    return send_file(img, mimetype='image/png')