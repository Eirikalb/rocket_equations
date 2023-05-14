
from RocketParts import Component, Rocket, RocketEngine, RocketStage
import math

# translate all snake_case to camelCase
raptor_engine_v1 = RocketEngine(mass_flow=650, thrust=2000000, specific_impulse=330)
raptor_engine_v2 = RocketEngine(mass_flow=650, thrust=2000000, specific_impulse=350)
raptor_engine_v3 = RocketEngine(mass_flow=650, thrust=2000000, specific_impulse=380)

starship_stage_1 = RocketStage(dry_mass=200, propellant_mass=3600, engine=raptor_engine_v2, number_of_engines=33)
starship_stage_2 = RocketStage(dry_mass=120, propellant_mass=1200, engine=raptor_engine_v2, number_of_engines=3)


starship = Rocket(stages=[starship_stage_1, starship_stage_2], payload_mass=100)

starship_stage_1_v2 = RocketStage(dry_mass=200, propellant_mass=3600, engine=raptor_engine_v3, number_of_engines=33)
starship_stage_2_v2 = RocketStage(dry_mass=120, propellant_mass=1200, engine=raptor_engine_v3, number_of_engines=3)
starship_v2 = Rocket(stages=[starship_stage_1_v2, starship_stage_2_v2], payload_mass=100)