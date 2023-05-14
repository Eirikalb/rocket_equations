from RocketParts import Component, MissionData, Rocket, RocketEngine, RocketStage
import math
import logging
import StarshipRocket 

logging.basicConfig(level=logging.DEBUG)


class Mission():
    def __init__(self, missionData: MissionData, debug:bool = False):
        self.missionData = missionData
        self.log_level = logging.DEBUG if debug else logging.INFO
        self.logger = logging.getLogger("Mission")
        self.logger.setLevel(self.log_level)
        self.logger.debug(f"Mission created with {self.missionData.rocket.stages} stages and {self.missionData.rocket.payload_mass} payload mass")
        
    #max_delta_v 
    def max_delta_v(self) -> float:
        rocket_delta_v = 0
        for i, stage in enumerate(self.missionData.rocket.stages):
            # add weight of stacked rocket stages
            current_stage_mass = self.missionData.rocket.payload_mass + sum([stage.dry_mass + stage.propellant_mass for stage in self.missionData.rocket.stages[i:]])
            expected_dry_mass = stage.dry_mass + self.missionData.rocket.payload_mass + sum([stage.dry_mass +stage.propellant_mass for stage in self.missionData.rocket.stages[i+1:]])
            stage_delta_v = stage.engine.specific_impulse * 9.81 * math.log(current_stage_mass / expected_dry_mass)
            self.logger.debug(f"Stage {i} contributes {stage_delta_v} m/s ({stage_delta_v * 3.6} km/h)")
            rocket_delta_v += stage_delta_v
        self.logger.debug(f"Full rocket delta_v {rocket_delta_v} m/s ({rocket_delta_v * 3.6} km/h)")
        return rocket_delta_v

    # can the rocket reach the delta_v required for the mission?
    def can_reach_delta_v(self) -> tuple[bool, float]:
        mission_delta_v = self.missionData.delta_v
        rocket_max_delta_v = self.max_delta_v()
        if rocket_max_delta_v >= mission_delta_v:
            return True, rocket_max_delta_v
        return False, rocket_max_delta_v

    def max_payload_mass(self, epsilon:float, step_size:float, iterations:int) -> float:
        copy_of_mission_payload_mass = self.missionData.rocket.payload_mass
        for i in range(iterations):
            self.logger.debug(f"Mission payload mass: {self.missionData.rocket.payload_mass}")
            if abs(self.max_delta_v() - self.missionData.delta_v)> epsilon:
                self.missionData.rocket.payload_mass += (self.max_delta_v() - self.missionData.delta_v)*step_size
                self.logger.info(f"Found Payload mass after {i} iterations: {self.missionData.rocket.payload_mass}")
            else:
                return self.missionData.rocket.payload_mass
            if self.missionData.rocket.payload_mass < 0:
                self.logger.info(f" Failed to find payload mass after {i} iterations: {self.missionData.rocket.payload_mass}")
                break
        self.logger.info(f"Failed to find max payload mass after {iterations} iterations: {self.missionData.rocket.payload_mass}")
        self.missionData.rocket.payload_mass = copy_of_mission_payload_mass
        return self.missionData.rocket.payload_mass
        
if __name__ == "__main__":
    print("Mission 1")
    low_earth_orbit_mission_data = MissionData(rocket=StarshipRocket.starship, delta_v=9400)
    mission = Mission(low_earth_orbit_mission_data,debug=False)
    max_payload = mission.max_payload_mass(0.01, 0.1, 1000)
    print(f"Mission 1 has a max payload mass of : {max_payload} tons")
    
    print("Mission 2")
    low_earth_orbit_mission_data = MissionData(rocket=StarshipRocket.starship_v2, delta_v=9400)
    mission_v2 = Mission(low_earth_orbit_mission_data,debug=False)
    max_payload = mission_v2.max_payload_mass(0.01, 0.1, 1000)
    print(f"Mission 2 has a max payload mass of : {max_payload} tons")