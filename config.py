import os
from dotenv import load_dotenv

# .envファイルを読み込み
load_dotenv()

# 環境変数を取得
NOTION_TOKEN = os.getenv('NOTION_TOKEN')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
NOTION_DATABASE_ID = os.getenv('NOTION_DATABASE_ID')
GITHUB_REPO = os.getenv('GITHUB_REPO')

# 設定の検証
def validate_config():
    """必須の設定が揃っているか確認"""
    required = {
        'NOTION_TOKEN': NOTION_TOKEN,
        'OPENAI_API_KEY': OPENAI_API_KEY,
        'GITHUB_TOKEN': GITHUB_TOKEN,
        'NOTION_DATABASE_ID': NOTION_DATABASE_ID,
        'GITHUB_REPO': GITHUB_REPO
    }
    
    missing = [k for k, v in required.items() if not v]
    
    if missing:
        print(f"❌ 以下の環境変数が設定されていません: {', '.join(missing)}")
        return False
    
    print("✅ すべての設定が揃っています")
    return True

if __name__ == '__main__':
    validate_config()