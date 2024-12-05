from dfcx_scrapi.core.intents import Intents
from dfcx_scrapi.tools.dataframe_functions import DataframeFunctions

creds_path = '<PATH_TO_CRED.json>'
agent_id = 'projects/<PROJECT_NAME>/locations/<LOCATION>/agents/<AGENT_ID>'


i = Intents(creds_path=creds_path,agent_id=agent_id)
#print(i.list_intents)
#Below txt file should have list of intents to delete
with open('intentsToDelete.txt', 'r') as f:
    intentsToDelete = [line.strip() for line in f]

presentIntentsDict = i.get_intents_map(agent_id=agent_id)
presentIntentIDList = list(presentIntentsDict.keys())
presentIntentNameList = list(presentIntentsDict.values())
for intentdel in intentsToDelete:
    intentIDIndex = presentIntentNameList.index(intentdel)
    try:
        i.delete_intent(intent_id=presentIntentIDList[intentIDIndex])
        print("[Info] Intent deleted successfully: %s",intentdel)
    except:
        print("[Error] Intent Not Deleted: %s",intentdel)
    