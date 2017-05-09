-module(tables).
-export([start/0]).


f(1) -> one;
f(2) -> two.

start() ->

    ets:new(mytable, [set, named_table, private]),
    ets:insert(mytable, {key1, a}),
    ets:insert(mytable, {key2, b}),
    ets:insert(mytable, {key3, a}),

    A = ets:match(mytable, '$1'),
    io:fwrite("table1: ~w~n", [A]),


    Caught1 = (catch ets:lookup(mytable, invalidkey)),
    io:fwrite("caught ~w~n", [Caught1]),

    Caught2 = (catch ets:lookup(mytable, key1)),
    io:fwrite("caught ~w~n", [Caught2]),

    Uncaught1 = ets:lookup(mytable, invalidkey),
    io:fwrite("uncaught ~w~n", [Uncaught1]),

    Uncaught2 = (catch ets:lookup(mytable, key1)),
    io:fwrite("uncaught ~w~n", [Uncaught2]),



    %
    Tid1 = ets:new(roottable, [set, named_table, private]),
    ets:insert(roottable, {key1, a}),
    ets:insert(roottable, {key2, b}),

    R1 = ets:tab2list(Tid1),
    R2 = ets:tab2list(roottable),
    io:fwrite("~w~n~w~n", [R1, R2]),

    spawn(fun() ->
        ets:new(roottable, [set, private])



    end),




    ets:new(emptylist, [set, named_table, private]),
    lists:unzip(ets:tab2list(emptylist)).

    %
    % T1 = spawn(fun() ->
    %     % timer:sleep(2000),
    %     % Res = ets:tab2list(roottable),
    %     % io:fwrite("pid ~w roottable: ~w~n", [self(), Res])
    %     ok
    %
    %     % ets:new(childtable, [set, named_table, private]),
    %     % ets:insert(childtable, {key2, b}),
    %     % io:fwrite("child thread table created~n")
    % end),
    % possible race condition here
    % ok.
    % timer:sleep(500),
    % ets:tab2list(childtable).



    % ok.
    % % [Result|_] = ets:lookup(mytable, key4),
    %
    %
    % Res = ets:member(mytable, invalidkey),
    % io:fwrite("mytable has member invalidkey: ~w~n", [Res]),
    %
    % ets:new(mytable2, [set, named_table, private]),
    % {_, B} = lists:unzip(ets:tab2list(mytable2)),
    % sets:to_list(sets:from_list(B)).
    %



    % spawn(fun() ->
    %     ets:new(mytable, [set, named_table, private]),
    %     ets:insert(mytable, {key1, a}),
    %     ets:insert(mytable, {key2, b}),
    %     ets:insert(mytable, {key3, c}),
    %
    %     A = ets:match(mytable, '$1'),
    %     io:fwrite("table1: ~w~n", [A]),
    %
    %     [Result|_] = ets:lookup(mytable, key4),
    %     io:fwrite("lookup result: ~w~n", [Result]),
    %
    %     lists:unzip(ets:to_list(mytable))
    %
    %
    %     % List1 = ets:tab2list(mytable),
    %     %
    %     % ets:new(mytable2, [set, named_table]),
    %     % ets:insert(mytable2, List1),
    %     % B = ets:match(mytable2, '$1'),
    %     %
    %     % ets:insert(mytable, {key4, d}),
    %     % A = ets:match(mytable, '$1'),
    %     % io:fwrite("table1: ~w~n", [A]),
    %     % io:fwrite("table2: ~w~n", [B]),
    %     %
    %     % ets:match_delete(mytable, '$1'),
    %     % C = ets:match(mytable, '$1'),
    %     % io:fwrite("cleaned table1: ~w~n", [C]),
    %     %
    %     % ets:insert(mytable, List1),
    %     % D = ets:match(mytable, '$1'),
    %     % io:fwrite("restored table1: ~w~n", [D])
    % end).

    %
    % spawn(fun() ->
    %     io:fwrite("spawning"),
    %     ets:new(mytable, [set, named_table, private]),
    %     E = ets:match(mytable, '$1'),
    %     io:fwrite("spawned table1: ~w~n", [E])
    % end).
