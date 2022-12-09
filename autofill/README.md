# Advent of code setup

Jumpstart your Advent of Code experience. Automate input downloads and easily create templates for your solutions, so you can focus on solving the challenges.

## Setup
Run `make setup`, this will create the `session.cookie` file, please remember to fill this with your session cookie to auto-download inputs, and add a newline after it, just in case.
To find it on Chrome: right-click, inspect, Application tab, Storage, Cookies, session.
If your repository is public add the `session.cookie` file to your `.gitignore`

Go to YEAR and fill in the year you're working on.

## Creating a new solution

```make new``` creates a new file for today, it checks for the directories in `/YEAR/` and creates the "next int" one. On the first run it will create `/YEAR/01`, later `/YEAR/02`, and so on.

## Pretty README
`make readme` creates a cool `README.md` file with a list of the solutions in the source directory, with working links. Note that this original readme will be overwritten.
If you want to use this, please edit `src/utils/build_md.py` with the correct repository link.
Also, the `parse` method could be extended to display what you want for each solution. For instance, by uncommenting line 8, and renaming your files like `DAY_Cool_Problem_name.py`, you will get a list entry like `DAY. Cool Problem name`.

## Solving other years
This repo can be used to setup past years aswell, the only downside is that you need to change the `YEAR` file.
