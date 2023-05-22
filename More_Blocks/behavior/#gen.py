# Generates all the blocks from the list.txt
import os
import re
import json

MOD_ID = 'moreblocks'

LOCAL = os.path.dirname(os.path.realpath(__file__))
opn = open(os.path.join(LOCAL, 'list.txt'))
names = opn.readlines()
opn.close()


for t in os.listdir(os.path.join(LOCAL, 'templates')):
    opn = open(os.path.join(LOCAL, 'templates', t))
    TEMPLATE = opn.read()
    opn.close()
    

    for n in names:
        name = re.sub(r'bricks$','brick',n.strip().replace('\\n',''))
        name2 = n.strip().replace('\\n','')
        id = MOD_ID+':'+name+'_'+t.replace('.json','')
        filename = name+'_'+t.replace('.json','')

        display_name = name.replace(MOD_ID, '').replace('_',' ').title()

        temp = TEMPLATE
        print(display_name)

        temp = temp.replace('{id}', id).replace('{name2}', name2).replace('{name}', name).replace('{filename}', filename)

        # make block
        wrt = open(os.path.join(LOCAL, 'blocks', 'gen', filename+'.json'),'w')
        wrt.write(temp)
        wrt.close()

        # make loot tables
        for i in range(1, 9):
            LOOT_TABLE = {
                    "pools": [
                        {
                            "rolls": 1,
                            "entries": [
                                {
                                    "type": "item",
                                    "name": id,
                                    "weight": 1,
                                    "functions": [
                                        {
                                            "function": "set_count",
                                            "count": 1
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }

            with open(os.path.join(LOCAL, 'loot_tables', 'blocks', filename+str(i)+'.json'), 'w') as w:
                w.write(json.dumps(LOOT_TABLE))

        # make recipes
        STONECUTTER = {
                "format_version": "1.17.1",
                "minecraft:recipe_shapeless": {
                    "description": {
                        "identifier": id+"_stonecutting"
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
                        "item": id,
                        "count": 8
                    }
                }
            }
        with open(os.path.join(LOCAL, 'recipes', 'layer', filename+'_stonecutter.json'), 'w') as w:
            w.write(json.dumps(STONECUTTER))