# This is a environment for simplified foster care environment. 

Some backgrounds about our simplified foster care system: <br/>
When some youth are admitted in the foster care, care workers will assign different casegoals for them according to their information. In our case, there are only two case goals -- 1) Reunification 2) Long Term Foster Care. We assume that if the youth are able to reunify with their parents, they have higher odds to have stable jobs when they arrive 25 years old. However, not all youth are suitable for returning home because of the situations at home might not be good for the youth. In that case, case worker will assgin Long Term Foster Care case goal for the youth and assign them services which help them obtain skills for job hunting. And in our simplified version, there is only one kind of service. In our setting, when Reunification case goal is assigned, the youth will not receive any service. And when Long Term Foster Care case goal is assigned, the youth will receive the service once a year. The probability of success of reunification is not aware by case workers. They will try to make decisions according to their experience. In reality, the probability of reunification is different across races which is source of the bias. 

What we want to do is to build a RL environment to mimic the simplified foster care system introduce above. And I will first introduce the overview of our RL system:
In our foster care system RL environment. Each **agent** represents a youth who enters the foster care system. The **policy** represents the strategy of case workers. The **state** represents the current information about the youth. **Reward** is expected odds of the youth has a stable job at age 25. **Action** is the decisions made by case workers which will change the status of the youth. **Environment** thus gives the transition probability of the states of the youth given the action of case worker. <br/>

Now I will introduce each concept in more details below: <br/>
 
## State
Each state represents the current state of the youth. It contains current casegoal, age, received service and some other features of the youth.

## Action
The first part of the action contains   
