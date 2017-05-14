Electronics
===========

It's our intention to make this project as easy as possible for us, which means that we will *not* rewire the machine
from scratch. Instead we'll replace the MPU board with a P-ROC or FAST WPC controller (MPF supports either with just a
few lines of config file changes). We'll reuse the existing WPC driver board.

We will be able to remove the DMD board and sound board. We'll replace the DMD board with a
`Smart Matrix RGB LED DMD <http://docs.missionpinball.org/en/latest/displays/display/physical_rgb_dmd.html>`_. Sound
will be driven by the host computer that runs MPF.

Removal of those two boards will free up space to install a small single-board computer to run MPF in the backbox. We'll
probably run Linux since it's free and easy to use with MPF.

We'll reuse the original transformer and power supply, but will also install an additional 5v power supply to power our
computer and LEDs since they will draw more current than is available in the built-in 5 volt line available in the 20+
year old machine.

Lights & LEDs
-------------

We will update the machine to LEDs, but use the "drop in replacement" style LEDs that are commonly available for pinball
machines. That will allow us to reuse the existing lamp matrix without a lot of rewiring.

Some of the playfield inserts are transparent, so for those we'll replace the original lamps with modern RGB LEDs so we
have full color control. We'll use either a FadeCandy (if we're using a P-ROC) or the built-in RGB LED controller of the
FAST Pinball controller to drive the LEDs.

Ticket Counter
--------------

Since :doc:`tickets </concepts/tickets>` is a central concept in the game, we want to add an LED segmented ticket
counter somewhere. We don't know where we'll add it yet. Possibly in the right rear corner.

Gun Replacement
---------------

We'll replace the gun-shaped ball launch switch with a regular switch.

Driver Reassignment
-------------------

We want to add some new drivers to *State Fair Pinball* that were not originally in *The Shadow*.

First is an powered up/down post which can hold balls in the right habitrail about 6 inches before it drops the ball
into the right inlane. This will use used in various game modes (basketball, quick draw).

We also want to add the rotating red beacon on the top of the machine.

Third is the mechanical bell on the side of the backbox.

One option would be to add a driver board (either a PD-16 if we're using a P-ROC or an 0804 if we're using a FAST Pinball
controller). Another option is to repurpose 3 flasher outputs to drive these devices and then to replace the original
high-voltage flashers with LEDs.