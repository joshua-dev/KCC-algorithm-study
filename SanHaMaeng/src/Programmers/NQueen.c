// #include <stdio.h>
// #include <stdbool.h>
// #include <stdlib.h>

// int solution(int n)
// {
//     int answer = 0;
//     return answer;
// }

#include <math.h>

#define N 4
int col[N];

int isPromising(int row)
{
    int k, promising;

    k = 0;
    promising = 1;
    while (k < row && promising)
    {
        if (col[row] == col[k] || abs(col[row] - col[k]) == row - k)
            promising = 0;
        k++;
    }

    return promising;
}

void nQueens(int row)
{
    if (isPromising(row))
        if (row == N - 1)
            printNqueens();
        else
            for (int i = 0; i < N; i++)
            {
                col[row + 1] = i;
                nQueens(row + 1);
            }
}

int main(int argc, char **argv)
{
    for (int i = 0; i < N; i++)
    {
        col[0] = i;
        nQueens(0);
    }

    return 0;
}
