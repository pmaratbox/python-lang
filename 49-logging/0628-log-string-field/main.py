import structlog, io, json, logging

buf = io.StringIO()
structlog.configure(
    processors=[structlog.processors.add_log_level, structlog.processors.JSONRenderer()],
    wrapper_class=structlog.make_filtering_bound_logger(logging.INFO),
    logger_factory=structlog.PrintLoggerFactory(file=buf),
)

log = structlog.get_logger()
log.info("login", user="alice")
# captured JSON line: {"user":"alice","event":"login","level":"info"}

INTERNAL = {"event", "level"}


def norm(d):
    lvl = d["level"]
    lvl = {"warning": "warn", "information": "info"}.get(lvl, lvl)
    msg = d["event"]
    fields = "".join(f"|{k}={d[k]}" for k in sorted(d) if k not in INTERNAL)
    return f"{lvl}|{msg}{fields}"


for line in buf.getvalue().splitlines():
    print(norm(json.loads(line)))
