/*
문제 설명
수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한 조건
시험은 최대 10,000 문제로 구성되어있습니다.
문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.
입출력 예
answers	return
[1,2,3,4,5]	[1]
[1,3,2,4,2]	[1,2,3]
입출력 예 설명
입출력 예 #1

수포자 1은 모든 문제를 맞혔습니다.
수포자 2는 모든 문제를 틀렸습니다.
수포자 3은 모든 문제를 틀렸습니다.
따라서 가장 문제를 많이 맞힌 사람은 수포자 1입니다.

입출력 예 #2

모든 사람이 2문제씩을 맞췄습니다.
so
*/
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> answers) {
    int first_supoza[10000], second_supoza[10000], third_supoza[10000];
    
    //각 수포자가 찍는 방식 예시 모음
    int first_supoza_method[5]={1,2,3,4,5};
    int second_supoza_method[8]={2,1,2,3,2,4,2,5};
    int third_supoza_method[10]={3,3,1,1,2,2,4,4,5,5};
    
    //최대 크기로 만들어 놓은 배열에 규칙대로 넣기
    for(int i=0;i<10000;i++){ 
        first_supoza[i]=first_supoza_method[i%5];
        second_supoza[i]=second_supoza_method[i%8];
        third_supoza[i]=third_supoza_method[i%10];
    }
    
    //맞춘 문제 카운트
    int first_check=0, second_check=0, third_check=0;
    for(int i=0;i<answers.size();i++){
        if(answers[i]==first_supoza[i])
            first_check++;
        if(answers[i]==second_supoza[i])
            second_check++;
        if(answers[i]==third_supoza[i])
            third_check++;
    }
    
    vector<int> answer;

    if(first_check>=second_check && first_check>=third_check)
        //1번이 많이 맞출 경우
        answer.push_back(1);
    if(second_check>=first_check && second_check>=third_check)
        //2번이 많이 맞출 경우
        answer.push_back(2);
    if(third_check>=first_check && third_check>=second_check)
        //3번이 많이 맞출 경우
        answer.push_back(3);
    //같은 문제를 맞출 경우를 고려해서 따로 if 문 제작   
    
    sort(answer.begin(), answer.end());
    return answer;
}