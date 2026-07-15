# Trapezoidal Velocity Profile

The **Trapezoidal Velocity Profile** is a standard robotic motion planning algorithm that profiles joint speed using three distinct temporal phases: linear acceleration, constant cruising, and linear deceleration.

---

## Profile Phases and Equations

Let start position be $x_0$, goal position be $x_g$, total duration be $t_f$, and acceleration duration be $t_a$. The total distance is $D = x_g - x_0$. Let the deceleration phase be symmetric ($t_d = t_a$).

The peak velocity $v_{\max}$ and acceleration $a$ are related to distance by:
$$D = v_{\max} (t_f - t_a)$$
$$v_{\max} = \frac{D}{t_f - t_a}$$
$$a = \frac{v_{\max}}{t_a}$$

The trajectory equations for position $x(t)$, velocity $v(t)$, and acceleration $a(t)$ are:

### Phase 1: Acceleration ($t \in [0, t_a]$)
$$a(t) = a$$
$$v(t) = a \cdot t$$
$$x(t) = x_0 + \frac{1}{2} a \cdot t^2$$

### Phase 2: Cruise ($t \in [t_a, t_f - t_a]$)
$$a(t) = 0$$
$$v(t) = v_{\max}$$
$$x(t) = x_0 + \frac{1}{2} a \cdot t_a^2 + v_{\max}(t - t_a)$$

### Phase 3: Deceleration ($t \in [t_f - t_a, t_f]$)
$$a(t) = -a$$
$$v(t) = v_{\max} - a(t - (t_f - t_a))$$
$$x(t) = x(t_f - t_a) + v_{\max}(t - (t_f - t_a)) - \frac{1}{2} a(t - (t_f - t_a))^2$$

---

## Discontinuity Limits

While the trapezoidal profile is widely used, it has **discontinuous acceleration transitions**:
- At $t=0, t_a, t_f - t_a, t_f$, the acceleration commands jump instantly.
- The mathematical derivative of acceleration (Jerk $j = \frac{da}{dt}$) is infinite at these transition boundaries.
- This infinite jerk causes minor mechanical vibrations, which can be avoided by transitioning to S-curve profiles for very high-performance systems.
