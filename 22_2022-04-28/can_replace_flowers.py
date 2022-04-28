class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        i = 0
        maximum_amount_of_extra_flowers = 0
        is_one_element = False
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                maximum_amount_of_extra_flowers += 1
            is_one_element = True

        while i < len(flowerbed):
            if is_one_element:
                break

            if flowerbed[i] == 0:
                if i - 1 < 0 and not flowerbed[i + 1] or i + 1 == len(flowerbed) and not flowerbed[i - 1] or not \
                flowerbed[i - 1] and not flowerbed[i + 1]:
                    maximum_amount_of_extra_flowers += 1
                    flowerbed[i] = 1
            i += 1
        print(flowerbed)
        print(maximum_amount_of_extra_flowers)
        return maximum_amount_of_extra_flowers >= n


