# OpenType Features Workshops

<img src="./_images/header.png">

## Introduction

OpenType features empower fonts to behave more responsively for users. They enable on-the-fly glyph substitution and positioning, providing a typesetting experience that is both seamless and highly customizable.

To enhance your fonts with the added power of OpenType features, all you need to do is:

1. Add extra glyphs for any desired substitutions.
2. Write a bit of code (in a syntax specified by Adobe) to define the conditions under which these swaps or positional changes occur.

## Basic Example of OpenType Feature Code

```afdko
# Establish the geographic and script locale
languagesystem DFLT dflt;
languagesystem latn dflt;

# Optional: Set up some nice organized swappable sets of glyph names, stored in “variables”
@ss01_off = [A      B      C     ];
@ss01_on  = [A.ss01 B.ss01 C.ss01];

# Write a feature, in this case, Stylistic Set 1
feature ss01 {
    sub @ss01_off by @ss01_on;
} ss01;
```

## Resources

* [OpenType Cookbook](https://opentypecookbook.com/), by Tal Leming
* [Introduction to OpenType Programming](https://simoncozens.github.io/fonts-and-layout/features.html), by Simon Cozens
* [OpenType Feature File Specification](https://adobe-type-tools.github.io/afdko/OpenTypeFeatureFileSpecification.html), by Adobe
* [OpenType Layout Specification](https://learn.microsoft.com/en-us/typography/opentype/spec/features_ae), by Microsoft
* [List of All OpenType Feature Tags](https://learn.microsoft.com/en-us/typography/opentype/spec/featurelist), by Microsoft

## Common OpenType Features
** in Latin-based type-setting

| Feature tag     | Friendly name                       | Description            
| --------------- | ----------------------------------- | ---------------------- 
| `calt`          | Contextual Alternates               | Glyph swaps depending on which glyphs are around them.
| `case`          | Case-sensitive Forms                | Glyph swaps depending on whether they’re in an all-caps context.
| `cpsp`          | Capital Spacing                     | Glyph spacing changes depending on whether they’re in an all-caps context.
| `c2sc`          | Small Capitals From Capitals        | Glyph swaps from uppercase to small capitals.
| `smcp`          | Small Capitals                      | Glyph swaps from lowercase to small capitals.
| `dlig`          | Discretionary Ligatures             | Glyph swaps from multiple glyphs to one ligature glyph, usually ornamental / decorative.
| `frac`          | Fractions                           | Glyph swaps from multiple glyphs to one or more fraction-specific glyph(s).
| `init`          | Initial Forms                       | Glyph swaps at the beginning of a word.
| `medi`          | Medial Forms                        | Glyph swaps in the middle of a word.
| `fina`          | Terminal Forms                      | Glyph swaps at the end of a word.
| `isol`          | Isolated Forms                      | Glyph swaps in a one-letter word.
| `liga`          | Standard Ligatures                  | Glyph swaps from multiple glyphs to one ligature glyph, usually functional / necessary.
| `lnum`          | Lining Figures                      | Glyph swaps from oldstyle (lowercase) figures to lining (uppercase) figures.
| `onum`          | Oldstyle Figures                    | Glyph swaps from lining (uppercase) figures to oldstyle (lowercase) figures.
| `tnum`          | Tabular Figures                     | Glyph swaps from proportional figures to tabular (monospaced) figures.
| `pnum`          | Tabular Figures                     | Glyph swaps from tabular (monospaced) figures to proportional figures.
| `locl`          | Localized Forms                     | Glyph swaps depending on geographic context.
| `salt`          | Stylistic Alternates                | Glyph swaps for general stylistic effect.
| `ss01` – `ss20` | Stylistic Set 1 – Stylistic Set 20  | Glyph swaps for stylistic effect, usually named sets with specific themes.
| `subs`          | Subscript                           | Glyph swaps from default figures to subscript figures.
| `sups`          | Superscript                         | Glyph swaps from default figures to superscript figures.
| `swsh`          | Swash                               | Glyph swaps from default glyphs to swash glyphs.
| `zero`          | Slashed Zero                        | Glyph swaps from default zeros to slashed zeros.

For a list of all supported OpenType features, refer to [here](https://learn.microsoft.com/en-us/typography/opentype/spec/featurelist).

