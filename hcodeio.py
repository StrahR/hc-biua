def in_file(filename):
    '''returns [orientation, [list of tags]]'''
    #filename = "a_example.txt"
    images = []
    with open(filename, 'r') as f:
        line_count = f.readline()
        for i in range(int(line_count)):
            orientation, tags_count, *tags = f.readline().split()
            images.append([orientation, set(tags)])
    return images


def output(filename: str, slides: list):
    with open(filename[:-4]+"_out.txt", 'w') as f:
        f.write(str(len(slides))+'\n')
        for slide in slides:
            line = ""
            for integer in slide:
                line += str(integer)+" "
            f.write(line[:-1]+'\n')

if __name__=="__main__":
    print(in_file('a_example.txt'))
    print(output("test", [[0], [3], [1,2]]))