# LinkedData and enveloping referencing #

<!--
{
  "tags": ["LIS","cataloguing","metadata","linked data","marc"]
}
-->

## intro ##

One of the great benefits linked data can afford us is in the area of referring
  relevant records (whether by edition [scholarly/technical/textbook], allusion
  [literary], reference [scientific journal], covers [music], parody [comedy],
  etc), or authority control.

No longer bound to the rigid and static marc format, easily prone to becoming
  overly bulky and difficult to read quickly - whether it's transferred and
  homogenized by an external authority (e.g. OCLC worldcat) or not - linked
  data, together with .json, can allow separately maintained elements to be
  shared independently.

Such a granular approach would enrich the capacity for more in-depth and
  programmatically useful record parts, and make individual records much more
  easy to read and generate, as well as much more resistant to change and the
  necessity to edit.

## ids ##
the

## enveloping hierarchy ##
Such a method would allow for - and encourage - the use of recursive, or
  _enveloping_ records and elements, which build upon one another and
  inter-operate.

These more granular pieces of information would allow for a much more reusable
  piece of shareable information that would not over-complicate an individual
  record. The use of a standardized reference for one of the

...

## example: covers ##

One of my favorite covers is 'Surf Wax America' by 'You Blew It!' covering
  'Weezer'.

In such an enveloping system, the record for the 'You Blew It!' version would
  have a section of related works with a link to the record for Wheezer's
  version


## example: linking authors to articles ##

these could be used retroactively by some bot to routinely search for suggested
  integrations cataloguers themselves may not be able to foresee, by hopping
  from paper to paper and relating it to authorship.

A student writer for their school paper, for instance, writing in the late
  1960s as a college student could later becomes a famous journalist. Such a
  method

## diamond problem ##
The perennial '[diamond problem](https://en.wikipedia.org/wiki/Multiple_inheritance#The_diamond_problem)'
  would arise and likely have to be solved or standardized away. Perhaps more
  on this later...

## notes ##
- This would be easily correlated to the dublin-core qualifier of 'relation',
  and piggyback off of that established precedent. (I don't know enough about
  MARC21 to know the effective corollary)
- This might basically be exactly how linked data already works, I don't know
  enough about it to say yet. If it is, awesome! Go linked data.
