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
morphology (fracture type, group, and, if applicable, subgroup).

Translations of the AO data will be supplied through different versions of the
YAML data. The language will be indicated by
[ISO 639-1](http://www.loc.gov/standards/iso639-2/php/English_list.php)
components in the YAML filenames. For example, the English translation is in
`ao_codes.EN.yaml`, and the Norwegian Bokmål translation is (or soon will be) in
'ao_codes.NB.yaml'.

The data content of these files will all be identical, independent of
language.

## Images

The second element of the toolbox is a collection of images for selecting
fractures based on AO classification.

### skeleton.svg

This is an SVG image of a skeleton with embedded structure to make it possible
to click on AO bone sections. In the image there is a layer called "click". This
layer is a the top of the Z-order, and it contains shapes which overlay the
various AO bone sections. For example, there is a shape that directly overlays
the proximal femur.

These overlay shapes are named in such a way that the names identify the AO
prefix and, if appropriate, side of the body of the bone section that they
overlay. The naming pattern is "ao-clickable-<prefix>[-<side>]". So, continuing
the example above, the shape overlaying the proximal femur on the left side of
the body (the *right* side of the image as displayed on-screen) is named
"ao-clickable-31-left". The "31" indicates the AO classification prefix for
proximal femur, i.e. 31. The "left" indicates the side of the body.

The intended use of this image is to allow users to click on the skeleton, for
example on a webpage. These clicks can be detected and, since the click can be
made to refer to the SVG elements from which they originate, programs can
determine which bone segment/side was clicked based on the name of the element.

*(This image is based on a public domain image originally created by [Mariana Ruiz Villarreal/LadyofHats](https://commons.wikimedia.org/wiki/User:LadyofHats) and [distributed through wikimedia](https://commons.wikimedia.org/wiki/File:Human_skeleton_front_-_no_labels.svg).)*
