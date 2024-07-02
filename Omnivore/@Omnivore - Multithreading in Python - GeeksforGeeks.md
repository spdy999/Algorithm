---
id: f6aa7574-dca7-430e-879b-3306fc09da2f
---

# Multithreading in Python - GeeksforGeeks
#Omnivore

[Read on Omnivore](https://omnivore.app/me/https-www-geeksforgeeks-org-multithreading-python-set-1-1906e1d8bd2)
[Read Original](https://www.geeksforgeeks.org/multithreading-python-set-1/)


---
Last Updated : 19 Jun, 2024 

This article covers the basics of multithreading in Python programming language. Just like [multiprocessing](https://www.geeksforgeeks.org/multiprocessing-python-set-1/), multithreading is a way of achieving multitasking. In multithreading, the concept of ****threads** is used. Let us first understand the concept of ****thread** in computer architecture.

## ****What is a Process in Python?**

In computing, a [****process**](https://www.geeksforgeeks.org/introduction-of-process-management/) is an instance of a computer program that is being executed. Any process has 3 basic components:

* An executable program.
* The associated data needed by the program (variables, workspace, buffers, etc.)
* The execution context of the program (State of the process)

## ****An Intro to Python Threading** 

A ****thread** is an entity within a process that can be scheduled for execution. Also, it is the smallest unit of processing that can be performed in an OS (Operating System). In simple words, a thread is a sequence of such instructions within a program that can be executed independently of other code. For simplicity, you can assume that a thread is simply a subset of a process! A thread contains all this information in a [****Thread Control Block**](https://www.geeksforgeeks.org/thread-control-block-in-operating-system/) **(TCB)**:

* ****Thread Identifier:** Unique id (TID) is assigned to every new thread
* ****Stack pointer:** Points to the thread’s stack in the process. The stack contains the local variables under the thread’s scope.
* ****Program counter:** a register that stores the address of the instruction currently being executed by a thread.
* ****Thread state:** can be running, ready, waiting, starting, or done.
* ****Thread’s register set:** registers assigned to thread for computations.
* ****Parent process Pointer:** A pointer to the Process control block (PCB) of the process that the thread lives on.

Consider the diagram below to understand the relationship between the process and its thread:

![multithreading-python-11](https://proxy-prod.omnivore-image-cache.app/631x802,skW1Mx4D3BiIO7LlCepQJB99YnWTPgYzIRvxlGcnRadE/https://media.geeksforgeeks.org/wp-content/uploads/20230824111308/multithreading-python-11.png)

Relationship between a Process and its Thread

Multiple threads can exist within one process where:

* Each thread contains its own ****register set** and ****local variables (stored in the stack)**.
* All threads of a process share ****global variables (stored in heap)** and the ****program code**.

Consider the diagram below to understand how multiple threads exist in memory:

![multithreading-python-21](https://proxy-prod.omnivore-image-cache.app/712x391,sbTbN4Zu5PPd-u-GuHkmxzJPSBLqjp3yBbrhXWhLkSN0/https://media.geeksforgeeks.org/wp-content/uploads/20230824111450/multithreading-python-21.png)

Existence of multiple threads in memory

## An Intro to Threading in Python

****Multithreading** is defined as the ability of a processor to execute multiple threads concurrently. In a simple, single-core CPU, it is achieved using frequent switching between threads. This is termed ****context switching**. In context switching, the state of a thread is saved and the state of another thread is loaded whenever any interrupt (due to I/O or manually set) takes place. Context switching takes place so frequently that all the threads appear to be running parallelly (this is termed ****multitasking**).

Consider the diagram below in which a process contains two active threads: 

![multithreading-python-31](https://proxy-prod.omnivore-image-cache.app/412x370,sF0O8yOnP6rtxh73EbNkeuL-UXrPWZgQ9RJTctN4pFEk/https://media.geeksforgeeks.org/wp-content/uploads/20230824111728/multithreading-python-31.png)

Multithreading

In [Python](https://www.geeksforgeeks.org/python-programming-language/), the ****threading** module provides a very simple and intuitive API for spawning multiple threads in a program. Let us try to understand multithreading code step-by-step.

****Step 1:** Import Module

First, import the threading module.

import threading  

****Step 2:** Create a Thread

To create a new thread, we create an object of the ****Thread** class. It takes the ‘target’ and ‘args’ as the parameters. The ****target** is the function to be executed by the thread whereas the ****args is** the arguments to be passed to the target function.

t1 = threading.Thread(target, args)  
t2 = threading.Thread(target, args)  

****Step 3:** Start a Thread

To start a thread, we use the ****start()** method of the Thread class.

t1.start()  
t2.start()  

****Step 4:** End the thread Execution

Once the threads start, the current program (you can think of it like a main thread) also keeps on executing. In order to stop the execution of the current program until a thread is complete, we use the ****join()** method.

t1.join()  
t2.join()  

As a result, the current program will first wait for the completion of ****t1** and then ****t2**. Once, they are finished, the remaining statements of the current program are executed.

****Example:**

Let us consider a simple example using a threading module.

This code demonstrates how to use Python’s threading module to calculate the square and cube of a number concurrently. Two threads,**`t1`**and**`t2`**, are created to perform these calculations. They are started, and their results are printed in parallel before the program prints “Done!” when both threads have finished. Threading is used to achieve parallelism and improve program performance when dealing with computationally intensive tasks.

Python `import threading def print_cube(num):print("Cube: {}" .format(num * num * num)) def print_square(num):print("Square: {}" .format(num * num))if __name__ =="__main__": t1 = threading.Thread(target=print_square, args=(10,)) t2 = threading.Thread(target=print_cube, args=(10,)) t1.start() t2.start() t1.join() t2.join()print("Done!")` 

****Output:**

Square: 100  
Cube: 1000  
Done!  

Consider the diagram below for a better understanding of how the above program works: 

![multithreading-python-4](https://proxy-prod.omnivore-image-cache.app/282x422,sROdSwczVNI48IYCvLx6pgbTMcO28tRZgHIUN1xENCis/https://media.geeksforgeeks.org/wp-content/uploads/20230824111906/multithreading-python-4.png)

Multithreading

****Example:**

In this example, we use ****os.getpid()** function to get the ID of the current process. We use ****threading.main\_thread()** function to get the main thread object. In normal conditions, the main thread is the thread from which the Python interpreter was started. ****name** attribute of the thread object is used to get the name of the thread. Then we use the ****threading.current\_thread()** function to get the current thread object.

Consider the Python program given below in which we print the thread name and corresponding process for each task. 

This code demonstrates how to use Python’s threading module to run two tasks concurrently. The main program initiates two threads,**`t1`**and **`t2`**, each responsible for executing a specific task. The threads run in parallel, and the code provides information about the process ID and thread names. The `os` module is used to access the process ID, and the ****‘** **`threading'`** module is used to manage threads and their execution.

Python `import threading import os def task1():print("Task 1 assigned to thread: {}".format(threading.current_thread().name))print("ID of process running task 1: {}".format(os.getpid())) def task2():print("Task 2 assigned to thread: {}".format(threading.current_thread().name))print("ID of process running task 2: {}".format(os.getpid()))if __name__ == "__main__":print("ID of process running main program: {}".format(os.getpid()))print("Main thread name: {}".format(threading.current_thread().name)) t1 = threading.Thread(target=task1, name='t1') t2 = threading.Thread(target=task2, name='t2') t1.start() t2.start() t1.join() t2.join()` 

****Output:**

ID of process running main program: 1141  
Main thread name: MainThread  
Task 1 assigned to thread: t1  
ID of process running task 1: 1141  
Task 2 assigned to thread: t2  
ID of process running task 2: 1141  

The diagram given below clears the above concept:

![multithreading-python-5](https://proxy-prod.omnivore-image-cache.app/402x402,sSxzzz4aBWbJ7BoAGUsmFQsd5ezZdHVB9hipE_3evQKQ/https://media.geeksforgeeks.org/wp-content/uploads/20230824111950/multithreading-python-5.png)

Multithreading

> So, this was a brief introduction to multithreading in Python. The next article in this series covers ****synchronization between multiple threads**. [Multithreading in Python | Set 2 (Synchronization)](https://www.geeksforgeeks.org/multithreading-in-python-set-2-synchronization/) 

## Python ThreadPool

A thread pool is a collection of threads that are created in advance and can be reused to execute multiple tasks. The concurrent.futures module in Python provides a ThreadPoolExecutor class that makes it easy to create and manage a thread pool. 

In this example, we define a function worker that will run in a thread. We create a ThreadPoolExecutor with a maximum of 2 worker threads. We then submit two tasks to the pool using the submit method. The pool manages the execution of the tasks in its worker threads. We use the shutdown method to wait for all tasks to complete before the main thread continues.

Multithreading can help you make your programs more efficient and responsive. However, it’s important to be careful when working with threads to avoid issues such as race conditions and deadlocks.

This code uses a thread pool created with**`concurrent.futures.ThreadPoolExecutor`** to run two worker tasks concurrently. The main thread waits for the worker threads to finish using **`pool.shutdown(wait=True)`**. This allows for efficient parallel processing of tasks in a multi-threaded environment.

Python `import concurrent.futures def worker():print("Worker thread running")pool = concurrent.futures.ThreadPoolExecutor(max_workers=2) pool.submit(worker) pool.submit(worker) pool.shutdown(wait=True)print("Main thread continuing to run")` 

**Output**

Worker thread running
Worker thread running
Main thread continuing to run


## Multithreading in Python – FAQs

### What is multithreading in Python?

> Multithreading in Python involves running multiple threads concurrently within a single process to achieve parallelism and utilize ****multiple CPU cores**.

### Is Python good for multithreading?

> Python is good for **I/O-bound** tasks with multithreading due to the Global Interpreter Lock (GIL), which limits the execution of only one thread at a time for CPU-bound tasks. For CPU-bound tasks, multiprocessing is often more effective.

### Which module is used for multithreading in Python?

> The ‘****threading’** module is used for multithreading in Python.

### What are the different types of threads in Python?

> The two main types of threads in Python are:
> 
> * ****Main Thread**: The initial thread of execution when the program starts.
> * ****Daemon Threads**: Background threads that automatically exit when the main thread terminates.
> * ****Non-Daemon Threads**: Threads that continue to run until they complete their task, even if the main thread exits.

### How many threads can Python multithreading have?

> There is no fixed limit to the number of threads in Python, but practical limits are determined by system resources and the GIL, which may hinder performance with a large number of threads. Typically, Python applications use tens to hundreds of threads, but for intensive tasks, it’s better to use multiprocessing.

  
"This course is very well structured and easy to learn. Anyone with zero experience of data science, python or ML can learn from this. This course makes things so easy that anybody can learn on their own. It's helping me a lot. Thanks for creating such a great course."- **Ayushi Jain | Placed at Microsoft**

Now's your chance to unlock high-earning job opportunities as a [Data Scientist](https://www.geeksforgeeks.org/courses/data-science-live?utm%5Fsource=geeksforgeeks&utm%5Fmedium=article%5Fbottom%5Ftext%5Fdatascience+pythoncategories&utm%5Fcampaign=courses)! Join our [**Complete Machine Learning & Data Science Program**](https://www.geeksforgeeks.org/courses/data-science-live?utm%5Fsource=geeksforgeeks&utm%5Fmedium=article%5Fbottom%5Ftext%5Fdatascience+pythoncategories&utm%5Fcampaign=courses) and get a 360-degree learning experience mentored by industry experts.

Get hands on practice with **40+ Industry Projects, regular doubt solving sessions**, and much more. [Register for the Program today!](https://www.geeksforgeeks.org/courses/data-science-live?utm%5Fsource=geeksforgeeks&utm%5Fmedium=article%5Fbottom%5Ftext%5Fdatascience+pythoncategories&utm%5Fcampaign=courses)

  
![](https://proxy-prod.omnivore-image-cache.app/0x0,sMTcIiYTLqvMUICHt1WPSoSa5ljNw-_104KbVxT60PG0/https://media.geeksforgeeks.org/auth-dashboard-uploads/Similarreadnew.svg) 

201

Improve ![](https://proxy-prod.omnivore-image-cache.app/0x0,sMTcIiYTLqvMUICHt1WPSoSa5ljNw-_104KbVxT60PG0/https://media.geeksforgeeks.org/auth-dashboard-uploads/Similarreadnew.svg) 

### Please Login to comment...

### Similar Reads

[ Difference Between Multithreading vs Multiprocessing in Python In this article, we will learn the what, why, and how of multithreading and multiprocessing in Python. Before we dive into the code, let us understand what these terms mean. A program is an executable file which consists of a set of instructions to perform some task and is usually stored on the disk of your computer.A process is what we call a prog ![](https://proxy-prod.omnivore-image-cache.app/0x0,sMTcIiYTLqvMUICHt1WPSoSa5ljNw-_104KbVxT60PG0/https://media.geeksforgeeks.org/auth-dashboard-uploads/Similarreadnew.svg) 8 min read ](https://www.geeksforgeeks.org/difference-between-multithreading-vs-multiprocessing-in-python/) [ Multithreading or Multiprocessing with Python and Selenium Multithreading and multiprocessing are two popular approaches for improving the performance of a program by allowing it to run tasks in parallel. These approaches can be particularly useful when working with Python and Selenium, as they allow you to perform multiple actions simultaneously, such as automating the testing of a web application. In thi ![](https://proxy-prod.omnivore-image-cache.app/0x0,sMTcIiYTLqvMUICHt1WPSoSa5ljNw-_104KbVxT60PG0/https://media.geeksforgeeks.org/auth-dashboard-uploads/Similarreadnew.svg) 11 min read ](https://www.geeksforgeeks.org/multithreading-or-multiprocessing-with-python-and-selenium/) [ Multithreading in Python | Set 2 (Synchronization) This article discusses the concept of thread synchronization in case of multithreading in Python programming language. Synchronization between threads Thread synchronization is defined as a mechanism which ensures that two or more concurrent threads do not simultaneously execute some particular program segment known as critical section. Critical se ![](https://proxy-prod.omnivore-image-cache.app/0x0,sMTcIiYTLqvMUICHt1WPSoSa5ljNw-_104KbVxT60PG0/https://media.geeksforgeeks.org/auth-dashboard-uploads/Similarreadnew.svg) 6 min read ](https://www.geeksforgeeks.org/multithreading-in-python-set-2-synchronization/) [ Important differences between Python 2.x and Python 3.x with examples In this article, we will see some important differences between Python 2.x and Python 3.x with the help of some examples. Differences between Python 2.x and Python 3.x Here, we will see the differences in the following libraries and modules: Division operatorprint functionUnicodexrangeError Handling\_future\_ modulePython Division operatorIf we are p ![](https://proxy-prod.omnivore-image-cache.app/0x0,sMTcIiYTLqvMUICHt1WPSoSa5ljNw-_104KbVxT60PG0/https://media.geeksforgeeks.org/auth-dashboard-uploads/Similarreadnew.svg) 5 min read ](https://www.geeksforgeeks.org/important-differences-between-python-2-x-and-python-3-x-with-examples/) [ Python program to build flashcard using class in Python In this article, we will see how to build a flashcard using class in python. A flashcard is a card having information on both sides, which can be used as an aid in memoization. Flashcards usually have a question on one side and an answer on the other. Particularly in this article, we are going to create flashcards that will be having a word and its ![](https://proxy-prod.omnivore-image-cache.app/0x0,sMTcIiYTLqvMUICHt1WPSoSa5ljNw-_104KbVxT60PG0/https://media.geeksforgeeks.org/auth-dashboard-uploads/Similarreadnew.svg) 2 min read ](https://www.geeksforgeeks.org/python-program-to-build-flashcard-using-class-in-python/) [ Reading Python File-Like Objects from C | Python Writing C extension code that consumes data from any Python file-like object (e.g., normal files, StringIO objects, etc.). read() method has to be repeatedly invoke to consume data on a file-like object and take steps to properly decode the resulting data. Given below is a C extension function that merely consumes all of the data on a file-like obj ![](https://proxy-prod.omnivore-image-cache.app/0x0,sMTcIiYTLqvMUICHt1WPSoSa5ljNw-_104KbVxT60PG0/https://media.geeksforgeeks.org/auth-dashboard-uploads/Similarreadnew.svg) 3 min read ](https://www.geeksforgeeks.org/reading-python-file-like-objects-from-c-python/) [ Python | Add Logging to a Python Script In this article, we will learn how to have scripts and simple programs to write diagnostic information to log files. Code #1 : Using the logging module to add logging to a simple program import logging def main(): # Configure the logging system logging.basicConfig(filename ='app.log', level = logging.ERROR) # Variables (to make the calls that follo ![](https://proxy-prod.omnivore-image-cache.app/0x0,sMTcIiYTLqvMUICHt1WPSoSa5ljNw-_104KbVxT60PG0/https://media.geeksforgeeks.org/auth-dashboard-uploads/Similarreadnew.svg) 2 min read ](https://www.geeksforgeeks.org/python-add-logging-to-a-python-script/) [ Python | Add Logging to Python Libraries In this article, we will learn how to add a logging capability to a library, but don’t want it to interfere with programs that don’t use logging. For libraries that want to perform logging, create a dedicated logger object, and initially configure it as shown in the code below - Code #1 : C/C++ Code # abc.py import logging log = logging.getLogger(\_ ![](https://proxy-prod.omnivore-image-cache.app/0x0,sMTcIiYTLqvMUICHt1WPSoSa5ljNw-_104KbVxT60PG0/https://media.geeksforgeeks.org/auth-dashboard-uploads/Similarreadnew.svg) 2 min read ](https://www.geeksforgeeks.org/python-add-logging-to-python-libraries/) [ JavaScript vs Python : Can Python Overtop JavaScript by 2020? This is the Clash of the Titans!! And no...I am not talking about the Hollywood movie (don’t bother watching it...it's horrible!). I am talking about JavaScript and Python, two of the most popular programming languages in existence today. JavaScript is currently the most commonly used programming language (and has been for quite some time!) but now ![](https://proxy-prod.omnivore-image-cache.app/0x0,sMTcIiYTLqvMUICHt1WPSoSa5ljNw-_104KbVxT60PG0/https://media.geeksforgeeks.org/auth-dashboard-uploads/Similarreadnew.svg) 5 min read ](https://www.geeksforgeeks.org/javascript-vs-python-can-python-overtop-javascript-by-2020/) [ Python | Index of Non-Zero elements in Python list Sometimes, while working with python list, we can have a problem in which we need to find positions of all the integers other than 0\. This can have application in day-day programming or competitive programming. Let's discuss a shorthand by which we can perform this particular task. Method : Using enumerate() + list comprehension This method can be ![](https://proxy-prod.omnivore-image-cache.app/0x0,sMTcIiYTLqvMUICHt1WPSoSa5ljNw-_104KbVxT60PG0/https://media.geeksforgeeks.org/auth-dashboard-uploads/Similarreadnew.svg) 6 min read ](https://www.geeksforgeeks.org/python-index-of-non-zero-elements-in-python-list/) 
