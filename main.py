from hcodeio import in_file
from matching import find_match, similarity

photos = in_file("a_example.txt")

used_photos = [False] * len(photos)

used_photos[0] = True

current_photo = 0

slideshow = [current_photo]

for i in range(len(photos)):
    new_photo = find_match(current_photo, photos, used_photos)
    used_photos[new_photo] = True
    slideshow.append(new_photo)
