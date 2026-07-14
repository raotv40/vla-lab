# Overshoot

**Overshoot** refers to the maximum peak value by which a system's output variable exceeds the desired target setpoint during its transient response phase.

---

## Mathematical Representation

Overshoot is typically expressed as a percentage of the step input magnitude:
$$\text{Overshoot (\%)} = \frac{y_{\max} - r}{r} \times 100\%$$

Where:
- $y_{\max}$ is the peak value of the output.
- $r$ is the target step setpoint.

---

## Causes of Overshoot in Robot Control

1. **High Proportional Gain ($Kp$)**: A large $K_p$ behaves like a stiff spring. It accelerates the arm rapidly toward the setpoint. By the time the arm reaches the setpoint, its momentum (inertia) carries it forward past the setpoint.
2. **Excessive Integral Gain ($Ki$)**: The integral term accumulates errors from the initial rise phase. When the system crosses the setpoint, this positive accumulated history continues to push the arm forward, causing overshoot.
3. **Underdamping**: A lack of friction or derivative damping ($K_d$) to slow the arm down as it approaches the setpoint.

---

## Mitigation Strategies

1. **Derivative Gain ($Kd$)**: Acts as a predictive brake by opposing velocity, adding damping to the control loop.
2. **Set Point Ramp Profiling**: Instead of commanding a step change ($r = 1.0\,\text{rad}$ instantly), feed a smooth trajectory profile (e.g., trapezoidal velocity profile) so the target changes slowly.
3. **Integral Clamping**: Clamp the integral term to small values to prevent windup.
