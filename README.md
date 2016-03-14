# ao-toolbox
A collection of tools for working with AO fracture classifications

## YAML data files

The first element of the toolbox is a set of [YAML](http://yaml.org/) files
which describe AO classifications in a hierarchical structure. The point of
these files is that they can be easily consumed by programs written in almost
any programming language and using almost any technology, thereby providing a
largely technology-agnostic yet programming-friendly representation of AO
classification data.

The data in these files currently includes localization (bone and segment) and
morphology (fracture type, group, and, if application, subgroup).

Translations of the AO data will be supplied through different versions of the
YAML data. The language will be indicated by
[ISO 639-1](http://www.loc.gov/standards/iso639-2/php/English_list.php)
components in the YAML filenames. For example, the English translation is in
`ao_codes.EN.yaml`, and the Norwegian Bokmål translation is (or soon will be) in
'ao_codes.NB.yaml'.

The data content of these files will all be identical, independent of
language.
