import os
from notion_client import Client

notion = Client(auth=os.environ["NOTION_TOKEN"])

DATABASE_ID = "あなたのDB_ID"

response = notion.databases.query(
    database_id=DATABASE_ID,
    filter={
        "property": "AI処理済み",
        "checkbox": {"equals": False}
    }
)

print(f"未処理メモ数: {len(response['results'])}")
