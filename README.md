# Notion Research Bot

Automate daily research reports in Notion using OpenAI GPT-4o and GitHub Actions.

## 🚀 What does this bot do?

- **Every day:**
  1. Pulls today's topic from a Notion database (filtered by a `Date` property).
  2. Sends the topic to OpenAI's GPT-4o for a deep, evidence-based research report.
  3. Inserts the resulting report back into the same Notion page under the `Research Report` property.
  4. Runs automatically via GitHub Actions on a daily schedule (9:30am ET).

---

## 🗂️ Project Structure

```
notion-research-bot/
├── .github/
│   └── workflows/
│       └── run_daily.yaml
├── config.py
├── notion_utils.py
├── openai_utils.py
├── main.py
└── README.md
```

---

## 📝 Notion Database Requirements

Your Notion database **must** have these properties:
- `Date` (type: Date): The date for which the topic should be researched.
- `Topic` (type: Title or Rich Text): The research topic for the day.
- `Research Report` (type: Rich Text): Where the bot will write the generated report.

> **Tip:** Only the first page found for today's date will be processed each day.

---

## ⚙️ Setup & Configuration

### 1. **OpenAI & Notion API Keys**
- Get your [OpenAI API key](https://platform.openai.com/account/api-keys)
- Get your [Notion integration token](https://developers.notion.com/docs/create-a-notion-integration)
- Share your Notion database with your integration
- Find your Notion database ID (from the URL)

### 2. **GitHub Actions Secrets**
Add these secrets to your GitHub repository:
- `NOTION_API_KEY`
- `NOTION_DATABASE_ID`
- `OPENAI_API_KEY`

> The workflow will dynamically populate `config.py` with these values at runtime.

---

## 🏃‍♂️ How it Works (CI/CD)

- The workflow in `.github/workflows/run_daily.yaml` runs every day at 9:30am ET.
- It installs dependencies, populates `config.py` from secrets, and runs `main.py`.
- The script fetches today's topic, generates a report, and updates Notion.

---

## 🖥️ Local Development

1. Install dependencies:
   ```bash
   pip install openai requests
   ```
2. Manually fill in `config.py` with your API keys and model (e.g., `gpt-4o`).
3. Run:
   ```bash
   python main.py
   ```

---

## 🛠️ Troubleshooting

- **No topic found for today:** Ensure your Notion database has a page with today's date in the `Date` property.
- **API errors:** Double-check your API keys, database ID, and property names.
- **Nothing written to Notion:** Make sure your integration has access to the database and the property names match exactly.

---

## 📄 License

MIT License. Feel free to use and adapt! 