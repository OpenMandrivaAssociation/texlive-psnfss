Name:		texlive-psnfss
Version:	54694
Release:	2
Summary:	Font support for common PostScript fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/required/psnfss
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/psnfss.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/psnfss.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/psnfss.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-tetex
Requires:	texlive-graphics

%description
Font definition files, macros and font metrics for freely-
available Adobe Type 1 fonts. The font set consists of the
'LaserWriter 35' set (originally 'freely available' because
embedded in PostScript printers), and a variety of other free
fonts, together with some additions. Note that while many of
the fonts are available in PostScript (and other) printers,
most publishers require fonts embedded in documents, which
requires that you have the fonts in your TeX system.
Fortunately, there are free versions of the fonts from URW
(available in the URW base5 bundle). The base set of text fonts
covered by PSNFSS are: AvantGarde, Bookman, Courier, Helvetica,
New Century Schoolbook, Palatino, Symbol, Times Roman and Zapf
Dingbats. In addition, the fonts Bitstream Charter and Adobe
Utopia are covered (those fonts were contributed to the Public
Domain by their commercial foundries). Separate packages are
provided to load each font for use as main text font. The
packages helvet (which allows Helvetica to be loaded with its
size scaled to something more nearly appropriate for its use as
a Sans-Serif font to match Times) and pifont (which provides
the means to select single glyphs from symbol fonts) are
tailored to special requirements of their fonts. Mathematics
are covered by the mathptmx package, which constructs passable
mathematics from a combination of Times Roman, Symbol and some
glyphs from Computer Modern, and by Pazo Math (optionally
extended with the fpl small-caps and old-style figures fonts)
which uses Palatino as base font, with the mathpazo fonts. The
bundle as a whole is part of the LaTeX 'required' set of
packages.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/map/dvips/psnfss
%{_texmfdistdir}/tex/latex/psnfss
%_texmf_updmap_d/psnfss
%doc %{_texmfdistdir}/doc/latex/psnfss
#- source
%doc %{_texmfdistdir}/source/latex/psnfss

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/psnfss <<EOF
Map charter.map
Map fpls.map
Map pazo.map
Map utopia.map
EOF
