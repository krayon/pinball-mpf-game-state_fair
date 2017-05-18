Welcome to State Fair Pinball!
==============================

This repository is for the *State Fair Pinball* (SFP) machine, a new machine currently being
conceived by the people who are creating the `Mission Pinball Framework <http://missionpinball.org>`_
(MPF).

The theme of the machine is a state fair. (Duh!) Think carnival games, demolition derbies,
livestock judging, pie-eating contests, amusement rides, and deep-fried food.

*State Fair Pinball* is designed to be a "teaching machine"—ultimately a complete game
that we can use for the MPF tutorial.

Our goal is to not use any licensed content and to make all the plans, assets, designs, etc.
available for free. So if you want to build your own (or use the base plans for your own),
then you're free to.

.. note::

   Everything here is just an early draft as our ideas come together. Lots will
   change, and we'd love your feedback too!

*State Fair Pinball* attempts to capture the experience of being at a state fair. All of
the game modes are based on things you do at a fair, including riding attractions,
playing carnival games, and eating food.

One of the central concepts of the game is "tickets" (which are tracked per player, separate
from score). Just like a real fair, you need tickets to do things, which you earn through
game play. Several game modes are carnival games, which cost tickets to play, but also where you can
win tickets which you can then use to do more things. (So everything you do costs tickets,
but some things earn you tickets as well.)

You get to the wizard mode by doing everything in at fair, so if you're good and you
can earn lots of tickets quickly then you can move through all the modes, but if you're
not as good you might have to play some of the carnival games a few times to earn enough tickets for the
later things. (More on tickets :doc:`here <concepts/tickets>`.)

Since SFP is a teaching machine, we're going to try to add as much as we can into it. So some things might be over
the top, but everything that's there is for the purpose of demonstrating how it could be done.

.. toctree::
   :titlesonly:
   :caption: The Machine / Hardware

   hardware/playfield
   hardware/backbox
   hardware/backbox_toy
   hardware/electronics

.. toctree::
   :titlesonly:
   :caption: Game Concepts, Rules & Modes

   concepts/tickets
   concepts/skill_shots
   concepts/food
   /midway_games/index
   /attractions/index
   concepts/multiballs
   concepts/bonus
   concepts/combos
   concepts/prize_booth
   concepts/rides
   concepts/wristband
   concepts/zoltar
   concepts/video_modes
   concepts/wizard_mode

.. toctree::

   Download <download>

Yet to figure out
-----------------

There are several other concepts which can be incorporated that we haven't figure out yet,
including:

* Ribbons & judging
* Day and night modes
* Power outage mode. Could have a cool light show effect of colored lights
  blowing up with bright white flashes.
* Mode stacking
* Modes you can play again and again
* Modes you have to play multiple times
* Modes you only do once and then complete