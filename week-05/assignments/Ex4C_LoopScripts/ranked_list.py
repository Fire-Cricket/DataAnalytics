# Jordan R. Worrobah    
# 5/13/2026
# Ranked List

favoriteFish = ["Discus", "Angelfish", "Corydora", "Guppies", "Flowerhorn"]

print("\n----- Favorite Fish Ranked List -----")

for i, fish in enumerate(favoriteFish, start=1):

    if i == 1:
        print(f"{i}. {fish} <- top pick!")

    else:
        print(f"{i}. {fish}")

print("\n----- Reverse Order -----")

reversedFish = list(reversed(favoriteFish))

for i, fish in enumerate(reversedFish, start=1):

    if i == 5:
        print(f"{i}. {fish} <- top pick!")
    else:
        print(f"{i}. {fish}")