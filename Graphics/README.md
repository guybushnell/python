# Graphics
Simple examples of 2D graphics using pygame

Keywords: `pygame` `2d graphics`

## bouncing-ball.py
Shows a ball appearing to bounce under some kind of gravity. Also make a noise on each bounce.

# Circles
Three examples based around painting circles. Each example includes functions defined in the previous one via Python's import mechanism. That way, we don't need to keep copy/pasting code into each.

Keywords: `circle` `lists` `tuple` `mouse` `time` `random`

## circles1.py
Paint circles at random positions with a short delay between each

## circles2.py
Paint 10 random circles and then erase each one while you continue painting new ones. 
This means you have to remember where each one is! 

- Draw a circle and add it's coordinate to the end of a list
- Erase the circle whose coordinate is at the start of the list
- Delete the first item from the list
- Repeat...

## circles3.py
Paint circles at the current mouse position and then remove each one once it has been on-screen for more than 2 seconds.

- Draw a circle and add it's coordinate and time of drawing to the end of a list
- Erase the circle at the start of the list only if it was drawn was more than 2 seconds ago
- Delete the first item from the list
- Repeat...

# Starbust / Flower
Keywords: `line` `sin` `cos` `radians`

## starburst1.py
Draws a simple fan of yellow lines from a centre-point outwards in a circle.
Wait for keypress, then draw a slighly different image in which the radius of the fan decreases as it rotates.

## starburst2-recursive.py

Demonstrates the use of simple recursion to acheive a complex result.

Keywords: `recursion` `call depth`

- call the function recursive_starburst() to draw a fan centre `(x,y)`, radius `r`
- at the end of each line drawn, the function calls itself using the end-point as the centre of a new, smaller starburst
- keep track of the call-depth to stop the thing going infinitely recursive. i.e. once the depth has reach 3, it doesn't bother calling itself any further.
