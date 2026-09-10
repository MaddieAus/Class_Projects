//#define clearBuffer() while (getchar() != '\n');
#include <stdio.h>
//#include <stdlib.h>
//#include <stdbool.h>
#include <string.h>
#include "tests.h"
#include "code.h"
// ----------------- MAIN PROGRAM -----------------

int main(int argc, char *argv[]) 
{
    int failed_tests  = 0;
    if (argc > 1 )
    {
        if(strcmp(argv[1], "--test") == 0) 
           failed_tests = run_unity_tests();
        else if(strcmp(argv[1], "--author") == 0) 
            printf(AUTHOR_NAME);
        else if(strcmp(argv[1], "--authorship") == 0) 
            printf(AUTHOR_AUTHORSHIP);
        else if(strcmp(argv[1], "--help") == 0) 
            printf("\n  --test\tRun unit tests\n  --author\tPrint author name\n  --authorship\tPrint academic honesty statement\n  --help\tShow this help message--test, --author, --authorship\n\n");
    }
    else
    {
        printf("Wrong parameter. Use --help to see available options.\n");
        return 1; // Wrong parameter
    }

    //run_unity_tests();
    //getchar(); // pause before exit (Windows)

    return failed_tests; // cmd/powershell:  echo $LASTEXITCODE
}

