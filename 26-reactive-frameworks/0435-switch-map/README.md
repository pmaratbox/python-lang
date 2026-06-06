# 0435 — SwitchMap

Use the library's switchMap on a virtual/test scheduler so a new outer value cancels the previous inner stream. Built with RxPY (reactivex) using `ops.map` + `ops.switch_latest` on a `TestScheduler`.

## Run

    python3 main.py
