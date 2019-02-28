photos = in_file("a_example.txt")

used_photos = [False] * len(photos)
used_counter = len(photos)

used_photos[0] = True
used_counter += 1


current_photo = 0

slideshow = [current_photo]

while used_counter < len(photos):
    new_photo = find_match(current_photo, photos, used_photos)
    used_photos[new_photo] = True
    slideshow.append(new_photo)
