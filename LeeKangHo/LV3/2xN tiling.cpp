#include<cstdio>
#include<iostream>
#include<stdio.h>
#include<algorithm>
int arr[3];

int main() {
	int i, j, min, index, temp;
	for (i = 0;i < 3;i++) {
		scanf("%d", &arr[i]);
	}
	for (i = 0; i < 3; i++) {
		min = 100001;
		for (j = i; j < 3; j++) {
			if (min > arr[j]) {
				min = arr[j];
				index = j;
			}
		}
		temp = arr[i];
		arr[i] = arr[index];
		arr[index] = temp;
	}
	for (i = 0; i < 3; i++) {
		printf("%d ", arr[i]);
	}
	return 0;
}