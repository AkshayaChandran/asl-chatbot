# asl_converter.py

from typing import Dict

# Dictionary mapping phrases to ASL image URLs
asl_images: Dict[str, str] = {
    "hello": "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExZTZiY2l3cndhejJ1NWs3NjRjNzZ0OWZjcDV2NTJydzRhdmd1MmVyayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/DcPfy7StVKeB5dv0ND/giphy.gif",
    "thank you": "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExeHhra3ZuamRlOGZsZm9xdG9rYW9zOTVubDMzYW9uaDNqbjN3NGIxbSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3s6MJXtehv1qx1K9zd/giphy.gif",
    "sorry": "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExaTdmbmxqM2dhMzMwYXpmYTgxMDc3d3l4YTZsazU4Y3ZncXpudjB6bCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/paRJJnkjPyKxHyTCAg/giphy.gif",
    "applause": "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExbjQ4OXJpMTI2ZTNxMmdxajU2MWN3MHgzaXFjMTJ3bDU1amFpZGpvbSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/T982vDYtrs4EjCZz2H/giphy.gif",
    "yes": "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExYzJzand1cXk4emZ4enJnajByeDVzMTJxYXV2bnZ1bGJiMWVqcGM2OSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/18OMELKhQaCIFFDufn/giphy.gif",
    "please":"https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExYzJzand1cXk4emZ4enJnajByeDVzMTJxYXV2bnZ1bGJiMWVqcGM2OSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/18OMELKhQaCIFFDufn/giphy.gif",
    "love":"https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExZmwzejdiaWlzbXJlNnprY3Q1NGZwOXE0ejc0bWRtZmp4b25iNnJ3ayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/WS3kS825MhYMVYVyy2/giphy.gif",
    "happy":"https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExMzlvYWNpY2k2eGJyZHBkeGVxNzY3dDZyNnphMG1vMm1uY2kwbGFyZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/p3ZPEgR60zYibeyqG2/giphy.gif",
    "no":"https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExMzlvYWNpY2k2eGJyZHBkeGVxNzY3dDZyNnphMG1vMm1uY2kwbGFyZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/p3ZPEgR60zYibeyqG2/giphy.gif",
    "cool":"https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExNXByeXd6cTVydjhuY2NsZTFpb3RpbjFkZTZ0dWhhN2p5c3d1bWp6dyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/2scJlQhO6pWZh2vkCT/giphy.gif",
    "super":"https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExaWI4aTk3c3MxcjQyNG8zenpnd2FwbXVvb2JiYzVmOXY1YTl0NXNwcyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/WS3dGW1lTn8NUO2vu1/giphy.gif",
    "wonderful":"https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExZ3dpbzdrMnc2NHZyeWdjcWR6d2J1NWdxNXF4bXZ4dW1rc2liMWRseSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3jaXtCOGSirVlcKVNb/giphy.gif",
    "understand": "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExdGhqOTlubWZuN3V4NG03NnZsZzllMWxqMXBqdjJ3a3ZrYmIxajE4eSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/jU352ABLe7FV9yGRSd/giphy.gif",
    "ok":"https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExd2oydTJpYWVjMXlrdGs3bnAya2ttZWpxaDB0ejFpYWk5NzQ0bzdxbiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3ov9jQlcpTSe4JsVSo/giphy.gif",
    "i don't know":"https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExbDE0eXJnMzdtb2Y3ZG5uYWV2ZTg4OGpmZzBpZDY3enMwMTJoeXozZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l378vagIIWwdI7q2Q/giphy.gif",
    "music":"https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExYWY3NzkwOW1vNzY2cTRrdGJmajczOWNuNHBiNWZ5bnppMjE1eWJzMSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3ohhweMU4WkSFc4fUQ/giphy.gif",
    "agreed":"https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExMXo5ZnozeDJwbHN0cXl4MXB6bm5xMmxhaGExdHE0a2cxb2FjOTNtbCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3ov9k9ULvZQYDUQJdC/giphy.gif",
    "goodbye":"https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExNmFtcDM2cmY0NHJ0OGpqbWl0dmdjZTNxY2I5N3cxcWlpeW8zOWhqdyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/26vIf8bHxBCzNmHhS/giphy.gif"
}

def get_asl_image(phrase: str):
    """
    Returns the ASL image URL for a given phrase.
    If not found, returns None.
    """
    return asl_images.get(phrase.lower(), "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExc28zcWMyMTliOTRkODVxZ3gyZTBwNjR0bmNyNnZwejZ5czh2aWJzaCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3zhxq2ttgN6rEw8SDx/giphy.gif")
