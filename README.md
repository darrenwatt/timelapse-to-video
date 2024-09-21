# timelapse-to-video
Glues a bunch of timelapse images into a video file

Based on code by [James Lloyd](https://james.lloyd.ws/)

## pre-requisites - working ffmpeg install
`sudo apt-get update && sudo apt-get install ffmpeg libsm6 libxext6 -y`

You probably want to do that in a virtual environment.
Not needed if running in docker.

## Running from Docker image:

Build docker image if you need to with:
`docker build -t darrenwatt/timelapse-to-video:v0.0.1 .`

Or pull and run from Dockerhub with this:
`docker run --rm -v '/home/username/photos-are-here:/data'  darrenwatt/timelapse-to-video:v0.0.1`

Output goes in /data/video, this directory needs to exist.

Put into a crontab to set it off when you need to, daily or whatever.
