# 0434 — FlatMap (mergeMap)

Use the library's flatMap/mergeMap on a virtual/test scheduler, mapping each outer value to a timed inner stream and merging them. Built with RxPY (reactivex) using `ops.flat_map` over a `TestScheduler` with hot/cold virtual-time observables.

## Run

    python3 main.py
