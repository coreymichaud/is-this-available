# Is This Available?

## Install

Clone the repo, then `cd` into the folder. From there, build the Docker image:
```{bash}
docker build -t is-this-available .
```

## Run
Start the container:
```{bash}
docker run -p 8501:8501 is-this-available
```

