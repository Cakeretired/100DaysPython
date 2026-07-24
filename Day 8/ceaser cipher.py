alphabet = [
    "a","b","c","d","e","f","g","h","i","j","k","l","m",
    "n","o","p","q","r","s","t","u","v","w","x","y","z"
]
option= input("enter encode to encrypt or decode to decrypt:  ")

text=input("enter text: ")
shift=int(input("enter shift: "))

def ceaser(original_Text, shift_Amount, encode_or_decode):
    output_text = ""


    if encode_or_decode == "decode":
        shift_Amount *= -1

    for letter in original_Text:
        if letter in alphabet:  # avoid crash on spaces
            shifted_position = alphabet.index(letter) + shift_Amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
        else:
            output_text

    print(f"Result: {output_text}")


ceaser(original_Text=text, shift_Amount=shift, encode_or_decode=option)


