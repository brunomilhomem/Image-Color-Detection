import requests
import pandas as pd
import streamlit as st
from PIL import Image
from streamlit_drawable_canvas import st_canvas
import os

uploaded = False

url = os.environ.get("URL")

st.title("Image Color Detection Web Application")

image = st.file_uploader("Choose an image")

if image is not None:
    files = {"file": (image.name, image.getvalue())}
    if not uploaded:
        res = requests.post(f"{url}upload", files=files)
        st.title(res.json()['message'])
        if res.json()['status'] == "success":
            uploaded = True
        else:
            uploaded = False

    if uploaded:
        bg_image = Image.open(image)
        width, height = bg_image.size

        canvas_result = st_canvas(
            stroke_width=3,
            background_image=bg_image,
            height=height,
            width=width,
            drawing_mode="circle",
            key="color_annotation_app",
        )
        df = pd.json_normalize(canvas_result.json_data["objects"])

        if df.size > 0:
            detect_resp = requests.post(f"{url}detect",
                                        json={"x": df['left'].tolist(),
                                              "y": df['top'].tolist(),
                                              "image_name": res.json()['filename']
                                              })

            df['color_name'] = pd.Series(detect_resp.json()['color_names'])
            st.dataframe(df[['left', 'top', 'color_name']])
