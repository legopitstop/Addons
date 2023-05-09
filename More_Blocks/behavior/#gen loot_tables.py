# Generates all loot tables from the block
import json
import os

MOD_ID = 'moreblocks'

LOCAL = os.path.dirname(os.path.realpath(__file__))



def create(rpath):
    for block in os.listdir(rpath):
        path = os.path.join(rpath, block)
        if os.path.isfile(path):
            # Create loot tables        
            print(block)
            for i in range(8):
                LOOT_TABLE = {
                    "pools": [
                        {
                            "rolls": 1,
                            "entries": [
                                {
                                    "type": "item",
                                    "name": MOD_ID + ':' + block.replace('.json', ''),
                                    "weight": 1,
                                    "functions": [
                                        {
                                            "function": "set_count",
                                            "count": i+1
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
                wrt = open(os.path.join(LOCAL, 'loot_tables', 'blocks', block.replace('.json','')+str(i+1)+'.json'),'w')
                wrt.write(json.dumps(LOOT_TABLE))
                wrt.close()    
        else:
            # Folder
            create(path)

create(os.path.join(LOCAL, 'blocks'))