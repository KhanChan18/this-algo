package main

import (
    "fmt"
    "io"
)

func isLeap(year int) bool {
    period_4 := year % 4 == 0
    period_100 := year % 100 != 0
    period_400 := year % 400 == 0

    return (period_4 && period_100) || period_400
}

func bool2int(val bool) int {
    if val == true {
        return 1
    } else {
        return 0
    }
}

func main() {
    calen := [13][2]int {
        {0, 0},   {31, 31}, {28, 29}, // Month 0, 1, 2, (0 to hold place)
        {31, 31}, {30, 30}, {31, 31}, // Month 3, 4, 5,
        {30, 30}, {31, 31}, {31, 31}, // Month 6, 7, 8,
        {30, 30}, {31, 31}, {31, 31}, // Month 9, 10, 11, 12
        {31, 31},
    }

    var time1, y1, m1, d1 int
    var time2, y2, m2, d2 int

    for {
        _, err := fmt.Scanf("%d\n%d", &time1, &time2)
        if err == io.EOF {
            break
        }
        if time1 > time2 {
            temp := time1
            time1 = time2
            time2 = temp
        }
        y1 = time1 / 10000
        y2 = time2 / 10000
        m1 = time1 % 10000 / 100
        m2 = time2 % 10000 / 100
        d1 = time1 % 100
        d2 = time2 % 100
        ans := 1;
        for ;(y1 < y2 || m1 < m2 || d1 < d2); {
            d1 = d1 + 1
            if d1 == calen[m1][bool2int(isLeap(y1))] + 1 {
                m1 = m1 + 1
                d1 = 1
            }

            if m1 == 13 {
                y1 = y1 + 1
                m1 = 1
            }
            ans = ans + 1
        }
        fmt.Printf("%d\n", ans)
    }
}
