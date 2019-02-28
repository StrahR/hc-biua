from hcodeio import in_file, output
from matching import find_match, similarity


filename = "b_lovely_landscapes.txt"
photos = in_file(filename)

used_photos = [False] * len(photos)

used_photos[0] = True

# current_photo = 0

slideshow = [] # calculate
# del photos[3]
# del photos[0]

# vertical_count = 2 # calculate
single = False

for img in range(len(photos)):
    if photos[img][0] == 'V':
        if single:
            slideshow[-1].append(img)
        else:
           slideshow.append([img])
        single = not single
    else:
        max_sim = 0
        space = 0
        for slide in range(len(slideshow) - 1):
            s = similarity(photos[slide + 1], photos[slide])
            sl = similarity(photos[img], photos[slide])
            sr = similarity(photos[img], photos[slide + 1])
            if sl + sr >= s and sl + sr - s > max_sim:
                space = slide + 1
                max_sim = sl + sr - s
        slideshow.insert(space, [img])


#     new_photo = find_match(current_photo, photos, used_photos)
#     used_photos[new_photo] = True
#     slideshow.append([new_photo])
#     current_photo = new_photo

output(filename, slideshow)