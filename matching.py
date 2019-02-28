def similarity(a: list, b: list) -> int:
    s0 = len(a[1].difference(b[1]))
    s1 = len(b[1].difference(a[1]))
    s2 = len(a[1].intersection(b[1]))
    return min(s0, s1, s2)

def find_match(image, images: list, used_images: list):
    max_similarity = 0
    simlar_image_i = 0
    for i in range(len(images)):
        if used_images[i] == True:
            continue
        s = similarity(image, images[i])
        if s < max_similarity:
            max_similarity = s
            simlar_image_i = i
    return simlar_image_i
