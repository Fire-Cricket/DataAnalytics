# Jordan R. Worrobah
# 5/11/2026
# Movie List

movieList = ["X-Men: Apocalypse", "The Truman Show", "Shang Chi"]

print(f"The list movieList includes my top {len(movieList)} movies of all time.")
print(movieList)

#Print the list sorted
print(sorted(movieList))
print(movieList)
# a) The sorted() function does not change the original list, it returns a new sorted list.

#Print with the sort. method
movieList.sort()
print(movieList)
# b) The difference between the sort() method and the sorted()
# function is that the sort() method modifies the original list in place, 
# while the sorted() function returns a new sorted list without changing the original list.