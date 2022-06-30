def fact(k):
  f = i = 1
  while i<=k:
    f = i*f
    i += 1
  return f

def findcomb(x, y):
  num = fact(x)
  den = fact(x - y)
  den = fact(y) * den
  comb = num / den
  return comb

def predict(sent, received):
    while '+' in received or '-' in received:
        if '+' in received and '+' in sent:
            received.remove('+')
            sent.remove('+')
        elif '-' in received and '-' in sent:
            received.remove('-')
            sent.remove('-')
        else:
            return 0
    if(len(received)==0):
        return 1
    else:
        if sent.count('+') != 0:
            return (findcomb(len(sent),sent.count('+')))/(2**len(sent))
        else:
            return (findcomb(len(sent),sent.count('-')))/(2**len(sent))

sent = input().strip()
received = input().strip()

sent = [i for i in sent]
received = [i for i in received]



print('{0:.12f}'.format(predict(sent, received)))
