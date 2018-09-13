package main

import (
    "fmt"
    "strings"
)

func main() {
    var input string
    fmt.Scanf("%s", &input)
    fmt.Printf("%s", input)

    words := strings.Split(input, " ")

    for i := len(words) - 1; i >= 0; i-- {
        fmt.Printf("%s", words[i])
        if i != 0 {
            fmt.Printf(" ")
        }
    }
    fmt.Printf("\n");
}
