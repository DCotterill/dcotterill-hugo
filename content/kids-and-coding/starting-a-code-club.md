---
title: Starting a Code Club
date: 2017-10-17T02:34:20.000Z
draft: false
Image: /kids-and-coding/images/dillon-coding.jpg
category: Kids and Coding
categoryurl: /kids-and-coding
published: true
---

One of the goals I had when finished up at work was to start a Code Club at my kids’ school. It took me a little longer than I’d hoped to get started, but now we’re into our 3rd Term. Everyone I talk to about it finds it an interesting topic, especially people with kids, so it’s about time I wrote a little about it.

I’ve learned a lot from the experience so far and I have a series of posts to write on the topic, but most people I speak to, even developers, have still not heard of Code Clubs, so I’ll start with a basic intro.

So.. What is a Code Club? Code Club Australia is a registered charity, which originally started in the UK, but was brought to Australia later on. They help teachers and volunteers setup clubs for kids, in schools, libraries, or anywhere that’s suitable, aimed at teaching Primary school students the basics of programming.

The most important thing they provide are the project materials for teaching. These start with Scratch projects, such as animations and games, but they also have Python, HTML/CSS, SonicPi, Raspberry Pi SenseHat projects, and more and more being added all the time.

The materials are provided for free, with the condition that there is no charge for attending the Code Club; they should remain free for the students. This is a fantastic idea that helps make sure it’s kept open to everyone, not just the parents who can afford extra curricular activities.

Our club runs with around ~30 kids from Year 3 and 4, but we were overwhelmed with the interest and had to put quite a lot on the wait list, who will hopefully be able to join a second class next year. With hindsight, this was a good decision as we have 2 teachers helping out with myself, and a 10-1 student-adult ratio is about as high as you can get to provide the attention they need without getting distracted. We also have a roughly 50/50 boy/girl mix, which I’m really happy with and am hoping to actively keep the girls engaged as they get a little older, as history tells us they can start to drop off if they lose interest.

We spent the first 2 terms building a selection of Scratch projects, which I chose from the available list based on what I thought would be interesting and what would introduce new programming skills at the right pace. I’d like to talk about Scratch more in a later post as I think it’s underrated as a teaching tool, and people are way too keen to move on to a ‘proper’ language without understanding how powerful Scratch can actually be.

As a basic intro though, it lets you drag and drop blocks to create programs, mainly triggered by events, such as key presses, collisions, messsages, etc.

Here’s a picture of the ‘Boat Race’ game. One of the first few projects we tackled:

![](/kids-and-coding/images/boat-race.png)

You can see the instructions that the students follow here, and test the game: https://codeclubprojects.org/en-GB/scratch/boat-race/

and you can see the code behind it here: https://scratch.mit.edu/projects/63957956/#editor

Here’s a simple snippet of code from the game (attached to the boat sprite) to explain how it works:

![](/kids-and-coding/images/boat-race-code.png)

When the ‘game start (green flag)’ event happens do this:

- Change the boat ‘costume’ to ‘normal’ (i.e not the crashed boat)
- Point it to 0 degrees (up)
- Move it to x:-190, y:-150 (the bottom left of the screen)
- In a ‘forever’ loop do this: - If the boat is more than 5 pixels away from the mouse pointer: - Turn the boat to point towards the mouse pointer - Move it one step forward

Simple, huh!

We’ve been extremely happy with the progress made in such as short time. Most of the students had zero programming knowledge at the start, and after a few weeks on handholding through the setup and initial steps, they quickly became independent and could follow a lot of the projects’ instructions themselves.

From the first few weeks of being crazily busy with a queue of hands always up asking for help, it quickly became a class where I could step back and choose to spend more involved time one-on-one working through more complex issues, and explaining the reasoning behind some of the code.

I’ve had a lot of feedback from the parents and the kids themselves about how much they enjoy it, which is really rewarding. You can see it in their engagement, and a few parents told me that Code Club morning is the only day they don’t have to convince them to get ready and go to school.

The picture of at the top of this post is of my son freestyling his new found skills building his own Minecraft game, complete with obligatory developer headphones.

Hopefully that’s given you a little insight into a Code Club, and maybe a little motivation to get involved or set one up yourself! It’s much easier than you think, and I would be happy to help guide people through the first few steps, or answer any questions. Just let me know!

I wanted to keep this short, but there’s a lot more detail I’m keen to write about on these topics, so more to come:

- Lots of tips for making Code Clubs effective, and my lessons learned so far
- Why Scratch is great for learning, and not just a ‘play language’
- Progressing from Scratch to Python (We’ve just started this now!).
