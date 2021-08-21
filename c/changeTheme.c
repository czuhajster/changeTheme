/* This file defines the functions for changing theme in alacritty and vim.
*/

#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

char *trim(char *);

int main() {
    FILE *ptr;
    char line[100], temp[100];

    if ((ptr = fopen("/Users/arek/.config/alacritty/alacritty.yml", "r+")) == NULL) {
        printf("%s", "Error opening the file!");
        exit(0);
    }

    while (fgets(line, 100, ptr)) {
        if (strncmp(line, "colors:", 7) == 0)
            break;
        printf("%s", line);
    }
    printf("Found\n");

    while (fgets(line, 100, ptr)) {
        if (strncmp(line, "   primary:", 11) == 0)
            break;
        printf("%s", line);
    }
    printf("Found primary\n");

    while (fgets(line, 100, ptr)) {
        if (strncmp(line, "   normal:", 10) == 0)
            break;
        printf("%s", line);
    }
    printf("Found normal\n");

    while (fgets(line, 100, ptr)) {
        if (strncmp(line, newColour, 10) == 0)
            break;
        printf("%s", line);
    }
    printf("Found normal\n");

    fclose(ptr);

}

char *trim(char *str) {
    while (isspace((unsigned char)*str)) str++;
    return str;
    
}
