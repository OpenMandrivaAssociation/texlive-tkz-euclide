# revision 22830
# category Package
# catalog-ctan /macros/latex/contrib/tkz/tkz-euclide
# catalog-date 2011-06-05 23:10:23 +0200
# catalog-license lppl
# catalog-version 1.16c
Name:		texlive-tkz-euclide
Version:	1.16c
Release:	8
Summary:	Tools for drawing euclidean geometry
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tkz/tkz-euclide
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tkz-euclide.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tkz-euclide.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The tkz-euclide package is tis a set of files, designed to give
math teachers and students) easy access at the programmation of
euclidean geometry with TikZ.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-euclide.sty
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-lib-symbols.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-obj-addpoints.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-obj-angles.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-obj-arcs.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-obj-circles.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-obj-lines.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-obj-polygons.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-obj-protractor.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-obj-sectors.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-obj-vectors.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-tools-intersections.tex
%{_texmfdistdir}/tex/latex/tkz-euclide/tkz-tools-transformations.tex
%doc %{_texmfdistdir}/doc/latex/tkz-euclide/README
%doc %{_texmfdistdir}/doc/latex/tkz-euclide/examples/Makefile
%doc %{_texmfdistdir}/doc/latex/tkz-euclide/examples/info_euclide_tex.txt
%doc %{_texmfdistdir}/doc/latex/tkz-euclide/examples/latex/euclide-tex.zip
%doc %{_texmfdistdir}/doc/latex/tkz-euclide/examples/tkzeuclpreamble.ltx
%doc %{_texmfdistdir}/doc/latex/tkz-euclide/latex/TKZdoc-euclide-FAQ.tex
%doc %{_texmfdistdir}/doc/latex/tkz-euclide/latex/TKZdoc-euclide-alea.tex
%doc %{_texmfdistdir}/doc/latex/tkz-euclide/latex/TKZdoc-euclide-arcs.tex
%doc %{_texmfdistdir}/doc/latex/tkz-euclide/latex/TKZdoc-euclide-base.tex
%doc %{_texmfdistdir}/doc/latex/tkz-euclide/latex/TKZdoc-euclide-circles.tex
%doc %{_texmfdistdir}/doc/latex/tkz-euclide/latex/TKZdoc-euclide-compass.tex
%doc %{_texmfdistdir}/doc/latex/tkz-euclide/latex/TKZdoc-euclide-config.tex
%doc %{_texmfdistdir}/doc/latex/tkz-euclide/latex/TKZdoc-euclide-example.tex
%doc %{_texmfdistdir}/doc/latex/tkz-euclide/latex/TKZdoc-euclide-exemples.tex
%doc %{_texmfdistdir}/doc/latex/tkz-euclide/latex/TKZdoc-euclide-installation.tex
%doc %{_texmfdistdir}/doc/latex/tkz-euclide/latex/TKZdoc-euclide-intersec.tex
%doc %{_texmfdistdir}/doc/latex/tkz-euclide/latex/TKZdoc-euclide-lines.tex
%doc %{_texmfdistdir}/doc/latex/tkz-euclide/latex/TKZdoc-euclide-main.tex
%doc %{_texmfdistdir}/doc/latex/tkz-euclide/latex/TKZdoc-euclide-obj.tex
%doc %{_texmfdistdir}/doc/latex/tkz-euclide/latex/TKZdoc-euclide-points.tex
%doc %{_texmfdistdir}/doc/latex/tkz-euclide/latex/TKZdoc-euclide-polygons.tex
%doc %{_texmfdistdir}/doc/latex/tkz-euclide/latex/TKZdoc-euclide-presentation.tex
%doc %{_texmfdistdir}/doc/latex/tkz-euclide/latex/TKZdoc-euclide-rapporteur.tex
%doc %{_texmfdistdir}/doc/latex/tkz-euclide/latex/TKZdoc-euclide-sectors.tex
%doc %{_texmfdistdir}/doc/latex/tkz-euclide/latex/TKZdoc-euclide-segments.tex
%doc %{_texmfdistdir}/doc/latex/tkz-euclide/latex/TKZdoc-euclide-tips_and_tricks.tex
%doc %{_texmfdistdir}/doc/latex/tkz-euclide/latex/TKZdoc-euclide-tools.tex
%doc %{_texmfdistdir}/doc/latex/tkz-euclide/latex/TKZdoc-euclide-transf.tex
%doc %{_texmfdistdir}/doc/latex/tkz-euclide/latex/TKZdoc-euclide-vec.tex
%doc %{_texmfdistdir}/doc/latex/tkz-euclide/latex/euclide.ist
%doc %{_texmfdistdir}/doc/latex/tkz-euclide/readme-tkz-euclide-fr.txt
%doc %{_texmfdistdir}/doc/latex/tkz-euclide/readme-tkz-euclide.txt
%doc %{_texmfdistdir}/doc/latex/tkz-euclide/tkz-euclide-screen.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.16c-2
+ Revision: 756977
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.16c-1
+ Revision: 719763
- texlive-tkz-euclide
- texlive-tkz-euclide
- texlive-tkz-euclide

