"""
Algorithm:
- create the longes prefix-suffig list
- go through the text one character at a time and do the following

Creating PSL:
...

KMP step:
- if character matches, we can move both in the text and in the pattern

TODO: 1. implement creation of the prefix-suffix list 2. make the algorithm work on a stream

"""

pattern = "foobarfoo"
pref_suff = [0,0,0,0,0,0,1,2,3]

text = "barfoobarfoobarfoobarfoobarfoo"

def kmp(text : str, pattern : str, lps : list[int]) -> list[int]:
    """Returns list of positions at which the pattern starts"""
    t_pos = 0
    p_pos = 0
    occurs = []
    while t_pos < len(text):
        print(f"{text[:t_pos+1]}")
        print(f"{pattern[:p_pos+1]}")

        if text[t_pos] == pattern[p_pos]: # the letter from text where we are can be appended to the currently loaded pattern
            if p_pos == len(pattern) - 1: # we have just checked that last letter of the pattern corresponds to the text
                occurs.append(t_pos-len(pattern)+1)
                print("MATCH")
                p_pos = lps[p_pos] # we cannot continue further in the pattern (there is nothing more) but in next step, we can try to append after our longest prefix that is also a suffix s.t. prefix != pattern
            else:
                p_pos += 1
            t_pos += 1
        else: # we have a mismatch
            if p_pos == 0:
                p_pos = 0
                t_pos += 1
            else:
                p_pos = lps[p_pos] + 1
        input("Press enter to continue")
        print("_____________________")
    return occurs

print(kmp(text,pattern,pref_suff))
              