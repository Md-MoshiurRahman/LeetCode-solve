class Solution(object):
    def corpFlightBookings(self, bookings, n):
        book = []
        for i in range(n):
            book.append(0)
        for array in bookings:
            frm = array[0] - 1
            to = array[1]
            book[frm] += array[2]
            if to < n:
                book[to] -= array[2]

        for i in range(1,n):
            book[i] += book[i-1]

        return book

print(Solution().corpFlightBookings([[1,2,10],[2,3,20],[2,5,25]], 5))


