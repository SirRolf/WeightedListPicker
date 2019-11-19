from random import randint

class ListPicker:
    
    def RandomList(aList, chances):
        package = aList
        result = 0
        maxScore = 0
        catagory = 0
        
        # add up all the score from chances
        for i in chances:
            maxScore += i

        # make random int to decide what the score is
        score = randint(0, maxScore)
        
        # check in what catagory score lands
        for i in chances:
            catagory += i
            if catagory >= score:
                # decide what list item to pick
                package = aList[result]
                return package
            result += 1
