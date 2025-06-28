---
id: 397d9bac-b9d8-4193-8285-9575bd923a13
---

# Why JavaScript is a single-thread language that can be non-blocking ? - GeeksforGeeks
#Omnivore

[Read on Omnivore](https://omnivore.app/me/https-www-geeksforgeeks-org-why-javascript-is-a-single-thread-la-19069ccbf2e)
[Read Original](https://www.geeksforgeeks.org/why-javascript-is-a-single-thread-language-that-can-be-non-blocking/)


---
Last Updated : 18 Jan, 2023 

The JavaScript within a chrome browser is implemented by a V8 engine.

* [Memory Heap](https://www.geeksforgeeks.org/what-is-a-memory-heap/)
* [Call Stack](https://www.geeksforgeeks.org/what-is-the-call-stack-in-javascript/)

**Memory Heap:** It is used to allocate the memory used by your JavaScript program. Remember memory heap is not the same as the heap data structures, they are totally different. It is the free space inside your OS.

**Call Stack:** Within the call stack, your JS code is read and gets executed line by line.

Now, JavaScript is a single-threaded language, which means it has only one call stack that is used to execute the program. The call stack is the same as the stack data structure that you might read in Data structures. As we know stacks are FILO that is First In Last Out. Similarly, within the call stack, whenever a line of code gets inside the call stack it gets executed and moves out of the stack. In this way, JavaScript is a single-thread language because of only one call stack.

JavaScript is a single-threaded language because while running code on a single thread, it can be really easy to implement as we don’t have to deal with the complicated scenarios that arise in the multi-threaded environment like a deadlock.

Since JavaScript is a single-threaded language, it is synchronous in nature. Now, you will wonder if you have used async calls in JavaScript so is it possible then?

So, let me explain to you the concept of async calls within JavaScript and how it is possible with single-threaded language. Before explaining it let’s discuss briefly why we require the async call or asynchronous calls. As we know within the synchronous calls, all the work is done line by line i.e. the first task is executed then the second task is executed, no matter how much time one task will take. This arises the problem of time wastage as well as resource wastage. These two problems are overcome by asynchronous calls, where one doesn’t wait for one call to complete instead it runs another task simultaneously. So, when we have to do things like image processing or making requests over the network like API calls, we use async calls.

Now, coming back to the previous question of how to use async calls within JS. Within JS we have a lexical environment, syntax parser, and an execution context (memory heap and call stack) that is used to execute the JS code. But these browsers also have Event Loops, Callback queue, and WebAPIs that are also used to run the JS code. Although these are not part of JS it also helps to execute the JS properly as we sometimes used the browser functions within the JS.

![](https://proxy-prod.omnivore-image-cache.app/0x0,svuzWQ5mi0kLImsnWLkl1HAYtRQIrWki5AmmtJqIGMR8/https://media.geeksforgeeks.org/wp-content/cdn-uploads/20210122115136/Untitled-Diagram3.jpg)

JavaScript RunTime Environment

As you can see in the above diagram, DOM, AJAX, and Timeout are not actually part of JavaScript but part of RunTime Environment or browser, so these can be run asynchronously within the WebAPI using the callback queue and again put in the call stack using event loop to execute.

**Example:** Let us take an example to be very clear of the concept. Suppose we have the following piece of code that we want to execute in the JS run-time environment.

* javascript

## javascript

`` `console.log(` `'A'` `); `

`` `setTimeout(() => { `

`` `console.log(` `'B'` `); `

`` `}, 3000); `

`` `console.log(` `'C'` `); `

**Output:**

 A 
 C 
 B

Let’s see why this happens as JavaScript is a single-threaded language so, the output should be **A B C** but it is not.

When JS tries to execute the above program, it places the first statement in the call stack which gets executed and prints A in the console and it gets to pop out of the stack. Now, it places the second statement in the call stack and when it tries to execute the statement, it finds out that setTimeout() doesn’t belong to JS so it pops out the function and puts in the WebAPI to get executed there. Since the call stack is now again empty, it places the third statement in the stack and executes it thus printing C in the console.

In the meanwhile, the WebAPI executes the timeout function and places the code in the callback queue. The event loop checks if the call stack is empty or not or whether there is any statement in the callback queue that needs to be executed all the time. As soon as the event loop checks that the call stack is empty and there is something in the callback queue that needs to be executed, it places the statement in the call stack and the call stack executes the statement and prints B in the console of the browser.

Imagine you're in a tech interview, and you get a tough question. Stay calm and confident with [**Tech Interview 101 - From DSA to System Design**](https://gfgcdn.com/tu/Q29/). This course is perfect for computer science enthusiasts. You'll learn all about **Data Structures**, **Algorithms**, and **System Design** with hands-on practice. Get the skills you need to succeed in any interview. Ready to land your dream job? Sign up today!

  
![](https://proxy-prod.omnivore-image-cache.app/0x0,sMTcIiYTLqvMUICHt1WPSoSa5ljNw-_104KbVxT60PG0/https://media.geeksforgeeks.org/auth-dashboard-uploads/Similarreadnew.svg) 

98

Improve ![](https://proxy-prod.omnivore-image-cache.app/0x0,sMTcIiYTLqvMUICHt1WPSoSa5ljNw-_104KbVxT60PG0/https://media.geeksforgeeks.org/auth-dashboard-uploads/Similarreadnew.svg) 

### Please Login to comment...

### Similar Reads

[ Blocking and Non-Blocking in Node Node is based on an event-driven non-blocking I/O model. This article discusses what does Blocking and Non-Blocking in Node means. Table of Content What is Blocking? What is Non-Blocking ?How Concurrency and throughput is handled?Drawback of mixing Blocking and Non-Blocking CodeWhat is Blocking? It refers to the blocking of further operation until ![](https://proxy-prod.omnivore-image-cache.app/0x0,sMTcIiYTLqvMUICHt1WPSoSa5ljNw-_104KbVxT60PG0/https://media.geeksforgeeks.org/auth-dashboard-uploads/Similarreadnew.svg) 3 min read ](https://www.geeksforgeeks.org/blocking-and-non-blocking-in-node-js/) [ How the single threaded non blocking IO model works in NodeJS ? Node.js is a JavaScript runtime environment that runs on the Chrome V8 engine and is used for server-side scripting. It takes requests from users, processes those requests, and returns responses to the corresponding users. Some important Node.js features are: It is based on single-threaded architecture: Since node.js gets multiple requests from mul ![](https://proxy-prod.omnivore-image-cache.app/0x0,sMTcIiYTLqvMUICHt1WPSoSa5ljNw-_104KbVxT60PG0/https://media.geeksforgeeks.org/auth-dashboard-uploads/Similarreadnew.svg) 2 min read ](https://www.geeksforgeeks.org/how-the-single-threaded-non-blocking-io-model-works-in-nodejs/) [ What is thread safe or non-thread safe in PHP ? Thread-safe: It is used to ensure that when the shared data structure which is manipulated by different threads are prevented from entering the race condition. Thread-safety is recommended when the web server run multiple threads of execution simultaneously for different requests. In Thread Safety binary can work in a multi-threaded web server cont ![](https://proxy-prod.omnivore-image-cache.app/0x0,sMTcIiYTLqvMUICHt1WPSoSa5ljNw-_104KbVxT60PG0/https://media.geeksforgeeks.org/auth-dashboard-uploads/Similarreadnew.svg) 2 min read ](https://www.geeksforgeeks.org/what-is-thread-safe-or-non-thread-safe-in-php/) [ Difference between Asynchronous and Non-blocking Asynchronous and non-blocking are related but distinct concepts in programming, particularly in the context of I/O operations. Asynchronous: Asynchronous refers to the ability of a program or system to perform multiple tasks simultaneously without waiting for each task to be complete before starting the next one. In an asynchronous system, a task c ![](https://proxy-prod.omnivore-image-cache.app/0x0,sMTcIiYTLqvMUICHt1WPSoSa5ljNw-_104KbVxT60PG0/https://media.geeksforgeeks.org/auth-dashboard-uploads/Similarreadnew.svg) 2 min read ](https://www.geeksforgeeks.org/difference-between-asynchronous-and-non-blocking/) [ Explain the concept of non-blocking I/O in Node In traditional synchronous programming models, I/O operations such as reading from a file or making network requests block the execution of the program until the operation completes. This means that if there are multiple I/O operations, they are processed sequentially, leading to potential bottlenecks and wasted resources as the program waits for e ![](https://proxy-prod.omnivore-image-cache.app/0x0,sMTcIiYTLqvMUICHt1WPSoSa5ljNw-_104KbVxT60PG0/https://media.geeksforgeeks.org/auth-dashboard-uploads/Similarreadnew.svg) 3 min read ](https://www.geeksforgeeks.org/explain-the-concept-of-non-blocking-i-o-in-node/) [ Non-Blocking event loop in Node.js Node.js operates on a single-threaded, event-driven architecture that relies heavily on non-blocking I/O operations to handle concurrent requests efficiently. This approach is enabled by its event loop mechanism, which allows Node.js to handle multiple requests concurrently without creating additional threads for each request. Let's explore how the ![](https://proxy-prod.omnivore-image-cache.app/0x0,sMTcIiYTLqvMUICHt1WPSoSa5ljNw-_104KbVxT60PG0/https://media.geeksforgeeks.org/auth-dashboard-uploads/Similarreadnew.svg) 5 min read ](https://www.geeksforgeeks.org/non-blocking-event-loop-in-node-js/) [ Why Node.js is a Single Threaded Language ? Node.js is a popular runtime environment that allows developers to build scalable network applications using JavaScript. One of the most distinctive features of Node.js is its single-threaded architecture, which often raises questions among new developers about why it was designed this way. This article will delve into the rationale behind Node.js ![](https://proxy-prod.omnivore-image-cache.app/0x0,sMTcIiYTLqvMUICHt1WPSoSa5ljNw-_104KbVxT60PG0/https://media.geeksforgeeks.org/auth-dashboard-uploads/Similarreadnew.svg) 4 min read ](https://www.geeksforgeeks.org/why-node-js-is-a-single-threaded-language/) [ Create a User Blocking project using HTML CSS & JavaScript The User Blocking project is a simple application that allows users to block or unblock certain users. It provides a basic interface to add users to a block list and remove them from the list. In this article, we are going to implement the functionality that can block a user by clicking a button and displaying the blocked username below. Preview Im ![](https://proxy-prod.omnivore-image-cache.app/0x0,sMTcIiYTLqvMUICHt1WPSoSa5ljNw-_104KbVxT60PG0/https://media.geeksforgeeks.org/auth-dashboard-uploads/Similarreadnew.svg) 4 min read ](https://www.geeksforgeeks.org/create-a-user-blocking-project-using-html-css-javascript/) [ Is Node.js entirely based on a single-thread ? Node.js is an open-source and cross-platform runtime environment for executing JavaScript code outside a browser. In this article, we'll try to dig a little deeper and understand if Node.js is entirely based on a single thread. However, before starting out, let's clear a few of our basics: Process: When a program begins running, it creates a proces ![](https://proxy-prod.omnivore-image-cache.app/0x0,sMTcIiYTLqvMUICHt1WPSoSa5ljNw-_104KbVxT60PG0/https://media.geeksforgeeks.org/auth-dashboard-uploads/Similarreadnew.svg) 4 min read ](https://www.geeksforgeeks.org/is-node-js-entirely-based-on-a-single-thread/) [ How node.js prevents blocking code ? Node.js is a cross-platform JavaScript runtime environment that helps to execute and implement server-side programs. Node is assumed to prevent blocking code by using a single-threaded event loop. In this article, we will discuss this event loop and how it asynchronously implements functions by using callbacks. Blocking and Non-blocking operations: ![](https://proxy-prod.omnivore-image-cache.app/0x0,sMTcIiYTLqvMUICHt1WPSoSa5ljNw-_104KbVxT60PG0/https://media.geeksforgeeks.org/auth-dashboard-uploads/Similarreadnew.svg) 3 min read ](https://www.geeksforgeeks.org/how-node-js-prevents-blocking-code/) 
