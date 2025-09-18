DB Script
create user usertest with NOINHERIT LOGIN ENCRYPTED PASSWORD 'usertest222';
create database dbtest owner=usertest;

--> How to run 
# uvicorn main:app --reload