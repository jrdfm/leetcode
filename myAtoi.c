#include <stdio.h>
#include <string.h>


int myAtoi(char* s) {
    int INT_MAX =  2147483647;
    int INT_MIN = -2147483648;
    int result = 0;
    int sign = 1;
    int i = 0;
    while (i < strlen(s) && s[i] == ' ')
        i++;  
    if (strlen(s) == i) 
        return result;
    if (s[i] =='+' || s[i] == '-') { 
        sign = (s[i] == '+') ? 1 : -1;
        i++;
    }
    
    while (i < strlen(s) && s[i] >= '0' && s[i] <= '9') {
        if (result > (INT_MAX - (s[i] - '0'))/10) 
            return (sign == 1) ? INT_MAX : INT_MIN;  
        result = result * 10 + (s[i] - '0');
        i++;
    }
    
    return sign * result;
}



int main() {
    char *arr[6];
    arr[0] = "-91283472332";
    arr[1] = "4193 with words";
    arr[2] = "   -42";
    arr[3] = ".words and 987";
    arr[4] = "91283472332"; 
    arr[5] = "3.14159";

    for (int i = 0; i < 6; i++)
    {
        printf("%d\n",myAtoi(arr[i]));
    }
    
    
}
