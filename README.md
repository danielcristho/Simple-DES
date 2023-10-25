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