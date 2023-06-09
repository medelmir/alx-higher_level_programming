#!/usr/bin/python3
if __name__ == "__main__":
    """Prints #pythoniscool followed by a new line"""
    import os
    os.write(1, b'#pythoniscool\n')
