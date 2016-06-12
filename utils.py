import os
from shutil import *


# changed to not throw an error if directory already exists
# changed to return a list of new file names
def copytree(src, dst, symlinks=False, ignore=None, _output=None):
        
    if _output is None:
        _output = []
        
    names = os.listdir(src)
    if ignore is not None:
        ignored_names = ignore(src, names)
    else:
        ignored_names = set()

    if not os.path.isdir(dst):  # This one line does the trick
        os.makedirs(dst)
    errors = []
    for name in names:
        if name in ignored_names:
            continue
        srcname = os.path.join(src, name)
        dstname = os.path.join(dst, name)
        try:
            if symlinks and os.path.islink(srcname):
                linkto = os.readlink(srcname)
                os.symlink(linkto, dstname)
            elif os.path.isdir(srcname):
                copytree(srcname, dstname, symlinks, ignore, _output)
            else:
                # Will raise a SpecialFileError for unsupported file types
                copy2(srcname, dstname)
                _output.append(dstname)
        # catch the Error from the recursive copytree so that we can
        # continue with other files
        except Error:
            errors.extend(Error)
        except EnvironmentError:
            errors.append((srcname, dstname, EnvironmentError))
    try:
        copystat(src, dst)
    except OSError:
        if WindowsError is not None and isinstance(OSError, WindowsError):
            # Copying file access times may fail on Windows
            pass
        else:
            errors.extend((src, dst, str(OSError)))
    if errors:
        raise Error
    
    return _output

