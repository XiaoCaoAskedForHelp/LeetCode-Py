class Solution:
    # 循环望里面加油，模拟加油，只要消耗了5升油就可以继续加油
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        tank = mainTank
        addition = 0
        while mainTank >= 5 and additionalTank:
            num = mainTank // 5
            addTank = min(num, additionalTank)
            addition += addTank
            mainTank = addTank + mainTank % 5
            additionalTank -= addTank
        return (tank + addition) * 10

    # 太慢了每次都只减5，如果mainTask很大，就会超时
    def distanceTraveled1(self, mainTank: int, additionalTank: int) -> int:
        ans = 0
        while mainTank >= 5:
            mainTank -= 5
            ans += 50
            if additionalTank:
                additionalTank -= 1
                mainTank += 1
        return ans + mainTank * 10  # 剩下的不满5升的油，加之前已经跑过的路程

    def distanceTraveled2(self, mainTank: int, additionalTank: int) -> int:
        ans = 0
        while mainTank >= 5:
            t = mainTank // 5
            ans += t * 50
            mainTank %= 5
            t = min(t, additionalTank)
            additionalTank -= t
            mainTank += t
        return ans + mainTank * 10

    # 如果副油箱有油的话，满4升就可以开五公里，但是得减去一升，因为8升只能从副油箱得到一升，9升才能从副油箱得到两升
    def distanceTraveled3(self, mainTank: int, additionalTank: int) -> int:
        return (mainTank + min((mainTank - 1) // 4, additionalTank)) * 10
