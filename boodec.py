from time import sleep
from decimal import Decimal, getcontext
import json



book=input("Enter the Charecter to Decode: ")
key=int(input("Enter the Key: "))

#Charecter to encoded data
dec_dict={
        #Whitespace
        '000':' ',
        #LowercaseAlphabet
        '001':'a',
        '002':'b',
        '003':'c',
        '004':'d',
        '005':'e',
        '006':'f',
        '007':'g',
        '008':'h',
        '009':'i',
        '010':'j',
        '011':'k',
        '012':'l',
        '013':'m',
        '014':'n',
        '015':'o',
        '016':'p',
        '017':'q',
        '018':'r',
        '019':'s',
        '020':'t',
        '021':'u',
        '022':'v',
        '023':'w',
        '024':'x',
        '025':'y',
        '026':'z',
        #UppercaseAlphabet
        '027':'A',
        '028':'B',
        '029':'C',
        '030':'D',
        '031':'E',
        '032':'F',
        '033':'G',
        '034':'H',
        '035':'I',
        '036':'J',
        '037':'K',
        '038':'L',
        '039':'M',
        '040':'N',
        '041':'O',
        '042':'P',
        '043':'Q',
        '044':'R',
        '045':'S',
        '046':'T',
        '047':'U',
        '048':'V',
        '049':'W',
        '050':'X',
        '051':'Y',
        '052':'Z',
        #Numbers
        '053':'0',
        '054':'1',
        '055':'2',
        '056':'3',
        '057':'4',
        '058':'5',
        '059':'6',
        '060':'7',
        '061':'8',
        '062':'9',
        #specialCharecters
        '063':'!',
        '064':'"',
        '065':'#',
        '066':'$',
        '067':'%',
        '068':'&',
        '069':"'",
        '070':'(',
        '071':')',
        '072':'*',
        '073':'+',
        '074':',',
        '075':'-',
        '076':'.',
        '077':'/',
        '078':':',
        '079':';',
        '080':'<',
        '081':'=',
        '082':'>',
        '083':'?',
        '084':'@',
        '085':'[',
        #086 for backslash
        '087':']',
        '088':'^',
        '089':'_',
        '090':'`',
        '091':'{',
        '092':'|',
        '093':'}',
        '094':'~'
        }

getcontext().prec = 1000

for i in range(key):
    book=float(book)/100
    print(float(book))
    print("Key: {}".format(key))
    sleep(1)

def decode(message):
    decoded_value=''
    j=0
    for i in range(10):
        if len(message[j:j+3])<3:
            exit()
        else:
            j+=3
            for charecter in range(0, len(message), 3):
                three_chars = message[charecter:charecter+3]
                for k in range(1):
                    decoded_value+=dec_dict[three_chars]
    return decoded_value

print(decode(book))

decoded_book=decode(book)
#output key value into .txt
json_string = json.dumps(decoded_book)
with open('decoded_book.txt', 'w') as f:
    # Write the json string to the text file
    f.write(json_string)