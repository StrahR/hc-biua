from hcodeio import in_file, output
from matching import find_match, similarity

# filename = "a_example.txt"
# filename = "b_lovely_landscapes.txt"
filename = "c_memorable_moments.txt"
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

for img in range(len(photos)):
    if photos[img][0] == 'V' and not used_photos[img]:
        max_sim = 0
        match = -1
        for candidate in range(len(photos)):
            if photos[candidate][0] == 'H' or used_photos[candidate] or candidate == img:
                continue
            s = len(photos[img]) + len(photos[candidate])
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

print("test")
for img in range(len(photos)):
    if photos[img][0] == 'H':
        max_sim = 0
        space = 0
        for slide in range(len(slideshow) - 1):
            s = similarity(photos[slide + 1], photos[slide])
            sl = similarity(photos[img], photos[slide])
            sr = similarity(photos[img], photos[slide + 1])
            if sl + sr >= s and sl + sr - s > max_sim:
                space = slide + 1
                max_sim = sl + sr - s
        slideshow.insert(space, photos[img][2])


#     new_photo = find_match(current_photo, photos, used_photos)
#     used_photos[new_photo] = True
#     slideshow.append([new_photo])
#     current_photo = new_photo

output(filename, slideshow)