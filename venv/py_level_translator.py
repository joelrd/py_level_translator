"""
Swap characters for a level generator.
"""

__author__ = "Henry Rojas Douglas"
__version__ = "1.0.0"
__copyright__ = "Henry Rojas"
__license__ = "MIT"

import io

if __name__ == '__main__':
    with io.open('reader/reader.txt', 'rb') as file_object:
        i = 5
        for line in file_object:
            string_line = str(line)
            if 'Level' in string_line or 'Moves' in string_line or 'Pushes' in string_line or 'BoxLines' in string_line \
                    or 'u' in string_line:
                continue
            string_line = string_line.replace('b', '').replace('#', 'M').replace('\'', '').replace('$', 'C')\
                .replace('@', 'J').replace('.', 'O').replace(' ', 'P')
            string_line = string_line.rstrip('\n')
            string_line += ',\n'
            f = open('levels/Level-' + str(i) + '.txt', "a")
            f.write(string_line)
            f.close()
            if line.isspace():
                i += 1