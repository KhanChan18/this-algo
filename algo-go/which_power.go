package main

import "fmt"

const MAX_LEN = 100000

func main() {
    var school [MAX_LEN]int;
    var n, schid, score int;
    fmt.Scanf("%d", &n);
    for i := 0; i < n; i++ {
        fmt.Scanf("%d %d", &schid, &score);
        school[schid] += score;
    }

    k := 0;
    MAX := -1;
    for i := 0; i < n; i++ {
        if (school[i] > MAX) {
            MAX = school[i];
            k = i;
        }
    }
    fmt.Printf("%d %d\n", k, MAX);
}
