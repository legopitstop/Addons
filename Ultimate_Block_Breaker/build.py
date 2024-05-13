"""
https://github.com/legopitstop/addons/tree/main/Ultimate_Block_Breaker
"""

from mcaddon import *
from More_Upgrades.build import main as mu

__version__ = Version(1, 3, 0)
MOD_ID = 'breaker'

class Breaker(Addon):
    def __init__(self):
        Addon.__init__(self)
        meta = Metadata(
            "https://license.lpsmods.dev", "https://lpsmods.dev"
        )
        meta.add_author("legopitstop")
        self["resources"].set_uuids(
            "fab6b726-c1f9-4fff-889b-27010898272a",
            "caec780d-cb60-4e44-8da8-43afb793a9fa",
        )
        self["data"].set_uuids(
            "7fda5795-39b2-40bb-8996-e20901af09ca",
            "35d35295-883a-483b-8c31-e17e4481166c",
        )
        self["data"].manifest.add_dependency(self["resources"])
        self["data"].manifest.add_dependency(mu["data"])
        for pack in self:
            pack.version = __version__
            pack.manifest.metadata = meta
            pack.set_details(
                "Ultimate Block Breaker", "Block Breaker! §8Developer: §6Legopitstop"
            )


class BreakerBlock(Block):
    def __init__(self, material_type: str, delay: int):
        Block.__init__(
            self,
            Identifier("breaker", f"{material_type}_block_breaker"),
            MenuCategory("items", "itemGroup.search"),
            sound_group="stone",
        )
        direction = self.add_trait(PlacementPositionTrait.block_face())
        powered = self.add_state(
            BooleanState(id=self.identifier.copy_with_path("powered"))
        )

        self.add_component(
            LootComponent(f"loot_tables/blocks/{self.identifier.path}.json")
        )
        self.add_component(LightDampeningComponent(0))
        self.add_component(DestructibleByMiningComponent(3.5))
        self.add_component(DestructibleByExplosionComponent(3.5))
        self.add_component(OnInteractComponent())
        self.add_component(UnitCubeComponent())

        oi = Sequence()
        oi.set_condition(0, Molang(f"q.block_property('{powered.id}')==true"))
        oi.add_event(
            0,
            RunCommand(
                [
                    'titleraw @s actionbar {"rawtext":[{"translate":"gui.false"}]}',
                    "playsound random.click @p",
                ]
            ),
        )
        oi.add_event(0, SetBlockProperty({powered.id: Molang("false")}))

        oi.set_condition(1, Molang(f"q.block_property('{powered.id}')==false"))
        oi.add_event(
            1,
            RunCommand(
                [
                    'titleraw @s actionbar {"rawtext":[{"translate":"gui.true"}]}',
                    "playsound random.click @p",
                ]
            ),
        )
        oi.add_event(1, SetBlockProperty({powered.id: Molang("true")}))
        self.add_event("on_interact", oi)

        oi = Sequence()
        for i, state in enumerate(direction):
            oi.set_condition(
                i, Molang(f"q.block_property('{direction[0].id}')=='{state}'")
            )
            oi.add_event(i, RunCommand("function breaker/" + state))
        self.add_event("break_block", oi)

        perm1 = BlockPermutation(Molang(f"q.block_property('{powered.id}')==true"))
        perm1.add_component(
            QueuedTickingComponent(
                delay, Trigger(self.identifier.copy_with_path("break_block")), True
            )
        )
        material1 = MaterialInstancesComponent()
        material1.add_material(
            "up", Material(f"breaker:{material_type}_block_breaker_top_on")
        )
        material1.add_material("down", Material("breaker:block_breaker_bottom"))
        material1.add_material(
            ("north", "south", "east", "west"),
            Material(f"breaker:{material_type}_block_breaker_side"),
        )
        perm1.add_component(material1)
        self.add_permutation(perm1)

        perm2 = BlockPermutation(Molang(f"q.block_property('{powered.id}')==false"))
        material2 = MaterialInstancesComponent()
        material2.add_material(
            "up", Material(f"breaker:{material_type}_block_breaker_top")
        )
        material2.add_material("down", Material("breaker:block_breaker_bottom"))
        material2.add_material(
            ("north", "south", "east", "west"),
            Material(f"breaker:{material_type}_block_breaker_side"),
        )
        perm2.add_component(material2)
        self.add_permutation(perm2)

        perm3 = BlockPermutation(
            Molang(f"q.block_property('{direction[0].id}')=='north'")
        )
        perm3.add_component(TransformationComponent([0, 0, 0]))
        self.add_permutation(perm3)

        perm4 = BlockPermutation(
            Molang(f"q.block_property('{direction[0].id}')=='south'")
        )
        perm4.add_component(TransformationComponent([180, 0, 0]))
        self.add_permutation(perm4)

        perm5 = BlockPermutation(
            Molang(f"q.block_property('{direction[0].id}')=='east'")
        )
        perm5.add_component(TransformationComponent([0, 90, 0]))
        self.add_permutation(perm5)

        perm6 = BlockPermutation(
            Molang(f"q.block_property('{direction[0].id}')=='west'")
        )
        perm6.add_component(TransformationComponent([0, -90, 0]))
        self.add_permutation(perm6)

        perm7 = BlockPermutation(Molang(f"q.block_property('{direction[0].id}')=='up'"))
        perm7.add_component(TransformationComponent([180, 0, 0]))
        self.add_permutation(perm7)

        perm8 = BlockPermutation(
            Molang(f"q.block_property('{direction[0].id}')=='down'")
        )
        perm8.add_component(TransformationComponent([0, 0, 0]))
        self.add_permutation(perm8)


main = Breaker()

tiers = {"diamond": 3, "gold": 5, "netherite": 1, "stone": 9, "wooden": 11}

for name, delay in tiers.items():
    main.add(BreakerBlock(name, delay))

for id in main.get_pack("data").blocks:
    main.add(LootTable.block(id))

if __name__ == "__main__":
    main.save(f"build/Breaker.mcaddon", zipped=False, overwrite=True)
