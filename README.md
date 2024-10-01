# automated-architecture-diagrams
Code-driven templates for generating automated software architecture diagrams, streamlining documentation and visualization of system designs.
## Python3 Virtualenv Setup

##### Requirements
* Python 3
* Pip 3
* graphviz
* diagrams

```bash
$ brew install python3
$ brew install graphviz
```

Verify 
Pip3 is installed with Python3

##### Installation
To install virtualenv via pip run:
```bash
$ pip3 install virtualenv
$ pip install diagrams
```

##### Usage
Creation of virtualenv:
```bash
$ virtualenv -p python3 <desired-path>
```

Activate the virtualenv:
```bash
$ source <desired-path>/bin/activate
```
Execute the code:
```bash
$ python architecture.py
```

Deactivate the virtualenv:
```bash
$ deactivate
```

Troubleshoot:
```bash
dot -V
export PATH="/opt/homebrew/bin:$PATH"
import shutil
print(shutil.which('dot'))
```