export AUDIO_IN='/home/myke/tmp/input'
export AUDIO_OUT='/home/myke/tmp/output'
export MODEL_DIRECTORY='/home/myke/tmp/model'

docker run \
    -v $AUDIO_IN:/input \
    -v $AUDIO_OUT:/output \
    -v $MODEL_DIRECTORY:/model \
    -e MODEL_PATH=/model \
    researchdeezer/spleeter \
    separate -i /input/song.mp3 -o /output

