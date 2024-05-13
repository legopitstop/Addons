from mcaddon import *

__version__ = Version(1, 5, 0)
MOD_ID = 'moreblocks'

LAYERS = [
    "acacia",
    "acacia_leaves",
    "acacia_log",
    "acacia_wood",
    "amethyst_block",
    "ancient_debris",
    "andesite",
    "azalea_leaves",
    "bamboo_block",
    "bamboo",
    "bamboo_mosaic",
    "basalt",
    "bedrock",
    "birch",
    "birch_leaves",
    "birch_log",
    "birch_wood",
    "blackstone",
    "black_concrete",
    "black_concrete_powder",
    "black_glazed_terracotta",
    "black_stained_glass",
    "black_terracotta",
    "black_wool",
    "blue_concrete",
    "blue_concrete_powder",
    "blue_glazed_terracotta",
    "blue_ice",
    "blue_stained_glass",
    "blue_terracotta",
    "blue_wool",
    "bone_block",
    "brain_coral_block",
    "brick_block",
    "brown_concrete",
    "brown_concrete_powder",
    "brown_glazed_terracotta",
    "brown_stained_glass",
    "brown_terracotta",
    "brown_wool",
    "bubble_coral_block",
    "budding_amethyst",
    "calcite",
    "cherry",
    "cherry_leaves",
    "cherry_log",
    "cherry_wood",
    "chiseled_deepslate",
    "chiseled_nether_brick",
    "chiseled_polished_blackstone",
    "chiseled_quartz_block",
    "chiseled_red_sandstone",
    "chiseled_sandstone",
    "chiseled_stone_brick",
    "clay_block",
    "coal_block",
    "coal_ore",
    "coarse_dirt",
    "cobbled_deepslate",
    "cobblestone",
    "copper_block",
    "copper_ore",
    "cracked_deepslate_brick",
    "cracked_deepslate_tile",
    "cracked_nether_brick",
    "cracked_polished_blackstone_brick",
    "cracked_stone_brick",
    "crimson_hyphae",
    "crimson",
    "crimson_nylium",
    "crimson_stem",
    "crying_obsidian",
    "cut_copper",
    "cut_red_sandstone",
    "cut_sandstone",
    "cyan_concrete",
    "cyan_concrete_powder",
    "cyan_glazed_terracotta",
    "cyan_stained_glass",
    "cyan_terracotta",
    "cyan_wool",
    "dark_oak",
    "dark_oak_leaves",
    "dark_oak_log",
    "dark_oak_wood",
    "dark_prismarine",
    "dead_brain_coral_block",
    "dead_bubble_coral_block",
    "dead_fire_coral_block",
    "dead_horn_coral_block",
    "dead_tube_coral_block",
    "deepslate_brick",
    "deepslate_coal_ore",
    "deepslate_copper_ore",
    "deepslate_diamond_ore",
    "deepslate_emerald_ore",
    "deepslate_gold_ore",
    "deepslate_iron_ore",
    "deepslate_lapis_ore",
    "deepslate",
    "deepslate_redstone_ore",
    "deepslate_tile",
    "diamond_block",
    "diamond_ore",
    "diorite",
    "dirt",
    "dirt_path",
    "dried_kelp_block",
    "dripstone_block",
    "emerald_block",
    "emerald_ore",
    "end_stone_brick",
    "end_stone",
    "exposed_copper",
    "exposed_cut_copper",
    "fire_coral_block",
    "flowering_azalea_leaves",
    "gilded_blackstone",
    "glass",
    "glowstone",
    "gold_block",
    "gold_ore",
    "granite",
    "grass_block",
    "gravel",
    "gray_concrete",
    "gray_concrete_powder",
    "gray_glazed_terracotta",
    "gray_stained_glass",
    "gray_terracotta",
    "gray_wool",
    "green_concrete",
    "green_concrete_powder",
    "green_glazed_terracotta",
    "green_stained_glass",
    "green_terracotta",
    "green_wool",
    "hay_block",
    "honeycomb_block",
    "honey_block",
    "horn_coral_block",
    "ice",
    "iron_block",
    "iron_ore",
    "jungle",
    "jungle_leaves",
    "jungle_log",
    "jungle_wood",
    "lapis_block",
    "lapis_ore",
    "light_blue_concrete",
    "light_blue_concrete_powder",
    "light_blue_glazed_terracotta",
    "light_blue_stained_glass",
    "light_blue_terracotta",
    "light_blue_wool",
    "light_gray_concrete",
    "light_gray_concrete_powder",
    "light_gray_glazed_terracotta",
    "light_gray_stained_glass",
    "light_gray_terracotta",
    "light_gray_wool",
    "lime_concrete",
    "lime_concrete_powder",
    "lime_glazed_terracotta",
    "lime_stained_glass",
    "lime_terracotta",
    "lime_wool",
    "magenta_concrete",
    "magenta_concrete_powder",
    "magenta_glazed_terracotta",
    "magenta_stained_glass",
    "magenta_terracotta",
    "magenta_wool",
    "magma_block",
    "mangrove",
    "mangrove_leaves",
    "mangrove_log",
    "mangrove_roots",
    "mangrove_wood",
    "mossy_cobblestone",
    "mossy_stone_brick",
    "moss",
    "muddy_mangrove_roots",
    "mud_brick",
    "mud",
    "mycelium",
    "netherite_block",
    "netherrack",
    "nether_brick_block",
    "nether_gold_ore",
    "nether_quartz_ore",
    "nether_wart_block",
    "oak",
    "oak_leaves",
    "oak_log",
    "oak_wood",
    "obsidian",
    "ochre_froglight",
    "orange_concrete",
    "orange_concrete_powder",
    "orange_glazed_terracotta",
    "orange_stained_glass",
    "orange_terracotta",
    "orange_wool",
    "oxidized_copper",
    "oxidized_cut_copper",
    "packed_ice",
    "packed_mud",
    "pearlescent_froglight",
    "pink_concrete",
    "pink_concrete_powder",
    "pink_glazed_terracotta",
    "pink_stained_glass",
    "pink_terracotta",
    "pink_wool",
    "podzol",
    "polished_andesite",
    "polished_basalt",
    "polished_blackstone_brick",
    "polished_blackstone",
    "polished_deepslate",
    "polished_diorite",
    "polished_granite",
    "prismarine_brick",
    "prismarine",
    "purple_concrete",
    "purple_concrete_powder",
    "purple_glazed_terracotta",
    "purple_stained_glass",
    "purple_terracotta",
    "purple_wool",
    "purpur_block",
    "purpur_pillar",
    "quartz_block",
    "quartz_brick",
    "quartz_pillar",
    "raw_copper_block",
    "raw_gold_block",
    "raw_iron_block",
    "redstone_block",
    "redstone_ore",
    "red_concrete",
    "red_concrete_powder",
    "red_glazed_terracotta",
    "red_nether_brick",
    "red_sandstone",
    "red_sand",
    "red_stained_glass",
    "red_terracotta",
    "red_wool",
    "reinforced_deepslate",
    "rooted_dirt",
    "sandstone",
    "sand",
    "sculk_catalyst",
    "sculk",
    "shroomlight",
    "slime_block",
    "smooth_basalt",
    "smooth_quartz_block",
    "smooth_red_sandstone",
    "smooth_sandstone",
    "smooth_stone",
    "soul_sand",
    "soul_soil",
    "sponge",
    "spruce",
    "spruce_leaves",
    "spruce_log",
    "spruce_wood",
    "stone_brick",
    "stone",
    "stripped_acacia_log",
    "stripped_acacia_wood",
    "stripped_bamboo_block",
    "stripped_birch_log",
    "stripped_birch_wood",
    "stripped_cherry_log",
    "stripped_cherry_wood",
    "stripped_crimson_hyphae",
    "stripped_crimson_stem",
    "stripped_dark_oak_log",
    "stripped_dark_oak_wood",
    "stripped_jungle_log",
    "stripped_jungle_wood",
    "stripped_mangrove_log",
    "stripped_mangrove_wood",
    "stripped_oak_log",
    "stripped_oak_wood",
    "stripped_spruce_log",
    "stripped_spruce_wood",
    "stripped_warped_hyphae",
    "stripped_warped_stem",
    "target",
    "terracotta",
    "tinted_glass",
    "tube_coral_block",
    "verdant_froglight",
    "warped_hyphae",
    "warped",
    "warped_nylium",
    "warped_stem",
    "warped_wart_block",
    "waxed_copper_block",
    "waxed_cut_copper",
    "waxed_exposed_copper",
    "waxed_exposed_cut_copper",
    "waxed_weathered_copper",
    "waxed_weathered_cut_copper",
    "weathered_copper",
    "weathered_cut_copper",
    "wet_sponge",
    "white_concrete",
    "white_concrete_powder",
    "white_glazed_terracotta",
    "white_stained_glass",
    "white_terracotta",
    "white_wool",
    "yellow_concrete",
    "yellow_concrete_powder",
    "yellow_glazed_terracotta",
    "yellow_stained_glass",
    "yellow_terracotta",
    "yellow_wool",
]

class MoreBlocks(Addon):
    def __init__(self):
        Addon.__init__(self)
        self.MOD_ID = "moreblocks"
        meta = Metadata(
            "https://license.lpsmods.dev", "https://lpsmods.dev"
        )
        meta.add_author("legopitstop")
        self["resources"].set_uuids(
            "4791d53e-88de-49f6-846b-a2cbe7508032",
            "2b8803db-9f65-4129-9798-b5da4b74d9b5",
        )
        self["data"].set_uuids(
            "bf24499d-0163-4ccb-a485-2c091c51317b",
            "55ceba31-af5d-4716-90f7-e5bfbd17c6ec",
        )
        self["data"].manifest.add_dependency(self["resources"])
        self["data"].manifest.add_dependency(
            Dependency("c86dd7d9-e84e-456f-a84f-1993e353da4c", Version(1, 6, 0))
        )
        for pack in self:
            pack.version = __version__
            pack.manifest.metadata = meta
            pack.set_details(
                "Ultimate Block Breaker", "Block Breaker! §8Developer: §6Legopitstop"
            )


class LayerBlock(Block):
    def __init__(self, id):
        Block.__init__(
            self, id, MenuCategory(Category.CONSTRUCTION, ItemGroup.SEARCH)
        )
        self.layers = self.add_state(
            IntegerState(8, 1, self.identifier.copy_with_path("layers"))
        )
        self.vertical_half = self.add_trait(PlacementPositionTrait.vertical_half())

        self.add_component(LightDampeningComponent(0))
        self.add_component(DestructibleByMiningComponent(1.2))
        self.add_component(DestructibleByExplosionComponent(1.2))
        mi = MaterialInstancesComponent()
        self.add_component(mi)
        self.add_component(
            OnInteractComponent(
                self.identifier.copy_with_path("increase_layers"),
                condition=Molang(
                    f"q.block_state('{ self.layers }')!=8&&q.is_item_name_any('slot.weapon.mainhand','{ self }')"
                ),
            )
        )

        perm1 = BlockPermutation.blockstate(self.vertical_half[0], "top")
        perm1.add_component(TransformationComponent.rotate(180, 0, 0))
        self.add_permutation(perm1)

        for i in range(1, 9):
            perm = BlockPermutation.blockstate(self.layers, i)
            perm.add_component(
                LootComponent(
                    f"loot_tables/blocks/{ self.identifier.path }{ str(i) }.json"
                )
            )

            if i < 8:
                perm.add_component(
                    GeometryComponent("geometry.template_height" + str(i - 1))
                )
                perm.add_component(
                    SelectionBoxComponent(Vector3(-8, 0, -8), Vector3(16, i * 2, 16))
                )
                perm.add_component(
                    CollisionBoxComponent(Vector3(-8, 0, -8), Vector3(16, i * 2, 16))
                )

            else:
                perm.add_component(UnitCubeComponent())
            self.add_permutation(perm)
        self.add_events(
            "increase_layers",
            DecrementStack(),
            IncrementBlockProperty(self.layers),
            RunCommand(f"playsound step.stone @a[r=17] ~ ~ ~"),
        )


main = MoreBlocks()

for name in LAYERS:
    main.add(LayerBlock(Identifier(main.MOD_ID, name).suffix("_layer")))

if __name__ == "__main__":
    main.save(f"build/More_Blocks.mcaddon", zipped=False, overwrite=True)
