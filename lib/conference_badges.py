def badge_maker(name):
    badge = f"Hello, my name is {name}."
    return badge

def batch_badge_creator(names):
    badges=[badge_maker(name) for name in names]
    return badges

def assign_rooms(names):
    i=1
    room = []
    for name in names:
        
        room.append(f"Hello, {name}! You'll be assigned to room {i}!")
        i+=1
    return room     

def printer(names):
    [print(badge) for badge in batch_badge_creator(names)]
    [print(room) for room in assign_rooms(names)]
    
