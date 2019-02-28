def in_file(filename):
    '''returns [orientation, [list of tags]]'''
    #filename = "a_example.txt"
    images = []
    with open(filename, 'r') as f:
        line_count = f.readline()
        for i in range(int(line_count)):
            orientation, tags_count, *tags = f.readline().split()
            images.append([orientation, tags])
    return images


if __name__=="__main__":
    print(in_file('a_example.txt'))