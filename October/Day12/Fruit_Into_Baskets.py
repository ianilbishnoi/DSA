class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        left = 0
        basket = {}
        max_length = 0

        for right in range(len(fruits)):
            # Add the current fruit to the basket
            fruit = fruits[right]
            basket[fruit] = basket.get(fruit, 0) + 1

            # Keep only two types of fruits in the baskets
            while len(basket) > 2:
                basket[fruits[left]] -= 1

                # Remove the fruit type if none are left
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]

                left += 1

            # Update the maximum number of fruits collected
            length = right - left + 1
            max_length = max(max_length, length)

        return max_length
