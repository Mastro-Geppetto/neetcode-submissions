class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        (l_ptr, r_ptr, max_len) = (0, 1, 0)
        window_hash = set(s[l_ptr])
        window_queue = [s[l_ptr]]
        while r_ptr < len(s):
            max_len = max(max_len, len(window_queue))
            print("r", r_ptr, "m", max_len, "c", s[r_ptr])
            if s[r_ptr] in window_hash:
                print("\tclenup:",window_queue)
                # pop till we reach current char
                while len(window_queue) > 0 and\
                window_queue[0] != s[r_ptr]:
                    _ = window_queue.pop(0)
                    print("\tpop",_)
                # pop the actual char
                _ = window_queue.pop(0)
                print("\tpop",_)
            # insert at end of window_queue
            window_queue.append(s[r_ptr])
            # update window_hash
            window_hash.clear()
            window_hash = set(window_queue)
            r_ptr += 1
        if len(window_queue) > max_len:
            max_len = len(window_queue)
        return max_len
