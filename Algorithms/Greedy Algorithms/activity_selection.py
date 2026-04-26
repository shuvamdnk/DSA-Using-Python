def MaxActivity(arr_start, arr_finish,n):
    i = 0
    print(i,end=" ")

    for j in range(1,n):
        if start_times[j] >= finish_times[i]:
            print(j,end=" ")
            i = j     


if __name__ == '__main__':
    start_times = [1, 3, 0, 5, 8, 5]
    finish_times = [2, 4, 6, 7, 9, 9]
    MaxActivity(start_times,finish_times,len(start_times))
