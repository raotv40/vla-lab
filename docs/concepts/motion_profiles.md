# Motion Profiles

**Motion Profiles** are specific velocity profiles used in robotics to interpolate position trajectories smoothly while matching mechanical actuator characteristics.

---

## Common Motion Profile Types

### 1. Linear (Constant Velocity) Profile
- **Characteristics**: Constant velocity throughout the motion, zero velocity before and after.
- **Waveforms**: Position is a linear ramp; velocity is a step function; acceleration consists of infinite impulses at start and end.
- **Drawbacks**: Infinite acceleration causes mechanical shock (jerk) and motor driver trips.

### 2. Trapezoidal Velocity Profile
- **Characteristics**: Divides motion into three phases: linear acceleration, constant cruising speed, and linear deceleration.
- **Waveforms**: Position rises quadratically, then linearly, then quadratically; velocity is trapezoidal; acceleration is a step function.
- **Drawbacks**: Discontinuous acceleration at transition boundaries causes minor vibrations (infinite jerk at phase shifts).

### 3. S-Curve (7-Segment) Profile
- **Characteristics**: Smooths acceleration transitions using linear acceleration ramps (trapezoidal acceleration).
- **Waveforms**: Position rises cubically; velocity is an S-curve; acceleration is trapezoidal; jerk is a step function (finite jerk).
- **Benefits**: Zero acceleration jumps, resulting in extremely smooth motion and minimal vibration, making it standard for high-speed CNC machines.
