#pyzepto

A crude way of interfacing zepto and Python.

## Requirements

You need to have [zepto](https://github.com/hellerve/zepto) installed.

## Usage

I really advise against using it. It's amazingly crude.
But if you really want to do this, it's relatively straight-forward.
The main function that is exposed by this package is `zepto`. It
takes a string of zepto code and evaluates it, returning the return
value as a string.

```python
from pyzepto import zepto

zepto("(+ 1 2 3)") # => "6"
zepto("(make-byte-vector 10 0)") # => "b{0 0 0 0 0 0 0 0 0 0}"
```

I also implemented a custom module loader for your convenience,
so you can import zepto files into Python using regular `import`
statements. What could possibly go wrong?
