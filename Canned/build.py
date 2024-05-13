"""
https://github.com/legopitstop/addons/tree/main/Canned
"""

from mcaddon import *

__version__ = Version(1, 3, 0)
MOD_ID = 'canned'

class Canned(Addon):
    def __init__(self):
        Addon.__init__(self)
        meta = Metadata(
            "https://license.lpsmods.dev", "https://lpsmods.dev"
        )
        meta.add_author("legopitstop")
        self["resources"].set_uuids(
            "7bcddacb-acea-4d89-a348-c5c358b0c143",
            "dd2fca4e-cffa-42d0-b1e0-3e786f5d701c",
        )
        self["data"].set_uuids(
            "7f7c8a3b-ca5a-41c5-885f-24ce7c6219ab",
            "666ec828-7581-47c5-926c-8d0013965e2d",
        )
        self["data"].manifest.add_dependency(self["resources"])
        for pack in self:
            pack.version = __version__
            pack.manifest.metadata = meta
            pack.set_details(
                "Canned", "Canned goods? §8Developer: §6Legopitstop"
            )

main = Canned()

if __name__ == "__main__":
    main.save(f"build/Canned.mcaddon", zipped=False, overwrite=True)
