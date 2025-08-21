# def extract_initials(text: str) -> list[str]:
#     words = text.split()
#     initials = []
#     for w in words:
#         if w[0].isalpha():
#             initials.append(w[0].upper())
#         else:
#             initials.append(w[0])
#     return initials


# def group_initials(text: str) -> list[str]:
#     lines = text.strip().split("\n")
#     grouped = []
#     for line in lines:
#         initials = extract_initials(line)
#         grouped.append("".join(initials))
#     return grouped


# if __name__ == "__main__":
#     text="""Ice Frog Zipper vase butterfly Heart Vase tiger Zero Sandwich Beach pyramid basket insect Beach keyboard camera magnet lighthouse 2 Zen Ship Beach Desk Ice Globe honey hedgehog camera yurt Bird utensil basket yak Beach snowman Yurt Watermelon Jet lighthouse butterfly Cookie 4 Nut Cake island Basket Watch butterfly 2 xmas 1 book Wheel Uniform garden Ukulele 2 Volcano yellow airplane Wheel Frog sock Iguana Engine 5 1 bicycle Whale Jellyfish lock cake island Bird pyramid clown yawn Book Butterfly Mask Dog cloud 5 Lock Utensil Fire Engine Radio king Ink Ninja Cake garden 0 Key Iguana Eagle Raccoon pineapple candle mask Vulture jungle doll Ghost 9 yak easel Spoon Bottle vest Zoo igloo Beach Drum Onion lighthouse xylophone Unicorn Zipper Wagon 1 wing Diamond Quartz owl Necklace Camera jigsaw Acrobat 1 Log zombie Astronaut 3 Lighthouse zombie Ice wallet Mailbox jigsaw Queen guitar Ice-cream Door Anchor 5 Ocean jet Instrument yurt Ice-cream Escalator Flag Necklace Igloo Cake Apple grape Insect Drum x-ray Elf Spoon Vine Island + Iron Castle Astronaut grape Island Cloud Album goat Island Cake Arrow grape Ink Computer 4 Ninja Car jack-o-lantern Airplane 1 Lemon zero Album 3 Ladder zen Invitation windmill Mango jacket Quail glasses Invitation Dinosaur Apple 5 Octopus juice Igloo yolk Ice Egg Fruit Ninja Iguana Cookie Anchor game Instrument Door xylulose Eagle Squirrel Vacuum Island + Insect Clown Album gift Ice-cream Computer Airplane guitar Invitation Cake Anchor globe Island Clown 4 umbrella Dolphin Quadrilateral oyster wand Necklace Squirrel 8 wing Nut yak 8 yawn Mountain Drum Invitation 0 Iron Candle Apple windmill Nail zero otter yew Mushroom yogurt Ball Beach Train Squirrel Anchor game Iguana Camera Arrow gift Island Cake Astronaut globe Notebook jellyfish castle snake Nose Telescope Eagle 1 Lock Door cookie 0 Nut Cookie Banana zipper bear Xerosis Butterfly orange basket 3 Nest 0 Lion microphone Vase 4 Zen Quiver 0 Koala Ice Candle Airplane garden Insect Candle Avocado globe Ice-cream Camera Apple ghost Insect Candle Arrow grape Invitation Camera Alarm glasses Magnet Sun Butterfly Goat astronaut Whale xerosis lighthouse Koala Honey Mask panda Ink Car Astronaut gem Instrument Camera Avocado 2 Nest yellow watermelon 1 Microphone Tree Unicorn sock Nest zero Question 0 Invitation Grape Jungle 5 drum Gem Vase zelda Door Quail oyster ghost Igloo Camera Avocado gift Ice Camera Astronaut gem Ink Candle Astronaut garden Ice Clown Avocado glasses Ice-cream Clown Anchor yucca Island Eagle Rainbow pencil car ice heart zone King Spoon Astronaut globe Mushroom jet kite spider Nose juice Mouse 4 Lion Duck Monkey 4 Nut Squirrel watermelon 2 Net jellyfish Quail grape Yogurt notebook log 0 Zero X-ray Mask glasses Zone necklace Jellyfish lemon Zoo Question 0 Kite"""
    
#     result = extract_initials(text)
#     print("".join(result))
# def extract_first_letters(file_path):
#     result = ""
#     try:
#         # Open the file for reading
#         with open(file_path, 'r') as file:
#             content = file.read()  # Read the entire content

#         # Split the content by spaces to get each word
#         words = content.split()
#         for word in words:
#             # If the word starts with an alphabetic letter, take its first character
#             if word[0].isalpha():
#                 result += word[0]
#             else:
#                 # Otherwise, keep the symbol or number as-is
#                 result += word[0]

#         print("Extracted String:", result)

#     except FileNotFoundError:
#         print(f"Error: File '{file_path}' not found.")
#     except Exception as e:
#         print(f"An error occurred: {e}")


# # Example usage
# file_path = r"C:\Users\nguye\Downloads\HTB\Fishy HTTP\Yo.txt"  # Change to the path of your text file
# extract_first_letters(file_path)


def extract_initials_from_file(file_path: str) -> list[str]:
    """Đọc file và trả về danh sách chữ cái đầu tiên của mỗi từ."""
    initials = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        words = content.split()
        for w in words:
            if w[0].isalpha():
                initials.append(w[0])   # giữ nguyên hoa/thường
            else:
                initials.append(w[0])

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return initials


# def group_initials_from_file(file_path: str) -> list[str]:
#     """Đọc file và nhóm chữ cái đầu theo từng dòng."""
#     grouped = []
#     try:
#         with open(file_path, "r", encoding="utf-8") as file:
#             lines = file.read().strip().split("\n")

#         for line in lines:
#             words = line.split()
#             initials = []
#             for w in words:
#                 if w and w[0].isalpha():
#                     initials.append(w[0])   # giữ nguyên
#                 elif w:
#                     initials.append(w[0])
#             grouped.append("".join(initials))

#     except FileNotFoundError:
#         print(f"Error: File '{file_path}' not found.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

#     return grouped


# Example usage
if __name__ == "__main__":
    file_path = r"C:\Users\nguye\Downloads\HTB\Fishy HTTP\Yo.txt"

    result = extract_initials_from_file(file_path)
    # print("Initials (list):", result)
    print("Joined string:", "".join(result))

    # grouped = group_initials_from_file(file_path)
    # print("Grouped by line:", grouped)

