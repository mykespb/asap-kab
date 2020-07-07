#!/bin/bash
echo ASAP-KAB project
echo Study www.bards.ru site

echo Step 1 - get persons
echo make database, version for all persons

sqlite3 brtall.db < brta-db1.sql

echo database creation completed
