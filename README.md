# Python Migemo

Python Binding for Migemo

## Installation

```sh
curl -L https://github.com/mitukiii/migemo-python/archive/v0.0.2.tar.gz -o migemo-0.0.2.tar.gz
pip install migemo-0.0.2.tar.gz
```

## Usage

```python
import migemo
import re

## Linux
dict_path = '/usr/local/share/migemo/utf-8/migemo-dict'
## OS X
# dict_path = '/usr/local/Cellar/cmigemo/20110227/share/migemo/utf-8/migemo-dict'

m = migemo.Migemo(dict_path)

re_str = m.query(u'nyan')
re.search(re_str, u'にゃん')
```

## Copyright

Copyright (c) 2014 [Kazuya Takeshima](mailto:mail@mitukiii.jp). See [LICENSE][license] for details.

[license]: LICENSE.md
