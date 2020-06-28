export AUDIO_IN='/home/myke/bards/bardswork/2020-ark/AI/spleeter-1/docker-spleeter/input'
export AUDIO_OUT='/home/myke/bards/bardswork/2020-ark/AI/spleeter-1/docker-spleeter/output'
export MODEL_DIRECTORY='/home/myke/bards/bardswork/2020-ark/AI/spleeter-1/docker-spleeter/model'

docker run \
    -v $AUDIO_IN:/input \
    -v $AUDIO_OUT:/output \
    -v $MODEL_DIRECTORY:/model \
    -e MODEL_PATH=/model \
    researchdeezer/spleeter \
    separate -i /input/kukin-poezd.mp3 /input/kukin-zatumanom.mp3 -o /output

