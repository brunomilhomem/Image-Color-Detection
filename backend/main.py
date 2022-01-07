import cv2
import uvicorn
from fastapi import File
from fastapi import FastAPI
from fastapi import UploadFile
from pydantic import BaseModel
from PIL import Image
import os


import colorDetector


class colorDetect(BaseModel):
    x: list
    y: list
    image_name: str


app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome from the API"}


# save the image file
@app.post("/upload")
async def get_image(file: UploadFile = File(...)):
    image = Image.open(file.file).convert('RGB')
    try:
        image.save(f"./storage/{file.filename}")
        return {"status": "success", "message": "Uploaded Successfully", "filename": file.filename}
    except OSError as e:
        return {"status": "failed", "message": "Uploaded Failed retry again\n" + str(e), "filename": file.filename}


# get x,y,image_name return the color name
@app.post("/detect")
async def detect_color(body: colorDetect):
    img = cv2.imread(f"./storage/{body.image_name}")
    color_names = []
    for index, value in enumerate(body.x):
        r, g, b = colorDetector.mouse_click(int(value), int(body.y[index]), img)
        color_names.append(colorDetector.recognize_color(r, g, b))
    return {"color_names": color_names}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=os.environ.get("PORT"))
