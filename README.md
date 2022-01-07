# Image Color Detection
Setup Steps
- python -m pip install -r backend/requirements.txt
- python -m pip install -r frontend/requirements.txt

#Heroku Build and Deployment From Apple M1

- docker buildx build --platform linux/amd64 -t color-detection-backend.
- docker tag color-detection-backend registry.heroku.com/color-detection-backend/web
- docker push registry.heroku.com/color-detection-backend/web
- heroku container:release web -a color-detection-backend
- heroku container:rm web -a color-detection-backend

# Streamlit URL: https://share.streamlit.io/nish97/image-color-detection/frontend/main.py
# Heroku URL: https://color-detection-backend.herokuapp.com