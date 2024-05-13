"""
https://github.com/legopitstop/addons/tree/main/Modders_Christmas
"""

from mcaddon import *

__version__ = Version(1, 3, 0)
MOD_ID = 'xmas'

class Xmas(Addon):
    def __init__(self):
        Addon.__init__(self)
        meta = Metadata(
            "https://license.lpsmods.dev", "https://lpsmods.dev"
        )
        meta.add_author("legopitstop")
        self["resources"].set_uuids(
            "2797755a-87a9-4885-86e0-05e182df1c41",
            "bb2b0e69-c925-44aa-9dd2-0ef0ff65cdc8",
        )
        self["data"].set_uuids(
            "738ff94a-dc4e-41d9-acce-3dadbebbc346",
            "7f436f08-3d18-4649-86e7-e317373f1c35",
        )
        self["data"].manifest.add_dependency(self["resources"])
        for pack in self:
            pack.version = __version__
            pack.manifest.metadata = meta
            pack.set_details(
                "Modder's Christmas", "§4M§2e§4r§2r§4y§2 C§4h§2r§4i§2s§4t§2m§4a§2s§4! §8Developer: §6Legopitstop"
            )

main = Xmas()

if __name__ == "__main__":
    main.save(f"build/Modders_Christmas.mcaddon", zipped=False, overwrite=True)
