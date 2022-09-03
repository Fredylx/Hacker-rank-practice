def minion_game(string):
    # 
    vowels = 'AEIOU'
    Stuart_score, Kevin_score = 0,0
    length = len(string)
    for i in range(length):
        score = length - i 
        if string[i] in vowels:
            Kevin_score += score
        else:
            Stuart_score += score
    if Stuart_score == Kevin_score:
        print('Draw')
    if Stuart_score > Kevin_score:
        print('Stuart {}'.format(Stuart_score))
    if Stuart_score < Kevin_score:
        print('Kevin {}'.format(Kevin_score))
    

if __name__ == '__main__':
    s = input()
    minion_game(s)
