Idris 2 version 0.8.0 Released
##############################

:date: 2025-10-31 21:00
:tags: Release
:category: News
:author: CodingCellist

A new version (0.8.0) of Idris 2 has been released. You can download the source
(including generated Scheme and Racket files for bootstrapping) from the
`download page <{filename}../pages/download.rst>`_.

Highlights include:

* Autobind and Typebind modifier on operators allow the user to customise the
  syntax of operator to look more like a binder.
* Totality checking will now look under data constructors, so ``Just xs`` will
  be considered smaller than ``Just (x :: xs)``.
* `Typst <https://typst.app/>`_ files can be compiled as Literate Idris.
* Constructors with certain tags (``CONS``, ``NIL``, ``JUST``, ``NOTHING``) are
  replaced with ``_builtin.<TAG>`` (eg ``_builtin.CONS``).  This allows the
  identity optimisation to optimise conversions between list-shaped things.
* Refactored ``Uninhabited`` implementation for ``Data.List.Elem``,
  ``Data.List1.Elem``, ``Data.SnocList.Elem``, and ``Data.Vect.Elem`` so it can
  be used for homogeneous (``===``) and heterogeneous (``~=~``) equality.
* The ``RefC`` backend compiler can emit precise reference counting instructions
  where a reference is dropped as soon as possible. This allows you to reuse
  unique variables and optimize memory consumption.
* Fix memory leaks of ``IORef`` in ``RefC`` backend.  Now that ``IORef`` holds
  values by itself, ``global_IORef_Storage`` is no longer needed.
* The NodeJS executable output to ``build/exec/`` now has its executable bit
  set.  That file already had a NodeJS shebang at the top, so now it is fully
  ready to go after compilation.

For a detailed list of changes, see the
`CHANGELOG <https://github.com/idris-lang/Idris2/blob/15a3e4e70843f7a34100f6470c04b791330788df/CHANGELOG.md>`_.

Thanks to the many people who have contributed, both old and new, whether by
adding features, fixing code, reporting issues, or anything else. You can find a
list of
`contributors <https://github.com/idris-lang/Idris2/blob/15a3e4e70843f7a34100f6470c04b791330788df/CONTRIBUTORS>`_
in the `GitHub repository <https://github.com/idris-lang/Idris2>`_.

Happy Hallowe'en! Have fun!
