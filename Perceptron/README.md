**What is classification problem?**
Trying to predict which group / groups our sample data falls into. 

**Perceptrons**


**Perceptron Trick**
Misclassified points want the boundary to move towards them so as to reduce the error. 

Lets assume that the boundary has the equation 3x<sub>1</sub> + 4x<sub>2</sub> - 10 = 0

Lets assume that the point (4, 5) is mis-classified as positive. 

So it would want to be classified correctly as negative by wanting the boundary equation adjusted such that when the (4, 5) values are plugged in, the equation gives a negative answer. 

So, we assume a learning rate of 0.1. The weights of x<sub>1</sub> and x<sub>2</sub> are
   	3      		4		-10
 -	0.1 * 4		0.1 * 5		0.1 * 1
======================================================
        2.6		3.5		-10.1


Now lets assume we have another point 1, 1 that is mis-classified as negative when it should actually be positiveand has the same learning rate of 0.1. The equation of the boudnary would gradually have to be changed as follows: 

	3		4		-10
+ 	0.1 * 1		0.1 * 1		0.1 * 1
======================================================
	3.1		4.1		0.9

We do these adjustments for every misclassified point and the boundary shifts slightly to accomadate for these mistakes and become more general


**Perceptron Algorithm**

We start with a random boundary that splits our data into two regions -> postitive and negative. 
Then we check which of our points were correctcly classified and mis-classified. 
Now we move the line around according to the mis-classified points to get better and better fits
We do this one mis-classified point at a time. 

Algo : 
1. start with random weights w<sub>1</sub>, w<sub>2</sub>, ......w<sub>n</sub>, b
2. For every mis-classified point (x<sub>1</sub>, x<sub>2</sub>)
3. if the prediction was negative for i = 1 -> n, we change w<sub>i</sub> to w<sub>i</sub> + lr * x<sub>i</sub>
   and the bias term to b = b + lr
4. If the prediction was positive for i = 1 -> n, we change  w<sub>i</sub> to w<sub>i</sub> - lr * x<sub>i</sub>
   and the bias term to b = b - lr

