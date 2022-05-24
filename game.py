def get_idx(list,*indexes):
    s=[]
    for index in indexes:
        s.append(list[index])
    return s
def check_game(game):
    s = [set(game[0:3]),
    set(game[3:6]),
    set(game[6:9]),
    set(get_idx(game,0,4,8)),
    set(get_idx(game,2,4,6))]
    s=s+list(map(
        lambda x:set(get_idx(game,x,3+x,6+x)),
        range(3)))
    if {'X'}in s:
        return 'X'
    elif {'O'} in s:
        return 'O'
    elif None not in game:
        return 0

def print_game(game):
    for i in range(3):
        g=list(map(lambda x:'—'if x==None else x,
        game))
        print('|'.join(g[i*3:3+(i*3)]))

opponent={
    'X':'O',
    'O':'X'}
def move(game,idx,player):
    g = game.copy()
    if game[idx]==None:
        g[idx]=player
    return g

