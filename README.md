## i3

To make `trust` float by default, add the following to your i3 config:

```
for_window [class="trust"] floating enable
```

## Install dependencies

### Using Pipenv

This might or might not work:

```
pipenv install
```

### Using requirements.txt

This will probably work:

```
pip install --user -r requirements.txt
```
