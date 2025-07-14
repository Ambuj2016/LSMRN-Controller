# lsmrn_controller.py
import numpy as np

class LSMRNController:
    def __init__(self, input_size=4, hidden_size=6, alpha_c=0.001, beta_c=0.9):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.alpha_c = alpha_c
        self.beta_c = beta_c
        self.xc = np.zeros(input_size)
        self.w1 = np.random.randn(hidden_size, input_size)
        self.w2 = np.random.randn(1, hidden_size)

    def activation(self, x):
        return np.tanh(x)

    def inverse_activation(self, y):
        return np.arctanh(np.clip(y, -0.999, 0.999))  # Safe inverse

    def sat(self, x):
        return np.clip(x, -0.999, 0.999)

    def compute_control(self, xc):
        phi = self.activation(self.w1 @ xc)
        return float(self.w2 @ phi)

    def update_weights(self, ec_prev, uc_prev, xc):
        delta = np.sqrt(self.beta_c * (ec_prev + uc_prev))
        lambda1 = 1e-4
        lambda2 = 1e-4
        lambda3 = 1e-4

        for j in range(self.hidden_size):
            Sj = np.dot(self.w1[j], xc)
            self.w2[0, j] = delta / (Sj + lambda1)
            numerator = self.sat(delta / (self.w2[0, j] + lambda3))
            denominator = xc + lambda2
            self.w1[j] = numerator / denominator
