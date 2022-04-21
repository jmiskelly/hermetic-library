# hermetic-library

This is a simple application for randomly generating libraries for Ars Magica 5th edition.

The app is just a python script, but there is an executable (bookgen.exe) you can run in /dist/gui if you don't have python installed or don't know how to run a python script.

## Basic Functions
The core of the app is a library generator. You supply it with a number of unused build points (based off the rules given in the "Covenants" supplement), hit "Generate Books" and it generates new books on random topics until all the build points are used up.

There are various options for adjusting this process, explained below. Once you have a library generated you can save and load library files as well. The file format doesn't actually matter, but saving as .txt makes them easy to view outside the app.

There is also a "scriptorium" where you can edit books in the randomly generated library, and add new ones. There is a delete button too, but it doesn't actually do anything right now.

## Options

Favoured Topics: You can provide a comma delineated list of things the library should focus on (e.g. "Magic Theory,Ignem,Penetration"). The book selection logic has a 50% chance to choose one of these topics each time, 25% to pick a random Art, 12.5% to pick from a pre-defined list of "hermetic favoured abilities", and 12.5% to pick a totally random ability. 

Library Build Points: Tracks the total bp spent on the library. Non-editable.

Unused Build Points: The number of build points to add to the library. You can keep adding to the library in chunks after the initial generation.

Tractatus Min/Max Quality: The range of quality values that a Tractatus can generate with. 11 is the upper limit set by Covenants so that's the default max.

Summa Min/Max Level: The range of level values that a Summa can generate with. Non-editable (for now)

Summa Min/Max Quality: The range of quality values that a Summa can generate with. Non-editable (for now)
