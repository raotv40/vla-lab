# System Architecture

This page details the technical architecture of the **VLA Learning Lab** workspace, illustrating how python code, the Gymnasium API wrapper, and the MuJoCo physics engine interface with each other.

---

## Technical Stack

The lab setup is composed of three primary layers:
1. **Core Physics Engine (MuJoCo)**: Performs numerical integration of multi-body dynamics, resolving gravity, contact forces, and joint constraints.
2. **Environment API Wrapper (Gymnasium)**: Formulates the raw physics state into a standard Reinforcement Learning framework (MDP) using observations, actions, rewards, and reset loops.
3. **Control Policy (Python)**: Reads the observations, applies control algorithms (heuristic PD, Transpose Jacobian, or trained networks), and feeds joint torque actions back to the environment.

---

## Architecture Block Diagram

The interaction loop is illustrated in the diagram below:

```mermaid
graph TD
    subgraph Python Control Layer
        A["Python Control Policy (e.g. lab05_policy.py)"]
    end

    subgraph Gymnasium Interface Layer
        B["Gymnasium Wrapper (Reacher-v4)"]
    end

    subgraph Physics Engine Layer
        C["MuJoCo Solver (mj_step)"]
        D["mjModel (Static XML Config)"]
        E["mjData (Dynamic state: qpos, qvel)"]
    end

    A -->|1. Sends Action (torques)| B
    B -->|2. Maps to actuator controls| C
    D -.->|Loads structure| C
    C -->|3. Integrates equations of motion| E
    E -->|4. Updates positions & velocities| C
    C -->|5. Returns updated state| B
    B -->|6. Packages Observation & Reward| A
```

---

## Detailed Component Interaction

### 1. Static Configuration (`mjModel`)
When `gym.make("Reacher-v4")` is called:
- The environment loads `reacher.xml` from the MuJoCo assets.
- This XML is parsed by MuJoCo to construct an `mjModel` C structure, containing fixed properties like link lengths ($0.1\text{m}$), body masses, and joint rotation axes.

### 2. Dynamic State (`mjData`)
- `mjData` represents the mutable simulator memory.
- Every call to `mj_step` reads the control torques from the actuators, solves the equations of motion:
  $$M(q)\ddot{q} + C(q, \dot{q}) + \tau_g(q) = \tau_{\text{applied}}$$
  and updates `qpos` (positions) and `qvel` (velocities) in `mjData`.

### 3. Gymnasium API Interface
- Gymnasium wraps these raw parameters into an observation vector (10D) and computes a reward at each step based on the distance between the fingertip and target, penalized by control effort:
  $$\text{reward} = -\text{distance} - \sum a_i^2$$
