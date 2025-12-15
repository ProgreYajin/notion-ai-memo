from notion_client import Client
import os

notion = Client(auth=os.environ["NOTION_TOKEN"])

DATABASE_ID = os.environ["NOTION_DATABASE_ID"]

response = notion.databases.query(
    database_id=DATABASE_ID,
    filter={
        "and": [
            {
                "property": "自動処理",
                "checkbox": {
                    "equals": True
                }
            },
            {
                "property": "処理状態",
                "select": {
                    "equals": "未処理"
                }
            }
        ]
    }
)

pages = response["results"]
