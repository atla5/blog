site status: the site now has a header and a footer that can be added and functional on every 
  page with one line each.

## problems ##
- existing file structure is wonky and uses relative paths. both need to be fixed at some point. 
  - apparently the php includes are pretty dumb under the hood, so the link I had in the .inc.php
  file is broken by a relative path error. 
  - I could solve this temporarily with the bootstrap CDN links on getbootstrap.com, but this will just grow into a bigger problem as the site grows.

## comments ##
- first experience with php, via includes. pretty interesting.
- using 'xampp' to serve my site on localhost via the `htdocs/<subfolder-name-here>` folder
- pretty surprised how easy the web stuff is to do from the ground up.
- more surprised at how much of a frenzy of languages it seems to be. `php`, `js`, `css`, `html` all 
 in one file and/or spread throughout a load of directories.

## learned ##
- php is a serverside language that you can do pretty powerful stuff with
  - includes can drastically decrease code duplication with very little cost
  - sending arguments via the url 

