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
        elif s == 11:   return f'Bad format ({s})'              # Code 11 (Bad format)
        elif s == 12:   return f'Invalid Access ({s})'          # Code 12 (Invalid Access)
        elif s == 13:   return f'Invalid Data ({s})'            # Code 13 (Invalid Data)
        elif s == 14:   return f'Out of memory ({s})'           # Code 14 (Out of memory)
        elif s == 15:   return f'Invalid drive ({s})'           # Code 15 (Invalid drive)
        elif s == 16:   return f'Current directory ({s})'       # Code 16 (Current directory)
        elif s == 17:   return f'Not same device ({s})'         # Code 17 (Not same device)
        elif s == 18:   return f'No more files ({s})'           # Code 18 (No more files)
        elif s == 19:   return f'Write protect ({s})'           # Code 19 (Write protect)
        elif s == 20:   return f'Bad unit ({s})'                # Code 20 (Bad unit)
        elif s == 21:   return f'Not ready ({s})'               # Code 21 (Not ready)
        elif s == 22:   return f'Bad command ({s})'             # Code 22 (Bad command)
        elif s == 23:   return f'Crc error ({s})'               # Code 23 (Crc error)
        else:           return f'Unknown ({s})'                 # Code ?? (Unknown)

    else:               # Linux error codes
        if s == 0:      return f'Success ({s})'                 # Code 0  (Success)
        elif s == 1:    return f'Error ({s})'                   # Code 1  (Error)
        else:           return f'Unknown ({s})'                 # Code ?? (Unknown)

    