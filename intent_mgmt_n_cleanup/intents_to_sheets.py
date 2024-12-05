from dfcx_scrapi.core.intents import Intents
from dfcx_scrapi.tools.dataframe_functions import DataframeFunctions

creds_path = '<PATH_TO_CRED.json>'
agent_id = 'projects/<PROJECT_NAME>/locations/<LOCATION>/agents/<AGENT_ID>'

google_sheet_name = '<SHEET_NAME>' #Make sure service account mentioned in credential json have access to sheet
google_sheet_tab_read = '<SHEET_TAB_NAME>'

i = Intents(creds_path=creds_path)
dffx = DataframeFunctions(creds_path=creds_path)

df = i.bulk_intent_to_df(agent_id,mode="advanced")
dffx.dataframe_to_sheets(google_sheet_name, google_sheet_tab_read, df)
