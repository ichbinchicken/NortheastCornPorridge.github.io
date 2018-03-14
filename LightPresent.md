## Simple Format Print exploit
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
 * We can manipulate the variable in memory in printf.
 */
int target;
void hacking(char *string) {
    printf(string);
    if (target) printf("target has been modified: \n");
}

int main(int argc, char *argv[]) {
    hacking(argv[1]);
    return 0;
}
```
* Try `argv[1] = "%x %x %x"`
* We can find it is a memory leak vulnerability.
* What values are the `printf` reading?
    * Whatever `printf` can find on the stack.
* Spec of `printf` on Linux Manual `man 3 printf`
```
Code such as printf(foo); often indicates a bug, since foo may contain a % 
character. If foo comes from untrusted user input, it may contain %n, causing 
the printf() call to write to memory and creating a security hole.
```
* What is `"%n"`?
```
It writes the amount of characters that were already printed into a variable.
```
For example,
```c
#include <stdio.h>
int main(void) {
    int num;
    printf("Hello %n World\n", &num);
    printf("num = %d\n", num);
    return 0;
}
