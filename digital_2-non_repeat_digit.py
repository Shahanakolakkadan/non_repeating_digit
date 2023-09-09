def non_repeat(n1,n2):
    count=0
    n=0
    for i in range(n1,n2+1):
        n+=1
        ls=[]
        while(i != 0):
            rem=i%10
            i=i//10
            if rem not in ls:
                ls.append(rem)
            else:
                ls.clear()
                count+=1
                break
    count=n-count      
    return count

num1=int(input())
num2=int(input())
result=non_repeat(num1,num2)
print(result)

