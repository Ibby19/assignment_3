# textpoker.py
# This program is a simple way to visually see if our poker app works

from pokerapp import PokerApp
from textpoker import TextInterface

inter = TextInterface()
app = PokerApp(inter)
app.run()
