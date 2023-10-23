# Simple-DES

Implementation of decryption and encryption algorithms for KI submission

## Build

Create environment (Linux)

```py
python3 -m venv venv
```

```bash
source venv/bin/activate
```

```bash
pip install -r requirements.txt
```

## Run

Build into executable

```py
pyinstaller --onefile -w DES.py
```

```bash
./dist/DES
```

## Explanation



```bash
hexa_to_bin = {
                '0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100',
                '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001',
                'a': '1010', 'b': '1011', 'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111'
}
```

```bash
hexa_to_char = {
                '61': 'a', '62': 'b', '63': 'c', '64': 'd', '65': 'e', '66': 'f', '67': 'g', '68': 'h', '69':'i',
                '6a':'j', '6b':'k', '6c':'l', '6d':'m', '6e':'n', '6f':'o', '70':'p', '71':'q', '72':'r', '73':'s',
                '74':'t', '75':'u', '76':'v', '77':'w', '78':'x', '79':'y', '7a':'z', '41':'A', '42':'B', '43':'C',
                '44':'D', '45':'E', '46':'F', '47':'G', '48':'H', '49':'I', '4a':'J', '4b':'K', '4c':'L', '4d':'M', '4e':'N',
                '4f':'O', '50':'P', '51':'Q', '52':'R', '53':'S', '54':'T', '55':'U', '56':'V', '57':'W', '58':'X', '59':'Y', '5a':'Z'
}
```