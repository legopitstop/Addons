"""
https://github.com/legopitstop/addons/tree/main/More_Gold
"""

from mcaddon import *

__version__ = Version(1, 3, 0)
MOD_ID = 'moregold'

class MoreGold(Addon):
    def __init__(self):
        Addon.__init__(self)
        meta = Metadata(
            "https://license.lpsmods.dev", "https://lpsmods.dev"
        )
        meta.add_author("legopitstop")
        self["resources"].set_uuids(
            "ebe601a9-616a-4d6e-9150-2c918c7c96f4",
            "e6720ad3-4a70-4d1a-bc68-aff96c7fe3ab",
        )
        self["data"].set_uuids(
            "8878bd80-768e-4b36-acee-5271216c02e7",
            "2afda408-1c21-42c0-8ed6-dba502923004",
        )
        self["data"].manifest.add_dependency(self["resources"])
        for pack in self:
            pack.version = __version__
            pack.manifest.metadata = meta
            pack.set_details(
                "More Gold", "What if Minecraft has more gold food? §8Developer: §6Legopitstop"
            )

main = MoreGold()

if __name__ == "__main__":
    main.save(f"build/More_Gold.mcaddon", zipped=False, overwrite=True)
