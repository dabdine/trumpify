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

end-to-end:
```
python3 trumpify.py -e 'hello' | xargs -I{} python3 trumpify.py -d {}
```
