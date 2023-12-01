#!/bin/bash

exit=0

while [ $exit = 0 ]
    do
    echo "Please choose an option"
    echo "1: Print hello world"
    echo "2: Ping self"
    echo "3: IP info"
    echo "4: Exit"
    read input
        if [ $input = 1 ]
            then
            echo "Hello World"
        fi
    
        if [ $input = 2 ]
            then
            ping 127.0.0.1 -c3
        fi

        if [ $input = 3 ]
            then
            ip a
        fi

        if [ $input = 4 ]
            then
            exit=1
        fi
    done
