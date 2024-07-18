"""
https://github.com/legopitstop/addons/tree/main/Christmas_Presents
"""

from mcaddon import *

__version__ = Version(1, 3, 0)
MOD_ID = 'presents'

class ChristmasPresents(Addon):
    def __init__(self):
        Addon.__init__(self)
        meta = Metadata(
            "https://license.lpsmods.dev", "https://lpsmods.dev"
        )
        meta.add_author("legopitstop")
        self["resources"].set_uuids(
            "07b40dd1-7356-4dd6-89fd-b4d0666d19cd",
            "a9dcb04c-69e4-42b7-852c-2e26f4e59d6d",
        )
        self["data"].set_uuids(
            "17217958-9dce-4150-9dd1-c3400bb73cbe",
            "1651ac7e-a6c8-449b-8933-b7dc459c1898",
        )
        self["data"].manifest.add_dependency(self["resources"])
        for pack in self:
            pack.version = __version__
            pack.manifest.metadata = meta
            pack.set_details(
                "Christmas Presents", "Christmas! §8Developer: §6Legopitstop"
            )

main = ChristmasPresents()

if __name__ == "__main__":
    main.save(f"build/Christmas_Presents.mcaddon", zipped=False, overwrite=True)
