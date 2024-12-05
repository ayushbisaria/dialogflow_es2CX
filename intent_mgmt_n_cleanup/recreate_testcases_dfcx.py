from typing import cast
from dfcx_scrapi.core.test_cases import TestCases
from google.cloud.dialogflowcx_v3beta1 import types
from google.cloud.dialogflowcx_v3beta1 import TestResult
from google.cloud.dialogflowcx_v3beta1 import TestCaseResult
from dfcx_scrapi.tools.dataframe_functions import DataframeFunctions
from google.cloud.dialogflowcx_v3beta1 import ConversationTurn 
import json


creds_path = '<PATH_TO_CRED.json>'
agent_id = 'projects/<PROJECT_NAME>/locations/<LOCATION>/agents/<AGENT_ID>'

#create client
tc_client = TestCases(creds_path=creds_path,agent_id=agent_id)
list_tc = tc_client.list_test_cases(agent_id,False)

#  loop through each Tc
for tc in list_tc:
    res = tc_client.get_test_case(tc.name)
    print(res.display_name)
    new_tc = types.TestCase()
    new_tc.display_name =  "<CHANGE-PREFIX>"+res.display_name
    new_tc.tags = res.tags
    #new_tc.test_config = res.test_config
    #new_tc.notes = res.notes
    
    # Below loop can be userd to change/patch user input in any conv turn within test case
    for i in range(len(res.test_case_conversation_turns)):
        tc_turn = types.ConversationTurn()
        tc_turn.user_input = res.test_case_conversation_turns[i].user_input
        new_tc.test_case_conversation_turns.append(tc_turn)
         
    #newresult = TestCaseResult()
    #newresult.test_result = "TestResult.PASSED"
    #new_tc.last_test_result = newresult
    tc_client.create_test_case(new_tc,agent_id)
