from dataclasses import dataclass

## data class rocket engine has mass_flow, thrust, and specific_impulse attributes
@dataclass
class RocketEngine:
    mass_flow: float
    thrust: float
    specific_impulse: float

## data class rocket stage has dry_mass, propellant_mass, and engine attributes number of engines is also needed
@dataclass
class RocketStage:
    dry_mass: float
    propellant_mass: float
    engine: RocketEngine
    number_of_engines: int

## data class rocket has stages and payload_mass attributes
@dataclass
class Rocket:
    stages: list[RocketStage]
    payload_mass: float

## data class mission has rocket and delta_v attributes
@dataclass
class MissionData:
    rocket: Rocket
    delta_v: float

## data class component has name, mass, and cost attributes
@dataclass
class Component:
    name: str
    mass: float
    cost: float