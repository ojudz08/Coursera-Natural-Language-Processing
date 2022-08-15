import pandas as pd


def costFunction(theta, X, y):
    m = len(X)
    temp = 0
    for i in range(0, m):
        temp += pow((theta[0] + theta[1] * X[i]) - y[i], 2)
        
    J = temp / (2 * m)
        
    return J

def thetaUpdate(theta):
    m = len(X)
    theta_up = []
    tmp0, tmp1, temp0, temp1 = 0, 0, 0, 0
    for i in range(0, m):
        tmp0 += (theta[0] + theta[1] * X[i]) - y[i]
        tmp1 += ((theta[0] + theta[1] * X[i]) - y[i]) * X[i]
    temp0 = theta[0] - ((alpha / m) * tmp0)
    temp1 = theta[1] - ((alpha / m) * tmp1)
    theta_up = [temp0, temp1]
    
    return theta_up

def gradientDescent(theta, X, y, alpha, iters):
    m = len(X)
    tmp0, tmp1, temp0, temp1 = 0, 0, 0, 0
    J_min = 0
    for itr in range(0, iters):
        for i in range(0, m):
            tmp0 += (theta[0] + theta[1] * X[i]) - y[i]
            tmp1 += ((theta[0] + theta[1] * X[i]) - y[i]) * X[i]
        temp0 = theta[0] - ((alpha / m) * tmp0)
        temp1 = theta[1] - ((alpha / m) * tmp1)
        theta_0 = temp0
        theta_1 = temp1
            
        J = costFunction([theta_0, theta_1], X, y)
        if J > J_min:
            J_min = J
            theta = [theta_0, theta_1]
            continue
        else:
            break
            
    return [theta_0, theta_1], J, J_min, iters


path = r'C:\Users\ojell\Desktop\Oj\3_Coursera\ML\exercises\ex1_linreg'
df = pd.read_csv(path + r'\ex1data1.txt', header=None, names=['Profit', 'City Population'])
X = df.loc[:, 'Profit']
y = df.loc[:, 'City Population']
m = len(X)


theta = [0, 0]
alpha = 0.01
iterations = 1500

#print(costFunction(theta, X, y))
print(gradientDescent(theta, X, y, alpha, iterations))

#temp_J = []
#for itr in range(0, iterations):
#    thetaUp = thetaUpdate(theta) 
#    J = costFunction(thetaUp, X, y)
#    temp_J = temp_J.append(J)
#    print(round(J, 4), thetaUp, temp_J, itr)
#    temp_J = J
#    theta = thetaUp
    

        
        
        
        
        
        
        