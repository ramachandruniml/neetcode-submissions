class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        need = {}
        for c in t:
            need[c] = 1 + need.get(c, 0)

        window = {}
        have, required = 0, len(need)

        result, result_len = [-1, -1], float("infinity")
        left = 0

        for right in range(len(s)):
            c = s[right]
            window[c] = 1 + window.get(c, 0)

            if c in need and window[c] == need[c]:
                have += 1

            while have == required:
                if (right - left + 1) < result_len:
                    result = [left, right]
                    result_len = right - left + 1

                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1
                left += 1

        left, right = result
        return s[left:right+1] if result_len != float("infinity") else ""
