"""
https://github.com/legopitstop/addons/tree/main/Simple_Magnets
"""

from mcaddon import *

__version__ = Version(1, 3, 0)
MOD_ID = 'magnet'

class Magnet(Addon):
    def __init__(self):
        Addon.__init__(self)
        meta = Metadata(
            "https://license.lpsmods.dev", "https://lpsmods.dev"
        )
        meta.add_author("legopitstop")
        self["resources"].set_uuids(
            "16a46bd0-f937-4f63-88f3-c70280f6ffac",
            "e7c093ec-fe51-469f-81a9-6b97bb13277c",
        )
        self["data"].set_uuids(
            "c626559c-6a9e-4851-9b97-0213a2650294",
            "a01d4625-ab34-4649-a0fd-ece3684d908e",
        )
        self["data"].manifest.add_dependency(self["resources"])
        for pack in self:
            pack.version = __version__
            pack.manifest.metadata = meta
            pack.set_details(
                "Simple Magnets", "Easly pickup items from far away! §8Developer: §6Legopitstop"
            )

main = Magnet()

if __name__ == "__main__":
    main.save(f"build/Simple_Magnets.mcaddon", zipped=False, overwrite=True)
