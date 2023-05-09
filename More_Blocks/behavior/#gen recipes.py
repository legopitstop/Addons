# Creates all recipes from blocks
import json
import os

LOCAL = os.path.dirname(os.path.realpath(__file__))

def create(path):
    for block in os.listdir(path):
        file = os.path.join(path, block)
        if os.path.isfile(file):
            name = block.replace('.json','')
            print(name)
            stonecutter = {
                "format_version": "1.17.1",
                "minecraft:recipe_shapeless": {
                    "description": {
                        "identifier": "moreblocks:"+name+"_stonecutting"
                    },
                    "tags": [
                        "stonecutter"
                    ],
                    "ingredients": [
                        {
                            "item": "minecraft:"+name.replace('_layer', '')
                        }
                    ],
                    "result": {
                        "item": "moreblocks:"+name,
                        "count": 8
                    }
                }
            }

            wrt = open(os.path.join(LOCAL, 'recipes', name+'_stonecutting.json'), 'w')
            wrt.write(json.dumps(stonecutter))
            wrt.close()

        else:
            create(file)


create(os.path.join(LOCAL,'blocks'))