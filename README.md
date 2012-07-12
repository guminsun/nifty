NJOY Input Format Translator
============================

License
-------
  Copyright (C) 2011, 2012 C. Emil Hessman
  
  Permission to use, copy, modify, and/or distribute this software for any
  purpose with or without fee is hereby granted, provided that the above
  copyright notice and this permission notice appear in all copies.

  THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
  WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
  MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
  ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
  WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
  ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
  OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.


Abstract
--------
The NJOY Nuclear Data Processing System is a software system used for nuclear data management [1]. In particular, it is used to convert evaluated nuclear data for materials stored in Evaluated Nuclear Data Files (ENDF) [2] into different formats, as well as performing operations on the data.

NJOY is widely used within nuclear data research, and as such, it is important that the system has a user friendly interface. The NJOY input instructions [4] is a non-interactive user interface used for specifying jobs to be run by NJOY. The input instructions are complex and hard to read compared to e.g. a high-level programming language. Working with a large and complex job easily becomes a daunting and error-prone task. Accordingly, there is a need for an improved input format.

In this thesis, a new input format has been designed. In order to make the new input format useable with NJOY, a translator which is able to translate the new input format into the original NJOY input instructions has also been implemented. The results have been verified by a small set of tests.

See http://urn.kb.se/resolve?urn=urn:nbn:se:uu:diva-156431 for the full report.

