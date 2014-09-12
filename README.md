# Python Migemo

Python Binding for Migemo

## Installation

```sh
curl -L https://github.com/mitukiii/migemo-python/archive/v0.0.1.tar.gz -o migemo-0.0.1.tar.gz
pip install migemo-0.0.1.tar.gz
```

## Usage

```python
import migemo

dict_path = '/usr/local/Cellar/cmigemo/20110227/share/migemo/utf-8/migemo-dict'
m = migemo.Migemo(dict_path)
re_str = m.query('a')
print re_str
```

## Copyright

Copyright (c) 2014 [Kazuya Takeshima](mailto:mail@mitukiii.jp). See [LICENSE][license] for details.

[license]: LICENSE.md
