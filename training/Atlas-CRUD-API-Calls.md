# Atlas-MongoDB CRUD API Operations 
### Ref:  https://www.mongodb.com/docs/atlas/app-services/data-api/generated-endpoints/#std-label-data-api-endpoints
import requests
import json
base_url = "https://us-east-1.aws.data.mongodb-api.com/app/data-pcjkv/endpoint/data/v1/action/"

headers = {
  'Content-Type': 'application/json',
  'Access-Control-Request-Headers': '*',
  'api-key': '6BqqTvcMXDHCheoxwsxIcvNXHlECL12l5RYlii8pTymyuyrmb2D5Pv6asmxynBjx',
}

# Find One Row from Index
find_payload = json.dumps({
    "collection": "SPI_COLLECTION",
    "database": "IGN_VECT_DB",
    "dataSource": "Ignaite",
    "projection": {
        "_id": 1
    }
})

#response = requests.request("POST", base_url+"findOne", headers=headers, data=find_payload)
#print(response.text)

# Insert One Row from Index
add_payload = json.dumps({
    "collection": "SPI_COLLECTION",
    "database": "IGN_VECT_DB",
    "dataSource": "Ignaite",
    "document": {"Question": "What are interesting application you are working on?", "Answer": "Navigate to Show Case Page"
    }
})

#response = requests.request("POST", base_url + "insertOne", headers=headers, data=add_payload)
#print(response.text)

# Find One Row by search criteria from Index
query_payload = json.dumps({
    "collection": "SPI_COLLECTION",
    "database": "IGN_VECT_DB",
    "dataSource": "Ignaite",
    "filter": {"Question": "What are interesting application you are working on?" }
})

response = requests.request("POST", base_url + "findOne", headers=headers, data=query_payload)
print(response.text)
