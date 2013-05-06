import string

def load_ciphertext(filename):
    in_file = open(filename, 'r')
    return bytearray.fromhex(in_file.read())
    
def decrypt(known_key, suspected_key):
    out_file = open("plain1.txt", 'w')
    ciph = load_ciphertext("Q1.txt")
    plain = bytearray()

    known_key.append(suspected_key)
    
    #Decrypt using either the suspected key, or just
    #ignore every fourth byte all together
    key_count = 0
    for i in range(len(ciph)):        
        plain.append(ciph[i] ^ known_key[key_count])
        
        #if key_count != 3:
        #    plain.append(ciph[i] ^ known_key[key_count])
        #else:
        #    plain.append("?")
            
        key_count = (key_count + 1)%4
        
    out_file.write(''.join(map(chr, plain)))

def key_brute():
    keys = []
    ciph = load_ciphertext("Q1.txt")
    
    #For every possible range of values of the
    #final key byte...
    for key in range(256):
        found = True
        
        #...decrypt every fourth character of the plaintext using the
        #suspected key (we assume the key is 32 bytes long) and check
        #if the result is a "valid" ASCII character
        for i in range(3, len(ciph), 4):
            pt = chr(ciph[i] ^ key)
            if not (pt in string.ascii_lowercase or pt in string.ascii_uppercase or pt in " ,.?!"):
                found = False
                break
                
        #If it is, append this suspected key to a list
        #of possible key values
        if found:
            keys.append(key)
        
    print keys
    
if __name__ == "__main__":
    suspected_keys = key_brute()
    for key in suspected_keys:
        decrypt([132, 179, 227], key)