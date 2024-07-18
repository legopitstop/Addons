# Generate stonecutter recipes
import glob
import json
import os

PATH = os.path.dirname(os.path.realpath(__file__))


def save(name, frm):
    n = (
        name.replace("_pumpkin", "")
        .replace("_jack_o", "")
        .replace("_soul_jack_o", "_soul")
    )
    f = (
        frm.replace("_pumpkin", "")
        .replace("_jack_o", "")
        .replace("_soul_jack_o", "_soul")
    )
    RECIPE = {
        "format_version": "1.19.40",
        "minecraft:recipe_shapeless": {
            "description": {"identifier": f"morepumpkin:{n}_from_{f}_stonecutting"},
            "tags": ["stonecutter"],
            "ingredients": [{"item": "morepumpkin:" + name}],
            "result": "morepumpkin:" + frm,
        },
    }
    with open(
        os.path.join(PATH, "recipes", "stonecutter", f"{n}_from_{f}.json"), "w"
    ) as w:
        w.write(json.dumps(RECIPE))


def recipe(files):
    for file in files:
        if os.path.isfile(file):
            name = os.path.basename(file).replace(".json", "")
            for file in files:
                if os.path.isfile(file):
                    frm = os.path.basename(file).replace(".json", "")
                    if name != frm:
                        print(name + " <- " + frm)
                        save(name, frm)


files = glob.glob(
    os.path.join(PATH, "blocks", "carved_pumpkin") + "/**", recursive=True
)
recipe(files)

files = glob.glob(
    os.path.join(PATH, "blocks", "jack_o_lantern") + "/**", recursive=True
)
recipe(files)

files = glob.glob(
    os.path.join(PATH, "blocks", "soul_jack_o_lantern") + "/**", recursive=True
)
recipe(files)
