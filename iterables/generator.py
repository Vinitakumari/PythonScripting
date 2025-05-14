# (example of processing large log files)

def get_error_lines(filename):
    return ( line for line in open(filename) if 'ERROR'in line)

for error in get_error_lines('app.log'):
    print(f"Found error: {error.strip()}")
