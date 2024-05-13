"""
https://github.com/legopitstop/addons/tree/main/More_Honey
"""

from mcaddon import *

__version__ = Version(1, 3, 0)
MOD_ID = 'morehoney'

class MoreHoney(Addon):
    def __init__(self):
        Addon.__init__(self)
        meta = Metadata(
            "https://license.lpsmods.dev", "https://lpsmods.dev"
        )
        meta.add_author("legopitstop")
        self["resources"].set_uuids(
            "788d3513-74d0-4e70-ac83-2df10359cd13",
            "88a0b76d-3424-4070-9d98-eb98e1fc6b39",
        )
        self["data"].set_uuids(
            "e03d56d5-090f-499a-b1be-d25764c6f009",
            "32fb52bc-fc12-451c-b8e8-b4bffc7afc56",
        )
        self["data"].manifest.add_dependency(self["resources"])
        for pack in self:
            pack.version = __version__
            pack.manifest.metadata = meta
            pack.set_details(
                "More Honey", "What if Minecraft had more honey food? §8Developer: §6Legopitstop"
            )

main = MoreHoney()

if __name__ == "__main__":
    main.save(f"build/More_Honey.mcaddon", zipped=False, overwrite=True)
