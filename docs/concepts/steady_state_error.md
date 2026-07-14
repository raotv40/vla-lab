# Steady-State Error

**Steady-State Error** ($e_{\text{ss}}$) is the persistent difference between the desired setpoint and the actual output of a control system as time approaches infinity ($t \to \infty$).

---

## Causes of Steady-State Error

1. **System Type & Input Class**: According to control loop type analysis, systems of lower "types" (fewer integrators in the open-loop transfer function) fail to track complex inputs (step, ramp, parabolic) without steady-state offset.
2. **Constant Disturbance Forces**: Constant external loads (gravity on a link, friction, or payload masses) oppose joint motion.
3. **P-Controller Limitations**: A proportional-only controller requires a non-zero error $e$ to generate any motor output torque:
   $$u = K_p \cdot e$$
   If an external disturbance torque $T_g$ must be countered, the joint must settle at a position where:
   $$K_p \cdot e_{\text{ss}} = T_g \implies e_{\text{ss}} = \frac{T_g}{K_p}$$
   Therefore, the error cannot be zero.

---

## How to Eliminate Steady-State Error

1. **Integrator Term ($K_i$)**: An integral term sums up the remaining error over time. The accumulator grows, forcing the control command to increase and drive the offset to exactly zero.
2. **Gravity Feedforward**: Adding a model-based torque command equal to the predicted gravity torque:
   $$u = u_{\text{PID}} + T_{\text{gravity\_model}}$$
   This offsets the disturbance directly, allowing the PID controller to only handle trajectory corrections.
