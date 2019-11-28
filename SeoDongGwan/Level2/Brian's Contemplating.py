def solution(sentence):

    array = []
    answer = []
    capital = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    
    # ['H', 'a', 'E', 'a', 'L', 'a', 'L', 'a', 'O', 'b', 'W', 'O', 'R', 'L', 'D', 'b']

    for i in sentence:
        array.append(i)


    for j in range((len(array))): #0~15
        for k in capital:
        
            if array[0] == k: #rule1
                rule1 = array[1]
                if rule1 == array[j]:
                    space = j
                    
                
            if array[1] == k: #rule2
                rule2 = array[0]
                if rule2 == array[j]:
                    print(j)

    array.insert(space+2, " ")            
    
    
    for i in range((len(array))): #0~15
        for j in capital:
        
            if array[i] == j or array[i] == " ":
                answer.append(array[i])
                array[i] = 1

    for i in answer:
        print(i , end = '')

    
