package main

import (
    "fmt"
    "bufio"
    "os"
    "strings"
    "runtime"
)

func main() {
    inputReader := bufio.NewReader(os.Stdin)
    input, _ := inputReader.ReadString('\n')
    runtime.Breakpoint()

    input = strings.Trim(input, "\n")
    words := strings.Split(input, " ")

    for i := len(words) - 1; i >= 0; i-- {
        fmt.Printf("%s", words[i])
        if i != 0 {
            fmt.Printf(" ")
        }
    }
    fmt.Printf("\n");
}
