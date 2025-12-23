# RPG Character Builder (Python)

This project is a simple Python program that creates a character for an RPG-style game.  
It focuses on practicing **input validation**, **functions**, and **string formatting** using basic Python syntax.

The project was built to pass a set of automated tests that strictly check validation order and output format.

---

## Features

- Validates a character name
- Validates character stats (strength, intelligence, charisma)
- Enforces a fixed total of stat points
- Displays character stats using visual dot indicators
- Uses clear error messages when validation fails

---

## Character Rules

### Name Rules
- Must be a string
- Cannot be empty
- Must be 10 characters or fewer
- Cannot contain spaces

### Stat Rules
- All stats must be integers
- Each stat must be between **1 and 4**
- Total stat points must equal **7**

---

## Example Output

```text
ren
STR ●●●●○○○○○○
INT ●●○○○○○○○○
CHA ●○○○○○○○○○
