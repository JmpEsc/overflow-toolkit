# overflow-toolkit

## Information
This is a small collection of scripts to help craft buffer overflows

##### fuzzer.py
Simple fuzzer that will loop through a list of commands, sending an array of A's in multiples of 50 up to 4000

##### test\_crash.py
This template of a script can be used to replicate the crash and which registers one has control of.

##### pattern\_tool.py
A python rewrite of the slow metasploit pattern\_create.rb tool.  With locate, hex to ascii, and endianess corrector built-in.

##### eip\_check.py
A template to check whether one has control of the EIP register.

##### bad\_chars.py
A template that contains a list of hex characters generated by python `for i in range(0,256): hex_list.append(hex(i))`

##### test\_exploit.py
A template for testing control of the flow of execution via either a placeholder or shellcode

### Typical order of scripts
fuzzer.py
test\_crash.py
pattern\_tool.py
test\_crash.py
pattern\_tool.py
eip\_check.py
bad\_chars.py
test\_exploit.py
test\_exploit.py

## Simple Walkthrough
### 1. fuzzer.py
TO-DO
