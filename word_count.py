"""Word count program"""
import sys
import stdarray
import stdio

word_count = 0
while not stdio.isEmpty():
    text = stdio.readString()
    word_count += 1
    if text == "'s":
        word_count += 1
stdio.write(word_count)