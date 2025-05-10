from notion_utils import get_today_topic, update_research_output
from openai_utils import generate_report


def main():
    page_id, topic = get_today_topic()
    if not page_id or not topic:
        print("No topic found for today. Exiting.")
        return
    print(f"Today's topic: {topic}")
    report = generate_report(topic)
    print("Generated research report. Updating Notion...")
    update_research_output(page_id, report)
    print("Research report updated in Notion.")

if __name__ == "__main__":
    main() 