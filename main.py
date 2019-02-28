from hcodeio import in_file, output
from matching import find_match, similarity

# filename = "a_example.txt"
filename = "b_lovely_landscapes.txt"
# filename = "c_memorable_moments.txt"
# filename = "d_pet_pictures.txt"
# filename = "e_shiny_selfies.txt"
photos = in_file(filename)

used_photos = [False] * len(photos)

# used_photos[0] = True

# current_photo = 0

slideshow = [] # calculate
# del photos[3]
# del photos[0]

# vertical_count = 2 # calculate
single = False
trashhole = 35

for img in range(len(photos)):
    # if img % 100 == 0:
        # print(img)
    if photos[img][0] == 'V' and not used_photos[img]:
        max_sim = 0
        match = -1
        for candidate in range(img + 1, len(photos)):
            if max_sim > trashhole:
                break
            if photos[candidate][0] == 'H' or used_photos[candidate]:
                continue
            s = len(photos[img][1].union(photos[candidate][1]))
            if s > max_sim:
                match = candidate
                max_sim = s
        used_photos[match] = True
        used_photos[img] = True
        photos.append(['H', photos[img][1].union(photos[match][1]), [img, match]])
        # slideshow.append([img, match])
        # if single:
        #     slideshow[-1].append(img)
        # else:
        #    slideshow.append([img])
        # single = not single

print("half")
slideshow.append(photos[-1][2])
for img in range(1, len(photos) - 1):
    if photos[img][0] == 'H':
        max_sim = 0
        space = 0
        a = photos[slideshow[0][0]][1]
        for slide in range((len(slideshow) - 1)//4):
            b = photos[slideshow[slide + 1][0]][1]
            if len(slideshow[slide + 1]) == 2:
                b = b.union(photos[slideshow[slide + 1][1]][1])
            s = similarity(['neki', a], ['neki', b])
            sl = similarity(photos[img], ['neki', a])
            sr = similarity(photos[img], ['neki', b])
            if sl + sr >= s and sl + sr - s > max_sim:
                space = slide + 1
                max_sim = sl + sr - s
                break
            a = set(list(b)[:])
            # if max_sim > 1:
            #     break
        slideshow.insert(space, photos[img][2])

output(filename, slideshow)