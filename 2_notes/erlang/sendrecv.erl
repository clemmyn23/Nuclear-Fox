-module(sendrecv).
-export([start/0]).

start() ->

    self() ! {hello1},
    self() ! {hello2},

    % receive
    %     {Any1, Any2} ->
    %         io:fwrite("~w message1: ~w ~w~n", [self(), Any1, Any2])
    % end,
    % receive
    %     {Any3} ->
    %         io:fwrite("~w message1: ~w ~n", [self(), Any3])
    % end,
    %
    % spawn(fun()->
    %     receive
    %         Any4 ->
    %             io:fwrite("~w message2: ~w~n", [self(), Any4])
    %     end
    % end),

    F = fun(F) ->
        self() ! hello,
        receive hello -> ok end,
        io:fwrite("got~n"),
        F(F)
    end,
    F(F),

    A = [a,fd,f,n,a,e,h,d,b,r,a,a,a,b,e,w,g,d,r],
    io:fwrite("~w~n", [A]),
    sets:to_list(sets:from_list(A)),


    lists:foreach(fun(X) -> io:fwrite("~w~n", [X]) end, [a,b,c,d,e]).
