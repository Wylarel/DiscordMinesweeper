import minesweeper
import pyperclip

text = (
    "**MINESWEEPER**"
    "\nBy Wylarel\n"
    "\n*Size:* `{size}x{size}` | *Difficulty:* `{difficulty}` | *Mines:* `{mines}`\n"
    "\n**Grid:**\n{grid}\n"
    "\n**Solution:**\n||{solution}||"
)

OUTPUT = minesweeper.main(text=text, size=10, difficulty=3)  # Get the output with the default
print(OUTPUT)  # Print the output in the console
pyperclip.copy(OUTPUT)  # Copy the output in the clipboard
