import json
from blockPY import *
from datetime import datetime
START=677001
END=677009


def print_tx(string,tx):
    pass
    #if('addr'in tx):
        #print(string+":",  tx['value'], "adr:", tx['addr'])

for i in range(START,END):
    with open('blocks/'+str(i)+'.json') as json_file:
        data = json.load(json_file)
        ##result = welcome_from_dict(data)
        print(datetime.fromtimestamp(data['time']))
        for transaction in data['tx']:
            #print('trans')
            inputs=transaction['inputs']
            outputs=transaction['out']
            for inp in inputs:
                inp_prev=inp['prev_out']
                if(inp_prev):
                    print_tx("In",out)
            for out in outputs:
                print_tx("Out",out)
        print("end")
            

    
