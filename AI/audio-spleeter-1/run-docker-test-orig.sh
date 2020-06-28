#/bin/bash

# starter for docker for splitting voice and music
# origin: https://github.com/deezer/spleeter/wiki/2.-Getting-started
# borrowed and tuned by Mikhail (myke) Kolodin
# ver. 2020-06-28 1.0

# specify you directories here

export AUDIO_IN='/path/to/directory/with/audio/file'
export AUDIO_OUT='/path/to/write/separated/source/into'
export MODEL_DIRECTORY='/path/to/model/storage'

# write paths to your input files here
# and run docker

docker run \
    -v $AUDIO_IN:/input \
    -v $AUDIO_OUT:/output \
    -v $MODEL_DIRECTORY:/model \
    -e MODEL_PATH=/model \
    researchdeezer/spleeter \
    separate -i /input/kukin-poezd.mp3 /input/kukin-zatumanom.mp3 -o /output

# listen to the results in 2* directories in ~/output

