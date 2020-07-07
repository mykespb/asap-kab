-- sqlite3 for asap/kab project
-- получение информации с сайта www.bards.ru
-- 1 этап -- получение спсика персон

drop table if exists personsd;
create table personsd (
pid,
page,
fio,
desc,
bio,
dbirth,
ddeath,
place
);
