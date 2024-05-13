"""
https://github.com/legopitstop/addons/tree/main/Basalt_Blocks
"""

from mcaddon import *
from assetplus import SlabBlock, StairsBlock

__version__ = Version(1, 3, 0)


class BasaltBlocks(Addon):
    def __init__(self):
        Addon.__init__(self)
        meta = Metadata(
            "https://license.lpsmods.dev", "https://lpsmods.dev"
        )
        meta.add_author("legopitstop")
        self["resources"].set_uuids(
            "2660f6c8-4130-4745-a6f9-75366d9c1c11",
            "725ad88e-6cd7-437a-91d6-e8dd3ae652cd",
        )
        self["data"].set_uuids(
            "d627db6d-5e48-425f-88d5-40f0ff30427f",
            "74eb9428-6eb2-4324-bd27-7187c4f346cb",
        )
        self["data"].manifest.add_dependency(self["resources"])
        for pack in self:
            pack.version = __version__
            pack.manifest.metadata = meta
            pack.set_details("Basalt Blocks", "More Basalt! §8Developer: §6Legopitstop")


class SimpleBlock(Block):
    def __init__(self, identifier, material: Material):
        Block.__init__(self, identifier, MenuCategory(Category.construction))
        self.add_component(
            LootComponent(
                f"loot_tables/basaltblocks/blocks/{self.identifier.path}.json"
            )
        )
        self.add_component(MapColorComponent("#191919"))
        self.add_component(UnitCubeComponent())
        self.add_component(DestructibleByMiningComponent(0.15))
        self.add_component(DestructibleByExplosionComponent(4.2))
        mi = MaterialInstancesComponent()
        mi.add_material("*", material)
        self.add_component(mi)


class PillarBlock(Block):
    def __init__(self, identifier, top_material: Material, side_material: Material):
        Block.__init__(self, identifier, MenuCategory(Category.construction))
        self.add_component(
            LootComponent(
                f"loot_tables/basaltblocks/blocks/{self.identifier.path}.json"
            )
        )
        self.add_component(MapColorComponent("#191919"))
        self.add_component(UnitCubeComponent())
        self.add_component(DestructibleByMiningComponent(0.15))
        self.add_component(DestructibleByExplosionComponent(4.2))
        mi = MaterialInstancesComponent()
        mi.add_material("up", top_material)
        mi.add_material("down", top_material)
        mi.add_material("*", side_material)
        self.add_component(mi)


main = BasaltBlocks()

solid = [
    "cobbled_basalt",
    "chiseled_polished_basalt",
    "cracked_polished_basalt",
    "polished_basalt_bricks",
    "smooth_polished_basalt",
]

for x in solid:
    id = Identifier("basaltblocks", x)
    main.add(SimpleBlock(id, Material(id)))

main.add(
    PillarBlock(
        "basaltblocks:polished_basalt_brick_pillar",
        Material("basaltblocks:polished_basalt_brick_pillar"),
        Material("basaltblocks:polished_basalt_brick_pillar_side"),
    )
)

shaped = [
    "cobbled_basalt",
    "chiseled_polished_basalt",
    "cracked_polished_basalt",
    "polished_basalt_brick",
    "smooth_polished_basalt",
]

for x in shaped:
    slab_id = Identifier("basaltblocks", x + "_slab")
    main.add(SlabBlock(slab_id, Material(id)))

    stairs_id = Identifier("basaltblocks", x + "_stairs")
    main.add(StairsBlock(stairs_id, Material(id)))

if __name__ == "__main__":
    main.save(
        f"build/Basalt_Blocks_{__version__}.mcaddon", zipped=False, overwrite=True
    )
