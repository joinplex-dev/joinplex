# Draft Example Usage of the Interface

Let's suppose we had two datasets as follows:

### `main_df`
|Name           |Group ID|Favourite Food  |
|---------------|--------|----------------|
| |2       |Egg             |
|John Cleese    |        |Spam            |
|Eric Idle      |3       |Spam            |
|Michael Palin  |        |Egg Bacon + Spam|
|    |        |Egg             |
|Terry Gilliam  |2       |Spam            |
|Carol Cleveland|        |Egg             |
|Neil Innes     |1       |Spam            |

### `cheese_df`
|Name           |Group ID|Favourite Food  |Cheese Choice      |
|---------------|--------|----------------|-------------------|
|Graham Chapman |        |Egg             |Red Leicester      |
|John Marwood Cleese|3       |Spam            |Tilsit             |
|Eric Idle      |3       |Spam            |Bel Paese          |
|Michael Palin  |        |Egg Bacon + Spam|Red Windsor        |
|Terry Jones    |2       |Egg             |Stitlton           |
|Winnie the Pooh|1       |Honey           |Gruyère            |
|Terrence Gilliam|2       |Spam            |Emmental           |
|Carol Cleveland|1       |Egg             |Norwegian Jarlsberg|
|Neil Innes     |1       |Egg             |Liptauer           |

We might want to join these two datasets together, but we have a problem: the names
don't match exactly. In this case, we could write some logic to automatically clean
the names and then join the datasets together. However, for a more complicated example,
this might not be possible so let's pretend we can't do that. In addition, some of the names are missing entirely.
