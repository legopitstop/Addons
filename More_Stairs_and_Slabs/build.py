"""
https://github.com/legopitstop/addons/tree/main/More_Stairs_and_Slabs
"""

from mcaddon import *

__version__ = Version(1, 3, 0)
MOD_ID = 'moress'

class MoreSS(Addon):
    def __init__(self):
        Addon.__init__(self)
        meta = Metadata(
            "https://license.lpsmods.dev", "https://lpsmods.dev"
        )
        meta.add_author("legopitstop")
        self["resources"].set_uuids(
            "f27ad127-cb0a-4185-96c3-483e1ba7142b",
            "e5031ffd-e6c3-466c-8d76-80b7540fdf04",
        )
        self["data"].set_uuids(
            "bfd091d1-2d3a-4e42-8856-cb546696262e",
            "041746e6-c9a2-420d-a5a6-79dfc0bbb80f",
        )
        self["data"].manifest.add_dependency(self["resources"])
        for pack in self:
            pack.version = __version__
            pack.manifest.metadata = meta
            pack.set_details(
                "More Stairs and Slabs", "New stairs and slab variants! §8Developer: §6Legopitstop"
            )

main = MoreSS()

if __name__ == "__main__":
    main.save(f"build/More_SS.mcaddon", zipped=False, overwrite=True)
