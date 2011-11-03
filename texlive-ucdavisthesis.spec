# revision 17687
# category Package
# catalog-ctan /macros/latex/contrib/ucdavisthesis
# catalog-date 2010-03-15 08:48:16 +0100
# catalog-license lppl
# catalog-version 1.1
Name:		texlive-ucdavisthesis
Version:	1.1
Release:	1
Summary:	A thesis/dissertation class for University of California Davis
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ucdavisthesis
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ucdavisthesis.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ucdavisthesis.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ucdavisthesis.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The class conforms to the University's requirements for 2009.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
