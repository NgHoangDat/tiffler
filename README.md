# Tiffler

> A Niffler that only likes shiny variables

## Installation

```sh
pip install -U tiffler
```

## Usage

```py
import tiffler

template = "One {unit} was equal to {num_sickles:int} Sickles or {num_knuts:int} Knuts."
variables = tiffler.scan(
    template, 
    "one Galleon was equal to 17 Sickles or 493 Knuts.", 
    case_sensitive=False
)

print(variables)

#{'unit': 'Galleon', 'num_sickles': 17, 'num_knuts': 493}
```

```py
import tiffler

template = "\s+{item}: {price:int} {unit:str:\w+}"
bill = """
    Pewter cauldron: 15 galeons,
    Brass cauldron: 21 galeons,
    Copper cauldron: 25 galeons,
"""
for match in tiffler.search(template, bill, case_sensitive=False):
    print(match)

# {'item': 'Pewter cauldron', 'price': 15, 'unit': 'galeons'}
# {'item': 'Brass cauldron', 'price': 21, 'unit': 'galeons'}
# {'item': 'Copper cauldron', 'price': 25, 'unit': 'galeons'}
```
