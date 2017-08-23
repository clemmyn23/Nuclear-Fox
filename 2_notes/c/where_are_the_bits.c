// where_are_the_bits.c ... determine bit-field order
// COMP1521 Lab 03 Exercise
// Written by ...

#include <stdio.h>
#include <stdlib.h>

struct _bit_fields {
    unsigned int a : 4,
                b : 8,
                c : 20;
};

int main(void)
{
   struct _bit_fields x;
   x.a = 0xf;
   x.b = 0xff;
   x.c = 0xfff;
   printf("%ul\n", (unsigned int) sizeof(x));

   return 0;
}
