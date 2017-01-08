# Dereference command for gdb

# Install

1. clone source code to your computer.
2. execute _ source /path/to/code/dereference_generic_pointer.py _ command or add your .gdbinit file.

# Use command

syntax.

```
    dgp [Format] [Address expression]
```

Format and Address expression are same as gdb x command. see [document](http://visualgdb.com/gdbreference/commands/x).

example.

```
(gdb) dgp s $rbp - 8
[*]execute: x/gx $rbp - 8
[*]execute: x/s 0x0000000000602010
0x602010:       "test"

(gdb) dgp 4c $rbp - 8
[*]execute: x/gx $rbp - 8
[*]execute: x/4c 0x0000000000602010
0x602010:       116 't' 101 'e' 115 's' 116 't'

(gdb) dgp 4x $rbp - 8
[*]execute: x/gx $rbp - 8
[*]execute: x/4x 0x0000000000602010
0x602010:       0x0000000074736574      0x0000000000000000
0x602020:       0x0000000000000000      0x0000000000020fe1

(gdb) dgp g $rbp
[*]execute: x/gx $rbp + 0
[*]execute: x/g 0x00007fffffffdca0
0x7fffffffdca0: 0x0000000000400720

```
