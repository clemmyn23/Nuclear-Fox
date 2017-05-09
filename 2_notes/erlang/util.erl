
-module(util).
-export([cls/0]).

cls() ->
    io:format("\033[2J"),
    os:cmd(clear).
