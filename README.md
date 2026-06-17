# Success-Snake-Game
This is a simple Snake game built with Python and Pygame.

It demonstrates several fundamental programming concepts. It introduces variables, data types, loops, conditional statements, lists, functions, keyboard input handling, collision detection, object manipulation, and basic game development principles. 

The game allows a snake to move around the screen, eat food to grow longer, keep track of a score, detect collisions with itself, and display a game-over screen. Through this project, a beginner can learn how Python programs are structured and how different programming concepts work together to create an interactive application.

<h2>Python concepts used</h2>
<ul>
  <li> 
    <h4>Variables</h4>
    <p>An example of a variable in the Snake game is WIDTH = 600 and HEIGHT = 400. Variables store the width and height of the game window. Variables allow data to be stored and reused throughout the program, making the code more organized, flexible, and easier to modify. If the game window size needs to be changed, only the variable values need to be updated rather than multiple lines of code.</p>
    
```python
WIDTH = 600
HEIGHT = 400
```
  </li>
  
  <li> 
    <h4>Lists</h4>
    <p>An example of a list in the Snake game is snake_list = []. This list keeps track of the snake's body positions as it moves. Lists can store multiple values in one variable and can be changed during program execution. In this game, the list is updated continuously to show the snake's movement and growth whenever it eats food. Using a list helps organize and manage the snake's body efficiently.</p>
    
```python
snake_list = []
```
  </li>
  
  <li>
    <h4>Functions</h4>
    
```python
len(snake_list)

append()
```
     
   <p>An example of a function in the Snake game is len(snake_list). Functions are reusable blocks of code that perform specific tasks. The len() function is used to determine the number of items in a list. In this game, it helps track the length of the snake by checking how many body segments are stored in snake_list. Another exammple is append() which adds a new snake segment to snake Functions make programs more efficient by reducing repetition and allowing tasks to be performed with a single command.</p>
  </li>
  
  <li>
  <h4>Data Types</h4> 
    
```python
    x = WIDTH // 2
    snake_list = []
    running = True
```
   <p>Different data types are used throughout the game. Integers store numerical values such as positions and dimensions, lists keep track of the snake's body segments, and Boolean values control game states such as whether the game is running or has ended.</p>
  </li>
  
</ul>



