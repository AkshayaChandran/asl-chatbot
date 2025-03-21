from typing import Dict, List

# Dictionary mapping words/phrases to ASL image URLs
asl_images: Dict[str, str] = {
    "hello": "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExZTZiY2l3cndhejJ1NWs3NjRjNzZ0OWZjcDV2NTJydzRhdmd1MmVyayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/DcPfy7StVKeB5dv0ND/giphy.gif",
    "thankyou": "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExMnZwbWE3eGcwZnh3amV6YW5rMmd3eW5tZTh6MHVqNm5yNTJ2N2Q4ayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3s6MJXtehv1qx1K9zd/giphy.gif",
    "sorry": "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExaTdmbmxqM2dhMzMwYXpmYTgxMDc3d3l4YTZsazU4Y3ZncXpudjB6bCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/paRJJnkjPyKxHyTCAg/giphy.gif",
    "applause": "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExbjQ4OXJpMTI2ZTNxMmdxajU2MWN3MHgzaXFjMTJ3bDU1amFpZGpvbSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/T982vDYtrs4EjCZz2H/giphy.gif",
    "yes": "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExYzJzand1cXk4emZ4enJnajByeDVzMTJxYXV2bnZ1bGJiMWVqcGM2OSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/18OMELKhQaCIFFDufn/giphy.gif",
    "please": "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExdmEwa2Myem03ajlicHZjZ2x6aDBxOTJmb2hubnJsenF3aHd4dG5wZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/5YnoT33x4CV5VxDw0o/giphy.gif",
    "love": "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExZmwzejdiaWlzbXJlNnprY3Q1NGZwOXE0ejc0bWRtZmp4b25iNnJ3ayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/WS3kS825MhYMVYVyy2/giphy.gif",
    "happy": "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExMzlvYWNpY2k2eGJyZHBkeGVxNzY3dDZyNnphMG1vMm1uY2kwbGFyZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/p3ZPEgR60zYibeyqG2/giphy.gif",
    "no": "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExaG1weHFrNXdpNDhreHFkbjE4MDlhOWV2ZXhxN2piam1ramx5dG9heCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/eenRMPBYE2jy80Fur9/giphy.gif",
    "goodbye": "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExNmFtcDM2cmY0NHJ0OGpqbWl0dmdjZTNxY2I5N3cxcWlpeW8zOWhqdyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/26vIf8bHxBCzNmHhS/giphy.gif"
}

# Common phrases mapped to key ASL words
phrase_mapping: Dict[str, str] = {
    "i love you": "love",
    "thank you very much": "thank you",
    "see you later": "goodbye"
}

# Fallback image for missing ASL signs
fallback_image = "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExc28zcWMyMTliOTRkODVxZ3gyZTBwNjR0bmNyNnZwejZ5czh2aWJzaCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3zhxq2ttgN6rEw8SDx/giphy.gif"

def get_asl_image(sentence: str) -> List[str]:
    """
    Converts a sentence into ASL images.
    - Checks full phrases first.
    - Breaks down the sentence into words.
    - Finds ASL images for each word.
    - Returns a list of ASL image URLs.
    """
    sentence = sentence.lower().strip()

    # Check for full phrase match first
    if sentence in phrase_mapping:
        key_word = phrase_mapping[sentence]
        return [asl_images.get(key_word, fallback_image)]

    words = sentence.split()  # Tokenize input
    asl_results = []

    for word in words:
        # Check if word has a direct ASL sign
        if word in asl_images:
            asl_results.append(asl_images[word])
        else:
            asl_results.append(fallback_image)  # Use fallback if not found

    return asl_results
