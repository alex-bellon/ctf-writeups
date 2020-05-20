       identification division.
          program-id. otp.

       environment division.
           input-output section.
           file-control.
               select key-file assign to 'key.txt' # keyfile = key.txt
               organization line sequential. # sequential - records are accessed in same order they are inserted

       data division.
           file section.
           fd key-file. # file name
           01 key-data pic x(50). # 01 - record description entry, pic x(50) - alphanumeric, 50 bytes

           working-storage section. # temporary vars and file structures
           01 ws-flag pic x(1). # flag is a 1 byte alphanumeric var
           01 ws-key pic x(50). # key is a 50 byte alphanumeric var
           01 ws-parse. # group item
                05 ws-parse-data pic S9(9). # 05 - elementary item in group, S - sign, 9 - number, of length 9
           01 ws-xor-len pic 9(1) value 1. # xor-len is a 1 byte number = 1
           77 ws-ctr pic 9(1). # ctr is 1 byte number

       procedure division.
           open input key-file.
           read key-file into ws-key end-read. # key = read(key-file)

           display 'Enter your message to encrypt:'.
           move 1 to ws-ctr. # ctr++
           perform 50 times
               call 'getchar' end-call
               move return-code to ws-parse # parse = getchar
               move ws-parse to ws-flag # flag = parse

               call 'CBL_XOR' using ws-key(ws-ctr:1) ws-flag by value # flag = xor(key[ctr], flag) limited to 1 byte (xor-len)
               ws-xor-len end-call

               display ws-flag with no advancing # print(flag, separator='')
               add 1 to ws-ctr end-add # ctr++
           end-perform.

       cleanup.
           close key-file.
           goback.
       end program otp.
