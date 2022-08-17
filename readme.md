# Kiki Case Study
Kiki, a first-time entrepreneur from the city of Koriko has decided to open a small distance courier service to deliver packages, with her friend Tombo and cat Joji.

## The possesion of the business
Kiki has invested in
* N no. of vehicles
* driver partners to drive each vehicle & deliver packages

## Problem 01
### Delivery Cost Estimation with Offers
Since it’s a new business, the team has decided to pass coupons around the town which will help them attract more customers.
_Things to keep in mind_
* Only one offer code can be applied for any given package
* Package should meet the required mentioned offer criteria
* If offer code is not valid/found, discounted amount will be equal to 0
### Offer Criteria
The offers can be used according to the criteria that Tombo has captured in this table. Discount will not be provided if no offer code is applied.
![offer criteria](https://github.com/hnhtran/kikiCaseStudy/blob/main/assets/offerCriteria.png)

### Challenge
Command line application to calculate the delivery cost for a given package with an offer code (if applicable).

Note: code should be extensible and scalable for more offer code, for example
Deliver_cost = base_cost + (weight * 10) + (distance *5)
