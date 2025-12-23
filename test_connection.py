from notion_client import Client
import openai
from github import Github
from config import *

def test_notion():
    """Notion接続テスト"""
    print("📝 Notion接続テスト中...")
    try:
        notion = Client(auth=NOTION_TOKEN)
        db = notion.databases.retrieve(database_id=NOTION_DATABASE_ID)
        db_title = db['title'][0]['plain_text'] if db['title'] else 'Database'
        print(f"  ✅ Notion接続成功: {db_title}")
        return True
    except Exception as e:
        print(f"  ❌ Notion接続失敗: {e}")
        return False

def test_openai():
    """OpenAI接続テスト"""
    print("🤖 OpenAI接続テスト中...")
    try:
        client = openai.OpenAI(api_key=OPENAI_API_KEY)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Hello"}],
            max_tokens=5
        )
        print("  ✅ OpenAI接続成功")
        return True
    except Exception as e:
        print(f"  ❌ OpenAI接続失敗: {e}")
        return False

def test_github():
    """GitHub接続テスト"""
    print("🐙 GitHub接続テスト中...")
    try:
        g = Github(GITHUB_TOKEN)
        repo = g.get_repo(GITHUB_REPO)
        print(f"  ✅ GitHub接続成功: {repo.full_name}")
        return True
    except Exception as e:
        print(f"  ❌ GitHub接続失敗: {e}")
        return False

if __name__ == '__main__':
    print("\n" + "="*50)
    print("🔍 接続テストを開始します")
    print("="*50 + "\n")
    
    results = {
        'Notion': test_notion(),
        'OpenAI': test_openai(),
        'GitHub': test_github()
    }
    
    print("\n" + "="*50)
    if all(results.values()):
        print("🎉 すべての接続テストに成功しました！")
        print("次はメインスクリプトを実行できます。")
    else:
        failed = [k for k, v in results.items() if not v]
        print(f"❌ 以下の接続に失敗しました: {', '.join(failed)}")
        print("\n🔧 確認事項:")
        print("  1. .envファイルの内容が正しいか")
        print("  2. トークンが有効か")
        print("  3. インターネット接続があるか")
    print("="*50 + "\n")