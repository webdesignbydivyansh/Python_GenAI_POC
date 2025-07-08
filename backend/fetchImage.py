import requests

def getImage(player_name):
    # TheSportsDB free API
    API_URL = "https://www.thesportsdb.com/api/v1/json/3/searchplayers.php"

    # Call the API
    response = requests.get(API_URL, params={"p": player_name})
    data = response.json()

    # Extract image URL
    player = data["player"][0]
    print("Name:", player["strPlayer"])
    print("Team:", player["strTeam"])
    print("Image URL:", player["strThumb"])

    # Download the image
    image_url = player["strThumb"]
    if image_url:
        img_data = requests.get(image_url).content
        file_name = f"{player_name.replace(' ', '_')}.jpg"
        with open(file_name, "wb") as f:
            f.write(img_data)
        print(f"Saved image as {player_name.replace(' ', '_')}.jpg")
        return file_name
    else:
        print("No image found.")
        return None