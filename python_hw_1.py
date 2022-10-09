#! /usr/bin/python 
def transcribe(seq):
    """Prints the transcribed sequence"""
    transcription_seq = ""
    transcription_dic = {"A" : "U", "T" : "A", "G" : "C", "C" : "G", 
                "a" : "u", "t" : "a", "g" : "c", "c" : "g"}
    for letter in seq:
        if letter not in transcription_dic.keys():
            print("Invalid alphabet")
            break
        else:
            transcription_seq += transcription_dic[letter]
    print(transcription_seq)
    return transcription_seq 

def reverse(seq):
    """Prints the reverse sequence"""
    rev_seq = ""
    for letter in seq:
        rev_seq = seq[::-1]
    print(rev_seq)
    return rev_seq 

def complement(seq):
    """Prints the complement sequence"""
    compl_seq = ""
    compl_dic = {"A" : "T", "T" : "A", "G" : "C", "C" : "G", 
                "a" : "t", "t" : "a", "g" : "c", "c" : "g"}
    for letter in seq:
        compl_seq += compl_dic[letter]
    print(compl_seq)
    return compl_seq

def reverse_complement(seq):
    """Prints the reverse complement sequence"""
    compl = ""
    rev_compl = ""
    compl_dic = {"A" : "T", "T" : "A", "G" : "C", "C" : "G", 
                 "a" : "t", "t" : "a", "g" : "c", "c" : "g"}
    for letter in seq:
        compl += compl_dic[letter]
        rev_compl = compl[::-1]
    print(rev_compl)
    return rev_compl

def check_letters(seq): 
    nucl = ["U", "T"]
    up_seq = seq.upper()
    for letter in seq:
        result = all(letter in up_seq for letter in nucl)
        if result:
            return False
    return True

def check_pept(seq):
    """Checks letters of input sequence"""
    check_dic = ["A", "T", "G", "C", "U",
                "a", "t", "g", "c", "u"]
    if check_letters(seq) == False:
        return False
    else: 
        for letter in seq:
            if letter not in check_dic:
                return False
        return True




if __name__ == "__main__":
    while True:
        print("Enter the command")
        command = str(input())
        com_dic = {"transcribe" : transcribe, "exit" : "Good luck!", "reverse" : reverse,
                  "complement" : complement, "reverse complement" : reverse_complement}
        if command not in com_dic:
            print("The command does not exist")
        elif command == "exit":
            print(com_dic.get(command))
            break
        else:
            print("Enter the sequence")
            seq = str(input())
            while check_pept(seq) == False:
                print("Invalid alphabet! Enter another sequence")
                seq = str(input())  
            else:
                command_fun = com_dic.get(command)
                command_fun(seq)






