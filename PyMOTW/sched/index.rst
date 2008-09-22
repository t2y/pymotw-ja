=====
sched
=====
.. module:: sched
    :synopsis: Generic event scheduler.

:Module: sched
:Purpose: Generic event scheduler.
:Python Version: 1.4
:Abstract:

    The sched module implements a generic event scheduler for running tasks at
    specific times.

Description
===========

The scheduler class uses a generic interface to schedule events. It uses a
time function to learn the current time, and a delay function to wait for a
specific period of time. The actual units of time are not important, which
makes the interface flexible enough to be used for many purposes.

The time function is called without any arguments, and should return a number
representing the current time. The delay function is called with a single
integer argument, using the same scale as the time function, and should wait
that many time units before returning. For example, the time.time() and
time.sleep() functions meet these requirements.

To support multi-threaded applications, the delay function is called with
argument 0 after each event is generated, to ensure that other threads also
have a chance to run.

Running Events With a Delay
===========================

Events can be scheduled to run after a delay, or at a specific time. To
schedule them with a delay, use the enter() method, which takes 4 arguments:

* A number representing the delay
* A priority value
* The function to call
* A tuple of arguments for the function

This example schedules 2 different events to run after 2 and 3 seconds
respectively. When the event's time comes up, print_event() is called and
prints the current time and the name argument passed to the event.

::

    import sched
    import time

    scheduler = sched.scheduler(time.time, time.sleep)

    def print_event(name):
        print 'EVENT:', time.time(), name

    print 'START:', time.time()
    scheduler.enter(2, 1, print_event, ('first',))
    scheduler.enter(3, 1, print_event, ('second',))

    scheduler.run()

The output will look something like this:

::

    $ python sched_basic.py
    START: 1190727943.36
    EVENT: 1190727945.36 first
    EVENT: 1190727946.36 second

The time printed for the first event is 2 seconds after start, and the time
for the second event is 3 seconds after start.

Overlapping Events
==================

The call to run() blocks until all of the events have been processed. Each
event is run in the same thread, so if an event takes longer to run than the
delay between events, there will be overlap. The overlap is resolved by
postponing the later event. No events are lost, but some events may be called
later than they were scheduled. In the next example, long_event() sleeps but
it could just as easily delay by performing a long calculation or by blocking
on I/O.

::

    import sched
    import time

    scheduler = sched.scheduler(time.time, time.sleep)

    def long_event(name):
        print 'BEGIN EVENT :', time.time(), name
        time.sleep(2)
        print 'FINISH EVENT:', time.time(), name

    print 'START:', time.time()
    scheduler.enter(2, 1, long_event, ('first',))
    scheduler.enter(3, 1, long_event, ('second',))

    scheduler.run()

The result is the second event is run immediately after the first finishes,
since the first event took long enough to push the clock past the desired
start time of the second event.

::

    $ python sched_overlap.py 
    START: 1190728573.16
    BEGIN EVENT : 1190728575.16 first
    FINISH EVENT: 1190728577.16 first
    BEGIN EVENT : 1190728577.16 second
    FINISH EVENT: 1190728579.16 second


Event Priorities
================

If more than one event is scheduled for the same time their priority values
are used to determine the order they are run. 

::

    now = time.time()
    print 'START:', now
    scheduler.enterabs(now+2, 2, print_event, ('first',))
    scheduler.enterabs(now+2, 1, print_event, ('second',))
    scheduler.run()

In order to ensure that they are scheduled for the exact same time, the
enterabs() method is used instead of enter(). The first argument to enterabs()
is the time to run the event, instead of the amount of time to delay.

::

    $ python sched_priority.py 
    START: 1190728789.4
    EVENT: 1190728791.4 second
    EVENT: 1190728791.4 first


Canceling Events
================

Both enter() and enterabs() return a reference to the event which can be used
to cancel it later. Since run() blocks, the event has to be canceled in a
different thread. For this example, a thread is started to run the scheduler
and the main processing thread is used to cancel the event.

::

    import sched
    import threading
    import time

    scheduler = sched.scheduler(time.time, time.sleep)

    # Set up a global to be modified by the threads
    counter = 0

    def increment_counter(name):
        global counter
        print 'EVENT:', time.time(), name
        counter += 1
        print 'NOW:', counter

    print 'START:', time.time()
    e1 = scheduler.enter(2, 1, increment_counter, ('E1',))
    e2 = scheduler.enter(3, 1, increment_counter, ('E2',))

    # Start a thread to run the events
    t = threading.Thread(target=scheduler.run)
    t.start()

    # Back in the main thread, cancel the first scheduled event.
    scheduler.cancel(e1)

    # Wait for the scheduler to finish running in the thread
    t.join()

    print 'FINAL:', counter

Two events were scheduled, but the first was later canceled. Only the second
event runs, so the counter variable is only incremented one time.

::

    $ python sched_cancel.py
    START: 1190729094.13
    EVENT: 1190729097.13 E2
    NOW: 1
    FINAL: 1

