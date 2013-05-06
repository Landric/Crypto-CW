from LFSR import lfsr
from itertools import islice

def load_ciphertext(file_location):
    file = open(file_location, 'r')
    return bytearray.fromhex(file.read())
    
def brute_force(ciphertext, known_plaintext):
    
    #The "goal" state of the LFSR is equal to the ciphertext XOR-ed with the known plaintext
    goal = []
    for i in range(len(known_plaintext)):
        goal.append(ciphertext[i] ^ known_plaintext[i])
        
    goal = bytearray(goal)
    
    #Brute force all possible all order 5 LFSRs
    #Order 5 is given for this coursework - this will be made parametric in later releases
    for characteristic in range(0b100000, 0b111111 + 1): #Range is not inclusive, so +1
        for state in range(0b000001, 0b11111 + 1): #Range is not inclusive, so +1

            register = lfsr(map(int, list(bin(characteristic)[2:])), map(int, list(bin(state)[2:])))

            #Collect an equivilant number of bits from the LFSR
            #as are known from the plaintext, and transform them
            #into a byte array
            byte_array = []
            for i in range(len(known_plaintext)):
                byte = ''.join(map(str, islice(register, 8)))
                byte_array.append(int(byte, 2))

            #Check if the first LFSR bytes match the goal bytes
            #If they do, print out the characteristic, state, and potential plaintext
            if bytearray(byte_array) == goal:
                print "POTENTIAL MATCH:"
                print "Char = {0}, State = {1}".format(characteristic, state)

                #Recreate the register and split it into bytes
                register = lfsr(map(int, list(bin(characteristic)[2:])), map(int, list(bin(state)[2:])))
                register_bytes = []
                for i in range(len(ciphertext)):
                    byte = ''.join(map(str, islice(register, 8)))
                    register_bytes.append(int(byte, 2))

                #Print the potential plaintext
                bit_file = open("bit_file.txt", "a")
                chr_file = open("chr_file.txt", "a")
                
                register = bytearray(register_bytes)
                count = 0
                for i in range(len(ciphertext)):
                    if count == 7:
                        bit_file.write("\n")
                        count = 0
                    register[i] = register[i] ^ ciphertext[i]
                    bit_file.write("{0} ".format(bin(register[i])[2:].zfill(8)))
                    count += 1
                chr_file.write(''.join(map(chr, register)))

#Default options are parameters given for the coursework
#Could use argparse in future
if __name__ == "__main__":
    brute_force(load_ciphertext("Q1.txt"), bytearray(b"Ur"))