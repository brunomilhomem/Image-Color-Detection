# Image Color Detection
_Color detection using python. The final user will be able to upload any image and recognite the color itself and RGB number._

# Installation

```sh
python -m pip install -r backend/requirements.txt
python -m pip install -r frontend/requirements.txt
```

# Heroku Build and Deployment From Windows

- docker buildx build --platform linux/amd64 -t color-detection-backend.
- docker tag color-detection-backend registry.heroku.com/color-detection-backend/web
- docker push registry.heroku.com/color-detection-backend/web
- heroku container:release web -a color-detection-backend
- heroku container:rm web -a color-detection-backend