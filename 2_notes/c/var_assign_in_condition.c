#include <stdio.h>
#include <stdlib.h>

int main() {
	char *demo;
	if ((demo = NULL) == NULL) {
		printf("null assignment inside conditional check works?\n");
	} else {
		printf("it no work u.u \n");
	}


	return 0;
}
