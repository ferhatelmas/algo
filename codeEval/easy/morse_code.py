import re, string, sys

codes = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---',
         '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-',
         '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---',
         '...--', '....-', '.....', '-....', '--...', '---..', '----.']

morse = dict(zip(codes, string.ascii_uppercase + string.digits))

def decode(ls):
    return ''.join(morse[l] for l in ls)

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    print ' '.join(map(lambda w: decode(w.split()),
                       re.split(r'\s{2}', test.strip())))
test_cases.close()
