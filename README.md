# LSMRN-Controller

This repository contains the full implementation and experimental framework for:

Title: Real-Time Adaptive Control of Agricultural Robots for Nonlinear Crop and Soil Systems Using Recurrent Lyapunov Neural Networks

Description

This project implements a Lyapunov-Stabilized Modular Recurrent Neural Network (LSMRN) for real-time adaptive control of agricultural ground vehicles operating in nonlinear crop-soil systems.

Components

- Python simulation environment for LSMRN and LNT comparison
- C++ embedded implementation for STM32/ESP32 with CMSIS-DSP
- Plotting utilities for generating RMSE, latency, memory, and control signal graphs
- Scripts to evaluate robustness under disturbances (sensor noise, delay, etc.)

Requirements

- Python 3.10+
- NumPy, SciPy, Matplotlib, PyTorch
- CMake / GCC for embedded builds (optional)

Repository Contents

- `/python_simulation`: LSMRN and LNT controller logic in Python
- `/embedded_c`: Optimized C++ code for microcontrollers
- `/docs`: Diagrams and supplementary materials

License

This project is licensed under the MIT License.

Citation

If you use this code, please cite the corresponding paper:

> Real-Time Adaptive Control of Agricultural Robots for Nonlinear Crop and Soil Systems Using Recurrent Lyapunov Neural Networks, 2025.
