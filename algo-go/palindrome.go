package main

import (
    "fmt"
    "io"
)

func ispalindrome(str string) bool {
    for i := 0; i < len(str) / 2; i++ {
        if str[i] != str[len(str) - i - 1] {
            return false
        }
    }
    return true;
}

func main() {
    var targ string;
    for {
        _, err := fmt.Scanf("%s", targ)
        if err == io.EOF {
            break
        }
        flag := ispalindrome(targ)
        if flag {
            fmt.Printf("YES\n")
        } else {
            fmt.Printf("NO\n")
        }
    }
}
