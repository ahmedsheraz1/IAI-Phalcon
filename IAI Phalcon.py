Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import pprint
stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
stuff.insert(0, stuff)
pprint.pprint(stuff)
[<Recursion on list with id=4329427712>,
 'spam',
 'eggs',
 'lumberjack',
 'knights',
 'ni']
