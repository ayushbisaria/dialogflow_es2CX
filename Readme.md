# Dialogflow Es To CX Migration

- Follow Official [Documentation](https://cloud.google.com/dialogflow/cx/docs/how/migrate) for Dialogflow ES to CX migration.
- [Migration Tool](https://cloud.google.com/dialogflow/cx/docs/how/migrate#tool-code) mentioned in above documentation needs some updates based on edge cases like - intents annotation metadata is missing for source agent.
- This is where we can use [custom_es2cx_main.go](https://github.com/ayushbisaria/dialogflow_es2CX/blob/main/custom_es2cx_main.go) which handles edge cases like this.
- Usage of this tool is mentioned [here](https://cloud.google.com/dialogflow/cx/docs/how/migrate#run_the_migration_tool)
- There are additional automation code is mentioned under directory [intent_mgmt_n_cleanup](https://github.com/ayushbisaria/dialogflow_es2CX/tree/main/intent_mgmt_n_cleanup) which can be used for intent management and cleanup.
  - [delete_intents_dfcx.py]  - can be used for bulk deleting unused intents
  - [intents_to_sheets.py]    - can be used to transfer all source intents to sheets for intent labelling task
  - [sheets_to_cx_intents.py] - can be used to create all intents and its related annotated data mentioned in sheets to CX 
  - [recreate_testcases_dfcx.py] - Can be used to bulk edit test cases in CX.