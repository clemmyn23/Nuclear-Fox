-module(pkiller).
-export([start/0]).

start() ->
    io:fwrite("spawning thread to print hello every second~n"),
    io:fwrite("killing spawned thread in 10 seconds~n"),
    Pid = spawn(fun() -> F = fun(F) -> io:fwrite("hello~n"), timer:sleep(1000), F(F) end, F(F) end),

    timer:sleep(10000),
    io:fwrite("killing thread..."),
    erlang:exit(Pid, kill).
