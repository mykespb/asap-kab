Face Detection using OpenCV Ver.1
========================================

М.Колодин

2020-06-21 2020-06-25 вер. 2.

Взята готовая программка (автор исходника -- Adarsh Menon), перенастроена и проверена.

Инструменты:
python3, OpenCV

Install
-------------------

a. Use virtualenv, e.g.
source venv/bin/activate

(aftere:
deactivate)

b. install software

pip install -r requirements.txt

c. Install ffmpeg or any other software for video convertion.

See ffmpeg.org . 

Photo processing
----------------------

Результат неплохой,
но трудно подобрать хорошие параметры для уровня распознавания.
Есть недообнаруженные и неправильно обнаруженные лица на фото,
но большинство -- правильно.

Есть 2 нормальной обработанных примера с фестиваля под Сосновым Бором.

Video processing
-----------------------

a. Convert long video to short one with
ffmpeg -t 10 -i input.avi output.avi
(or use mp4 instead of avi)

b. Run
python ./detect_face_video.py

Please make screenshots when needed.


