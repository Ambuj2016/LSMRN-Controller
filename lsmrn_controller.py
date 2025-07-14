# lsmrn_controller.py
import numpy as np

class LSMRNController:
    def __init__(self, input_size=4, hidden_size=6, alpha_c=0.001, beta_c=0.9):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.alpha_c = alpha_c
        self.beta_c = beta_c
        self.w1 = np.random.randn(hidden_size, input_size)
        self.w2 = np.random.randn(1, hidden_size)

    def activation(self, x):
        return np.tanh(x)

    def inverse_activation(self, y):
        return np.arctanh(np.clip(y, -0.999, 0.999))

    def update_weights(self, ec, uc_prev, xc):
        delta = np.sqrt(self.beta_c * (ec + uc_prev))
        for j in range(self.hidden_size):
            Sj = np.dot(self.w1[j], xc)
            self.w2[0, j] = delta / (Sj + 1e-4)
            self.w1[j] = (delta / (self.w2[0, j] + 1e-4)) / (xc + 1e-4)

    def compute_control(self, xc):
        phi = self.activation(np.dot(self.w1, xc))
        uc = np.dot(self.w2, phi)
        return uc.item()
