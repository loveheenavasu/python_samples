
import requests

jokes = ["iuygftghjkl", "jiuygtfgvhbjnmk", 'iuyftgvhbjnkm', 'koiuygtfgvhbj', 'iuytfdrhbjnklmk', 'ojiugyftcgvhbjnk', 'ojiugyftcgvhbjnkm', 'ioyftdvhbjnkml', 'ijuhygtfdrjk', 'ojiuytfdrdrfghbjn', 'oiuytrdfgvhbjnkm', 'ijuytdrfcgvhbjnkmjbhvgfx', 'kjyftdrtfyuijoklmkm']
# https://api.telegram.org/bot6269557659:AAEVBiPrBpXgOZr0PEVwtU2W7BsVPHxqFzo/sendMessage?chat_id=-882710570

for joke in jokes:
    print(joke)
    base_url = "https://api.telegram.org/bot6269557659:AAEVBiPrBpXgOZr0PEVwtU2W7BsVPHxqFzo/sendMessage?chat_id=-882710570&text='{}'".format(joke)
    print(base_url)
    requests.get(base_url)