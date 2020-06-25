# DiscordMinesweeper
## A minesweeper grid generator for, inter alia, [Discord](https://discord.com/) markdown
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://wylarel.com/mit/)
[![Discord](https://img.shields.io/badge/Chat-Discord-blue)](https://discord.gg/7qvmeh2)
[![Python](https://img.shields.io/badge/Made%20With-Python-orange)](https://www.python.org/)

## Demo
You can either easily use the project by importing `minesweeper.py` and ignoring/deleting the other files, or use `demo.py` wich will print the result in the console and in your clipboard.
  
![Demo](https://file.wylarel.com/discordminesweeper.gif)

## Discord Bot
You can freely edit and/or copy the `discordbot.py` file to make your own minesweeper discord bot, try to give me some credit if you use it tho :wink:
Don't forget to replace in placeholder in the `TOKEN` text file with your [Discord bot token](https://discord.com/developers/applications) and never publish it online with your token in the code.

## Dependencies
minesweeper.py: `random, numpy`
demo.py: `minesweeper, pyperclip`
discordbot.py: `minesweeper, discord`

## Example
### Input  
**Text**="\*\*MINESWEEPER\*\*"\nBy Wylarel\n\n\*Size:\* \`%size%x%size%\` | \*Difficulty:\* \`%difficulty%\` | \*Mines:\* \`%mines%\`\n\n\*\*Grid:\*\*\n%grid%\n\n\*\*Solution:\*\*\n||%solution%||"  
**Size**=10  
**Difficulty**=4  
### Output
```
**MINESWEEPER**
By Wylarel

*Size:* `10x10` | *Difficulty:* `4` | *Mines:* `40`

**Grid:**
||1️⃣||||1️⃣||||🔳||🔳||🔳||||2️⃣||||💥||||3️⃣||||💥||||2️⃣||
||💥||||2️⃣||||2️⃣||||3️⃣||||2️⃣||||3️⃣||||💥||||4️⃣||||3️⃣||||💥||
||1️⃣||||2️⃣||||💥||||💥||||💥||||4️⃣||||3️⃣||||💥||||3️⃣||||2️⃣||
||2️⃣||||4️⃣||||5️⃣||||💥||||💥||||💥||||2️⃣||||1️⃣||||3️⃣||||💥||
||💥||||💥||||💥||||6️⃣||||💥||||5️⃣||||2️⃣||||🔳||||3️⃣||||💥||
||4️⃣||||💥||||7️⃣||||💥||||💥||||💥||||2️⃣||||1️⃣||||3️⃣||||💥||
||4️⃣||||💥||||💥||||💥||||💥||||💥||||3️⃣||||2️⃣||||💥||||3️⃣||
||💥||||💥||||5️⃣||||4️⃣||||4️⃣||||3️⃣||||💥||||3️⃣||||3️⃣||||💥||
||3️⃣||||4️⃣||||4️⃣||||💥||||3️⃣||||2️⃣||||3️⃣||||💥||||3️⃣||||1️⃣||
||💥||||2️⃣||||💥||||💥||||💥||||1️⃣||||2️⃣||||💥||||2️⃣||||🔳||

**Solution:**
||1️⃣1️⃣🔳🔳🔳2️⃣💥3️⃣💥2️⃣
💥2️⃣2️⃣3️⃣2️⃣3️⃣💥4️⃣3️⃣💥
1️⃣2️⃣💥💥💥4️⃣3️⃣💥3️⃣2️⃣
2️⃣4️⃣5️⃣💥💥💥2️⃣1️⃣3️⃣💥
💥💥💥6️⃣💥5️⃣2️⃣🔳3️⃣💥
4️⃣💥7️⃣💥💥💥2️⃣1️⃣3️⃣💥
4️⃣💥💥💥💥💥3️⃣2️⃣💥3️⃣
💥💥5️⃣4️⃣4️⃣3️⃣💥3️⃣3️⃣💥
3️⃣4️⃣4️⃣💥3️⃣2️⃣3️⃣💥3️⃣1️⃣
💥2️⃣💥💥💥1️⃣2️⃣💥2️⃣🔳||
```

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
