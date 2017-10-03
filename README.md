
#### Description ####

##### Short #####
Series of markdown entries regarding my work, which I hope to include on my 
 personal site later.

##### Long #####
An updating list of blog-style entries regarding my ideas, thoughts, and developments
 on relevant personal, academic, and work-related pursuits and on important topics in 
 the field/s I'm going into. This will allow me to track, monitor, archive, and share 
 my relevant thoughts and activities in a simple, quick, and familiar way with very 
 little overhead.
 
_note: this is not a blog about my social life. I intend to use it primarily as a sort
 of work log_

#### Background ####
I've toyed with the idea for a while of including some sort of blog element to my 
  personal/professional site containing information relevant to my studies and 
  professional pursuits.
  
I wanted something that would:
- be accessible anywhere
- update easily 
- integrate with my existing release plan and process
- provide easy formatting without CSS (leveraging markdown)
- be decoupled from its representation on the site
- be readable and coherent before it's totally hosted
- require very little overhead or learning, but be extendable

#### Rationale ####
I chose a github repository because:
- I can log in and write easily from anywhere - even on my mobile device.
- it's easy to automate the updates (travis CI, jenkins, etc.)
- that's where I do most of the work I'm going to describe anway
- github markdown is familiar, preview-able, and well-supported
- can restrict this repo to only the text (model)/formatting (view) and not the control
- browsing through github defaults to rendered view, easy to use tools locally (e.g atom) as well.
- usable out of the box, but open to more complicated features with Issues and TravisCI

#### Plan ####
- [ ] determine a json schema to improve the existing `tags:[]` only one going right now (embedded and from the naming/metadata)
- [ ] go through and ensure that all of them have the embedded tags
- [ ] create an aggregator script to generate a `blogs.json` for `atla5.github.io` consumption ;]
