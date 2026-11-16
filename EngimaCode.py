import EnigmaKey
import Enigma_Protatip
import EnigmaDECODE
import Enigma_Main
import random
import string

a = input("Do you wanna start?: ")
while a.lower() == "yes" or a.lower() == "y" :
    user_choice = input("What would you like to do?: ")
    if user_choice.lower() == "hide" or user_choice.lower() == "h" :
        cipher, key = Enigma_Protatip.generate_cipher()
        text = input("Enter Text : ")
        CodeKey = EnigmaKey.RotarKey()
        CodeRotars_Hidden = ""
        CodePositions_Hidden = str(Enigma_Main.encode(CodeKey['positions']))
        CodeReflector = CodeKey['reflector']

        for i in range(3):
            CodeRotars_Hidden = CodeRotars_Hidden + str(CodeKey["rotors"][i])
        Code = CodePositions_Hidden
        Code = Code +Enigma_Protatip.encrypt(text,cipher) + CodeRotars_Hidden + CodeReflector
        print(Code,"\n")





    if user_choice.lower() == "decode" or user_choice.lower() == "d":
        text = input("Enter Text : ")
        text_rotors = text[-4:-1]
        text_positions = text[0:8]
        key_reflector = text[-1]
        key_rotors = list(map(int, text_rotors))
        key_positions = Enigma_Main.decode(text_positions)

        Orgin_key = EnigmaDECODE.find_key(key_rotors, key_positions, key_reflector)
        key = Orgin_key
        alphabet = list(string.ascii_uppercase + "!@#$%^&*+-/? ")
        rng = random.Random(key)
        shuffled = alphabet.copy()
        rng.shuffle(shuffled)
        cipher = dict(zip(alphabet, shuffled))
        text_orgin = text[8:-4]

        print(Enigma_Protatip.decrypt(text_orgin,cipher),"\n")




#         text = input("Enter Text : ")
#         CodeR= {"rotors":[], "positions":[], "reflector":""}
#         # pos
#         thepositions = ''
#         for i in range(8):
#             thepositions += text[i]
#         CodeR["positions"] = Enigma_Main.decode(thepositions)
#         #rotor
#         therotors = ''
#         for i in range(-1,-4):
#             therotors += text[i]
#         CodeR["rotors"] = list(map(int, therotors.split(",")))
# #         ref
#         theref = text[-1]
#         CodeR["reflector"] = theref


