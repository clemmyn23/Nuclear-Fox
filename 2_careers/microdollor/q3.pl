#!/usr/bin/perl -W

$num = 1;
for (<>) {
    if ($_ =~ '//----') {
        for (sort keys %currBlock) {
            if ($currBlock{$_} == $num) {
                push @curr, $_;
            }
        }

        for (sort special @curr) {
            print $_;
        }

        splice(@curr);  #empty array

        print '//----', "\n";
        $num++;

    } else {
        if ($_ =~ '//Used') {
            $currBlock{$_} = $num;
        }
    }
}

sub special {
    my $c = $a;
    my $d = $b;
    $c =~ s/;\s\/\/Used//;
    $d =~ s/;\s\/\/Used//;
    if ($c =~ $d) {
        return 1;
    }
    else {
        return $c cmp $d;
    }


}
