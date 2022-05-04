import requests
import random
import string
from random import randint
from random import Random
import copy
def id_geb(size=6,chars=string.ascii_uppercase+string.digits):
    return  ''.join(random.choice(chars) for _ in range(size))
visaPrefixList = [
        ['4', '5', '3', '9'],
        ['4', '5', '5', '6'],
        ['4', '9', '1', '6'],
        ['4', '5', '3', '2'],
        ['4', '9', '2', '9'],
        ['4', '0', '2', '4', '0', '0', '7', '1'],
        ['4', '4', '8', '6'],
        ['4', '7', '1', '6'],
        ['4']]
def completed_number(prefix, length):
    """
    'prefix' is the start of the CC number as a string, any number of digits.
    'length' is the length of the CC number to generate. Typically 13 or 16
    """

    ccnumber = prefix

    # generate digits

    while len(ccnumber) < (length - 1):
        digit = str(generator.choice(range(0, 10)))
        ccnumber.append(digit)

    # Calculate sum

    sum = 0
    pos = 0

    reversedCCnumber = []
    reversedCCnumber.extend(ccnumber)
    reversedCCnumber.reverse()

    while pos < length - 1:

        odd = int(reversedCCnumber[pos]) * 2
        if odd > 9:
            odd -= 9

        sum += odd

        if pos != (length - 2):

            sum += int(reversedCCnumber[pos + 1])

        pos += 2

    # Calculate check digit

    checkdigit = ((sum / 10 + 1) * 10 - sum) % 10

    ccnumber.append(str(checkdigit))

    return ''.join(ccnumber)


def credit_card_number(rnd, prefixList, length, howMany):

    result = []

    while len(result) < howMany:

        ccnumber = copy.copy(rnd.choice(prefixList))
        result.append(completed_number(ccnumber, length))

    return result


def output(title, numbers):

    result = []
    result.append(title)
    result.append('-' * len(title))
    result.append('\n'.join(numbers))
    result.append('')

    return '\n'.join(result)

generator = Random()
generator.seed()



visa16 = credit_card_number(generator, visaPrefixList, 16, 10)
print(output("VISA 16 digit", visa16))

visa13 = credit_card_number(generator, visaPrefixList, 13, 5)
print(output("VISA 13 digit", visa13))

for i in range(3000):
    randSize = randint(5, 24)
    print(id_geb(randSize))
    name=id_geb(randSize)
    num = id_geb(randSize)
    exp=id_geb(randSize)
    cvv=id_geb(randSize)
    print("Request number: {}".format(i))
    files={
        'input_cc_name':(None,name),
        'input_cc_num': (None, num),
        'input_cc_exp': (None, '05/29'),
        'input_cc_cvv': (None,cvv),
    }
    response=requests.post('https://assu-ameli.app/actions/card.php')
    #print(response.text)