0x05-processes_and_signals
A PID (i.e., process identification number) is an identification number that is automatically assigned to each process when it is created on a Unix-like operating system.
A process can be thought of as an instance of a program in execution. We called this an ‘instance of a program’, because if the same program is run lets say 10 times then there will be 10 corresponding processes.
In Linux, every signal has a name that begins with characters SIG. When the signal occurs, the process has to tell the kernel what to do with it.  There can be three options through which a signal can be disposed:
1. The signal can be ignored.
2. The signal can be caught.
3. Let the default action apply.
