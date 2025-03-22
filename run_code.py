import sys
from changeFormat import convert_to_format

for image_file in sys.argv[2:]:
    # with open("hello.txt", "a") as file:
    #     file.write(f'{sys.argv}\n')
    convert_to_format(image_file, sys.argv[1]) #sys.argv[1]  contains format


