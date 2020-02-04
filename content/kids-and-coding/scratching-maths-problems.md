---
title: Scratching with Maths Homework Problems
date: 2019-02-15T02:34:20.000Z
draft: false
Image: /kids-and-coding/images/maths-problem.jpeg
category: Kids and Coding
categoryurl: /kids-and-coding
published: true
---
My 10 yo son came home with some maths problems last week, and as soon as I read them, I immediately saw the opportunity to work with him to solve one of them using code.
A language like Python would be perfect for writing a solution to it, but he’s most familiar with Scratch and I didn’t want the ‘lesson’ to be about coding, but about how to use code to come up with a solution.
Hopefully this will give you some tips on how to work on similar problems yourself either in Code Club, in the classroom, or at home.
Here is a photo of his problem:

![](/kids-and-coding/images/maths-problem.jpeg)

I set about solving it myself first, as it’s a little tricky sometimes to bend Scratch to do this type of thing and I wanted to make it as simple as possible to work through together.
At the same time, I got him working on manually solving the problem on paper by hand, so he understood what needed to be done.
The solution is essentially:
 
- Loop through all all the numbers
- Add each number to every other number
- Check if the sum is divisible by 11 (if ‘total’ mod 11 = 0)
- If it is, add the numbers to the list of answers.

One tricky part is making sure you don’t add the numbers twice, i.e. 4+7 = 11, and 7+4 = 11. I initially put in a check for this in the code, then realised the proper solution:

- When adding the numbers you only need to add the numbers after the first number, as the previous combinations have already been checked
- This is also faster, and removes the need for the check, making the code much simpler.

So… let’s go through the code. First we:

- Create a list ‘numbers’ and manually add the numbers from the problem
- Create an empty list ‘all answers’, which is cleared when the program starts
- Create a variable ‘index’ for counting through the list as we loop

![](/kids-and-coding/images/numbers-list.png)

This gives us this code to start with:

![](/kids-and-coding/images/maths-code-1.png)

Then, we add another loop, inside the first loop, to go through the numbers again, starting at the next number after the first one:

- Create another index for this loop ‘index2’
- Set ‘index2’ to ‘index’ at the start of this loop. It will be incremented by 1 at the start, so will always start at the next number in the list
- Each time through the loop, set ‘number 1’ to the item at ‘index’ and ‘number 2’ to the item at ‘index2’ in the list

This gives us the two numbers to add stored in the variables ‘number 1’ and ‘number 2’

![](/kids-and-coding/images/maths-code-2.png)

The number of times we need to loop through this second list is:

- length of ‘numbers’ minus ‘index’ as we’re starting at the first number

Lastly, all we need to do is:

- Add the two numbers together
- Check the sum is divisible by 11 (‘number 1’ + ‘number 2’ mod 11 = 0)
- If it is, add the answer to the list ‘all answers’. I do this by creating a string with the ‘join’ block like this:

![](/kids-and-coding/images/maths-code-3.png)

Here’s the final working code:

![](/kids-and-coding/images/maths-code-4.png)

And here’s the [project on Scratch](https://scratch.mit.edu/projects/286164050/) if you would like to take a look.

Hopefully this gives you some tools and inspiration for using Scratch with this kind of problem. It really helps show understanding of the power of computing and coding to solve real world maths problems, and how it can be used to make maths (and homework!) easier.

I’d love to hear some thoughts and ideas on how others have tried to use Scratch for this type of problem.