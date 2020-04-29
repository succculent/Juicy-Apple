## Juicy-Apple

#Inspiration
Food waste is an immense problem in the produce industry: "Half of all US food produce is thrown away" (The Gaurdian). This has a terrible impact on the environment as we are pushing the soil to its limits to grow well over twice as much food as we need. We are also emitting lots of green house gasses by transporting spoiled food around the nation. Our group wanted to make a difference to this by creating a scalable automated solution to food waste that can be implemented at any point of the supply chain by any size of business. link

#What it does
Our product uses multiple neural networks to locate produce in an image and determine whether or not it is spoiled. Any images sent to our server will get a response with how many produce were located in the image, and whether or not each of these produce were spoiled. We have also integrated this with Twilio allowing notifications to a operations manager if there are over a user set threshold of rotten images. This is key in some small operations where keeping the produce fresh at a certain percentage can keep the company on its legs.

#How we built it
Using GCP we linked together multiple neural networks to solve this problem. The first network detects objects in the image. Using this we were able to parse the image by each object and test each of them individually to see if they were rotten. The second network determined what each of these objects were. We used this to filter out non-produce objects so they would not be passed into our final network. The third and final network determined whether or not the produce was fresh. This was a binary classification problem, and our network was able to converge on an average accuracy of over 99%.

#Challenges we ran into
We have our program running on a server, but figuring out how to send a POST request in the correct formatting took us a long time. This was many of our members first times working on an application which requests from a server making the task prove difficult. Through trial and error and learning more about POST requests we were able to tackle this problem. This also allowed us to implement a demo on our website that is fully functional in accessing the networks.

#Accomplishments that we're proud of
We are very proud of the overall polish of our project. We were able to get a large variety of different tasks to work together. This includes our neural networks, our server-side development, our back end, our Twilio integration, and even our web development. This project came together very well and made us proud of our work.

#What's next for Juicy-Apple
Juicy-Apple was implemented on a dataset of spoiled v fresh apples, oranges, and bananas; we would like to expand this to other produce using iTradeNetwork's image dataset. We were not able to implement this at LA hacks due to security constraints of the dataset, but with a larger time-span this could be implemented and largely increase the variety of produce that our program is functional in determining the freshness of.

#Built With
- css3
- flask
- google-cloud
- html5
- python
- tensorflow
- twilio
