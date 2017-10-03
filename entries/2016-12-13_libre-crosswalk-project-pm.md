# lib-re/crosswalk - Project "Post Mortem" 

<!-- {
  "json": ["lib-re", "crosswalk", "post-mortem", "metadata", "interoperability"]
} -->


Although I originally intended to have a runnable and workable translation program running by the end of the semester, I 
  wasn’t entirely certain even at the outset that it was possible to. As I realized through the course of working on the 
  project the enormity of what I was really taking on, I focused instead on clarifying the information architecture, purpose, 
  background, and design of the system.

What’s come out of that remains something I am very proud of and something that is a marked improvement over some existing 
  and proposed solutions to the problem that I’ve seen. I think by conducting the literature review at the beginning I was able 
  to circumnavigate some of the pitfalls experienced by other researchers and developers, particularly in avoiding the creation 
  of any “peta-standard” which I would then jam other existing metadata standards into. Overall, I think the work represents a 
  critical foundation from which to implement the actual thing in the coming months/years.

My care in abstracting each step of the information architecture, ensuring the separation of syntax and schema, standard and 
  accessible,  and accessible from aggregate, as well as  my recognition of the joint description of the actual entity, 
  represent very strong aspects to the design that make it much more extensible, flexible, and useful than it otherwise could 
  have been. I think, while bold and perhaps optimistic, that the idea of creating a shared “data type” across the LAM 
  institutions is one pregnant with possibility as well as complication.

As I look further into the operative complexity of the work this information architecture entails, I realize that I’ll almost 
  certainly want to rewrite my existing code in C++ instead of Java in order to keep it running at a reasonable pace. I also 
  need to look more critically at the exact way to incorporate new standards as “modules” to make them easier to 
  include/exclude as well as update, as the project is purposed towards and made successful by the ease of adding on new 
  standards with time.

Whether or not this specific project ends up being the most understandable and efficient implementation of these ideas or 
  not, the project represents an important means by which I can (and have) reach(ed) a better understanding of standards 
  interoperability and metadata management.  
  
The problem I’m trying to solve is surely an important and impactful one with a high degree of potential risk associated  
  with getting things wrong, as errors and subtleties in standards that go unnoticed often lead to painstaking manual rework 
  on behalf of archivists and librarians around the world
