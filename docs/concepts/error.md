# Tracking Error in Control Systems

In control theory, **Error** is the primary signal that drives closed-loop feedback systems. It represents the difference between where the system is desired to be (the setpoint) and where it currently is (the measured output).

---

## Mathematical Definition

The tracking error $e(t)$ at time $t$ is calculated as:
$$e(t) = r(t) - y(t)$$

Where:
- **$r(t)$**: The reference input or **setpoint** (desired state).
- **$y(t)$**: The process variable or **measured output** (actual state).

For multi-axis robotic joints or Cartesian coordinates, error is represented as a vector:
$$\mathbf{e}(t) = \mathbf{x}_{\text{target}}(t) - \mathbf{x}_{\text{actual}}(t)$$

---

## Role in the Control Loop

The error signal acts as the feedback interface for the controller:

```text
  [Setpoint r] ---> (+) -----------------> [ Controller ] ---> [ Action u ]
                     ^  | (Error e = r - y)
                     |  v
  [Sensor Output y] -(-)
```

- If $e(t) = 0$, the robot has reached its target, and the feedback controller will not apply restorative forces.
- If $e(t) > 0$ or $e(t) < 0$, the controller applies corrective actions proportional to the error's magnitude and sign to drive the system back toward zero error.
