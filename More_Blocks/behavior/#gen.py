# Generates all the blocks from the list.txt
import os
import re

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

        # Save block
        wrt = open(os.path.join(LOCAL, 'blocks', filename+'.json'),'w')
        wrt.write(temp)
        wrt.close()