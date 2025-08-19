Download
========

Idris 2
-------

To get the cutting edge version of Idris 2, use the package manager ``pack`` –
please see `pack's install & usage instructions <https://github.com/stefan-hoeck/idris2-pack>`_.

``pack`` will also handle your dependencies using the
`pack collection <https://github.com/stefan-hoeck/idris2-pack-db/blob/main/collections/HEAD.toml>`_.
You will have to use ``pack build`` instead of ``idris2 --build`` to compile a
package.

If you already use ``pack``, you can update your Idris version to the latest git
commit (``HEAD``) by using ``pack switch latest``.

Alternatively, the latest formally released version is Idris2-0.7.0,
`released 2023-12-22 <{filename}../posts/idris2-0-7-0-released.rst>`_,
with its associated source tarball:

* `idris2-0.7.0.tgz <{static}../releases/idris2-0.7.0.tgz>`_
  `(SHA 256 hash) <{static}../releases/idris2-0.7.0.tgz.sha256>`__

Both ``pack`` and the release tarball include generated Scheme sources
sufficient for bootstrapping, so you don't need an existing Idris 2 system to
build. You need:

* Either `Chez Scheme <https://cisco.github.io/ChezScheme/>`_ or `Racket
  <https://racket-lang.org>`_ to build the generated Scheme source
* ``bash``, with ``realpath``. On Linux, you probably already have this. On
  a Mac, you can install this with ``brew install coreutils``.
* A C compiler, to build the library support code.

You can always find the latest development version `on github
<http://github.com/idris-lang/Idris2>`_:

* ``git clone`` `https://github.com/idris-lang/Idris2.git <https://github.com/idris-lang/Idris2>`_

Previous releases are also available:

* `idris2-0.6.0.tgz <{static}../releases/idris2-0.6.0.tgz>`_ `(SHA 256 hash) <{static}../releases/idris2-0.6.0.tgz.sha256>`__
* `idris2-0.5.1.tgz <{static}../releases/idris2-0.5.1.tgz>`_ `(SHA 256 hash) <{static}../releases/idris2-0.5.1.tgz.sha256>`__
* `idris2-0.4.0.tgz <{static}../releases/idris2-0.4.0.tgz>`_ `(SHA 256 hash) <{static}../releases/idris2-0.4.0.tgz.sha256>`__

Idris 1 (legacy)
----------------

Idris 1 is no longer maintained but remains available. If you are still using Idris 1, consider switching to Idris 2.

* A list of differences is available
  `in the documentation <https://idris2.readthedocs.io/en/latest/updates/updates.html>`_.

You can find the source from the following places:

* `Hackage <http://hackage.haskell.org/package/idris>`_ has the most recently
  released version. Assuming you have an up to date Haskell distribution,
  at the shell prompt, type

  + ``cabal update``
  + ``cabal install idris``
* The latest development version is available from github:

  + ``git clone`` `git://github.com/idris-lang/Idris-dev.git <https://github.com/idris-lang/Idris-dev>`_

More detailed installation instructions that are maintained by the Idris
community are available on the wiki for the following platforms:

* `MacOS <https://github.com/idris-lang/Idris-dev/wiki/Idris-on-OS-X-using-Homebrew>`_
* `Windows <https://github.com/idris-lang/Idris-dev/wiki/Idris-on-Windows>`_
* `Ubuntu <https://github.com/idris-lang/Idris-dev/wiki/Idris-on-Ubuntu>`_
* `Debian <https://github.com/idris-lang/Idris-dev/wiki/Idris-on-Debian>`_

Binary
------

There are binary packages available for various platforms:

* For Windows: `Windows Binaries <https://github.com/idris-lang/Idris-dev/wiki/Windows-Binaries>`_
* For OS X: `idris-current.pkg <http://www.idris-lang.org/pkgs/idris-current.pkg>`_ `(SHA 256 hash) <http://www.idris-lang.org/pkgs/idris-current.pkg.sha256>`__

If you require any optional features (e.g. GMP or compile time FFI support),
you will need to build from source.

Editor Support
--------------

There are editor modes which support interactive editing:

* Idris 2

  * `Vim mode (for Idris 2) <https://github.com/edwinb/idris2-vim>`_
  * `Emacs mode (for Idris 1 and 2) <https://github.com/idris-hackers/idris-mode>`_
  * `Emacs mode (for Idris 2 only) <https://github.com/idris-community/idris2-mode>`_
  * `Language Server Protocol <https://github.com/idris-community/idris2-lsp>`_

* Idris 1

  * `Vim mode (for Idris 1) <https://github.com/idris-hackers/idris-vim>`_
  * `Emacs mode (for Idris 1 and 2) <https://github.com/idris-hackers/idris-mode>`_
  * `(DEPRECATED) <https://github.blog/news-insights/product-news/sunsetting-atom/>`_ `Atom package <https://atom.io/packages/language-idris>`__
