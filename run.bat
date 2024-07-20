@echo off
rem chrome

REM pytest -s -v -m "sanity and regression" --html=./Reports/report.html testCases/ --browser chrome
pytest -s -v -m "sanity" --html=./Reports/report.html testCases/ --browser chrome
REM pytest -s -v -m "regression" --html=./Reports/report.html testCases/ --browser chrome
REM pytest -s -v -m "sanity or regression" --html=./Reports/report.html testCases/ --browser chrome

rem internet explore
REM pytest -s -v -m "sanity and regression" --html=./Reports/report.html testCases/ --browser ie
pytest -s -v -m "sanity" --html=./Reports/report.html testCases/ --browser ie
REM pytest -s -v -m "regression" --html=./Reports/report.html testCases/ --browser ie
REM pytest -s -v -m "sanity or regression" --html=./Reports/report.html testCases/ --browser ie
pause