# Is This Available?

Have you ever started a project, thought of a great name, and then realized that the name was taken for the domain you wanted? Or maybe the social media account name? Well this is designed to relieve that issue!

Currently, it checks for the following TLDs:
- .com
- .net
- .org
- .ai
- .io
- .xyz
- .dev

and the following social media:
- [Instagram](https://instagram.com)
- [Youtube](https://youtube.com)
- [Facebook](https://facebook.com)
- [TikTok](https://tiktok.com)
- [Twitch](https://twitch.tv)
- [Bluesky](https://bsky.app)
- [LinkedIn](https://linkedin.com)

## Tools
- **Streamlit** for UI
- **Streamlit Community Cloud** for hosting
- **Docker** for containerization

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