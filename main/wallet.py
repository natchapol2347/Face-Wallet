import json
import os

def pay(face_names,store_name):
    for i in face_names:
        account = i +'.txt'
        if(os.path.exists(account)):
            temp ={}
            with open(account,'r') as json_file:
                temp = json.load(json_file)
                
                if store_name not in temp['paid'].keys():
                    print("adding store")
                    temp['paid'][store_name] = False

                if(temp['paid'][store_name]) is False: 
                    if temp["balance"]-300 >= 0:
                        temp["balance"] -= 300
                        temp['paid'][store_name] = True
                    else:
                        print("Insufficient funds")
                json_file.close()

            with open(account, 'w') as outfile:
                json.dump(temp, outfile)
        else:
            data = {'name':i,'balance': 1000,'paid':{store_name:False}}
            with open(account, 'w') as outfile:
                json.dump(data, outfile)

