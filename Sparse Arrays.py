def matchingStrings(strings, queries):

    '''
    psudo code:
    q = queries
    s = strings
    split q and s
    count for q [0], q[1], q[2]
    if s[i] == q[0,1,2]
    count += 1
    return q[0,1,2]
    '''
    
    return [strings.count(queries[c]) for c in range(len(queries))]
    
