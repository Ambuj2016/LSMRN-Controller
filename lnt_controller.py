# lnt_controller.py
import numpy as np

class LNTController:
    def __init__(self):
        self.kp = 0.5
        self.ki = 0.1
        self.integral = 0

    def compute_control(self, e):
        self.integral += e
        return self.kp * e + self.ki * self.integral
