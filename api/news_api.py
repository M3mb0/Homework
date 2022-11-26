import requests
import pathlib

URL = "https://newsapi.org/v2/everything?q=nato&apiKEY=4efd8d5d0eba43e6b9fd9c7a9f623a84"
ROOT = pathlib.Path(__file__).parent
NEWS_DIR = ROOT / "news"

try:
    NEWS_DIR.mkdir(exist_ok=True)
except OSError:
    print("Error")


resp = requests.get(URL)

data = resp.json()
# print(data)
articles = data.get("articles")
# print(articles)
for ele in articles:
    print(ele)
    if ele.get("source") and ele["source"].get("id"):
        source_dir = NEWS_DIR / ele["source"]["id"]
        source_dir.mkdir(exist_ok=True)
        with open(source_dir / f"{ele['title']:30s}.txt", "w") as f:
            f.write(ele['content'])
