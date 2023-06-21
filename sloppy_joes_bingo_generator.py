import random

occurrence = ["Kid out too late", "Wheely bin", "Matching outfits", "Cowboy hat", "Barefoot", "Jeans & Flip Flops", "Twerking", "Dancing", "Trip", "Double fisting", "Dumb hat", "Offensive shirt", "Couple fighting/Regular fight", "Pink taxi", "Ghost Tour/Street Train", "Sitting on the street", "Handshake", "High Five", "Litterbug", "Yawning", "Guy-on-Guy Scooter", "Hoofing it", "Spilled drink/food", "Acknowledge camera", "Almost get hit by car", "Crying", "American flag clothes", "Chug", "Can see FaceTime", "Go cart", "Tricycle", "Puking", "Drunk walk", "Skateboard", "Hug", "Luxury car", "Bachelorette party", "Aggressive honking", "Trying to get in wrong car", "Cop car/ambulance/fire truck", "Camera shy", "Bandage dude", "Formal attire", "Dropped something", "Nighttime shades", "Seperated at crosswalk", "Car delivery/pickup", "Car with ground effects"]
sorted_occurrence = sorted(occurrence)
# print(sorted_occurrence)
# print(len(sorted_occurrence))


def generate():
  row_number = 1
  for column in range(5):

    print(" ")
    print("Row", str(row_number) + ": ")

    for box in range(5):
        box = random.choice(occurrence)
        print(box)
        occurrence.remove(box)

    row_number += 1  
        

print("Get ready for Sloppy Joe's Bingo!")
print("Get 5 across in any direction to win!")
generate()

# TODO: Add "Free Space" in middle of card
