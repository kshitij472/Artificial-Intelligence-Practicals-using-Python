#implement the minimax search algorithm for 2-player games. You may use a game tree with 3piles

t
tree = [
    [[2,4],[3,8]],
    [[0,2],[3,-2]]
]

def minimax(node, depth, isMax):
    if depth == 3:
        return node
    vals = [minimax(child,depth+1,not isMax)for child in node]
    return max(vals) if isMax else min(vals)

print("best value:",minimax(tree,1,True))