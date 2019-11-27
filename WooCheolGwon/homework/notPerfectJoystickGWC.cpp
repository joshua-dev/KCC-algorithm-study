//63.5점...
#include <string>
#include <vector>
#include <cstring>

using namespace std;
//각 알파벳의 위 아래 이동 수 계산 함수
int alpabet_number(char input_alpabet){
    int answer=0;
    switch(input_alpabet){
        case 'A':
            answer = 0;
            break;
        case 'B':
        case 'Z':
            answer = 1;
            break;
        case 'C':
        case 'Y':
            answer = 2;
            break;
        case 'D':
        case 'X':
            answer=3;
            break;
        case 'E':
        case 'W':
            answer=4;
            break;
        case 'F':
        case 'V':
            answer=5;
            break;
        case 'G':
        case 'U':
            answer=6;
            break;
        case 'H':
        case 'T':
            answer=7;
            break;
        case 'I':
        case 'S':
            answer=8;
            break;
        case 'J':
        case 'R':
            answer=9;
            break;
        case 'K':
        case 'Q':
            answer=10;
            break;
        case 'L':
        case 'P':
            answer=11;
            break;
        case 'M':
        case 'O':
            answer=12;
            break;
        case 'N':
            answer=13;
            break;
    }
    return answer;
}

int solution(string name) {
    int answer=0, cnt=0;
    //alpabet_array에 입력한 이름의 알파벳을 각각 char로 저장
    char alpabet_array[20];
    strcpy(alpabet_array, name.c_str());
    
    //각 알파벳의 위 아래 이동 수 계산 + 'A' 갯수 측정
    for(int i=0;i<name.size();i++){
        if(alpabet_array[i]=='A')
            cnt++;
        answer += alpabet_number(alpabet_array[i]);
    }
    //왼쪽 오른쪽 이동 횟수 결정
    int left_right_move = 0;
    if(name.size()>=3){
        if(alpabet_array[1] =='A'&&alpabet_array[name.size()-1]=='A')
            left_right_move = name.size()-1;
        else if(alpabet_array[1] == 'A' || alpabet_array[name.size()-1] =='A')
            left_right_move = name.size()-cnt-1;
        else
            left_right_move = name.size()-1;
        //(추가)A로만 구성되었을 경우
        if (name.size() == cnt)
			left_right_move = 0;
    }
    else{
        if(name.size()==2)
            left_right_move = 1;
        else
            left_right_move = 0;
        //(추가)A로만 구성되었을 경우
        if (name.size() == cnt)
			left_right_move = 0;
    }
    
    answer = answer+left_right_move;
    return answer;
}