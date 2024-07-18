"""
https://github.com/legopitstop/addons/tree/main/main
"""

from mcaddon import *

__version__ = Version(1, 0, 0)


class MoreUpgrades(Addon):
    def __init__(self):
        Addon.__init__(self)
        meta = Metadata(
            "https://license.lpsmods.dev", "https://lpsmods.dev"
        )
        meta.add_author("legopitstop")
        self["resources"].set_uuids(
            "e14c6c75-4156-4909-80a4-844def413a59",
            "4582f150-2c5b-4167-a5cc-21df9cf3581e",
        )
        self["data"].set_uuids(
            "26c9f428-63d6-4cfa-a98d-bb20f7af661a",
            "e39e77fb-2061-4e0f-be3c-1cc8f4379d09",
        )
        self["data"].manifest.add_dependency(self["resources"])
        for pack in self:
            pack.version = __version__
            pack.manifest.metadata = meta
            pack.set_details(
                "More Upgrades", "More upgrade templates! §8Developer: §6Legopitstop"
            )


class UpgradeTemplate(Item):
    def __init__(self, material_type: str):
        id = Identifier("moreupgrades", f"{material_type}_upgrade_smithing_template")
        Item.__init__(self, id)
        self.add_component(IconComponent(id))


main = MoreUpgrades()

items = ["stone", "iron", "gold", "diamond"]

ia = ItemAtlas()

# ITEMS

for name in items:
    main.add(UpgradeTemplate(name))
    t = ItemTexture(
        f"moreupgrades:{name}_upgrade_smithing_template",
        [Texture.load(f"assets/{name}_upgrade_smithing_template.png", "items")],
    )
    ia.add_texture(t)
main.add(ia)

# RECIPES

for name in items:
    this = f"{name}_upgrade_smithing_template"
    rpe = ShapedRecipe(
        Identifier("moreupgrades", this + "_duplicate"),
        ["#S#", "#C#", "###"],
        ItemStack(Identifier("moreupgrades", this), 2),
    )
    rpe.add_key("S", ItemStack(Identifier("moreupgrades", this)))
    ing = name + "_ingot" if name in ["iron", "gold"] else name
    rpe.add_key("#", ItemStack(ing))
    rpe.add_key("C", ItemStack("cobblestone"))
    main.add(rpe)

tooltypes = ["sword", "shovel", "pickaxe", "hoe", "axe"]
for tool in tooltypes:
    main.add(
        SmithingTransformRecipe(
            "moreupgrades:smithing_stone_" + tool,
            ItemStack("moreupgrades:stone_upgrade_smithing_template"),
            ItemStack("wooden_" + tool),
            ItemStack("cobblestone"),
            ItemStack("stone_" + tool),
        )
    )
    main.add(
        SmithingTransformRecipe(
            "moreupgrades:smithing_iron_" + tool,
            ItemStack("moreupgrades:iron_upgrade_smithing_template"),
            ItemStack("stone_" + tool),
            ItemStack("iron_ingot"),
            ItemStack("iron_" + tool),
        )
    )
    main.add(
        SmithingTransformRecipe(
            "moreupgrades:smithing_gold_" + tool,
            ItemStack("moreupgrades:gold_upgrade_smithing_template"),
            ItemStack("iron_" + tool),
            ItemStack("gold_ingot"),
            ItemStack("golden_" + tool),
        )
    )
    main.add(
        SmithingTransformRecipe(
            "moreupgrades:smithing_diamond_" + tool,
            ItemStack("moreupgrades:diamond_upgrade_smithing_template"),
            ItemStack("golden_" + tool),
            ItemStack("diamond"),
            ItemStack("diamond_" + tool),
        )
    )

if __name__ == "__main__":
    main.save(
        f"build/More_Upgrades.mcaddon", zipped=False, overwrite=True
    )
