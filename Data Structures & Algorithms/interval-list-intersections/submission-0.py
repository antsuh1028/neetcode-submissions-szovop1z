class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        len_first = len(firstList)
        len_second = len(secondList)

        first,second = 0,0
        res = []

        while first < len_first and second < len_second:
            int1,int2 = firstList[first],secondList[second]
            start_time,end_time = max(int1[0],int2[0]), min(int1[1],int2[1])

            if start_time <= end_time: #interesction exists
                res.append([start_time,end_time])

            #increment lower end time
            if int1[1] < int2[1]:
                first += 1
            else:
                second += 1
        return res
