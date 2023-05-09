import json
import os

LOCAL = os.path.dirname(os.path.realpath(__file__))

# Open list
opn = open(os.path.join(LOCAL, 'list.txt'),'r')
list = opn.readlines()
opn.close()

for i in list:
    name = i.replace('\n','').replace(' ','_').strip()
    print(name)

    # Block template
    opn = open(os.path.join(LOCAL, 'template', 'block.json'),'r')
    TEMPLATE_BLOCK = opn.read()
    opn.close()

    TEMPLATE_BLOCK = TEMPLATE_BLOCK.replace('NAME', name)

    wrt = open(os.path.join(LOCAL, 'blocks', '%s_can.json'%(name)),'w')
    wrt.write(TEMPLATE_BLOCK)
    wrt.close()

    # Item Template
    opn = open(os.path.join(LOCAL, 'template', 'item.json'),'r')
    TEMPLATE_ITEM = opn.read()
    opn.close()

    TEMPLATE_ITEM = TEMPLATE_ITEM.replace('NAME', name)

    wrt = open(os.path.join(LOCAL, 'items', '%s_can.json'%(name)),'w')
    wrt.write(TEMPLATE_ITEM)
    wrt.close()

    # Loot Table Template
    tables = {'one': 1,'two': 2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8}
    for table in tables:
        TEMPLATE_TABLE = {
            "pools": [
                {
                    "rolls": 1,
                    "entries": [
                        {
                            "type": "item",
                            "name": "canned:%s_can"%(name),
                            "weight": 1,
                            "functions": [
                                {
                                    "function": "set_count",
                                    "count": tables[table]
                                }
                            ]
                        }
                    ]
                }
            ]
        }

        wrt = open(os.path.join(LOCAL, 'loot_tables', 'blocks', '%s_%s_can.json'%(table,name)),'w')
        wrt.write(json.dumps(TEMPLATE_TABLE))
        wrt.close()

    # Recipe Template
    opn = open(os.path.join(LOCAL, 'template', 'recipe.json'),'r')
    TEMPLATE_RECIPE = opn.read()
    opn.close()
    TEMPLATE_RECIPE = TEMPLATE_RECIPE.replace('NAME', name)
    wrt = open(os.path.join(LOCAL, 'recipes', '%s_can.json'%(name)),'w')
    wrt.write(TEMPLATE_RECIPE)
    wrt.close()

