def exitCodes(s, os):
    c = f'Unknown ({s})'
    if os == 'nt':      # Windows error codes
        if s == 0:      return f'Success ({s})'                 # Code 0  (Success)
        elif s == 1:    return f'Error ({s})'                   # Code 1  (Error)
        elif s == 2:    return f'File not found ({s})'          # Code 2  (File not find)
        elif s == 3:    return f'Path not found ({s})'          # Code 3  (Path not find)
        elif s == 4:    return f'Too many open files ({s})'     # Code 4  (Too many open files)
        elif s == 5:    return f'Access denied ({s})'           # Code 5  (Access denied)
        elif s == 6:    return f'Invalid handle ({s})'          # Code 6  (Invalid handle)
        elif s == 7:    return f'Area trashed ({s})'            # Code 7  (Area trashed)
        elif s == 8:    return f'Not enough memory ({s})'       # Code 8  (Not enough memory)
        elif s == 9:    return f'Invalid block ({s})'           # Code 9  (Invalid block)
        elif s == 10:   return f'Bad enviroment ({s})'          # Code 10 (Bad enviroment)
        else:           return f'Unknown ({s})'                 # Code ?? (Unknown)

    else:               # Linux error codes
        if s == 0:      return f'Success ({s})'                 # Code 0  (Success)
        elif s == 1:    return f'Error ({s})'                   # Code 1  (Error)
        else:           return f'Unknown ({s})'                 # Code ?? (Unknown)

    