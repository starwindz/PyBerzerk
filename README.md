**PyBerzerk**
===================
Clone of the 1980s **Berzerk** arcade game. 
Forked from [flyingthing/PyBerzerk](https://github.com/flyingthing/PyBerzerk) written by TerryO.
Bugs fix and features improvement by starwindz

**SCREENSHOTS:**
<table>
 <tr>
  <td><img src="./Screenshots/Gameplay3.png" alt="GamePlay3" /></td>
  <td><img src="./Screenshots/Gameplay2.png" alt="GamePlay2" /></td>
 </tr>
 <tr>
  <td><img src="./Screenshots/GamePlayDemo.gif" alt="GamePlayDemo" /></td>
  <td><img src="./Screenshots/HighScore.png" alt="HighScore" /></td>
 </tr>
</table>

----------

**REQUIREMENTS:**
Before running the game, please make sure you have [Python v3.x](http://www.python.org/download/) installed. You will also need to install the latest version of [PyGame](http://www.pygame.org/download.shtml). You can install PyGame too by entering `pip install pygame` on console window.

**GAME PLAY:**
Use the **ARROW** key(s) to navigate the player through a maze filled with robots who have an extreme dislike for humanoids.  Hold the **LEFT CONTROL** and press **ARROW** key(s) to fire player's laser weapon. The player can be killed by being blasted by a robot, running into a robot, exploding robot shrapnel, coming into contact with the electrified maze walls or being touched by Evil Otto(bouncing smiley face).

<table>
 <tr>
  <th align="left">Game Controls</th>
  <th align="left">Player/Laser</th>
 </tr>
 <tr>
  <td><kbd>&larr;</kbd> LEFT ARROW</td>
  <td>Move the player left</td>
 </tr>
  <tr>
  <td><kbd>&rarr;</kbd> RIGHT ARROW</td>
  <td>Move the player right</td>
 </tr>
  <tr>
  <td><kbd>&uarr;</kbd> UP ARROW</td>
  <td>Move the player up</td>
 </tr>
  <tr>
  <td><kbd>&darr;</kbd> DOWN ARROW</td>
  <td>Move the player down</td>
 </tr>
  <tr>
  <td><kbd>LEFT CONTROL</kbd></td>
  <td>Fire laser in direction of ARROW key(s)</td>
 </tr>
</table>

> **Helpful Hints:**
> 
> - Robots can destroy themselves by running into walls or each other, shooting each other, or colliding with Evil Otto.
> - Robot lasers cannot penetrate the maze walls, use this to your advantage.
> - Evil Otto is impervious to lasers, robots or the electrified maze walls.
> - If player nears an electrified maze wall that section of the wall changes color.
> - Each robot destroyed is worth 50 points,  bonus points are earned by destroying all robots. A new life is awarded at 5,000 points.

**Have fun!**
Critiques regarding game play, bugs, glitches are most welcome.

-----------------------------------------------------------------------------
Please see [the issue list](https://github.com/starwindz/PyBerzerk/issues) for issues and features to be developed.

#### References
1. https://en.wikipedia.org/wiki/Berzerk_(video_game)
1. http://www.robotron2084guidebook.com/home/games/berzerk/
