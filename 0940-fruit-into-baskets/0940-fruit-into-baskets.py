class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # Hash map 'basket' to store the types of fruits.
        basket = {}
        left = 0
        
        # Add fruit from the right index (right) of the window.
        for right, fruit in enumerate(fruits):   # right 은 counter역할, loop이 돌아갈때마다 1씩 증가
            basket[fruit] = basket.get(fruit, 0) + 1 # 해당 과일이 fruits에 없으면 0을 리턴. 그리고 해당 과일을 찾으면 그 과일이 속한 set에 가서 1을 증가.

            # If the current window has more than 2 types of fruit,
            # we remove one fruit from the left index (left) of the window.
            if len(basket) > 2:
                basket[fruits[left]] -= 1

                # If the number of fruits[left] is 0, remove it from the basket.
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1
        
        # Once we finish the iteration, the indexes left and right 
        # stands for the longest valid subarray we encountered.
        return right - left + 1