echo "starting processing..."
python3 ./proc3a.py ./ap-2010-2013.txt  ./out-ap-2010-2013.tab
python3 ./proc3a.py ./ap.2004-2010.txt  ./out-ap.2004-2010.tab
python3 ./proc3a.py ./ap-2013endu.txt   ./out-ap-2013endu.tab
python3 ./proc3a.py ./ap2014u.txt       ./out-ap2014u.tab
echo "all done."
