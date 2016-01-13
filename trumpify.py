import re
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
         c = 'chii%sna' % ('i' * (ord(c) - 65)) if c.isupper() else 'CHII%sNA' % ('I' * (ord(c) - 97))
         if not first:
            c = ' %s' % c

         first = False
         print(c, end='')
      else:
         print(c, end='')

def trump_decode(decode_text):
   lcexpr = re.compile('^(chii+na)(.*)$')
   ucexpr = re.compile('^(CHII+NA)(.*)$')
   for china in decode_text.split():
      if china.lower() == 'china':
         print(' ', end='')
      else:
         m = lcexpr.search(china)
         if not m:
            m = ucexpr.search(china)
            if not m:
               raise Exception("invalid input: %s" % china) 

         # group(1) contins china variant
         # group(2) contains non-space/non-alpha parts
         print(chr(m.group(1).count('i') - 2 + 65) if m.group(1).count('i') > 0 else chr(m.group(1).count('I') - 2 + 97), end='')
         print(m.group(2), end='')

if (__name__ == '__main__'):
   run()
