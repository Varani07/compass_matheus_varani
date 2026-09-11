package main

import "core:fmt"
import "core:os"
import "core:strings"
import "core:strconv"
import "core:math/rand"

main :: proc() {
    buf := make([]byte, 2048)
    defer delete(buf)

    if total_read, err := os.read(os.stdin, buf); err == nil {
        input_str := strings.trim_space(string(buf[:total_read]))
        parts := strings.split(input_str, "\n")
        defer delete(parts)

        my_points, err_parse := strconv.parse_int(parts[0])
        challanger_points, err_parse_2 := strconv.parse_int(parts[1])

        if challanger_points - my_points > 1 {
            fmt.print("quit")
        } else {
            options := [?]string{"rock", "scissor", "paper"}
            opt_id := rand.uint32_max(len(options) - 1)
            fmt.print(options[opt_id])
        }
    } else {
        fmt.print("quit")
    }
}

// package main
//
// import "core:bufio"
// import "core:fmt"
// import "core:os"
//
// main :: proc() {
//     reader: bufio.Reader
//     bufio.reader_init(&reader, os.to_stream(os.stdin))
//
//     for {
//         line, err := bufio.reader_read_string(&reader, '\n')
//
//         if err != nil {
//             break
//         }
//
//         fmt.print(line)
//     }
//
//     bufio.reader_destroy(&reader)
// }
