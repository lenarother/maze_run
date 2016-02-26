# Review by MR 26.03.16
# Nice to have such a short script for the beginnging
# I would rather go for full words instead of abbreviations for clarity
# This is what pylint says: Your code has been rated at -4.00/10
# Could not execute because of missing file.

from pygame import image, Rect

bg = image.load('bg.xpm')
ex = image.load('explo.xpm')

bg.blit(ex, Rect((15,15, 0,0)), Rect((0,0,32,32)))

image.save(bg, 'merged.png')
