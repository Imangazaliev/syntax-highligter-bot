# Syntax Highlighter Bot

A Telegram bot for generating screenshots with highlighted code.

## How it works

There are two services - `bot.py` and `screenshot-service.js`.

- `bot.py` - bot written in [AIOgram](https://github.com/aiogram/aiogram)
- `screenshot-service.js` - a service for generating screenshots

1. Bot requests the screenshot service to generate an image with code.
2. Screenshot service in turn does:
   1. Highlights a code via [highlight.js](https://highlightjs.org)
   2. Load generated HTML and takes  a screenshot via Puppeteer (headless Chrome driver)
   3. Saves generated screenshot to a directory and returns it's path.
3. Bot sends generated image to a user.

## Quick start

1. Install dependencies:
```bash
# Python dependencies
$ poetry install
# JavaScript dependencies
$ npm i
```

2. Copy `.env.example` to `.env`:
```bash
$ cp .env.example .env
```

3. Specify a bot token in `.env`.
4. Execute services:
```bash
# execute bot
$ poetry run bot.py
# execute bot (in another terminal)
$ node screenshot-service.js
```

If you are running a bot locally don't forget to start Telegram Bot API.

## Development

For local development use [Telegram Bot API](https://github.com/tdlib/telegram-bot-api).

## Roadmap

- Rate limiting
- Use queue to limit the number of pages generated in parallel 
- Containerize
