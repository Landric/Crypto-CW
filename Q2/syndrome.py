from H_matrix import paritycheck_matrix

def check_syndrome(codeword, paritycheck):
    syndrome = [0] * len(codeword)
    
    for p in paritycheck:
        for i in range(len(p)):
            syndrome[i] = (syndrome[i] + (codeword[i] * p[i]))%2
       
    if 1 in syndrome:
        print "Not a codeword"
    else:
        print "Valid codeword"
    
    
if __name__ == "__main__":
    
    #Transpose H to get H^T
    cols = map(list, paritycheck_matrix())

    rows = ['']*6
    for c in cols:
        for i in range(len(c)):
            rows[i] = rows[i] + c[i]
             
    paritycheck = []
    for r in rows:
        paritycheck.append(map(int, r))
        
    #Check codewords
    m1 = "101001111000000000000000000000000000000000000000000000000000000"
    m2 = "100001100000000000000000000000000000000000000000000000001000011"
    m3 = "100001100000000000000000000010000000000000000000000000001000011"

    codewords = [map(int, list(m1)), map(int, list(m2)), map(int, list(m3))]

    for c in codewords:
        check_syndrome(c, paritycheck)