# Now, let's use our knowledge of sets and help Mickey.
# Ms. Gabriel Williams is a botany professor at District College.
# One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.
k = int(input())
rooms = (map(int,input().split()))
total_rooms, repeated_rooms= set(), set()
for room in rooms:
    
    if room in total_rooms:
        repeated_rooms.add(room)
        
    else:
        total_rooms.add(room)
       
  

print(total_rooms.difference(repeated_rooms).pop())






