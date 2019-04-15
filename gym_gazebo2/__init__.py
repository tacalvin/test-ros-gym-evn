from gym.envs.registration import register

# Gazebo
# ----------------------------------------
# MARA
register(
    id='MARA-v0',
    entry_point='gym_gazebo2.envs.MARA:MARAEnv',
)

register(
    id='MARARand-v0',
    entry_point='gym_gazebo2.envs.MARA:MARARandEnv',
)



register(
    id='MARAReal-v0',
    entry_point='gym_gazebo2.envs.MARA:MARARealEnv',
)

register(
    id='MARACamera-v0',
    entry_point='gym_gazebo2.envs.MARA:MARACameraEnv',
)

register(
    id='MARAOrient-v0',
    entry_point='gym_gazebo2.envs.MARA:MARAOrientEnv',
)

register(
    id='MARACollision-v0',
    entry_point='gym_gazebo2.envs.MARA:MARACollisionEnv',
)

register(
    id='MARACollisionOrient-v0',
    entry_point='gym_gazebo2.envs.MARA:MARACollisionOrientEnv',
)
