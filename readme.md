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

## Problem 02
### Delivery Time Estimation
Now all these packages should be delivered to their destinations in the fleet of vehicles Kiki owns. She has N no. of vehicles available for delivering the packages.
_Things to keep in mind_
* Each vehicle has a limit (L) on maximum weight (kg) that can be carried
* All vehicles travel at the same speed (S km/hr) and in the same route. It is assumed that all the destinations can be covered in a single route.
### Delivery Criteria
1. Always travelling at maximum speed (S km/hr)
2. Multiple shipment? Heavier package preferred
3. Multiple shipment? Same weight? Pickup closest to destination
4. Finish delivery? Vehicle return to source station with same speed and available for another shipment
### Challenge
Tombo, the geeky business partner obsessed with delivery metrics wants to maximise efficiency.
You are required to build a command line application to calculate the estimated delivery time for every package by maximizing no. of packages in every shipment.

Note: Roundoff estimated delivery time upto 2 digits, e.g 3.456 -> 3.45
