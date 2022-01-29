/*
 * https://boards.4channel.org/g/thread/85435082
 *
 * can /g/ code a triforce?
 *
 * write a program that generates [a triforce made of ▲ characters]
 * for any given height
 *
 * (Jan 29, 2022)
*/

#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <wchar.h>

void tfgen(int height) {
  wchar_t t[2];
  t[0] = 0x25B2;
  t[1] = '\0';
  int og_height = height;
  int diff = height;
  int half = 0;

  while (height) {
    for (int i = height; i-1; --i)
      printf(" ");
    printf("%ls", t);

    for (int i = diff - height; i; --i) {
      if (height <= og_height / 2 && (i < og_height && i > half*2)) {
        printf(" ");
      } else {
        printf("%ls", t);
      }
    }

    if (height <= og_height / 2)
        ++half;

    if (diff != height) {
      printf("%ls", t);
      ++diff;
    }
    printf("\n");
    --height;
  }
}

int main (int argc, char *argv[]) {
  if (argc != 2) return -1;
  setlocale(LC_ALL, "");
  int height = atoi(argv[1]);
  tfgen(height);
}
