import random
import copy
import multiprocessing as mp
import math


def in_file():
    '''returns [orientation, [list of tags]]'''
    filename = "b_lovely_landscapes.txt"
    images = []
    with open(filename, 'r') as f:
        line_count = f.readline()
        for i in range(int(line_count)):
            orientation, tags_count, *tags = f.readline().split()
            images.append(set(tags))
    return images


def output(slides: list):
    with open("b_lovely_landscapes_out.txt", 'w') as f:
        f.write(str(len(slides))+'\n')
        for slide in slides:
            f.write(str(slide)+'\n')


# [1, 2, 5, 7, 3, 6, 4, 8]
def calculate_score(index, images):
    score = 0
    for i in range(len(index) - 1):
        s1, s2, s3 = 0, 0, 0
        s1 = len(images[index[i]].difference(images[index[i + 1]]))
        s2 = len(images[index[i + 1]].difference(images[index[i]]))
        s3 = len(images[index[i]].intersection(images[index[i + 1]]))
        score += min(s1, s2, s3)
    #print("attempt: ", score)
    return score


def instance(q, index, agg, dim):
    generation = copy.copy(index)
    for attempt in range(agg):
        first = random.randint(0, dim - 1)
        second = random.randint(0, dim - 1)
        generation[first], generation[second] = generation[second], generation[first]
    cur_score = calculate_score(generation, images)
    q.put((cur_score, generation))


def genetic_threaded(images, aggressivenes, repetitions, threads):
    dim = len(images)
    index = list(range(dim))
    max_score = 12

    while max_score < 1500:
        cur_score = max_score
        generation = []
        q = mp.Queue()
        thread_attempts = []
        for i in range(threads):
            thread_attempts.append(mp.Process(target=instance, args=(q, index, aggressivenes, dim)))
            thread_attempts[i].start()
        for _ in range(threads):
            thread_score, thread_index = q.get()
            if thread_score > cur_score:
                cur_score = thread_score
                generation = thread_index
        for thread_l in thread_attempts:
            thread_l.join()
        print("max local: ", max_score)
        if cur_score > max_score:
            index = generation
            max_score = cur_score
            print("new max: ", max_score)
    return index


def genetic(images, agg, repetitions):
    dim = len(images)
    index = list(range(dim))
    random.shuffle(index)
    max_score = 0

    while max_score < 1500:
        cur_score = max_score
        generation = copy.copy(index)

        for attempt in range(agg):  # - 100*max_score)):
            first = random.randint(0, dim - 1)
            second = random.randint(0, dim - 1)
            generation[first], generation[second] = generation[second], generation[first]

        random.shuffle(generation)
        cur_score = calculate_score(generation, images)
        print("cur_score: ", cur_score)
        if cur_score > max_score:
            index = generation
            max_score = cur_score
            print("new max: ", max_score)
    return index


images = in_file()
# index = genetic_threaded(images, 100, 1000, 10)
index = genetic(images, 500, 1000)
output(index)
