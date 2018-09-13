package main

import (
    "fmt"
    "io"
)

const MAX_LEN = 200;

func main() {
    var arr_len int;
    var arr [MAX_LEN] int;
    for {
        _, err := fmt.Scanf("%d", &arr_len);
        if err == io.EOF {
            break;
        }
        for i := 0; i < arr_len; i++ {
            fmt.Scanf("%d", &arr[i]);
        }

        var targ, j int;
        fmt.Scanf("%d", &targ);
        for j := 0; j < arr_len; j++ {
            if arr[j] == targ {
                fmt.Printf("%d\n", j);
                break;
            }
        }

        if j == arr_len {
            fmt.Printf("-1\n");
        }
    }
}
