# API Server Control Script
A rudimentary control script is supplied, suitable for development use on Linux
systems. The script supports the standard start, stop, and status functions,
and if `lsof` is available, will also find processes listening on the port used
by the system.
```bash
./ai-engineer-ctrl start|stop|status|listeners
```

```
USAGE:
./ai-engineer-ctrl
    start      launch the server
    stop       stop a running server
    status     print the current process tree
    listeners  find processes listening on 8001
```

## Start
```bash
./ai-engineer-ctrl start
```

The `start` command launches the API server.

It will fail if the port configured in environment variables is not available.
In that case, use the `listeners` command to see what is listening on the port.
The `lsof` system command is required by `listeners`.

## Stop
```bash
./ai-engineer-ctrl stop
```

If the process IDs in `ai-engineer-ctl.pid` are correct, the `stop` command
will gracefully terminate the system.

## Status
```bash
./ai-engineer-ctrl status
```

Use `status` to see a tree of processes launched by `start`. This requires the
`proctree` system command.

## Listeners
```bash
./ai-engineer-ctrl listeners
```

If `start` fails because the port is busy, use the `listeners` command to see
which process has it tied up.

## Logs
The `start` command redirects both `stdout` and `stderr` to a log file at
`ai-engineer-ctrl.log`. Use `cat` or `tail` to view the contents of the file.

```bash
cat ai-engineer-ctrl.log
```

```bash
tail -f ai-engineer-ctrl.log
```

```bash
tail -50 ai-engineer-ctrl.log
```


