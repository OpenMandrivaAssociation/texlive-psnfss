# revision 33946
# category Package
# catalog-ctan /macros/latex/required/psnfss
# catalog-date 2012-07-23 15:04:13 +0200
# catalog-license lppl
# catalog-version 9.2a
Name:		texlive-psnfss
Version:	9.2a
Release:	9
Summary:	Font support for common PostScript fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/required/psnfss
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/psnfss.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/psnfss.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/psnfss.source.tar.xz
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
%{_texmfdistdir}/fonts/map/dvips/psnfss/charter.map
%{_texmfdistdir}/fonts/map/dvips/psnfss/fpls.map
%{_texmfdistdir}/fonts/map/dvips/psnfss/pazo.map
%{_texmfdistdir}/fonts/map/dvips/psnfss/psnfss.map
%{_texmfdistdir}/fonts/map/dvips/psnfss/utopia.map
%{_texmfdistdir}/tex/latex/psnfss/8rbch.fd
%{_texmfdistdir}/tex/latex/psnfss/8rpag.fd
%{_texmfdistdir}/tex/latex/psnfss/8rpbk.fd
%{_texmfdistdir}/tex/latex/psnfss/8rpcr.fd
%{_texmfdistdir}/tex/latex/psnfss/8rphv.fd
%{_texmfdistdir}/tex/latex/psnfss/8rpnc.fd
%{_texmfdistdir}/tex/latex/psnfss/8rppl.fd
%{_texmfdistdir}/tex/latex/psnfss/8rptm.fd
%{_texmfdistdir}/tex/latex/psnfss/8rput.fd
%{_texmfdistdir}/tex/latex/psnfss/8rpzc.fd
%{_texmfdistdir}/tex/latex/psnfss/avant.sty
%{_texmfdistdir}/tex/latex/psnfss/bookman.sty
%{_texmfdistdir}/tex/latex/psnfss/chancery.sty
%{_texmfdistdir}/tex/latex/psnfss/charter.sty
%{_texmfdistdir}/tex/latex/psnfss/courier.sty
%{_texmfdistdir}/tex/latex/psnfss/helvet.sty
%{_texmfdistdir}/tex/latex/psnfss/mathpazo.sty
%{_texmfdistdir}/tex/latex/psnfss/mathpple.sty
%{_texmfdistdir}/tex/latex/psnfss/mathptm.sty
%{_texmfdistdir}/tex/latex/psnfss/mathptmx.sty
%{_texmfdistdir}/tex/latex/psnfss/newcent.sty
%{_texmfdistdir}/tex/latex/psnfss/omlbch.fd
%{_texmfdistdir}/tex/latex/psnfss/omlpag.fd
%{_texmfdistdir}/tex/latex/psnfss/omlpbk.fd
%{_texmfdistdir}/tex/latex/psnfss/omlpcr.fd
%{_texmfdistdir}/tex/latex/psnfss/omlphv.fd
%{_texmfdistdir}/tex/latex/psnfss/omlpnc.fd
%{_texmfdistdir}/tex/latex/psnfss/omlppl.fd
%{_texmfdistdir}/tex/latex/psnfss/omlptm.fd
%{_texmfdistdir}/tex/latex/psnfss/omlptmcm.fd
%{_texmfdistdir}/tex/latex/psnfss/omlput.fd
%{_texmfdistdir}/tex/latex/psnfss/omlpzc.fd
%{_texmfdistdir}/tex/latex/psnfss/omlzplm.fd
%{_texmfdistdir}/tex/latex/psnfss/omlzpple.fd
%{_texmfdistdir}/tex/latex/psnfss/omlztmcm.fd
%{_texmfdistdir}/tex/latex/psnfss/omsbch.fd
%{_texmfdistdir}/tex/latex/psnfss/omspag.fd
%{_texmfdistdir}/tex/latex/psnfss/omspbk.fd
%{_texmfdistdir}/tex/latex/psnfss/omspcr.fd
%{_texmfdistdir}/tex/latex/psnfss/omsphv.fd
%{_texmfdistdir}/tex/latex/psnfss/omspnc.fd
%{_texmfdistdir}/tex/latex/psnfss/omsppl.fd
%{_texmfdistdir}/tex/latex/psnfss/omsptm.fd
%{_texmfdistdir}/tex/latex/psnfss/omsput.fd
%{_texmfdistdir}/tex/latex/psnfss/omspzc.fd
%{_texmfdistdir}/tex/latex/psnfss/omspzccm.fd
%{_texmfdistdir}/tex/latex/psnfss/omszplm.fd
%{_texmfdistdir}/tex/latex/psnfss/omszpple.fd
%{_texmfdistdir}/tex/latex/psnfss/omsztmcm.fd
%{_texmfdistdir}/tex/latex/psnfss/omxpsycm.fd
%{_texmfdistdir}/tex/latex/psnfss/omxzplm.fd
%{_texmfdistdir}/tex/latex/psnfss/omxzpple.fd
%{_texmfdistdir}/tex/latex/psnfss/omxztmcm.fd
%{_texmfdistdir}/tex/latex/psnfss/ot1bch.fd
%{_texmfdistdir}/tex/latex/psnfss/ot1pag.fd
%{_texmfdistdir}/tex/latex/psnfss/ot1pbk.fd
%{_texmfdistdir}/tex/latex/psnfss/ot1pcr.fd
%{_texmfdistdir}/tex/latex/psnfss/ot1phv.fd
%{_texmfdistdir}/tex/latex/psnfss/ot1pnc.fd
%{_texmfdistdir}/tex/latex/psnfss/ot1ppl.fd
%{_texmfdistdir}/tex/latex/psnfss/ot1pplj.fd
%{_texmfdistdir}/tex/latex/psnfss/ot1pplx.fd
%{_texmfdistdir}/tex/latex/psnfss/ot1ptm.fd
%{_texmfdistdir}/tex/latex/psnfss/ot1ptmcm.fd
%{_texmfdistdir}/tex/latex/psnfss/ot1put.fd
%{_texmfdistdir}/tex/latex/psnfss/ot1pzc.fd
%{_texmfdistdir}/tex/latex/psnfss/ot1zplm.fd
%{_texmfdistdir}/tex/latex/psnfss/ot1zpple.fd
%{_texmfdistdir}/tex/latex/psnfss/ot1ztmcm.fd
%{_texmfdistdir}/tex/latex/psnfss/palatino.sty
%{_texmfdistdir}/tex/latex/psnfss/pifont.sty
%{_texmfdistdir}/tex/latex/psnfss/t1bch.fd
%{_texmfdistdir}/tex/latex/psnfss/t1pag.fd
%{_texmfdistdir}/tex/latex/psnfss/t1pbk.fd
%{_texmfdistdir}/tex/latex/psnfss/t1pcr.fd
%{_texmfdistdir}/tex/latex/psnfss/t1phv.fd
%{_texmfdistdir}/tex/latex/psnfss/t1pnc.fd
%{_texmfdistdir}/tex/latex/psnfss/t1ppl.fd
%{_texmfdistdir}/tex/latex/psnfss/t1pplj.fd
%{_texmfdistdir}/tex/latex/psnfss/t1pplx.fd
%{_texmfdistdir}/tex/latex/psnfss/t1ptm.fd
%{_texmfdistdir}/tex/latex/psnfss/t1put.fd
%{_texmfdistdir}/tex/latex/psnfss/t1pzc.fd
%{_texmfdistdir}/tex/latex/psnfss/times.sty
%{_texmfdistdir}/tex/latex/psnfss/ts1bch.fd
%{_texmfdistdir}/tex/latex/psnfss/ts1pag.fd
%{_texmfdistdir}/tex/latex/psnfss/ts1pbk.fd
%{_texmfdistdir}/tex/latex/psnfss/ts1pcr.fd
%{_texmfdistdir}/tex/latex/psnfss/ts1phv.fd
%{_texmfdistdir}/tex/latex/psnfss/ts1pnc.fd
%{_texmfdistdir}/tex/latex/psnfss/ts1ppl.fd
%{_texmfdistdir}/tex/latex/psnfss/ts1pplj.fd
%{_texmfdistdir}/tex/latex/psnfss/ts1pplx.fd
%{_texmfdistdir}/tex/latex/psnfss/ts1ptm.fd
%{_texmfdistdir}/tex/latex/psnfss/ts1put.fd
%{_texmfdistdir}/tex/latex/psnfss/ts1pzc.fd
%{_texmfdistdir}/tex/latex/psnfss/ufplm.fd
%{_texmfdistdir}/tex/latex/psnfss/ufplmbb.fd
%{_texmfdistdir}/tex/latex/psnfss/upsy.fd
%{_texmfdistdir}/tex/latex/psnfss/upzd.fd
%{_texmfdistdir}/tex/latex/psnfss/utopia.sty
%_texmf_updmap_d/psnfss
%doc %{_texmfdistdir}/doc/latex/psnfss/00readme.txt
%doc %{_texmfdistdir}/doc/latex/psnfss/changes.txt
%doc %{_texmfdistdir}/doc/latex/psnfss/manifest.txt
%doc %{_texmfdistdir}/doc/latex/psnfss/psfonts.pdf
%doc %{_texmfdistdir}/doc/latex/psnfss/psnfss2e.pdf
%doc %{_texmfdistdir}/doc/latex/psnfss/test/mathtest.tex
%doc %{_texmfdistdir}/doc/latex/psnfss/test/pitest.tex
%doc %{_texmfdistdir}/doc/latex/psnfss/test/test0.tex
%doc %{_texmfdistdir}/doc/latex/psnfss/test/test1.tex
%doc %{_texmfdistdir}/doc/latex/psnfss/test/test2.tex
%doc %{_texmfdistdir}/doc/latex/psnfss/test/test3.tex
#- source
%doc %{_texmfdistdir}/source/latex/psnfss/psfonts.dtx
%doc %{_texmfdistdir}/source/latex/psnfss/psfonts.ins
%doc %{_texmfdistdir}/source/latex/psnfss/psnfss2e.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

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
