message = 'Był jasny, zimny dzień kwietniowy i zegary biły trzynastą oraz przy okazji Lamberta'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)