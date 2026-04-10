#implement the minimax search algorithm for 2-player games. You may use a game tree with 3piles

tree = [
    [[5,2],[9,6]],
    [[1,3],[-1,0]]
]

def minimax(node,depth,isMax):
    if depth == 3:
        return node
    vals = [minimax(child, depth+1, not isMax) for child in node]
    return max(vals) if isMax else min(vals)

print("bets value:", minimax(tree, 1, True))