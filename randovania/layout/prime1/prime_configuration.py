import dataclasses

from randovania.games.game import RandovaniaGame
from randovania.layout.base.base_configuration import BaseConfiguration
from randovania.layout.prime1.artifact_mode import LayoutArtifactMode
from randovania.layout.lib.teleporters import TeleporterConfiguration


@dataclasses.dataclass(frozen=True)
class PrimeConfiguration(BaseConfiguration):
    elevators: TeleporterConfiguration
    energy_per_tank: int = dataclasses.field(metadata={"min": 1, "max": 1000, "precision": 1})
    artifacts: LayoutArtifactMode
    heat_damage: float = dataclasses.field(metadata={"min": 0.1, "max": 99.9, "precision": 3.0})
    heat_protection_only_varia: bool
    progressive_damage_reduction: bool
    allow_underwater_movement_without_gravity: bool
    small_samus: bool

    main_plaza_door: bool
    backwards_frigate: bool
    backwards_labs: bool
    backwards_upper_mines: bool
    backwards_lower_mines: bool
    phazon_elite_without_dynamo: bool

    qol_game_breaking: bool
    qol_minor_cutscenes: bool
    qol_major_cutscenes: bool

    @classmethod
    def game_enum(cls) -> RandovaniaGame:
        return RandovaniaGame.PRIME1
