# My Love of JSON and What ~its Getting~ it Can Get Me

<!-- {
  "tags": ["json", "tags", "data", "separation of concerns"]
} -->


### Background

so, there's no real reason you'd pick up on this, but a large number of my projects have a significant portion of their data stored in json, and almost all of those related to my site have `tags` values:

| project | json files |
|:--------|:---------|
|[resume](/atla5/resume) | about, additional, education, experience, projects |
|[blog](/atla5/blog) | hidden in (almost) every `.md` entry (e.g. [semantic-file-system](https://raw.githubusercontent.com/atla5/blog/master/Entries/2016-08-26_semantic-file-system.md)) |
|[FeedReader](/atla5/FeedReader/)|listing of feeds in [feeds.json](/atla5/FeedReader/blob/master/feeds.json)|
|[lib-re/crosswalk](/lib-re/crosswalk/)| language encodings (e.g. [dc.json](https://github.com/lib-re/crosswalk/blob/master/res/dc.json)) |

the thing is, i didn't entirely do this with the plan of having all of them displayed on my site (someday, lol). i just really love reusable data that is _just data_. i also didn't know much of anything about react, or how great it is at dealing with remote data.

### Plans

in the future, a part of my site i've been planning for a while, will collect all of the tags in particular and display them all on one page within their given header (ideally even with their given components [v3.0]):

>## Tagged 'Library Science':
> ### Blog Posts  (from /atla5/blog/entries/)
> - [Linked Data and Enveloping Referencing](https://github.com/atla5/blog/blob/master/Entries/2016-06-12_LinkedData-EnvelopingReferencing.md)
> - [Leveraging High Static Complexity](https://github.com/atla5/blog/blob/master/Entries/2016-06-13_DCJson.md)
> ### Projects (from /resume/projects.json)
> - lib-re/dublin-core-text-parser
> - lib-re/lib-name-parser
> - lib-re/organon
> ### Work Experience (from resume/experience.json)
> - ITHAKA - JSTOR
> - Wallace Library
> ### Courses (from /resume/education.json)
> - MUSE-340: Introduction to Archives
> - MUSE-359: Cultural Informatics
> - ...
> ### Feeds (from /feedreader/feeds.json)
> - Lost in the Stacks
> - Cataloguing Matters
> - Thingology
> - ...


### How

The difficulty will come with writing some sort of aggregator in each repository to surface these tags in the cleanest way possible. Since I don't want a single repository responsible for interpreting the schemas all the others (way too complex), i'll likely have to house that in each repository.

Even with this, though, I'll end up having to watch out for any changes and potentially make edits to 4-5 repositories to get it working. I'll have to think on this more.

### Why

- be able to click on a single listed 'tag' and find my interests, experience, resources, and musings on a given subject
- helpful for me to find some of this content anywhere without having to search through 4-5 places
- be able to point someone (future employer) to a url containing my collected background on a given thing.
- it demonstrates the full power of keeping your data separate and clean.
- makes use of all the miscellaneous extra content on `resume` that i had no direct use for in exporting to pdf.
- intense exercise in data curation across distributed sources.
- i mean, come on, how cool with this be to see working across my entire corpus?
