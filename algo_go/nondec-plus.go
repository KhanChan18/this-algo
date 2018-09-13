package main

import (
    "fmt"
    "io"
)

func main() {
    var ans [30]int
    for {
        var num1, num2, dig int
        _, err := fmt.Scanf(
            "%d %d %d",
            &num1, &num2, &dig,
        )
        if err == io.EOF {
            break
        }

        sum := num1 + num2

        n := 0
        ans[n] = sum % dig
        sum = sum / dig

        for ; sum != 0; {
            n = n + 1
            ans[n] = sum % dig
            sum = sum / dig
        }

        for i := n ; i >= 0; i-- {
            fmt.Printf("%d", ans[i])
        }
        fmt.Printf("\n");
    }
}
