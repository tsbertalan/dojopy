import dojopy 
from julia import Base
from julia import Dojo as dojo
import numpy as np

# get an environment
env = dojo.get_environment('pendulum')
dojo.initialize_pendulum_b(env.mechanism, angle=0.0, angular_velocity=0.0)

# get state
x1 = dojo.get_minimal_state(env.mechanism)

# random control
# u1 = Base.rand(nu)
u1 = np.random.uniform(size=(1,))

# simulate one time step
dojo.step(env, x1, u1)

