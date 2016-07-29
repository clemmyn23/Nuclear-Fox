#include <stdio.h>
#include <stdlib.h>

int main (int argc, char *argv[]) {

    // the original
    int magic_number = 0xaabbccdd;
    
    printf ("%p  0x%x\n", &magic_number, magic_number);
    
    // get pointer
    int *magic_pointer = &magic_number;
    printf("%p  0x%x\n", magic_pointer, *magic_pointer);
    
    // cast int ptr into char ptr
    char *small_pointer = (char *) magic_pointer;
    printf ("%p  0x%x\n", small_pointer, *small_pointer);
    
    // pointer deref and manipulation
    char *temp_ptr = small_pointer;
    printf ("%p  0x%x  0x%hhx\n", temp_ptr, *temp_ptr, *temp_ptr);       // use %hhx to force type to char
    temp_ptr++;
    printf ("%p  0x%x  0x%hhx\n", temp_ptr, *temp_ptr, *temp_ptr);
    temp_ptr++;
    printf ("%p  0x%x  0x%hhx\n", temp_ptr, *temp_ptr, *temp_ptr);
    temp_ptr++;
    printf ("%p  0x%x  0x%hhx\n", temp_ptr, *temp_ptr, *temp_ptr);
    
    temp_ptr++;
    printf ("%p  0x%x  0x%hhx out-of-bounds\n", temp_ptr, *temp_ptr, *temp_ptr);
    
    return 0;
}