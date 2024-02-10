# MongoDB Management

### Connection String:
mongodb+srv://SPIDEV:PWD@ignaite.mongocluster.cosmos.azure.com/?tls=true&authMechanism=SCRAM-SHA-256&retrywrites=false&maxIdleTimeMS=120000

### Python Connectivity
```
from pymongo import MongoClient 
import urllib.parse 
from easygui 
import passwordbox 
mongo_username = urllib.parse.quote_plus("SPIDEV") 
password = passwordbox("Enter password:") 
mongo_password = urllib.parse.quote_plus(password) 
mongo_host = "ignaite.mongocluster.cosmos.azure.com" 
mongo_database = "quickstartDB" 
client = MongoClient(f"mongodb+srv://{mongo_username}:{mongo_password}@{mongo_host}/{mongo_database}") 
db = client[mongo_database] collection_names = db.list_collection_names() 
print(f"Collections in the database: {collection_names}") 
client.close()
```

References: 
Vector Index: https://python.langchain.com/docs/integrations/vectorstores/azure_cosmos_db
Python Connectivity: 
