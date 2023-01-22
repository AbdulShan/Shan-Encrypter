import json
import time
#Book to Encode
book=input("Enter the Charecter to Encode: ")


back_slash=chr(92)
#Charecter to encoded data
enc_dict={
        #Whitespace
        ' ':'000',
        #LowercaseAlphabet
        'a':'001',
        'b':'002',
        'c':'003',
        'd':'004',
        'e':'005',
        'f':'006',
        'g':'007',
        'h':'008',
        'i':'009',
        'j':'010',
        'k':'011',
        'l':'012',
        'm':'013',
        'n':'014',
        'o':'015',
        'p':'016',
        'q':'017',
        'r':'018',
        's':'019',
        't':'020',
        'u':'021',
        'v':'022',
        'w':'023',
        'x':'024',
        'y':'025',
        'z':'026',
        #UppercaseAlphabet
        'A':'027',
        'B':'028',
        'C':'029',
        'D':'030',
        'E':'031',
        'F':'032',
        'G':'033',
        'H':'034',
        'I':'035',
        'J':'036',
        'K':'037',
        'L':'038',
        'M':'039',
        'N':'040',
        'O':'041',
        'P':'042',
        'Q':'043',
        'R':'044',
        'S':'045',
        'T':'046',
        'U':'047',
        'V':'048',
        'W':'049',
        'X':'050',
        'Y':'051',
        'Z':'052',
        #Numbers
        '0':'053',
        '1':'054',
        '2':'055',
        '3':'056',
        '4':'057',
        '5':'058',
        '6':'059',
        '7':'060',
        '8':'061',
        '9':'062',
        #specialCharecters
        '!':'063',
        '"':'064',
        '#':'065',
        '$':'066',
        '%':'067',
        '&':'068',
        "'":'069',
        '(':'070',
        ')':'071',
        '*':'072',
        '+':'073',
        ',':'074',
        '-':'075',
        '.':'076',
        '/':'077',
        ':':'078',
        ';':'079',
        '<':'080',
        '=':'081',
        '>':'082',
        '?':'083',
        '@':'084',
        '[':'085',
        #086 for backslash
        ']':'087',
        '^':'088',
        '_':'089',
        '`':'090',
        '{':'091',
        '|':'092',
        '}':'093',
        '~':'094'
        }




#encode
def encode(message):
    encoded_number=''
    for charecter in message:
        encoded_number+=enc_dict[charecter]
    return '0.'+encoded_number

encoded_book = str(encode(book))

#output key value into .txt
json_string = json.dumps(encoded_book)
with open('encoded_book.txt', 'w') as f:
    # Write the json string to the text file
    f.write(json_string)




key=0

from decimal import Decimal,getcontext

getcontext().prec=10000

while len(str(encoded_book)) >20:
    encoded_book=float(encoded_book)*100
    key+=1
    print(Decimal(encoded_book))
    print("Key: {}".format(key))
    time.sleep(1)

length=len(str(encode(book)))
print("Length : {}".format(length))
    
'''print(encoded_book)

encoded_book=float(encoded_book)/100

print(encoded_book)'''



