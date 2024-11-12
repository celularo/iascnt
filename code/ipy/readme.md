# directory for interactive modules
(pwd for ipython) 

## code-as-frame paradigm for interaction

reminding principles like 'infrastructure-as-code' or 'everything-as-code'
we observe sooner or later that in our situation of 

	[-DataFrames in pandas occupied with integers 
	which we implement to help our own interactive 
	factorization and primality testing goals within ipython-]

it could be benefitial to follow an ansatz that I would call 'code-as-frame'.

.. meaning that for human interaction in ipython with integers to crack ahead the role 
code usually plays is actually settled in the frame itself.

But this also means that the python code for the frames should not be considered as readable clean code 
in its literal meaning. It's actually better to consider it as not 
necessarily clean pre-version of code for the sake of producing clean code-as-frame at the frontend
in the client in any way possible. 

Along these lines it becomes logical even, to remove not only semantics from the modules,
but result functionality in general. 
That way forcing the interaction and the 'compilation' of the frames
in the users own investigations.

Nevertheless the python coding for the frames contains their persistence as gear for usage in interactive
sessions. This requires frequent use of ipys `autoreload` functionality on the one hand and also to consider
the stretches as products which we bring to the state of 'zuhandenheit' (cf. m heidegger, sein und zeit)
on the other hand.
And the continuous development of this state is part of every interactive session.

Thus it is better to let them carry  additional product information instead of result functionality. 

In particular a start date of devel, an end date of devel, an owner, a ringing name.
The same way an astronomer would name a new star or a nebula...
This way the persistant frames hopefully will become ready for frequent re-use for a long time.

In other words: 
In the code-as-frame paradigm we expect persistant frames to come with a lifecycle
that that can be key idea of meaningful and efficient interactive sessions.
And here the emphasis is put on efficient. Indicating again that the reasonable view of 
'sustained' pre-version stretches 'under the hood' for factoring integers with `iascnt`.
