_"Dammit! So let's recap: there are four directions that I can move in and none of them work. What the fuck am I supposed to do?"_

An annoying aspect of old-school Text Parser\-based Adventure Games, especially Interactive Fiction, was a limited ability to recognize command inputs. These games would frequently not only refuse to do what you wanted them to do, but also not give you any hint as to what you were _supposed_ to do. For example, let's say the command to look at a monster was "look monster". If you typed in "look at monster", the game might say something like, "I don't know how to do that" or "I don't see an 'at' here". It was enough to make you want to put your fist through the screen.

The Trope Namer is _Homestar Runner_, specifically the _Strong Bad Email_ "video games", where Strong Bad imagines himself as a character in a text-based adventure game and envisions this problem occurring:

**Strong Bad:** And you'd be all like, "get ye flask", and it'd say "You can't get ye flask", and you'd just have to sit there and imagine _why on Earth_ you can't get ye flask! Because the game's certainly not going to tell you.

This phenomenon, alternatively known as "Guess the Verb" or "Guess the Syntax", is a defining trope of Interactive Fiction; although parsers have improved over time, the problem has never gone away completely, and probably won't for as long as developers amuse themselves with text parsers that try to predict a player's off-the-wall inputs and create suitably off-the-wall responses. Fans of the genre insist the problem was never as bad as people claim and lament it being the genre's defining characteristic, but it remains a sign of shoddy programming.

Different games have developed different ways to avoid the problem over time. Some games will tell you up-front all of the verbs and nouns it will accept; Chris Crawford's _Storytron_ engine gives you a drop-down list for each part of the sentence which will only offer you valid combinations. Another way is to anticipate archaic or unusual synonyms for certain words (_e.g._ calling a bathtub plug a "stopper"); some games even allowed you to define a word in terms of the game's established vocabulary, effectively giving you a custom command.

Some companies had better parsers than others; Infocom and Legend tended to have good, responsive parsers, whereas Sierra games were infamous for this problem.

Compare Pixel Hunt, the equivalent trope for Point-and-Click games. Contrast Developer's Foresight and Unexpectedly Realistic Gameplay, which in text-based games generally means that even commands you _wouldn't_ expect to work will do something. Has nothing to do with You Cannot Grasp the True Form.

___

## Examples

    open/close all folders 

    Adventure Games 

-   Notably averted in _AI Dungeon 2_. As the name suggests, the game uses an advanced AI to generate its prompts on the fly based on the player's input. No matter _what_ the player types in, the AI will usually respond to it in some way. It still sometimes gets stuck or repeats itself, requiring a rewind to the previous prompt, but most coherent inputs will get some kind of response from the game (though not necessarily one that makes much sense).
-   _Deathmaze 5000_, for the TRS-80 and Apple \]\[, contained (among other things) several problems of this type:
    -   In the first level, there's a pit containing an item you need to complete the game. Once you stepped on it, you were stuck in one place, and your only clue was "To everything there is a season," and, to hammer the point home, after a few minutes it would also shout, "To everything, TURN TURN TURN." Typing in "Turn" did nothing. Physically turning using the move keys did nothing. None of the items on that level were "turnable". The only way to know what to do was to buy the hint sheet from the software company.
    -   At another point in the game, you had to fart to get out of trouble. You had to guess that you had to type "fart" to do this. There were no hints that this was a valid command, and even if you used it before, there was no indication that it did anything useful (although it did propel you down the hallway on a jet of your own exhaust).
-   8-bit adventure _Heroes Of Karn_ required you to extinguish some smouldering ashes with the water you were carrying. None of PUT WATER ON, DROP WATER ON, POUR WATER ON, USE WATER WITH, QUENCH, DOUSE, EXTINGUISH, COOL, DAMPEN, MOISTEN, SOAK, DRENCH, FLOOD, WET or IMMERSE ASHES would work. It would only accept "WATER ASHES". Figuring this out was by far the hardest part of the game.
-   Parodied in _Hugo's House of Horrors_:
    
    \-> open bolt
    
    Please say "undo bolt".
    
-   _Laura Bow_ had issues with the generic "use" command, which adventure gamers had been conditioned to use as a catch-all verb to use an item. Here, you had to guess the correct verb; typing "Use crank", for instance, would give you "How do you want to use the crank, Laura?"
-   Pretty much the entire point of _Pick Up the Phone Booth and Aisle_ is trying different verbs to see what ending you get.
-   Sierra was infamous for this sort of problem, as its parser never evolved beyond simple "<verb> <noun>" phrases, even after a decade:
    -   Sierra's very first game, _Mystery House_, infamously accepted "PRESS BUTTON" but not "PUSH BUTTON".
    -   _Leisure Suit Larry 2: Looking for Love (in Several Wrong Places)_ had an infamous sequence at the end where the player has to make a bomb using an airsick bag as the wick. The problem is that "bag" is not considered a synonym for "airsick bag", despite there being no other bag in a five-mile radius. Lead programmer Al Lowe explained that this was the result of an unrelated bug which another programmer fixed by turning "bag" into a verb, which Lowe never noticed and escaped all testing. Longtime scuttlebutt suggested that the correct command was a full but grammatically incorrect sentence with the word "the" repeated several times.
    -   _King's Quest_ games mostly allowed you to unlock doors with a variety of phrases, such as "open door with key", "put key in hole", or "use key to open door" — but the magical door in _King's Quest II: Romancing the Throne_ could only be opened with the command "unlock door".
    -   _King's Quest III: To Heir Is Human_:
        -   As part of its copy protection, the game included several spells the player needed to cast. Rather than an easily-copied phrase, each spell consisted of several steps requiring advance preparation. Unfortunately, several of those steps required a specific verb or the entire process would fail.
        -   A key item is located on top of a wardrobe. Unfortunately, while "look on wardrobe" is accepted, it only gives the player a description of the wardrobe itself. This can cause the player to then walk off assuming that they have already tried looking on top of the wardrobe. "Look _above_ wardrobe" is the command actually needed.
    -   In the first _Space Quest_ game, you have to "insert" the keycard. No synonym or rephrasing of that unusual and unnecessarily technical term will be accepted.
    -   Parodied at one point in _Quest for Glory II_, where the player has to use a lamp to catch a fire elemental. While "Use lamp" is the "correct" input, the game will not only accept synonyms but even has funny messages tied to them; "put down lamp" has the player verbally abuse the lamp, while "drop lamp" has the player break up with it.
        -   Likewise, later in the game the player has to steal a "Blackbird statue" for a local thief. When he asks you to hand it over, the command "give Ferrari the bird" not only works but produces the expected result.
    -   If you enter something incorrectly in the latter half of _Gold Rush!_, it would tell you that "there ain't such a word as ...". Humorously, it will still give you that message if the word in question is "ain't".
-   Among the many frustrating puzzles in _Starship Titanic_ is obtaining a broken eye from Titania, the ship's AI. It's one of four similar looking globes (the others are light bulbs). You can poke it, and the game will tell you what it is. But you can't just grab it yourself; you have to summon the Bellbot, hold your cursor over the correct globe, and type, "Get the broken eye". "Get the eye", "Hand me the eye", "Give me Titania's eye", and "Give the eye to me" will not work; bizarrely, "Get the broken bulb" will.
-   A Spanish-language video game adaptation of _Zipi y Zape_ had a sequence where you had to drop a nail on the ground so that your father sits on it and drops a patch. It took players _seventeen years_ to find the correct command, "throw nail under tree" — and that only through hacking the game files. People had been trying all sorts of variations of "drop nail" or "put nail near father", with no success. More detail in Spanish here.
-   _Heroine's Quest_ references the Trope Namer; if you try to take certain flasks from the herbalist's shop, it will straight-up tell you that "you can't get ye flask".

    Interactive Fiction 

-   Scott Adams' 1978 _Adventureland_ required the player to enter the unintuitive UNLIGHT LAMP in order to prevent a lamp from using up its fuel; it would not recognize the verb EXTINGUISH (and certainly not the phrases PUT OUT or TURN OFF).
-   The Angry Video Game Nerd encountered this problem trying to play _The Count_ on the VIC-20, resulting in this exchange where he can't even find his way out of a room:
    
    "Okay, so I went north? What'd that do?"  
    \> go east  
    OK. What shall I do now?  
    \> go east again  
    Use 1 or 2 words only!  
    "Oh, okay, I'll give you two words!"  
    \> fuck you  
    Don't know how to "FUCK" something.
    
-   _Bureaucracy_ uses this as a game mechanic; you get penalized for inputting an incorrect command, by an increase in "blood pressure". If blood pressure becomes dangerously high, your character dies.
-   _Curses_ by Graham Nelson had a section where you had to cram a voice-operated robot mouse into a mouse hole and then give it instructions — only the standard commanding language explained in the instructions ("mouse, go north") didn't work. Trying every verb on every object randomly might bring you to the correct solution: you have to address the hole, not the mouse ("hole, go north").
-   The _Fahrenheit 451_ text adventure, already fiendishly difficult, exacerbated the problem with parser issues. Sometimes different commands worked in different situations; you might need "talk to man" in one instance, but "ask man" in another, and there was no indication of which one to use. Worse, you advanced the plot by contacting members of the Underground, using literary quotations as pass-phrases — but if you typed them in incorrectly, even the punctuation, the game would boot you out of the building and force you to make your way all the way back inside.
-   _Guess the Verb_ is an Interactive Fiction game that satirizes the concept; each scenario can only be resolved by guessing an uncommon verb.
-   The text adventure adaptation of _The Hitchhiker's Guide to the Galaxy (1984)_ seemed to use bad parsing and senseless commands almost deliberately; one PC magazine described the game as "toying with various ways of saying PUT BABEL FISH UP ZAPHOD'S JACKSIE." Specifically:
    -   An early puzzle on the Vogon ship required you to remember a particular word from the Vogon poetry and type it in while you were in the airlock. But you need to include quotation marks — and not all ports of the game supported them.
    -   At one point in the game, you're _expected_ to type in an invalid command; it's designed to spontaneously enter a wormhole, be interpreted as a grave insult, and instigate a bloody war between two alien races, but you couldn't have guessed that. If you could, though, you do get extra kudos for inputting the actual line from the book that serves this purpose: "I seem to be having tremendous difficulty with my lifestyle".
    -   You have to obtain a cup of tea, but the game will reject the command GET TEA. That's because it's _not_ actually tea, but rather an "Advanced Tea Substitute" (or "ATS" — almost, but not quite, entirely unlike tea). You had to type GET CUP or GET ATS. It's important to know this distinction because later in the game, you obtain real tea, and you have to demonstrate your philosophical depth by carrying tea and no tea at the same time.
-   The _Spellcasting 101_ series tried to avert this trope by showing a complete list of all the verbs the game would accept in a sidebar; you could play the entire game with just a mouse.
-   Infocom's text adventure adaptation of James Clavell's _Shogun_ has the protagonist trying to communicate with the Japanese by searching for a common language. Some players tried inputs in actual foreign languages, which wouldn't work. But if you typed something like "Say 'where am I' in Spanish", you'd crash the parser.
-   _The Multi Dimensional Thief_ has some changes between version 1 and version 2. "Put Hole on North" works in the AGT version, but version 2 requires typing the full "put hole on north wall".
-   _Murder in the Museum_ on the _Big Blue Disk_ deliberately and cruelly invoked this trope and forced the player to guess obscure nouns — _e.g._ you must type "femur" for what was described as a "leg bone" or "Derringer" for what was described as "small gun". It also gave you a time limit, which limited the number of guesses you could make.
-   The original _ADVENT_, _a.k.a._ _Colossal Cave_, had a sequence that looked like a snappy comeback to a stupid input, but was actually required to progress, as it was the only way to kill the dragon:
-   The Edutainment Game _Voices Of Spoon River_ several times explicitly tells the player to "place" something on something else — but the verb "place" isn't implemented. It's not too hard to figure out that you have to "put" instead, but it's still weird.
-   _Ad Verbum_ makes an art of this — for instance, one room is described entirely in words beginning with S, and will only accept commands beginning with S (of note: the only exit is to the north). On the plus side, the parser is willing to accept a large number of words that wouldn't appear in a normal game.
-   In _The Six Foot Tall Man Eating Chicken_ asks you at one point to plug a hole in a bucket with a cork. The words "plug" and "use" don't work; you have to write "put", which is not otherwise used.
-   Infocom's _Enchanter_ at one point places an essential scroll (essential as in "the game cannot be successfully completed without it") inside a mouse hole. Retrieving the scroll is complicated in that "get scroll" doesn't work, and neither does "get all from hole," or any permutation thereof. The only command that will work is "reach into hole," which wouldn't have been so aggravating if "reach" was used anywhere else in the game.
-   This sort of problem, among others, is heavily parodied in the Adrift games featuring Clueless Bob Newbie, text adventure "author" and legend in his own mind.
-   Apple II adventure game _The Mask of the Sun_ featured a battle against a skeleton which could only be defeated by using a magic amulet picked up earlier in the game. Unfortunately, the only phrase which would allow you to successfully battle the skeleton was the non-intuitive "FIGHT AMULET". Computer game developer Dan Spitzley described the anguish this generated within his family on IGN's RPG Vault in 1999.
-   One puzzle in the ZX Spectrum game _Danger! Adventurer at Work!_ is to animate a monster using electricity. The only commands which will do this are "ATTACH ELECTRODES" followed by "THROW SWITCH". Reasonable alternatives such as "CONNECT WIRES" or "TURN ON POWER" don't work.
-   _Mystery Science Theater 3000 Presents "Detective"_ parodies this frequently, even outside the context of the game it's riffing on.
    -   The introduction touches on it when Mike attempts to play Gypsy's game _Richard Basehart Adventure_. He's unable to EXAMINE or TALK TO RICHARD BASEHART, and Gypsy has to tell him that the solution is to KISS RICHARD BASEHART (which also concludes the game).
    -   The Invention Exchange directly spoofs it with the Mads' "Fictionary", which attempts to circumvent the problem by sending the game's vocabulary directly into your brain. Naturally, the demonstration goes awry:
        
        **Dr. Forrester:** Frank?  
        **Frank:** Sorry, but I don't know the word "Frank."  
        **Dr. Forrester:** _\[a little alarmed\]_ Frank, what's happening?  
        **Frank:** Sorry, but I don't know the word "happening."  
        **Dr. Forrester:** What the...?  
        _\[Forrester opens the computer case and looks inside\]_  
        **Dr. Forrester:** Frank, you numbskull, you wired it all wrong! It's sending the parser itself into his brain. Right now, Frank thinks he's a ZIP interpreter.  
        **Frank:** I don't understand. Please try rephrasing that.  
        **Dr. Forrester:** _\[a little embarrassed\]_ As you can see, we still haven't gotten all the bugs worked out...  
        **Frank:** I can't go that way.
        
    -   The game itself has an example almost exactly like the Trope Namer: one room outright tells the player they see a knife, yet refuses to allow them to interact with it in any way.
        
        \>examine knife
        
-   _Burial Ground Adventure_ for the TRS-80 has at least two puzzles which suffer from this problem, both times apparently forced by the limitation of two-word commands. In the first one, you need to get out of the pit by making a lasso with a rope and catching a rock outside the pit to climb out. Commands such as "tie rope", "attach rope" etc. don't work—you need to "throw rope". In another example, a trap door in the ceiling must be opened by pushing it open with a bamboo stalk. The command to type? Not "open door" or even "push door": it's _"push bamboo"_.
-   Parodied in _The Very Big Cave Adventure_, in the location "The Brand New Sophisticated Parser Cave". The game takes every opportunity to misinterpret the commands you enter, including taking advantage of the fact that only the first four letters of a word are significant:
    
    \>get parser
    
    You can't see a parsimonious filing-clerk here.
    
-   _Supernova_ had two cases where the player need to use an adverb in order to progress the game: "Listen carefully", and "examine robot carefully". As a side note, adverbs themselves had synonyms, which would accept "Listen gently".
-   Text adventures released by Spinnaker Software (including their subsidiary, Windham Classics) would often let you call up a list of words that could be accepted in the context of the current screen as Anti-Frustration Features.
-   The trope namer was directly inspired by a game called "Vampire's Castle", a game written in only 181 lines of Basic code and with a particularly fussy text parser that only looks at the first three letters of each word you type.
    -   Vampire's Castle eventually got a playthrough/mockery video from Strong Bad.
-   _Orfeo en los Infiernos_ by Xavier Carrascosa was noted for this sort of problem, to the point where a review upon initial release in 1997 was roughly titled "I can't do that." A remake in 2004 had a more advanced parser, but still ran into this during a point where you have to pour water on an olive tree to make it grow, as neither "poner agua en el arbol" or "verter agua en el árbol" work, with the correct solution being "riega el árbol" (water the tree).

    MMORPGs 

-   Parodied in the screenshots of this _City of Heroes_ April Fools' Day announcement, which illustrates a text-based version of the game.
-   _Everquest_ suffers from a form of this trope. When talking to NPCs, you will find certain words in \[brackets\], indicating that they have more to say on that subject; you need to type those words into the chat log to continue down that line of conversation. But it's not always as simple as just repeating the words; sometimes, you have to put it in the form of a question, and just as often you just added the word "what" before the bracketed text without regard for syntax. Other times, the developers are clearly messing with you, like when you ask Bootstrutter about "jboots" only for him to say, "What nonsense is this about jboots? Speak to me of Journeyman's Boots!"
-   In one storyline mission in _Forum Warz_, you have to complete a text adventure game and tell the character who gave you the mission how you did it. In the mission ending conversation, you tell him you have to enter the command "push button", not "press button". But while playing the text adventure itself, you can complete that section with the command "use button".
-   The Leaflet Quest section of _Kingdom of Loathing_ that is a Shout-Out to the _Zork_ games. Since it's not too large, a _lot_ of detail was put into putting smart-aleck responses to random commands not facilitated by the usual Infocom queue. But it also had its Ye Flask moments; typing "enter house" makes you go inside the house, but "leave house" and "exit house" won't work; you have to "(go) west" to get back outside. This is especially confusing for text-quest newbies, as the house is right next to the starting point and they may not even realize that "go \[direction\]" commands exist.
-   To this day, LPMUD still can't parse _look <object>_ without admonishing the player to "Look AT or IN something." Even some Diku MUDS still hold to this convention. Even though _examine <object>_ can be abbreviated to _x <object>_, _look_ won't be accepted without a preposition. Infocom and Legend games likewise do not accept "look <object>" or "use <object>" on grounds that they aren't meaningful sentences.

    Role-Playing Games 

-   Oddly enough, this was a reason the answer puzzles were so reviled in _Tales of Rebirth_, despite coming out in 2004 when such problems should have been long fixed. Instead of having a list of choices to input, one had to write out their answer to the puzzle — and it was very fussy about the specific wordings it would accept, taking almost no synonyms. No other _Tales Series_ game uses this system, instead offering several dialogue options. Several of these puzzles were dropped in the remake, and this may have contributed to the game not being translated.
-   _Elona_ occasionally lets you type in an item's name and have it granted to you. However, the text parser is wonky and sometimes grants you something different from what you wanted.

    Survival Horror 

-   _LifeLine_ on the PS2 plays similarly to a text adventure, albeit one controlled by the player's voice than with a keyboard. Aside from the joys of iffy voice recognition causing much frustration and the genre standard "Guess the Noun" portions, there are several instances in which very specific phrases must be used to get the proper effect. One chip is particularly difficult to acquire, just because it was located behind a bag of some sort, and telling Rio to "check behind bag" didn't work for some reason.

## Non-video game examples:

    Comedy 

-   _John Robertson's The Dark Room_, the "world's first live-action text adventure game", lampshades this in its opening narration, as the Guardian of the Dark Room describes text-based adventure games as "you, locked in a room with a fascist Old Testament God who loved grammar, and hated you."

    Films — Live-Action 

-   Phelous points out that the website in _FeardotCom_ seems to run on this sort of interface.
-   _I, Robot_ shows Detective Spooner speaking with Dr. Lanning's hologram several times, and is frequently frustrated at the rather shallow pool of questions that it has been programmed to answer.

    Literature 

-   Brought up a few times in "The Craft of the Adventure". One item on the "Bill of Player's Rights" is "Not to have to type exactly the right verb". Another is "To be allowed reasonable synonyms". And "…At War With a Crossword" lists "The 'What's-The-Verb' syndrome" as one of the three big pitfalls in making puzzles.

    Live-Action TV 

-   Parodied in an episode of the _Limmy's Show_ sketch "Adventure Call" (part adventure game, part premium-rate phone-in game show), when a contestant encounters a troll. He attempts both "Get troll" and "Put troll in bag" to no avail, before attempting "Get troll" again, learning that Falconhoof doesn't understand how to "get" the troll. But then...

    Tabletop Games 

-   This can occasionally happen in Tabletop Games, even though there's a real person at the other end who can presumably understand you. It usually happens when the PC and the GM have completely different ideas about what the player is trying to do. This can lead to hysterical and/or catastrophic results.

    Web Animation 

-   _Homestar Runner_ is the Trope Namer, and that reference (seen in the trope description) has become so famous that it's become a Running Gag in _Homestar Runner_ media — especially its video games. For instance:
    -   In _Thy Dungeonman_, you have to guess the correct command as the dungeon caves in on you.
    -   In _Thy Dungeonman 2_, the game explicitly tells you in certain rooms that cardinal directions like "east" and "west" won't work, and instead you have to use commands like "eastward" and "roughly westish".
    -   Several games explicitly reference "ye flask"; _Thy Dungeonman 3_ makes getting ye flask the object of the game, and _Strong Bad's Cool Game for Attractive People_ has an extended rant about leaving "ye flasks" around without letting others get them. We even get to see Strong Bad struggling mightily and failing to reach it onscreen, just to make it even more ridiculous when we can plainly see he shouldn't have trouble getting it.
    -   The bonus email "E-Mail Birds" features another parody of this phenomenon. Strong Bad decides to play "Text Quest", which describes a room as containing "a dagger" and "another dagger". But when Strong Bad types "get dagger" it just responds "What is 'dagger'?"
        
        **Strong Bad:** Oh, you stupid game! The dagger you just told me about!
        

    Webcomics 

-   _Dinosaur Comics_ references the phenomenon, along with other early Adventure Game tropes, especially their tendency to be Nintendo Hard. One strip sees T-Rex wondering what life would be like as a text-based adventure; Utahraptor points out that no one would ever be able to get out of bed until they found the right command:
    
    get up  
    I don't see "up" here
    
-   At one point, the cast of _Okashina Okashi_ gets trapped in an alternate dimension based on these games. It was a dark void where the girls had to shout out commands based on the old text adventure games. This led to jokes about bad parsing, shouting "_Why_ can't I get ye flask!", and crying.
-   Several of the _MS Paint Adventures_ comics (primarily _Problem Sleuth_, _Homestuck_ and _Jailbreak_) have a Running Gag where attempts to interact with pumpkins would always cause the narration to deny that there are any pumpkins present, usually with the phrase "What pumpkin?"

-   uni.xkcd.com (viewable here), a UNIX interface based on _xkcd_, is all about this sort of thing:
    
    $ where am i
    
    Unrecognized command. Type "help" for assistance.
    
    $ help
    
    That would be cheating!
    
-   During a 'dream-sequence' in _S.S.D.D._, Tess finds herself beset by a text-parser and - with her habitual lack of patience for AI's - quickly pissed off by it. This eventually results in a strip which is actually a fully-functional text-adventure, complete with low-def images in brilliant TANDY colors. Playable here.

    Web Original 

-   The _Cracked_ page ""Revisiting Old School Text Adventures as a Jaded Modern Gamer" describes the AI reacting with shocked horror to the insane player's sadistic commands and eventually feeding him to a swarm of monsters out of spite.
-   _SCP Foundation_: SCP-603-44 is an Interactive Fiction game in which almost all commands players have tried to input have resulted in messages saying that there is no such object here or that "you cannot \[do X\]." "Die" is the only command known to have an effect, and it affects the actual player.
-   Parodied in _Zero Punctuation_'s review of _Super Mario Galaxy 2_:
    
    **You are a greasy Italian spaz standing on a platform unsupported in the middle of the yawning void of space.**
    
    **What Now?**
    
    **\> DIE OF ASPHYXIATION**
    
    -   Also, in the website's review of _Thief (2014)_, Yahtzee feels that the convoluted gameplay of choosing which door or window to open or enter feels like "playing a bad text adventure", which he imagines the game to be like as follows:
        
        You see a door.  
        \> enter door  
        You can't enter the door.  
        \> search room  
        You find one door you can actually enter and several guards spinning in place 'cause their AI bollocked up.
        
-   In the _Mario Party TV_ series, after several incidents where correctly guessing a certain fruit during Mic Mini-games was treated as a mistake, the guys realized that they were saying _grape_, not _grapes_.
-   Parodied in the "Death of Adventure Games" article of Old Man Murray.
    
    **You are on a pirate ship!**
    
    \> Go north!
    
    **You can't go north!**
    
    \> Examine ship!
    
    **I don't see a ship here!**
    
-   The article Creation Under Capitalism and the Twine Revolution by Charity Porpentine Heartscape identifies this trope as a major limitation of text parser-based interactive fiction: "5 minutes of fighting the parser to hug someone is not ideal. It’s like your movie has 5 minutes of someone drooling during a romantic interlude."
-   There's an example of this in _Ruby Quest_, as a result of a player misspelling a word and Weaver not understanding the resulting command. The player said 'pick up monocol', which was presumably a misspelling of 'monocle'. Weaver replied that there was no 'monocol' in the room. The item the player was probably referring to was the eye dial, which pretty much just looked like a small circle in the simplistic art style.

    Real Life 

-   Many text parsers are modelled off UNIX command lines. UNIX in general is precise, arbitrary, and _case-sensitive_. "/Home" would be interpreted as a different directory than "/home". It doubles as a Damn You, Muscle Memory! if you're used to another command-line interface like DOS (used in Windows Command Prompt) — all command lines have a tendency to do this (which is why they're not used so much today). Fortunately, the command _man \[command\]_ will print an extensive manual page for whatever command "\[command\]" is; unfortunately, you basically have to be fluent in Linux jargon anyway to decipher half of it. Among the parser issues:
    -   A simple arithmetic operation like "2+2" will, in many shells, result in "Command Not Found". You have to type _echo $((2+2))_. And shell scripts are considered one of the easier programming languages.
    -   UNIX doesn't quite know how to cope with spaces in filenames, so you can't save a file as "Some File.jpg". To fix the problem, you have to enter _mv "Some File.jpg" Some\_File.jpg_, essentially forcing UNIX to read the filename as a single string.
        -   And before any Windows users start looking smug, the Windows Command Prompt behaves the same way. If you want to cd into something under "C:\\Program Files", you'll have to put it in quotes.
    -   The command to print the contents of a file to your terminal is not _read file1_, _print file1_, or even _echo file1_, but **_cat_** _file1_. "cat" stands for "**cat**enate", a somewhat esoteric term referring to the program's ability for sequential linkage and printing to stdout of multiple files — even though it's used much more often to print the contents of just a single file. Its touted sequential linkage functionality is useful for shell scripts, however.
    -   If you try to close a Python session by typing _exit_, it will not work. However, the parser will understand what you wanted to do and helpfully inform you that you should type _exit()_ instead. Gee, thanks.
        -   The parser actually still sees _exit_ as a regular variable name, which just happens to be a function with a particularly unusual string representation.
-   The Xbox One's voice recognition can feel like this sometimes, due to the unintuitive nature of some of the commands and the fact that a list of commands is not included with the console (though one can be found on the official Xbox support forums). For instance, if you want to start playing a game, you can't say, "Xbox, play \[game\]", or "Xbox, start \[game\]", or "Xbox, launch \[game\]"; you have to say "Xbox, _go to_ \[game\]." And while you can say "Xbox on" to power the Xbox up, saying "Xbox off" doesn't turn it off; you have to say "Xbox, _turn_ off."
-   Remotes for "smart" televisions and other modern devices often have a feature which allows the user to speak a command to the device rather than press a button, but don't give much if any hint as to which commands can be issued or what syntax is required, resulting in exactly this problem.

___