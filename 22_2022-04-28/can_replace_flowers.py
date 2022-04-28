class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        i = 0
        maximum_amount_of_extra_flowers = 0
        while i < len(flowerbed):
            if flowerbed[i] == 0:
                if flowerbed[i - 1] == 0 and flowerbed[i+1] == 0:
                    maximum_amount_of_extra_flowers += 1
                    flowerbed[i] = 1
            i += 1
        print(flowerbed)
        return maximum_amount_of_extra_flowers




