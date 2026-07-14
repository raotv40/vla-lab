# Week 2: Robotic Control Frameworks

This directory covers **Robotic Controllers**, focusing on classical feedback loops, Proportional-Integral-Derivative (PID) algorithms, and physical step-response characteristics.

---

## 📂 Lab Directory

| Lab Script | Controller Type | Description |
| :--- | :--- | :--- |
| [lab22_p_controller.py](file:///C:/Users/Vishrao/vla-lab/vla-lab/week02/lab22_p_controller.py) | Proportional (P) | Simulates a single joint under P feedback. Demonstrates rise time, overshoot, and steady-state error under gravity. |
| [lab23_pi_controller.py](file:///C:/Users/Vishrao/vla-lab/vla-lab/week02/lab23_pi_controller.py) | Proportional-Integral (PI) | Introduces integral accumulation to cancel steady-state gravity offset. Demonstrates integral windup and phase lag. |
| [lab24_pid_controller.py](file:///C:/Users/Vishrao/vla-lab/vla-lab/week02/lab24_pid_controller.py) | Proportional-Integral-Derivative (PID) | Implements full PID feedback control. Demonstrates how derivative braking dampens oscillations and speeds up settling. |

---

## Running the Labs

Ensure you have activated your virtual environment:
```powershell
# Windows PowerShell
.venv\Scripts\Activate.ps1
```

Run each lab script from the repository root:
```bash
python week02/lab22_p_controller.py
python week02/lab23_pi_controller.py
python week02/lab24_pid_controller.py
```
Each script will output text results to the console and save step-response plots to the `assets/day10/` directory.
