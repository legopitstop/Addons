"""
https://github.com/legopitstop/addons/tree/main/Spawner_Craft
"""

from mcaddon import *

__version__ = Version(1, 3, 0)
MOD_ID = 'spawnercraft'

class SpawnerCraft(BehaviorPack):
    def __init__(self):
        BehaviorPack.__init__(self)
        meta = Metadata(
            "https://license.lpsmods.dev", "https://lpsmods.dev"
        )
        meta.add_author("legopitstop")
        self.set_uuids(
            "52e6666c-5423-4c0b-bf8c-12f75f3b0d3c",
            "09b258fc-96b1-4d7c-a1fa-e414f66cfb40",
        )
        self.version = __version__
        self.manifest.metadata = meta
        self.set_details(
            "Spawner Craft", f"{__version__} - Craft spawn eggs & spawners! §8Developer: §6Legopitstop"
        )


main = SpawnerCraft()

if __name__ == "__main__":
    main.save(f"build/Spawner_Craft.mcpack", zipped=False, overwrite=True)
