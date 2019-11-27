#include <cstring>
#include <string>
#include <cctype>

using namespace std;

// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
string solution(string sentence) {
    string answer="";
    
    char sentence_array[1000];
    strcpy(sentence_array, sentence.c_str());
    
    int sentence_array_check1[1000]; //1번 int배열은 대문자는 1, 소문자는 2로 표현
    for(int a=0;a<sentence.length();a++){
        if(isupper(sentence_array[a])==true)
            sentence_array_check1[a] = 1;
        else
            sentence_array_check1[a] = 2;
    }
    //1번 배열은 규칙 5번 검사에 사용될 예정 & 문자 출력할 때 사용 예정
    char temp_ch;
    int temp_int;
    
    int i = 0;
    bool solution_check = true;
    
    //1. 공백이 제거 되지 않았을 경우
    for(int a =0;a<sentence.length();i++){
        if(sentence_array[i]==' '){
            solution_check=false;
            break;
        }
    }
    //2. 규칙1은 단어의 모든 글자 사이에 적용되어야 함
   
    
    
    //3. 단어가 한 개인 경우
    if(sentence_array[0] == sentence_array[sentence.length()-1])
        solution_check = false;
    
    
    
    //4. 첫번째 사용된 기호를 또 사용할 수 없음.
    
    //5. 하나의 규칙을 같은 단어에 두번 적용할 수 없다.
    for(int a=0;a<sentence.length()-1;a++){
        if(sentence_array_check1[a]==2 && sentence_array_check1[a+1]==2){
            solution_check=false; 
            break;
        } 
    }
    
    //맞다는 가정 하에 단어 추출하기. 대문자만 추출하면 된다.
    //1. 연속해서 소문자 또는 대문자가 나올 경우
    //2. 그외의 경우
    if(solution_check){
        //연속해서 나올 1 또는 2가 연속으로 나오는 곳 찾기
        int index=0;
        for(int a=0;a<sentence.length()-1;a++){
            if((sentence_array_check1[a]==2 && sentence_array_check1[a+1]==2)
               ||(sentence_array_check1[a]==1 && sentence_array_check1[a+1]==1)){
                index = a;
                break;
            }
        }
        if(index != 0){ //1번 case: 연속해서 수가 나올 경우
            for(int a=0;a<sentence.length();a++){
                if(index==a)
                    answer.append(" ");
                if(isupper(sentence_array[a]) == true){
                    char temp_char = sentence_array[a];
                    string temp;
                    temp.push_back(temp_char);
                    answer.append(temp);
                }
            }
        }          
        else{ //2번 case: 그외의 경우
            
        }
        
        
        
    }
    
    if(solution_check==false)
        answer="invalid";
    return answer;
}