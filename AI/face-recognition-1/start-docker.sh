docker run \
   -v /home/myke/bards/bardswork/2020-ark/AI/face-recognition-1/dataset-image:/root/dataset-image \
   -v /home/myke/bards/bardswork/2020-ark/AI/face-recognition-1/images:/root/images \
   -p 9000:9000 -p 8000:8000 \
   -t -i bamos/openface /bin/bash
#   -v /home/myke/bards/bardswork/2020-ark/AI/face-recognition-1:/root/openface \

