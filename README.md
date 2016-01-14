# trumpify
Now you can speak like Trump, too! https://www.youtube.com/watch?v=RDrfE9I8_hs

# Usage
Encode a string:
```
python3 trumpify.py -e 'china'
CHIIIINA CHIIIIIIIIINA CHIIIIIIIIIINA CHIIIIIIIIIIIIIIINA CHIINA
```

Decode a string:
```
python3 trumpify.py -d 'CHIIIINA CHIIIIIIIIINA CHIIIIIIIIIINA CHIIIIIIIIIIIIIIINA CHIINA'
china
```

End-to-end:
```
python3 trumpify.py -e 'china' | xargs -I{} python3 trumpify.py -d {}
china
```

If you're on a mac, vocalize it:
```
python3 trumpify.py -e 'china' | say -v Deranged
```
