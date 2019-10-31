/*
문제 설명
2016년 1월 1일은 금요일입니다. 2016년 a월 b일은 무슨 요일일까요? 두 수 a ,b를 입력받아 2016년 a월 b일이 무슨 요일인지 리턴하는 함수, solution을 완성하세요. 요일의 이름은 일요일부터 토요일까지 각각 SUN,MON,TUE,WED,THU,FRI,SAT

입니다. 예를 들어 a=5, b=24라면 5월 24일은 화요일이므로 문자열 TUE를 반환하세요.

제한 조건
2016년은 윤년입니다.
2016년 a월 b일은 실제로 있는 날입니다. (13월 26일이나 2월 45일같은 날짜는 주어지지 않습니다)
입출력 예
a	b	result
5	24	TUE

*/
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

char* solution(int a, int b) {
    // 리턴할 값은 메모리를 동적 할당해주세요.
    char* answer = (char*)malloc(10);
    
    //day_sum = 날짜 합
    int day_sum=0;
    for(int i=1;i<a;i++){
        if(i==2)
            day_sum+=29;
        else if(i==1||i==3||i==5||i==7||i==8||i==10||i==12)
            day_sum+=31;
        else
            day_sum+=30;
    }
    day_sum +=b;
    day_sum = day_sum%7;
    if(day_sum==1)
        answer = "FRI";
    else if(day_sum == 2)
        answer = "SAT";
    else if(day_sum == 3)
        answer = "SUN";
    else if(day_sum == 4)
        answer = "MON";
    else if(day_sum == 5)
        answer = "TUE";
    else if(day_sum == 6)
        answer = "WED";
    else
        answer = "THU";

    return answer;
}