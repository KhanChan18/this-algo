package main

import (
    "fmt"
)

func main() {
   var n, step int;
   fmt.Scanf("%d", &n);

   for ; (n != 1); {
       if n % 2 == 0 {
           n = n / 2;
       } else {
           n = (3 * n + 1) / 2
       }
       step++;
   }
   fmt.Printf("%d\n", step);
}
