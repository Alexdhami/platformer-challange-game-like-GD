# platformer-challange-game-like-GD

This is a basic 2D platformer game created using the Pygame library in Python. The goal is to navigate a series of increasingly challenging levels by avoiding obstacles.

## Features

* **Basic Player Movement:** Move left and right using the 'A' and 'D' keys.
* **Jumping:** Jump by pressing the mouse button, Spacebar, or 'W' key while on the ground.
* **Level Progression:** The game features multiple levels with different layouts and increasing difficulty.
* **Triangle Spikes:** Avoid triangle spikes placed on the ground, which cause the player to restart the level upon contact.
* **Death Counter:** Tracks the number of times the player has died.
* **Moving Platforms:** Some levels introduce moving black platforms that affect the player's gravity.
* **Score Display:** Shows the current level and the death count.

## How to Run

1.  **Prerequisites:**
    * Python 3.x installed on your system.
    * Pygame library installed. You can install it using pip:
        ```bash
        pip install pygame
        ```
2.  **Download the Code:** Download the `main.py` file (or any other relevant Python files and the `triangle.png` image) from this repository.
3.  **Run the Game:** Open your terminal or command prompt, navigate to the directory where you saved the files, and run the game using:
    ```bash
    python main.py
    ```

## Game Controls

* **A:** Move left
* **D:** Move right
* **Mouse Button (Left Click):** Jump
* **Spacebar:** Jump
* **W:** Jump

## Game Assets

* `triangle.png`: Image file for the triangle spike obstacle.
* `Pixeltype.ttf`: Font file used for displaying the score and death count.

**Note:** Make sure these asset files are in the same directory as your `main.py` file.
