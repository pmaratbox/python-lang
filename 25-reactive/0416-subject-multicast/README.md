# 0416 — Subject Multicast

Implement a Subject that multicasts each emission to all current observers; two observers both receive 1 then 2. In Python the Subject just holds a list of observers and iterates it on each `next`, so the loop order gives obs1 before obs2 per value.

## Run

    python3 main.py
