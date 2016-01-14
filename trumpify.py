import re
import random
from optparse import OptionParser

def run():
   parser = OptionParser()
   parser.add_option("-e", "--encode", dest="encode_text")
   parser.add_option("-d", "--decode", dest="decode_text")
   (options, args) = parser.parse_args()

   if options.encode_text and options.decode_text:
      parser.error("cannot specify both encode and decode simultaneously")
   if not options.encode_text and not options.decode_text:
      parser.error("must specify either encode or decode")

   trump_encode(options.encode_text) if options.encode_text else trump_decode(options.decode_text)
   print()

def trump_encode(encode_text):
   first = True
   for c in encode_text:
      if c == ' ':
         print(' china', end='')
      elif c.isalpha():
         china = 'c' if c.islower() else 'C'
         china = '%shii%sna' % (china, 'i' * (ord(c.upper()) - 65))
         if c.isupper() and random.randint(1,2) % 2 == 0:
            china = china.upper()
         if not first:
            china = ' %s' % china 
         first = False
         print(china, end='')
      else:
         print(c, end='')

def trump_decode(decode_text):
   expr = re.compile('^(chii+na)(.*)$', re.IGNORECASE)
   for china in decode_text.split():
      if china.lower() == 'china':
         print(' ', end='')
      else:
         m = expr.search(china)
         if not m:
            raise Exception("invalid input: %s" % china) 

         # group(1) contins china variant
         # group(2) contains non-space/non-alpha parts
         ucase = m.group(1)[0].isupper();
         china = m.group(1).lower();
         print(chr(china.count('i') - 2 + 65) if ucase else chr(china.count('i') - 2 + 97), end='')
         print(m.group(2), end='')

if (__name__ == '__main__'):
   run()
