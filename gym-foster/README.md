# This is a environment for simplified foster care environment. 

Some backgrounds about our simplified foster care system: <br/>
When some youth are admitted in the foster care, care workers will assign different casegoals for them according to their information. In our case, there are only two case goals -- 1) Reunification 2) Long Term Foster Care. We assume that if the youth are able to reunify with their parents, they have higher odds to have stable jobs when they arrive 25 years old. However, not all youth are suitable for returning home because of the situations at home might not be good for the youth. In that case, case worker will assgin Long Term Foster Care case goal for the youth and assign them services which help them obtain skills for job hunting. The ultimate goal of foster care system is to help the youth obtain a stable job when they arrive 25 years old. And in our simplified version, there is only one kind of service. When Reunification case goal is assigned, the youth will not receive any service. And when Long Term Foster Care case goal is assigned, the youth will receive the service once a year. The probability of success of reunification is not aware in advance by case workers. They will try to make decisions according to their experience. The probability of reunification is a function of the information of the youth which could potentially denpend on protected attributes. 

**Motivation:** What we want to do is to build a RL environment to mimic the simplified foster care system introduce above. By learning the best policy in the environment, we are able to simulate how case workers learn strategies to maximize their total reward and understand how the dynamic in the foster care system will influence the strategies of case workers. 

In our foster care system RL environment. Each **agent** represents a youth who enters the foster care system. The **policy** represents the strategy of case workers. The **state** represents the current information about the youth. **Reward** is expected odds of the youth has a stable job at age 25. **Action** is the decisions made by case workers which will change the status of the youth. **Environment** thus gives the transition probability of the states of the youth given the action of case worker. <br/>

Now I will introduce each concept in more details below: <br/>
 
## State
Each state represents the current state of the youth. It contains current casegoal, age, received service, race and other features (e.g. Remove reason) which are correlated to the race but will not change after each iteration.

## Action
Action models the decisions made by case workers. Case work is able to change casegoal for the youth and also is able to assign service to the youth. 

## Reward
Increasing the odds of getting a stable job is the goal of foster care systems. We assume that reunification will help the youth get jobs. So the reward for reunification is 1. And services will help the youth increase the probability of getting jobs in the future. So the reward for service is 0.1

## Policy 
Define the strategy of agent which is simulated behavior of case workers. And it will make decisions like, whether the casegoal will be changed or not, according to the youth's state. 




