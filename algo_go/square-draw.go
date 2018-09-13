package main

import "fmt"

func main() {
    var col, row int;
    var mark string;
    fmt.Scanf("%d%s", &col, &mark);

    if (col % 2 == 1) {
        row = col / 2 + 1;
    } else {
        row = col / 2;
    }

    //Line 0
    for i := 0; i < col; i++ {
        fmt.Printf("%s", mark);
    }
    fmt.Println();

    //Lines in the middle
    for i := 0; i < row - 2; i++ {
        fmt.Printf("%s", mark);
        for j := 0; j < col -2 ; j++ {
            fmt.Printf(" ");
        }
        fmt.Printf("%s\n", mark);
    }

    //Line N-1
    for i := 0; i < col; i++ {
        fmt.Printf("%s", mark);
    }
    fmt.Println();

}
