# This is my autoclicker for a certain game:

The purpose of this autoclicker is to execute a simple task many, many times. 

But the game which I made this for has very good bot detection so i've tried a lot of things to get around that

First it will try and locate the client window by comparing it with a screenshot (CV2, dir has to be changed to location of your
screenshot) and focus to that window.

Then it will determin the position of the two icons it has to click. It will then select a random pixel on that icon and
move towards it in a human-like(Randomised Bezier-curve) way with random intervals.

The script can be stopped by pressing F12.

