class Solution:
    def getLength(self, arr):
        start, cur, i = 0, 0, 0
        local_len, global_len = 0, 0
        while i <len(arr):
            if arr[i] not in arr[start, cur+1]:
                cur += 1
                local_len = cur - start + 1
            else:
                while arr[i] in arr[start, cur+1]:
                    start += 1
                    local_len -= 1
            i += 1
            if local_len > global_len:
                global_len = local_len
        return global_len

if __name__ == "__main__":
    result = Solution().getLength('abccabc')
    print result