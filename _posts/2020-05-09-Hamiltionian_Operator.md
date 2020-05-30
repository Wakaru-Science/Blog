---
layout: post
date: 2020-05-09
comments: true
title: Three Great Guardsd - The Hamiltionian Operator
---

One of the three guards that scare away new learners of quantum mechanics is the Hamiltonian operator. Hamiltonian is the single most crucial operator in quantum mechanics; the king of operators, because of the simple fact that it operates upon the king itself, energy. We meet the king in postulate 5 of quantum mechanics without any explanation of the nature of the Hamiltonian or time-dependent Schrodinger wave equation. Without a proper understanding Hamiltonian or the wave equation, the intuition of quantum mechanics goes downhill real fast. All you are left with is pulling your hair out with a bunch of equations.

If you have no idea what I just said, don't worry and come with me to play with some magical quantum dice.

Suppose we have a quantum dice. It follows all laws of quantum mechanics. Because it is a dice, it can exist in $6$ possible states. But we cannot represent it as $1,2,3,4,5,6$. We use Dirac notation to distinguish them from normal numbers. So $\ket{2}$ represents the state of the dice with $1$ on its top face; $\ket{2}$ represents the state of dice with $2$ on its top face ... We can have a whole lot of fun with this, but because we are hunting for Hamiltonian, we need to include time. So, after every one second, the dice randomly turns into any possible states.
	
We take some time here to get used to Dirac notation. You are playing quantum ludo, and you see the dice has $1$ on its top face. We denoted this initial state as $\bra{1}$. Dirac called it "bra". Just to start the game you desperately need a $6$. This is the final state of dice, so it is represented as $\ket{6}$. Dirac called it "ket". So one turning spontaneously into a $6$ is represented as $\bra{6}\ket{1}$ which is called "bra ket". No points for guessing. This whole dice turning business is based upon $6$ possible states, so the dice are having any $1$ of $6$ numbers on the top face, or the states of $\ket{1}$, $\ket{2}$, $\ket{3}$, $\ket{4}$, $\ket{5}$, $\ket{6}$ which are called "base states".
	
That is not what I said. I included time, that is, the dice randomly turns into any number after one second. When we do something to dice in quantum mechanics, it is called an *operation*. It's a pretty serious word for throwing around dice, turning it, putting it under a magnet, burning it with a laser and what not. All of those are *operations* and definitely not fooling around with the dice. But there is unsung underdog operation which we ignore—doing nothing. Yeah, just let the poor dice sit quietly for a second, doing nothing. That is an *operation* too.
	
But how do we write on paper that such operation occurred? In normal mechanics, if you move something by $5$ meters, you do $+5$, you stretch something $10 times$, you do $x10$. That is called the operator of the operation. In quantum mechanics, there is an operator for moving that tells you how much it moved, an operator of momentum that tells you what the momentum was and the royal operator of energy, which tells you what the energy is. This operator is so special that it was given a royal name, **Hamiltonian**.
	
Just like you use $+, -, \times, / $ in normal mechanics, you use matrices in quantum mechanics. Matrices are big boy operators. I like to call them transformers because they transform cars into cool robots, and it almost seems like magic. But if you have ever handled a transformer toy, you know there is delicate and beautiful machinery under it. So, our operator for time, is a matrix and we denote it as $U$. $U$ is nothing special, you can have anything. $U$ depends on time. Because $U$ is a function of time, $U$ is written as $U(t_2,t_1)$. That is simply, we wait from $t_1$ to $t_2$. For waiting from $t_1 = 0$ and $t_2 = 1$, $U(t_2,t_1)$ is $U(1,0)$.

Now we have all we need to write on paper, how dice has $1$ on the top face, waits for $1$ sec and then rolls to a $6$. It is written as,
$$\bra{6}U(1,0)\ket{1}$$.

Dirac notation is read as Japanese manga, from left to right. The above equation is read as, the dice has state $\ket{1}$ (1 in on top face), it waits for $1$ second, i.e. $U(1,0)$, and then it has state $\bra{6}$ (6 is on top face). Left to right.

What are the chances of dice turning from $1$ to $6$ in a second? It is one state out of $6$ possible states, so the chances are $\frac{1}{6}$. In fact,

$\bra{1}U(1,0)\ket{1}$ | $\bra{2}U(1,0)\ket{1}$ | $\bra{3}U(1,0)\ket{1}$
$\bra{4}U(1,0)\ket{1}$ | $\bra{5}U(1,0)\ket{1}$ | $\bra{6}U(1,0)\ket{1}$

All have $\frac{1}{6}$ chances. See if you can read them.

What about we wait for $2$ seconds? $10$ seconds? An hour? At this point, things get dicey. Ideally, we would want to treat the whole process as a single process and solve it in one go, which we do for relativity. But for non-relative purposes, we have to chop our process in $1$-second intervals, and then multiply them to stitch them together. So,

$$U(2,0) = U(2,1)U(1,0)$$

Again, read from left to right.

Why multiply to stitch them together and not add them together? Great! This is a good time as any to make one thing absolutely clear. In quantum mechanics, no matter what hi-fi stuff you are doing, if things occur one after another, i.e. consecutively, **we multiply** them. If things *can* occur at the same time, i.e. there is more than one way to it, **we add**. I cannot stress how important it is. In our case, every second is followed by the next second, so we multiply. The is no question of the possibility of $2$ seconds occurring at the same time. No addition.

Now you wonder, in your game of quantum ludo, what if you wait for $2$ seconds? Will your chances of getting a $6$ increase? Or decrease? Or will it remain the same? Place your bets.

	$$\bra{6}U(2,1)\ket{2}\bra{2}U(1,0)\ket{1}$$
	
Can you read it? We start with $1$, wait for a second, $1$ becomes $2$. Now $2$ is our initial state, so we use a bra to denote it, wait for a second and then the dice turns $6$. But but but, you might say why $2$, the dice can go from $1$ to $5$ to $6$ or $1$ to $3$ to $6$. The focus is on **or**. Because all these possibilities can occur, there is more than one way to do this; we have to **add** the possibilities.

	$$\bra{6}U(2,0)\ket{1} = $$ $$\bra{6}U(2,1)\ket{1}\bra{1}U(1,0)\ket{1} + \bra{6}U(2,1)\ket{2}\bra{2}U(1,0)\ket{1} +$$ $$ \bra{6}U(2,1)\ket{3}\bra{3}U(1,0)\ket{1} + \bra{6}U(2,1)\ket{4}\bra{4}U(1,0)\ket{1} + $$ $$ \bra{6}U(2,1)\ket{5}\bra{5}U(1,0)\ket{1} + \bra{6}U(2,1)\ket{6}\bra{6}U(1,0)\ket{1} .$$

Wow, this is wayyy too long. We need to shorten this. Remember, when we defined all possible states from $1$ to $6$. We called them base states. Let us denote all the base state as $\bra{i}$ or $\ket{i}$. Then we can use summation and sum over all base states.

$$\bra{6}U(2,0)\ket{1} = \Sigma_i\bra{6}U(2,1)\ket{i}\bra{i}U(1,0)\ket{1}$$

It looks a lot nicer now. The symbols just mean 1, wait for a sec, to any base state i, and wait a sec more and then to 6. What about the probability?
⟨6| U(2,1)|i⟩ = 1/6 and ⟨i| U(1,0)|1⟩ = 1/6 so ⟨6| U(2, 1)|i⟩⟨i| U(1,0)|1⟩ = 1/36.
We total six cases, so 1/36 + 1/36 + 1/36 + 1/36 + 1/36 + 1/36 = 1/6. If you did not bet on the chance is the same, you lost.
This wait one more second business was not a fun side trip. In fact, any operation in quantum mechanics is the sum of all of its base states. And if you want to go from state φ to another state χ, with base states |i⟩, the equation looks like,
⟨ χ | φ ⟩ = Σi⟨ χ |i⟩⟨i| φ ⟩
You can have a different base state if you want, like |j⟩.
⟨ χ | φ ⟩ = Σi⟨ χ |j⟩⟨j| i⟩⟨i| φ ⟩
Φ to i to j to χ
And an operator is nothing more than |j⟩⟨j| i⟩⟨i| so ⟨ χ | φ ⟩ = Σi⟨ χ |A| φ ⟩and A is an operator.
	These are the unseen building blocks of quantum mechanics. Everything is made up of this. Notice that all the base states are discrete, they are separate and not continuous, and the word "quantum" arises from this fact.
We need to simplify U(t2,t1) more. U depending on two variables is overkill; we can get away with t2 as t+Δt and t1 as t. It is more natural as we always said there was a time interval of 1 second. Now we can write Δt = 1 second.
The probability we calculated for a particular time is a number, which we call C. For 1 second the chance was 1/6, for 2 seconds the chance is again 1/6, for 3 seconds it is 1/36 and so on. So we notice C depends on time. As C is a function of time, it is much better to write C as C(t).
How about in your game of quantum ludo, if you want to know what are your chances at time t+Δt when you know chance at t?
Let’s look back at equation 
⟨6| U(2.5,1)|1⟩ = ⟨6| U(2.5,2)|1⟩⟨1| U(2,1)|1⟩ + ⟨6| U(3,2)|2⟩⟨2| U(2,1)|1⟩ + ….
We know the probability of ⟨1| U(2,1)|1⟩ , ⟨2| U(2,1)|1⟩ … We do not know ⟨6| U(2.5,2)|1⟩ , ⟨6| U(2.5,2)|2⟩ … In other words, know what happens during second 1 and 2, but we do not know what happens during second 2 and 2.5.
⟨1| U(2,1)|1⟩ is just a number which we know so ⟨1| U(2,1)|1⟩ = C11 and ⟨2| U(2,1)|1⟩ = C21 and so on.
So, ⟨6| U(2.5,2)|1⟩ = ⟨6| U(2.5,2)|1⟩ C11 + ⟨6| U(3,2)|2⟩ C21 + ….
Because U is an operator, which is a matrix, ⟨6| U(2.5,2)|1⟩ is a matrix. Let us denote that as ⟨6| U(2.5,2)|1⟩ = U61 and ⟨6| U(3,2)|2⟩ = U62 and so on. We have lost time in the process, so I have to mention that Δt = 0.5.
⟨6| U(2.5,1)|1⟩ = U61 C11 + U62 C21 + ….
We can make it look cleaner by ⟨6| U(2.5,1)|1⟩ = ∑_ij▒〖UijCij(t)〗. Every time we make something small and compact, we may lose sight of our physical meaning. The idea behind it is straightforward, Uij is a matrix that can be thought of taking a part of Cij, just like cosθ means a % of something and sinθ is the remaining %. Uij divides Cij into a fraction of what it is, and each possibility contributes something to the probability of the final state. It is a common recurring theme in Quantum Mechanics.
Let us probe into the nature of Uij more. Uij tells us what % of probability each face comes up. Right now, it is equal. Suppose we put our dice under a magnet. Whatever mathematical shenanigans might happen, the probability of each face to turn up is still equal. Uij is essentially unchanged. But what if the face of 3 is filled with iron dots while the rest of it is just black paint. Now the dice really wants to face 3 up; the U31C31 is significantly larger. Thus, Uij we can define the physical conditions of our object, provided we know the base states. We are on to something here. As Dirac said, if you know about the character of the solution before solving the equation, you have truly understood the equation.
We now know C(0,1) , C(1,2) , C(2.5,2). To solve the equation and get an idea of the value of matrix Uij, we can push Δt to 0. At such a small interval, let's say at Δt = 0.001 seconds, for Uij there is a high chance that |1⟩ remains |1⟩, so ⟨1|1⟩ = 1 and there is a very low chance that |1⟩ changes to |2⟩, so ⟨2|1⟩ = 0. Generally, ⟨i|i⟩ = 1 and ⟨j|i⟩ = 0. If we write a that into a matrix,
[■(ii&ij@ji&jj)]  ii = 1, jj = 1 and ij=0 and ji = 0. Thus Uij = [■(1&0@0&1)] is an Identity matrix, δij.
This whole story is all fine for what we know, but if we have an unknown Uij(t+Δt,t), it depends upon both t and Δt. They are both times, and we can't have two of them. So to move further, we are going to do something special, we are going to make an assumption. We are going to assume that the change, i.e. Uij - δij α Δt. That is Uij makes incremental changes which are proportional to Δt. Uij(t+Δt,t) increases in steps, proportional to Δt.
Uij¬(t+Δt,t) is a matrix; δij is a matrix; Δt is a constant, difference of two matrices cannot be a constant. Thus our proportionality constant has to be a matrix, let's say Kij.
Thus, Uij(t+Δt,t) - δij = Kij(t) Δt and thus Uij = δij + Kij(t) Δt. And now our Uij does not depend both on t and Δt, and we have Kij(t) which depends only on t. Problem solved.
Let us go back to ⟨6| U(2.5,1)|1⟩ = U61 C11 + U62 C21 + ….
⟨6| U(2.5,1)|1⟩ is Cij(t+Δt). I did not write that avoid more symbols than necessary. So,
Cij(t+Δt) = U61(t+Δt, t) C11(t) + U62 C21(t) + ….
Substituting Uij(t+Δt, t) = δij + Kij(t) Δt,
Cij(t+Δt) = [δ11 + K11(t) Δt] C11(t) + [δ21 + K21(t) Δt] C21(t) + ….
δij is just an Identity matrix. It’s like 1. 1 x something = something, so δij x Cij = Cij
Cij(t+Δt) = C11(t) + K11(t) Δt C11(t) + C21(t) + K21(t) Δt C21(t) + ….
Cij(t+Δt) = C11(t) + C21(t) + C31(t) + C41(t) + C51(t) + C61(t) + Kij(t)ΔtC11 + K21(t)ΔtC21 + ….
Cij(t+Δt) = Cij(t) + K11(t) Δt C11(t) + K21(t) Δt C21(t) + ….
Cij(t+Δt) - Cij(t) = K11(t) Δt C11(t) + K21(t) Δt C21(t) + ….
Cij(t+Δt) - Cij(t) = Δt [K11(t) C11(t) + K21(t) C21(t) + …. ]
(Cij(t+Δt)- Cij(t))/( Δt) = K11(t) C11(t) + K21(t) C21(t) + ….
If you know basic calculus, you know the next step.
d/dx Cij(t) = K11(t) C11(t) + K21(t) C21(t) + ….
Oh, I almost forgot, if you take i/ℏ common,
-ιℏd/dx Cij(t) = H11(t) C11(t) + H21(t) C21(t) + ….
And there is our Hamilton, which brought Schrodinger's time-independent equation along with him. What a pleasant surprise!
Did the physical meaning and intuition of Uij change? 
Nope. Hij is Uij in more royal clothes.
Remember, when I chose to call the function C(t)? Well, I gave Ψ(t) some common clothes so that you won't get scared by the big scary Ψ(t).
-ιℏd/dx Ψ ij(t) = H11(t) Ψ 11(t) + H21(t) Ψ 21(t) + ….
Ψ(t) is nothing but a state in which something can exist. H(t) is the operator that decides how much contribution the state has. Let's take up an ammonia molecule. It can exist in two states, so our equation becomes,
-ιℏd/dx Ψ 12(t) = H1(t) Ψ 1(t) + H2(t) Ψ 2(t)
Now we can see that Ψ 1 and Ψ 2 are two states of ammonia while H1 and H2 are the % of energy contributed by each state. 
If we take the Hydrogen atom. In the ground state, it can exist only in one state, so our equation becomes,
-ιℏd/dx Ψ (t) = H(t) Ψ (t)
If we do not play with hydrogen, and nothing changes Ψ and H are independent of time.
-ιℏd/dx Ψ = HΨ is perfectly solvable, and you get a very nice solution. The Hamiltonian matrix is made up of derivate of time, which is curvature. The more the curvature, the more the energy of the wave, the more the contribution.


	 

