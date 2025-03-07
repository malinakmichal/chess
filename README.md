# Chess  

## 1. Introduction  
This work focuses on the implementation of artificial intelligence in the game of chess. It is a rather complex problem due to the vast number of possible moves. It is not feasible to evaluate all possible solutions and select the best one, as after just four moves, there are approximately 168,421 possible combinations, and this number grows exponentially. A perfect strategy for this game has not yet been found.  

## 2. Methods and Algorithms  
I used the minimax algorithm together with alpha-beta pruning. The score for the minimax algorithm was calculated using a heuristic function.  

### 2.1 Minimax  
The algorithm evaluates all possible moves using recursion up to a depth of 4 and selects the one most advantageous for the player. At each level of recursion, the selection alternates between maximizing and minimizing the evaluation score, depending on whose turn it is.  

### 2.2 Heuristic Function  
The function evaluates the current positions of the pieces on the board and determines which player has the advantage. The value is calculated as the sum of the piece values for one color minus the sum of the piece values for the other color, where each piece has its own value based on its capabilities. Additional evaluation criteria are introduced, such as the distance of a pawn from its starting position or the positioning of pieces around the center of the board.  

### 2.3 Alpha-Beta Pruning  
The algorithm keeps track of alpha and beta values and discards branches that do not improve the move evaluation. This pruning significantly reduces the number of positions that need to be examined, thereby improving time complexity. This allows for deeper recursion and, consequently, more accurate moves.  

## 3. Results  
The artificial intelligence we developed performs better than an average player. Further improvements could involve enhancing the heuristic function and incorporating well-known opening sequences. To achieve even greater improvements, a different approach, such as neural networks, would be required.



## 4. Running locally

``` sh
    conda create -n chess python=3.9 -y
```
``` sh
    conda activate chess
```
``` sh
    pip install -r requirements.txt
```
``` sh
    python main.py
```
