from dfcx_scrapi.core.intents import Intents
from dfcx_scrapi.tools.dataframe_functions import DataframeFunctions

creds_path = '<PATH_TO_CRED.json>'
agent_id = 'projects/<PROJECT_NAME>/locations/<LOCATION>/agents/<AGENT_ID>'

google_sheet_name = '<SHEET_NAME>' #Make sure service account mentioned in credential json have access to sheet
google_sheet_tab_read = '<SHEET_TAB_NAME>'

i = Intents(creds_path=creds_path)
dffx = DataframeFunctions(creds_path)

df = dffx.sheets_to_dataframe(google_sheet_name, google_sheet_tab_read)

dffx.bulk_create_intent_from_dataframe(agent_id=agent_id, tp_df=df, update_flag=True)


