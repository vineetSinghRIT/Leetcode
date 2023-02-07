class asteroid:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        result=[asteroids.pop(0)]
        second = asteroids.pop(0)
        while len(asteroids)>0 or second!=None:
            process=True
            while len(result)>0 and process==True:
                if result[-1]>0 and second<0:
                    if abs(result[-1])>abs(second):
                        second=result.pop(-1)
                    elif abs(result[-1])<abs(second):
                        result.pop(-1)
                    else:
                        result.pop(-1)
                        if len(result)>0:
                            second=result.pop(-1)
                        else:
                            second=None

                else:
                    process=False
                    result.append(second)

            if len(result)==0 and second!=None:
                result=[second]


            if len(asteroids)>0:
                second=asteroids.pop(0)
            else:
                second=None
        return result

if __name__ == '__main__':
    obj=asteroid()
    print(obj.asteroidCollision([5,10,-5]))
    print(obj.asteroidCollision([8,-8]))
    print(obj.asteroidCollision([10,2,-5]))
    print(obj.asteroidCollision([5,5,5]))
    print(obj.asteroidCollision([-2,-1,1,2]))
    print(obj.asteroidCollision([1,1,-2,-2]))
    print(obj.asteroidCollision([-2,1,-1,-2]))

