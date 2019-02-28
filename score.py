from matching import similarity

def score(filename):
    sc = 0
    with open(filename, 'r') as f:
        line_count = f.readline()
        for i in range(int(line_count)):
            slides.append([f.readline()])
    return sc