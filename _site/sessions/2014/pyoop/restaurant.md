#Restaurant Automation in Python

####Problem
Develop a list of (sub)classes and methods for this problem. Discuss how they would interact with each other.

A large problem that restaurants face is that tickets are written on pieces of paper when an automated process is much better for tracking and management. The purpose of this project example is to help a restaurant coordinate their activities, improve productivity, and track business growth. 

Restaurants can be confusing businesses. Typical problems restaurant personnel face include:
*	Coordination of restaurant work activities
*	Anticipating and handling periods of low/high patron traffic
*	Recognizing trends early enough to take advantage of bestsellers or abandon the flops
*	Lowering operating costs, and increasing efficiency/productivity and profits

We want to build a restaurant automation system that will track the food items, employees, tables, orders, customers, and stock ingredients. For food items there are main dishes, side dishes, and drinks each that have a preparation time and cost. Employees are broken into hosts (that greet and seat customers), cooks (that prepare food), and waiters (that take orders, bring food, and clean tables). Customers arrive in parties that are seated together and leave when the last person is done eating. Cooks prepare the food using certain amounts of raw ingredients and a preparation time.

A general restaurant flow is:
Host seats party of customers -> Waiter takes orders (each customer orders a main dish, side dish, and a drink) -> Cook prepares meals -> Waiter brings meal -> Customers eat meals in party and leave when last customer is done -> Busboy cleans -> Host can seat new customers

