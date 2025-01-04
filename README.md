# Fantasy Football Draft Bot

## Project Description

This Fantasy Football Draft Bot is an automated solution to assist users during live fantasy football drafts. By integrating ranking systems, real-time data scraping, and AI decision-making, the bot selects the best available players based on predefined constraints and strategy.

The bot analyzes top-ranked players, evaluates current team composition, and uses intelligent logic to make optimal draft picks. It interacts directly with fantasy football platforms to execute selections in real time.

## Tech Stack

- **Python**: Core programming language.
- **Selenium**: For web scraping and automating interactions with the fantasy football website.
- **LangChain**: Provides chat model interaction for generating intelligent player recommendations.
- **LlamaIndex**: Handles vector indexing for storing and querying draft-related data.
- **OpenAI GPT-3.5-turbo**: Powers the decision-making logic for selecting players.

## Features

- **Real-Time Drafting**: Uses Selenium to interface with fantasy football platforms and make draft picks.
- **Player Ranking System**: Dynamically updates available players and ranks them based on position, stats, and bye weeks.
- **AI-Powered Recommendations**: GPT evaluates the best player options based on constraints like position caps and team needs.
- **Customizable Constraints**: Allows users to enforce position-based roster limits.

## Setup Guide

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repo/fantasy-draft-bot.git
   cd fantasy-draft-bot
   ```

3. **Set up environment variables**:
   - Create a `.env` file and add your OpenAI API key:
     ```
     API_KEY=your_openai_api_key
     ```

4. **Prepare data**:
   - Place the player rankings CSV file (`Ranking.csv`) in the root directory.

5. **Run the bot**:
   ```bash
   python app.py
   ```

6. **Optional**: Configure your Selenium WebDriver (e.g., ChromeDriver or SafariDriver).

## Challenges Faced

The most challenging aspect of this project was integrating real-time data scraping with AI decision-making. Handling asynchronous events during live drafts required careful coordination between Selenium and the GPT-based logic. By introducing robust error handling and ensuring the AI logic could make decisions in milliseconds, these issues were successfully resolved.

## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests.
