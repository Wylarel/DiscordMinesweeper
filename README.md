# DiscordMinesweeper
## A minesweeper grid generator for, inter alia, [Discord](https://discord.com/) markdown
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://wylarel.com/mit/)
[![Discord](https://img.shields.io/badge/Chat-Discord-blue)](https://discord.gg/7qvmeh2)
[![Python](https://img.shields.io/badge/Made%20with-Python-orange)](https://www.python.org/)
[![Invite](https://img.shields.io/badge/Discord%20bot-Invite-orange)](https://discord.com/oauth2/authorize?client_id=725682323449839737&permissions=8&scope=bot)

## Demo
You can either easily use the project by importing `minesweeper.py` and ignoring/deleting the other files, or use `demo.py` wich will print the result in the console and in your clipboard.
  
![Demo](https://file.wylarel.com/discordminesweeper.gif)

## Discord Bot
You can freely edit and/or copy `discordbot.py` to make your own minesweeper discord bot, try to give me some credit if you use it tho :wink:
Don't forget to put your [Discord bot token](https://discord.com/developers/applications) in the `TOKEN` text file and never publish it online with your token in the code.

Alternatively, you can [invite my minesweeper discord bot](https://discord.com/oauth2/authorize?client_id=725682323449839737&permissions=8&scope=bot). Commands: `ms help` & `ms new <size> <difficulty>`

## Dependencies
minesweeper.py: `random, numpy`
demo.py: `minesweeper, pyperclip`
discordbot.py: `minesweeper, discord`

## [MIT License](https://wylarel.com/mit/)
```
Copyright (c) 2020 Wylarel

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
