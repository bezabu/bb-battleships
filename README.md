BATTLESHIPS


![Battleships Command line splash page](assets/images/battleships_splash.jpg)

BATTLESHIPS is a digital reimagining of the classic strategy guessing game. It runs in the Code Institute mock terminal on Heroku.

The goal of the game is to guess the locations of the computer player's warships before it can guess yours. Players take turns calling shots and those locations are recorded on two grids.

The game can be accessed [here](https://bb-battleships-f22f01c35958.herokuapp.com/)


## How to Play


- Each player first chooses the locations of their warships, and then take turns calling shots
- During the player's turn, they are prompted to enter a grid coordinate to guess. If the coordinate chosen contains an enemy warship, a hit is recorded on the grid and the warship is destroyed. If the grid coordinate contains no enemy warship then a miss is recorded as a blue x.
- The game ends when one player has eliminated all of their oponent's warships

## Features

![Starting inputs; name, board size](assets/images/starting_parameters.jpg)

- A splash 'page' welcomes the player and prompts them to enter their name
- The user can choose between 3 sizes of game grid; 5x5, 6x6 or 7x7

![Ship placement](assets/images/ship_placement.jpg)

- The user can choose to place their ships themselves by entering coordinates or opt to place them randomly. Ships are displayed in yellow to differentiate between the setup phase and the guessing phase.

![Game play](assets/images/gameplay.jpg)

- A grid is displayed in text showing the player's ships and all previous computer guesses. If the player's ships have been hit, they are displayed in red. Missed shots are shown in blue.

- A second grid is shown with the same information minus the location of the computer player's ships, which only appear once they have been hit.

- Underneath the grid, the results of both player's previous guesses are shown. Hits are shown in red, misses in blue.

- Any error messages include the grids so that in the event of an invalid input, the previous guesses text is replaced by the error message.

- The user can enter guesses using the command line. The expected format is given as an example.

- When one player has hit all of the other player's warships, the user is asked if they want to play again.

### Input validation

- All user inputs can be entered in upper or lower case, the game automatically converts all inputs into upper case as part of the validation.

![Yes/No](assets/images/yes_no_input.jpg)

- Yes/No inputs such as the choice of random ship placement or to play again are tested so that only an input containing Y but not N will count as a yes input and vice versa. If the user inputs neither Y or N then they will be prompted to try again.

![Invalid coordinates entered](assets/images/error_coords.jpg)

- Grid coordinate inputs are expected in letter-number format, for example A1, B2 and so on.
  - Inputs that are not exactly 2 characters are rejected
  - Inputs that are number-letter (1A, 2B etc) are rejected
  - Inputs that are number-number (11, 22 etc) are rejected
  - Inputs that are letter-letter (AA, BB etc) are rejected
  - Inputs that are outside of the grid size (A0, B9 etc) are rejected
  - Inputs that have already been successfully entered(previous guesses or already placed ships) are rejected
- All rejected inputs are handled through an except block which also prints the grid. As this all takes place in a while loop it prevents lines building up underneath the grid, pushing it out of view

![Name Validation](assets/images/name_validation.jpg)

- The name entered at the beginning of the game is limited to a maximum of 30 characters so that it does not result in a new line.

### Data Model

The GAME class stores information like board size, player guesses and warship locations.

Warship locations are stored as grid references. These are strings 2 characters long; the first character is an upper case letter, the second character is a number ( A1, B2 etc)

Previous guesses and warship locations are stored as lists of grid references in the GAME class. When validating guesses, the input is compared to these lists.

["A1", "B2"]

When randomly generating locations or checking if inputs are within the bounds of the game, each character is converted to an integer to compare against the grid.

Characters to display on the game boards are stored in arrays, which are updated when guesses are made.
The x and y values are compared to the appropriate list to determine what character to display ("@", "X" or " ").

When displaying each player's game boards, for loops are used to print the characters ─, │, ┌, ┐, └, ┘, ├, ┤, ┬, ┴ and ┼ to draw a grid over several lines. During iteration:
- the board label list is used to provide values for the horizontal axis labels.
- the appropriate array is checked to determine the character to display and what colour it should be.



# Technologies

- Python was used as the programming language to make the game.
- The [Random](https://docs.python.org/3/library/random.html#random.Random) Python module has been used to provide randomly generated numbers
- GitHub has been used to store the code, images and other content.
- Heroku was used to deploy the game to the web.
- Git was used for version control, pushing contents to github.
- Codeanywhere was used as IDE.
- [CI Python Linter](https://pep8ci.herokuapp.com/) was used to test Python code.
- Paint.NET was used to edit images for the readme.
- [TinyPNG](https://tinypng.com/) was used to optimise images for the readme

# Testing

# Deployment

The following steps were taken to deploy:
- Go to [Heroku](https://heroku.com/), click 'New', 'create new app'
- Set the App name, choose Europe as region
- In Settings, set a new config var with a key of PORT and a value of 8000
- In Settings, add buildpacks Python and NodeJS in that order
- In Deploy, set deployment method to GitHub
- Connect to GitHub and search for the correct repository
- Ensure deploment is from main branch
- Enable Automatic Deploys
- Click Deploy Branch
- The deployed app can be found [here](https://bb-battleships-f22f01c35958.herokuapp.com/)

# Features to implement

- Seperate name from game
- more sophisticated coordinate validation
- ships that span more than one cell

# Credits

Instructions on how to use ANSI escape codes to set the colour of the text were taken from [here](https://www.geeksforgeeks.org/how-to-add-colour-to-text-python/).