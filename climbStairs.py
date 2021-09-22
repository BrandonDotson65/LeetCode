# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct 
# ways can you climb to the top?

def climbStairs(n):
    if (n <= 0): return 0
    if (n == 1): return 1
    if (n == 2): return 2
    prevprevStep = 1
    prevStep = 2
    allSteps = 0
    for i in range(2, n):
        allSteps = prevprevStep + prevStep
        prevprevStep = prevStep
        prevStep = allSteps
    
    return allSteps

print(climbStairs(20))

def climbStairs2(n):
    a, b = 1, 1
    for i in range(n):
        a, b = b, a + b
    return a

print(climbStairs2(20))