import os
from fetchImage import getImage
from textToSpeach import generateText
from videoGeneration import generateVideo
from videoUpload import upload_to_gcs
from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post('/api/video')
async def main(request: Request):

    data = await request.json()
    player_name = data.get("player", "").strip().lower()
    if not player_name:
        raise HTTPException(status_code=400, detail="Missing 'player' parameter")
    
    lockfile = f"{player_name.replace(' ', '_')}.lock"
    if os.path.exists(lockfile):
        raise HTTPException(status_code=429, detail="Processing already in progress.")
    with open(lockfile, 'w') as f:
        f.write("processing")
    
    try:
        print("player_name", player_name)
        image_file=getImage(player_name)
        if image_file==None:
            raise HTTPException(status_code=404, detail="Image not found")
        audio_file=generateText(player_name)
        if audio_file==None:
            raise HTTPException(status_code=404, detail="Audio not found")
        video_file=generateVideo(player_name)
        if video_file==None:
            raise HTTPException(status_code=404, detail="Video not found")
        video_url=upload_to_gcs(player_name)
        

        for file in [image_file, audio_file, video_file]:
            if os.path.exists(file):
                os.remove(file)
                print(f"Deleted local file: {file}")
            else:
                print(f"File not found, skipping delete: {file}")
        return {"video_url": video_url}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        os.remove(lockfile)



