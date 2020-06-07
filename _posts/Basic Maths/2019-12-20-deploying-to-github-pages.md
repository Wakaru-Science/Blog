---
layout: post
title: "Deploying Odin to Github Pages"
date: 2019-11-05 08:44:38 -0400
category: subcategory-vectors
author: wakaru
comments:true
short-description: How to automatically deploy on Github Pages, for free!
---

Vectors are generally introduced as something with both magnitude and direction. Then we learn how to add vectors, the law of parallelogram and out of nowhere we are introduced to scalar and vector product, with no explanation from where it came from. Why do we need two types of multiplication anyways? Randomly, textbooks include the projection of a vector and somehow sinθ and cosθ appear. Then you might forget about vectors till you reencounter them as divergence and curl or some other place.

That is unfair. Vectors are one of the most fundamental concepts in science, if not the most fundamental concept. You cannot have a movement without direction. If there is a direction, there has to be a vector somewhere. Most of the places where you don’t see a vector have a vector hidden from plain sight.

Anything without a direction is called a scalar. Anything you can measure with some kind of scale is a scalar. Do you want to measure sheep? There is a number scale for that. Want to measure distance? Use a metric scale. Weight? A weighing scale. Refractive Index? There is a scale of refractive indices. Toughness? Moh’s scale. The magnitude of an Earthquake? Richter’s scale. Work? Energy. All of them are scalars.
Now I challenge you to measure speed with a scale. Sure you can take a scale, measure the distance travelled, measure the time taken, divide and find out the speed. Well, it won’t work. You can say the speed is this much, but If I give you a car and speed is 50 km/hr, you will from where? Because 50km/hr up a hill is not the same as 50 km/hr down a hill. I dig a hole and drop a car from there, and the speed is still 50 km/hr—the where is really important.

Then why don’t we worry about the direction in real life? Because we artificially restrict the direction. The car goes along the road, and the road goes in one direction, so saying 50 km/hr is good enough as the direction is obviously the road. The vector is hidden away, treated like a scalar, but vector is still a vector. The distinction is important, so we call such one direction speeds as “velocity”.
You can go even further. You can fix the distance by making the car race around in a closed circular road. There is no need to mention the distance, so we measure race speed in time. Race records are in XYZ seconds for a particular distance in a particular direction, also called as a race track.
When we want to see how fast the car accelerates, have to mention the speed of the car, the distance and the direction. Nope. What is done is on a fixed race track, we count how fast car reaches 60 km/hr. Then we say, oh tesla reaches 0-60 in 2.3 seconds, that is crazy. Or you know how much time it takes to reach 60? 23 seconds! A bullock cart is faster than that! We are talking about acceleration here, i.e. metres travelled per second per second in terms of seconds!

But what is the direction? How do we define it? How do we decide something has direction, and something does not? 
Suppose you place a mango at a certain point on a table. You want to know where that mango is, you decide some point of a table and call it “origin”. Then you can say, it is x distance away from the origin and y distance away from the origin. You can even include the height of the table and call it z distance away. We call these 3 numbers “position” of the mango as these three numbers uniquely tell you where the mango is. No other numbers can give the same position. You do a bunch of stuff with the mango, throw it and calculate momentum, spin it and calculate inertia, whatnot.
Now a cat named mau comes and decides that she wants the origin at some other point. Cats are very finicky. The mango hasn’t moved at all, but the numbers have changed. Now you have to do a bunch of math stuff to recalculate everything. You can re-derive the formula. But does the momentum change with origin? No.

How about when mau changes the location of a mango? The origin is still the same but location has changed. Does the value of momentum change? Does physical law change because we have a new origin? Nope.

What about when mau rotates the mango? The mango is not the same as the original mango. But neither momentum or law changes. This irritates mau. She decides to rotate the origin itself. Everything has now rotated by an angle, say α. The x-axis is not x-axis anymore, the y-axis is not y-axis. Simple calculations now involve sin and cos, and everything is complicated. So you ask yourself. What if I decide to redefine my axis. The x-axis, y-axis and z-axis are rotated by angle α, but will the law of physics change? Will the value of momentum change just because we decided to redefine our axis? No.

But mau is a smart cat. Mau has an ace in a hole. She just waits. And does nothing. You are like, ha! Nothing happened! But. Your mathematics just turned ugly. Time is change, and no matter how you beat around it, you have to write derivates and partial derivatives and integrals. We all know how fun it is to solve integrals and differential equations. But. Will waiting a few seconds and throwing a mango have a different momentum than throwing a mango right now? (Assuming everything remains same) No.

Changing the origin does nothing. It doesn’t matter from where you start counting, nor does it matter where the mango is. It doesn’t matter which direction you choose as x-axis; every direction is the same. It doesn’t matter which second you choose to take the reading; every second is the same. (Unless you are in a field, like a changing magnetic field. Now the position time and angle will matter).

We asked what the direction is? And the answer we got instead is there no such thing as unique direction, origin or time. Pick one; they are all the same. That is what we are going to do. We are going to pick a random direction, origin and time. Direction cannot exist on its own. If a car is moving in a specific direction, it hs some mass. All the three numbers that come with an origin, (x,y,z coordinates), the direction and magnitude(mass), we are going to represent with a single character, i. We call it a vector.



