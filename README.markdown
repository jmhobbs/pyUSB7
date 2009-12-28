What is it?
===========
pyUSB7 is a collection of scripts designed for use with the USB7 hardware display kit from [Spiffie.org][1].  These scripts use [pySerial][2] and are designed to run on Linux, but can be run on Windows.

Why?
====
Why not? This is a fun and easy piece of hardware, so why not have some fun and easy scripts available?

Linux
=====
According to the [Spiffie.org Linux driver page][4] the USB7 will not work on unpatched 2.6.23 and later kernels.

Some known working kernels are:

* slh kernels from the [Sidux distribution][5] (2.6.32 confirmed)

Windows
=======
pyUSB7 is untested on Windows. It should work though.

Protocol
========
These scripts are written with the [3.0 protocol][3] in mind. The major difference is that 3.0 instances have a full (if somewhat ugly) alpha character set.  Most will work with 1.x & 2.0, but be aware of versioning if you see strange behavior.

License
=======
pyUSB7 scripts are released under the MIT license. See the file "LICENSE" for details.

[1]: http://spiffie.org/kits/usb7/ "Spiffie.org"
[2]: http://pyserial.sourceforge.net/ "pySerial"
[3]: http://spiffie.org/kits/usb7/protocol_3.shtml "3.0 Protocol"
[4]: http://spiffie.org/kits/usb7/driver_linux.shtml "Linux Driver"
[5]: http://sidux.com "Sidux"
