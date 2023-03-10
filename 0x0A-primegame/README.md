# A. Prime Game
### Maria and Ben are playing a game. Given a set of consecutive integers starting from 1 up to and including n, they take turns choosing a prime number from the set and removing that number and its multiples from the set. The player that cannot make a move loses the game.
---

- Prototype: def isWinner(x, nums)
- where x is the number of rounds and nums is an array of n
- Return: name of the player that won the most rounds
- If the winner cannot be determined, return None
- You can assume n and x will not be larger than 10000
- You cannot import any packages in this task

## Pseudocode  Code
```sql
    1. Define a function called isWinner1 that takes two arguments: x and nums.
    2. If x equals zero or the length of nums equals zero, return None.
    3. Create a dictionary called players with keys "maria" and "ben" and initialize both values to 0.
    4. Loop over a range of x.
    5. Set the currentPlayer variable to "maria".
    6. Create a list called values that contains all integers from 1 up to nums[i].
    7. If values contains only 1 and no other integers, increment players["ben"] by 1.
    8. Loop over each integer x in values[1:].
    9. Set the variable num to x.
    10. Set the variable multiple to num squared.
    11. If num is prime, remove num and multiple from the values list (if they exist) and increment players[currentPlayer] by 1.
    12. Set the currentPlayer variable to "ben" if it was previously "maria", and vice versa.
    13. If the currentPlayer is "maria" and players[currentPlayer] is greater than 0, decrement players[currentPlayer] by 1.
    14. If players["maria"] is greater than players["ben"], return "Maria".
    15. If players["ben"] is greater than players["maria"], return "Ben".
    Otherwise, return None.

```
