"""
https://github.com/legopitstop/addons/tree/main/Construction_Blocks
"""

from mcaddon import *

__version__ = Version(1, 3, 0)
MOD_ID = 'const'

class ConstBlocks(Addon):
    def __init__(self):
        Addon.__init__(self)
        meta = Metadata(
            "https://license.lpsmods.dev", "https://lpsmods.dev"
        )
        meta.add_author("legopitstop")
        self["resources"].set_uuids(
            "14b9a43a-8846-42e5-9eb5-d547510a60c7",
            "13c88350-9128-471f-8217-73cb87060874",
        )
        self["data"].set_uuids(
            "654051c3-adf1-439c-87ee-6c92a1fbcec9",
            "b820eed4-e49a-44aa-975a-1c6d85420d16",
        )
        self["data"].manifest.add_dependency(self["resources"])
        for pack in self:
            pack.version = __version__
            pack.manifest.metadata = meta
            pack.set_details(
                "Construction Blocks", "Get Your Built On! §8Developer: §6Legopitstop"
            )

main = ConstBlocks()

if __name__ == "__main__":
    main.save(f"build/Construction_Blocks.mcaddon", zipped=False, overwrite=True)
