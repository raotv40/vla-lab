# Velocity Profile

A **Velocity Profile** defines how the speed of a robot joint or end-effector changes over the course of a trajectory, ensuring that motion respects physical actuator speed and torque limits.

---

## Velocity Profiling Importance

If a robot only has path coordinates without a velocity profile:
- Intermediate speeds are undefined, forcing the controller to step between positions abruptly.
- At the boundaries (start and end), the instantaneous change in position commands infinite velocity and acceleration.
- In physical systems, this causes extreme torque spikes, joint shaking (jerk), mechanical wear, and tracking failures.

A velocity profile maps geometric paths to smooth, continuous speed variations:

```text
  Velocity Profile Shape:
  
    Vel
     ▲
v_max│     /───────────\
     │    /             \
     │   /               \
     └──/─────────────────\───► Time (t)
       ta               tf-ta
```

---

## Key Velocity Constraints

- **Maximum Velocity ($v_{\max}$)**: Bounded by joint motor voltage limits and safety limits.
- **Maximum Acceleration ($a_{\max}$)**: Bounded by joint motor torque limits (from $F = m \cdot a$ or $\tau = I \cdot \alpha$).
- **Maximum Jerk ($j_{\max}$)**: Bounded by mechanical vibration tolerance.
