import requests
import datetime
from config import NOTION_API_KEY, NOTION_DATABASE_ID

NOTION_API_URL = "https://api.notion.com/v1"
NOTION_VERSION = "2022-06-28"

HEADERS = {
    "Authorization": f"Bearer {NOTION_API_KEY}",
    "Notion-Version": NOTION_VERSION,
    "Content-Type": "application/json"
}

def get_today_topic():
    """
    Query the Notion database for today's topic based on the 'Date' property.
    Returns (page_id, topic_string) or (None, None) if not found.
    """
    today = datetime.date.today().isoformat()
    url = f"{NOTION_API_URL}/databases/{NOTION_DATABASE_ID}/query"
    payload = {
        "filter": {
            "property": "Date",
            "date": {"equals": today}
        }
    }
    resp = requests.post(url, headers=HEADERS, json=payload)
    resp.raise_for_status()
    results = resp.json().get("results", [])
    if not results:
        return None, None
    page = results[0]
    page_id = page["id"]
    # Assume the topic is in a property called 'Topic' (type: title or rich_text)
    props = page["properties"]
    topic_prop = props.get("Topic")
    if not topic_prop:
        return page_id, None
    if topic_prop["type"] == "title":
        topic = "".join([t["plain_text"] for t in topic_prop["title"]])
    elif topic_prop["type"] == "rich_text":
        topic = "".join([t["plain_text"] for t in topic_prop["rich_text"]])
    else:
        topic = None
    return page_id, topic

def update_research_output(page_id, content):
    """
    Update the 'Research Report' rich_text property of the given page.
    """
    url = f"{NOTION_API_URL}/pages/{page_id}"
    payload = {
        "properties": {
            "Research Report": {
                "rich_text": [
                    {"type": "text", "text": {"content": content}}
                ]
            }
        }
    }
    resp = requests.patch(url, headers=HEADERS, json=payload)
    resp.raise_for_status() 