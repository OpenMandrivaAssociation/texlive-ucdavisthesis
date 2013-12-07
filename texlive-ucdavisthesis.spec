# revision 31476
# category Package
# catalog-ctan /macros/latex/contrib/ucdavisthesis
# catalog-date 2012-02-09 21:58:23 +0100
# catalog-license lppl
# catalog-version 1.1
Name:		texlive-ucdavisthesis
Version:	1.1
Release:	5
Summary:	A thesis/dissertation class for University of California Davis
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ucdavisthesis
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ucdavisthesis.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ucdavisthesis.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ucdavisthesis.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The class conforms to the University's requirements for 2009.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ucdavisthesis/ucdavisthesis.cls
%{_texmfdistdir}/tex/latex/ucdavisthesis/ucdthesis10.clo
%{_texmfdistdir}/tex/latex/ucdavisthesis/ucdthesis11.clo
%{_texmfdistdir}/tex/latex/ucdavisthesis/ucdthesis12.clo
%{_texmfdistdir}/tex/latex/ucdavisthesis/ucdthesis13.clo
%doc %{_texmfdistdir}/doc/latex/ucdavisthesis/Example/ucdavisthesis_example.bib
%doc %{_texmfdistdir}/doc/latex/ucdavisthesis/Example/ucdavisthesis_example_Chap1.tex
%doc %{_texmfdistdir}/doc/latex/ucdavisthesis/Example/ucdavisthesis_example_Chap2.tex
%doc %{_texmfdistdir}/doc/latex/ucdavisthesis/Example/ucdavisthesis_example_Chap3.tex
%doc %{_texmfdistdir}/doc/latex/ucdavisthesis/Example/ucdavisthesis_example_figure.eps
%doc %{_texmfdistdir}/doc/latex/ucdavisthesis/Example/ucdavisthesis_example_figure.pdf
%doc %{_texmfdistdir}/doc/latex/ucdavisthesis/Example/ucdavisthesis_example_main.pdf
%doc %{_texmfdistdir}/doc/latex/ucdavisthesis/Example/ucdavisthesis_example_main.tex
%doc %{_texmfdistdir}/doc/latex/ucdavisthesis/README
%doc %{_texmfdistdir}/doc/latex/ucdavisthesis/ucdavisthesis.pdf
#- source
%doc %{_texmfdistdir}/source/latex/ucdavisthesis/ucdavisthesis.dtx
%doc %{_texmfdistdir}/source/latex/ucdavisthesis/ucdavisthesis.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
