"""
https://github.com/legopitstop/addons/tree/main/More_Pumpkins
"""

from mcaddon import *

__version__ = Version(1, 3, 0)
MOD_ID = 'morepumpkin'

class MorePumpkin(Addon):
    def __init__(self):
        Addon.__init__(self)
        meta = Metadata(
            "https://license.lpsmods.dev", "https://lpsmods.dev"
        )
        meta.add_author("legopitstop")
        self["resources"].set_uuids(
            "fc1059e6-366e-4fde-9b49-8be5b1434b3d",
            "5e6b0fc0-897a-4afa-9198-d511dd9bc640",
        )
        self["data"].set_uuids(
            "4e1db273-4d60-4728-a674-7e5b3648f180",
            "c2ecdc36-955c-4e22-9b69-3aea371005a6",
        )
        self["data"].manifest.add_dependency(self["resources"])
        for pack in self:
            pack.version = __version__
            pack.manifest.metadata = meta
            pack.set_details(
                "More Pumpkins", "Happy Halloween! §8Developer: §6Legopitstop"
            )

main = MorePumpkin()

if __name__ == "__main__":
    main.save(f"build/More_Pumpkins.mcaddon", zipped=False, overwrite=True)
